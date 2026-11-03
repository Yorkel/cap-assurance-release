#!/usr/bin/env python3
"""Compare rebuilt results, claim-level values and PDF text with frozen targets."""
from pathlib import Path
from collections import Counter
import csv,json,re,hashlib
import pandas as pd
import numpy as np
import fitz
ROOT=Path(__file__).resolve().parent.parent;OUT=ROOT/'06_outputs/tables/current'

def main():
 csvs=[]
 for expected in sorted((ROOT/'expected/tables').glob('*.csv')):
  current=OUT/expected.name;assert current.exists(),current.name
  a=pd.read_csv(expected);b=pd.read_csv(current)
  pd.testing.assert_frame_equal(a,b,check_dtype=False,check_exact=False,rtol=1e-10,atol=1e-10)
  csvs.append(expected.name)
 audit=json.loads((OUT/'retained_findings_audit.json').read_text())
 assert audit['n_configurations']==8 and audit['n_questions']==1200 and audit['n_complete']==1199
 assert audit['n_varying_labels']==291 and audit['repeats']['n_raw_answers_matched']==6000
 assert audit['repeats']['mean_pair_disagreement']==334/12000
 buckets=pd.read_csv(OUT/'retained_configuration_buckets.csv');assert list(buckets.n)==[717,215,76,191]
 filtering=pd.read_csv(OUT/'retained_agreement_filtering.csv').set_index('variant');assert filtering.loc['anchor','correct_unanimous']==717 and filtering.loc['anchor','n_unanimous']==908
 pair=json.loads((OUT/'retained_ai_agreement_audit.json').read_text());assert pair['every_AI_pair_agreement_exceeds_every_AI_CAP_agreement'] and pair['historical_vendor_example']['source']=='recorded_disagreement'
 coding=pd.read_csv(OUT/'documentary_cell_counts.csv');assert coding.groupby('map').placements.sum().to_dict()=={'UK':2057,'EU':2318}
 themes=pd.read_csv(OUT/'documentary_shared_themes.csv');assert len(themes)==71
 sub=pd.read_csv(OUT/'documentary_subtheme_map.csv');assert len(sub)==395
 cat=pd.read_csv(ROOT/'documentary/workbook/Documents.csv');assert len(cat)==37 and Counter(cat.Map)=={'UK':19,'EU':18}
 source=pd.read_csv(ROOT/'documentary/source_catalogue.csv');assert len(source)==54 and source.document.nunique()==37
 m=pd.read_csv(OUT/'retained_mcnemar.csv');assert len(m)==28 and (m.p_two_sided<.05).sum()==6 and not (m.p_holm<.05).any() and not (m.p_bh<.05).any()
 boot=pd.read_csv(OUT/'bootstrap_winner_stability.csv').set_index('specification');assert boot.loc['L2_D_time','wins']==889 and boot.loc['anchor','wins']==74
 # The fixed manuscript table cells are presentation inputs. Check headline numbers against recomputation.
 tables={}
 for x in json.loads((ROOT/'paper_tables/catalogue.json').read_text()):
  with (ROOT/'paper_tables'/x['file']).open(newline='') as f:tables[x['number']]=list(csv.reader(f))
 assert [int(row[1].replace(',','')) for row in tables['2'][1:]]==[717,215,76,191,1199]
 assert int(tables['A3'][-1][1].replace(',',''))==2057 and int(tables['A3'][-1][3].replace(',',''))==2318
 assert [int(row[1]) for row in tables['A10'][1:-1]]==audit['repeats']['pair_disagreements']
 labels=pd.read_csv(ROOT/'05_evidence/confidence_per_question.csv')
 names=pd.read_csv(ROOT/'01_data/category_names.csv');codes=dict(zip(names.gold_name,names.gold_code))
 for row in tables['A11'][1:]:
  label={'Labour':'Labor','Government Operations':'Govt Operations','Law and Crime':'Law & Crime'}.get(row[0],row[0]);code=codes[label];values={}
  for variant,g in labels.groupby('variant'):
   tp=int((g.gold.eq(code)&g.predicted_label.eq(code)).sum());fp=int((~g.gold.eq(code)&g.predicted_label.eq(code)).sum());fn=int((g.gold.eq(code)&~g.predicted_label.eq(code)).sum());values[variant]=2*tp/(2*tp+fp+fn) if 2*tp+fp+fn else 0.
  expected=[round(values['anchor'],3),round(min(values.values()),3),round(max(values.values()),3),round((max(values.values())-min(values.values()))*100,1)]
  actual=[float(row[j].replace(' pp','')) for j in range(1,5)]
  assert all(abs(a-b)<.0000001 for a,b in zip(actual,expected)),('Table A11 value mismatch',row,expected)
 pdf_count=0
 def normalized(text):return re.sub(r'\s+','',text)
 for expected in sorted((ROOT/'paper_assets').glob('*.pdf')):
  rebuilt=ROOT/'06_outputs/paper_assets'/expected.name
  assert rebuilt.exists(),expected.name
  with fitz.open(expected) as a,fitz.open(rebuilt) as b:
   assert a.page_count==b.page_count==1
   assert normalized(a[0].get_text())==normalized(b[0].get_text()),('PDF text differs',expected.name)
  pdf_count+=1
 for expected in sorted((ROOT/'expected/figures').glob('*.pdf')):
  with fitz.open(expected) as a,fitz.open(ROOT/'06_outputs/figures'/expected.name) as b:
   assert normalized(a[0].get_text())==normalized(b[0].get_text()),('figure text differs',expected.name)
 assert pdf_count==22
 print('Verified',len(csvs),'frozen CSV targets, principal numeric claims, documentary counts, paired tests and 22 paper PDFs.')
if __name__=='__main__':main()
