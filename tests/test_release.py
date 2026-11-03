from pathlib import Path
from collections import Counter
import csv,json,re,unittest
import pandas as pd
import fitz
ROOT=Path(__file__).resolve().parent.parent
class ReleaseTests(unittest.TestCase):
 def test_matched_input_integrity(self):
  d=pd.read_csv(ROOT/'05_evidence/confidence_per_question.csv');s=pd.read_csv(ROOT/'01_data/splits/sst_main.csv').set_index('id')
  self.assertEqual(len(d),9599);self.assertFalse(d.duplicated(['question_id','variant']).any());self.assertTrue(d.gold.eq(d.question_id.map(s.majortopic)).all())
 def test_independent_item_partition(self):
  d=pd.read_csv(ROOT/'05_evidence/confidence_per_question.csv');gold=d.drop_duplicates('question_id').set_index('question_id').gold.to_dict();w=d.pivot(index='question_id',columns='variant',values='predicted_label').dropna();counts=Counter()
  for qid,row in w.iterrows():
   labels=list(row);k=sum(x==gold[qid] for x in labels)
   key='all' if k==8 else 'some' if k else 'same_other' if len(set(labels))==1 else 'varying_other';counts[key]+=1
  self.assertEqual(counts,{'all':717,'some':215,'varying_other':76,'same_other':191});self.assertEqual(sum(counts.values()),1199)
 def test_raw_repeats_are_parseable_and_aligned(self):
  prompts={};total=0
  for p in sorted((ROOT/'05_evidence/raw/25_repeated_anchor').glob('*.jsonl')):
   expected=pd.read_csv(p.with_suffix('.csv')).set_index('question_id').label.to_dict();seen=set()
   for line in p.read_text().splitlines():
    r=json.loads(line);raw=r['raw_response'].strip();raw=re.sub(r'^```(?:json)?\s*','',raw);raw=re.sub(r'\s*```\s*$','',raw);label=int(json.loads(raw)['label']);qid=r['question_id']
    self.assertEqual(label,expected[qid]);self.assertNotIn(qid,seen);seen.add(qid);prompt=(r['system'],r['user']);self.assertEqual(prompts.setdefault(qid,prompt),prompt);total+=1
   self.assertEqual(len(seen),1200)
  self.assertEqual(total,6000)
 def test_documentary_scope_and_counts(self):
  counts=pd.read_csv(ROOT/'06_outputs/tables/current/documentary_cell_counts.csv');self.assertEqual(counts.groupby('map').placements.sum().to_dict(),{'UK':2057,'EU':2318})
  docs=pd.read_csv(ROOT/'documentary/workbook/Documents.csv');self.assertEqual(Counter(docs.Map),{'UK':19,'EU':18})
  self.assertEqual(len(pd.read_csv(ROOT/'06_outputs/tables/current/documentary_shared_themes.csv')),71)
 def test_historical_vendor_example_is_not_imputed(self):
  d=pd.read_csv(ROOT/'06_outputs/tables/current/claude_labels_reconstructed.csv');r=d[d.question_id.eq(6265)].iloc[0];self.assertEqual(r.source,'recorded_disagreement');self.assertEqual(r.predicted_label,9)
 def test_no_working_manuscript_or_credentials(self):
  for ext in ['*.docx','*.xlsx','*.ipynb']:
   self.assertFalse(list(ROOT.rglob(ext)),ext)
  self.assertFalse((ROOT/'.env').exists());self.assertFalse((ROOT/'TRANSCRIPTS').exists());self.assertFalse((ROOT/'.codex').exists())
  self.assertIn('Anonymous artifact contributors',(ROOT/'CITATION.cff').read_text())
 def test_all_numbered_assets_are_searchable(self):
  files=list((ROOT/'paper_assets').glob('*.pdf'));self.assertEqual(len(files),22)
  for p in files:
   with fitz.open(p) as d:self.assertEqual(d.page_count,1);self.assertGreater(len(d[0].get_text()),30)
if __name__=='__main__':unittest.main()
