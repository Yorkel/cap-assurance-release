#!/usr/bin/env python3
"""Rebuild placement counts and shared-theme maps from frozen coding inputs.

The initial A/B passes were AI-assisted. Counts are analytic placements, not
unique passages or measured independent-human agreement. No coding is rerun.
"""
from pathlib import Path
from collections import defaultdict,Counter
import csv,json,re
ROOT=Path(__file__).resolve().parent.parent
INPUT=ROOT/'documentary';OUT=ROOT/'06_outputs/tables/current';OUT.mkdir(parents=True,exist_ok=True)
def read(name):
 with (INPUT/'workbook'/name).open(newline='') as f:return list(csv.DictReader(f))
def short(s,n):
 s=re.sub(r'\s+',' ',s or '').strip()
 return s if len(s)<=n else s[:n-1].rstrip()+'…'
order=[x['Document'] for x in read('Summary.csv')];about={x['Document']:x for x in read('Documents.csv')}
assert len(order)==len(set(order))==37 and set(order)==set(about)
assert Counter(x['Map'] for x in about.values())=={'UK':19,'EU':18}
groups=defaultdict(list)
def add(m,f,d,doc,quote,loc,holder,obligation,ifnot,note,basis,sheet,row):
 groups[(m,f,d)].append(dict(document=doc,map=m,function=f,dimension=d,quote=quote,location=loc,holder=holder,obligation=obligation,if_not_met=ifnot,note=note,basis=basis,source_sheet=sheet,source_row=row))
for i,r in enumerate(read('Agreed.csv'),2):
 add(r['Map'],r['Function'],r['Dimension'],r['Document'],r['Quote (A)'],r['Location (A)'],r['Holder (A)'],r['Level of obligation (A)'],r['If not met (A)'],r['Note (A)'],'both AI passes','Agreed',i)
for i,r in enumerate(read('Different_cell.csv'),2):
 for side,other in [('A','B'),('B','A')]:
  add(r['Map'],r[f'Function ({side})'],r[f'Dimension ({side})'],r['Document'],r[f'Quote ({side})'],r['Location (A)'],r[f'Holder ({side})'],r['Level of obligation (A)'],r['If not met (A)'],r[f'Note ({side})'],f'AI pass {side}; different cell in pass {other}','Different cell',i)
for name,side in [('Coder_A_only.csv','A'),('Coder_B_only.csv','B')]:
 for i,r in enumerate(read(name),2):add(r['Map'],r['Function'],r['Dimension'],r['Document'],r['Quote'],r['Location'],r['Holder'],r['Level of obligation'],r['If not met'],r['Note'],f'AI pass {side} only',name,i)
abb={'Decision-making':'DM','Delivery':'DEL','Coordination':'COO','Accountability':'ACC','Design':'DES','Resources':'RES'}
placements=[];counts=[];by_id={}
index=json.loads((INPUT/'thematic/inputs/index.json').read_text());original={x['group']:x for x in index}
for (m,f,d),rows in sorted(groups.items()):
 gid=f'{m}-{abb[f]}-{abb[d]}';rows.sort(key=lambda r:(order.index(r['document']),short(r['location'],50)))
 frozen={}
 for line in (INPUT/'thematic/inputs'/(gid+'.txt')).read_text().splitlines():
  match=re.match(r'\[(\S+)\] (\S+) \|',line)
  if match:frozen[match.group(1)]=(match.group(2),line)
 assert len(rows)==original[gid]['passages']==len(frozen)
 for i,row in enumerate(rows,1):
  pid=f'{gid}-{i:03d}';assert frozen[pid][0]==row['document']
  # Frozen theme inputs shorten quotes; retain complete quotes in this output.
  assert short(row['quote'],320) in frozen[pid][1],pid
  row={'passage_id':pid,**row};placements.append(row);by_id[pid]=row
 counts.append({'map':m,'function':f,'dimension':d,'placements':len(rows),'documents':len({r['document'] for r in rows})})
assert len(placements)==4375 and Counter(x['map'] for x in placements)=={'UK':2057,'EU':2318}
structure=json.loads((INPUT/'thematic/structure.json').read_text());maps=[];missing=[];all_themes=[]
for gid in sorted(original):
 sub=[];nt=[]
 files=sorted((INPUT/'thematic/outputs').glob(gid+'.json'))+sorted((INPUT/'thematic/outputs').glob(gid+'__part*.json'))
 assert files,gid
 for p in files:
  raw=json.loads(p.read_text());sub+=raw.get('themes',[]);nt+=raw.get('not_themed',[])
 assigned=structure['groups'][gid];assert len(assigned)==len(sub),(gid,len(assigned),len(sub))
 used=set()
 for i,(theme,assignment) in enumerate(zip(sub,assigned),1):
  assert theme['theme']==assignment['subtheme'],(gid,i)
  ids=theme.get('passage_ids',[]);assert set(ids)<=set(by_id),(gid,'unknown passage')
  assert all(pid.startswith(gid+'-') for pid in ids)
  used.update(ids);all_themes.append(theme)
  maps.append({'group':gid,'subtheme_number':i,'subtheme':theme['theme'],'shared_theme_key':assignment['theme_key'],'passage_ids':';'.join(ids)})
 accounted=used|{x.get('id') for x in nt};expected={x for x in by_id if x.startswith(gid+'-')};missing.append({'group':gid,'n_input':len(expected),'n_themed':len(used),'n_not_themed':len({x.get('id') for x in nt}),'n_unaccounted':len(expected-accounted)})
assert len(maps)==395
shared=[{'function':key.split('|')[0],'dimension':key.split('|')[1],**t} for key,ts in structure['themes'].items() for t in ts];assert len(shared)==71
for name,rows in [('documentary_placements.csv',placements),('documentary_cell_counts.csv',counts),('documentary_subtheme_map.csv',maps),('documentary_shared_themes.csv',shared),('documentary_theme_coverage.csv',missing)]:
 with (OUT/name).open('w',newline='') as f:
  wr=csv.DictWriter(f,fieldnames=list(rows[0]));wr.writeheader();wr.writerows(rows)
print('Verified 37 documentary units, 4375 placements, 395 subthemes and 71 shared themes. Frozen qualitative judgements are not independently recoded.')
