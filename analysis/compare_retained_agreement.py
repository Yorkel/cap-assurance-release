#!/usr/bin/env python3
"""Verify AI–AI versus AI–CAP agreement on one matched retained-label cohort.

No API calls; the historical recorded vendor example is checked separately.
"""
from pathlib import Path
from itertools import combinations
import argparse, hashlib, json
import pandas as pd
ROOT=Path(__file__).resolve().parent.parent
EXPECTED={"anchor","L2_C_drop_bundle","L2_C_drop_fewshot","L2_F_reasoning","L2_F_cot","L2_D_time","L2_D_speaker","L3_freetext"}
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--data-root',type=Path,default=ROOT);p.add_argument('--output-dir',type=Path);args=p.parse_args();root=args.data_root;out=args.output_dir or root/'06_outputs/tables/current'
 labels_path=root/'05_evidence/confidence_per_question.csv';sample_path=root/'01_data/splits/sst_main.csv';vendor_path=root/'06_outputs/tables/current/claude_labels_reconstructed.csv'
 labels=pd.read_csv(labels_path);sample=pd.read_csv(sample_path).set_index('id');vendor=pd.read_csv(vendor_path)
 assert set(labels.variant)==EXPECTED and not labels.duplicated(['question_id','variant']).any()
 assert labels.gold.eq(labels.question_id.map(sample.majortopic)).all()
 wide=labels.pivot(index='question_id',columns='variant',values='predicted_label').dropna().astype(int);gold=sample.majortopic.reindex(wide.index);assert len(wide)==1199
 rows=[]
 for a,b in combinations(sorted(wide.columns),2):
  n=int(wide[a].eq(wide[b]).sum());rows.append(dict(comparison='AI-AI',configuration_a=a,configuration_b=b,n_questions=len(wide),n_agree=n,agreement=n/len(wide)))
 for a in sorted(wide.columns):
  n=int(wide[a].eq(gold).sum());rows.append(dict(comparison='AI-CAP',configuration_a=a,configuration_b='CAP',n_questions=len(wide),n_agree=n,agreement=n/len(wide)))
 results=pd.DataFrame(rows);ai=results[results.comparison.eq('AI-AI')];cap=results[results.comparison.eq('AI-CAP')]
 assert len(ai)==28 and len(cap)==8 and ai.agreement.min()>cap.agreement.max()
 historical=vendor[vendor.question_id.eq(6265)];assert len(historical)==1
 assert historical.iloc[0].source=='recorded_disagreement' and historical.iloc[0].predicted_label==9 and historical.iloc[0].gold==14
 examples={}
 for qid in [6728,6265]:
  actual=wide.loc[qid].value_counts().sort_index();examples[str(qid)]={'CAP':int(gold.loc[qid]),'retained_label_counts':{str(int(k)):int(v) for k,v in actual.items()}}
 assert examples['6265']['retained_label_counts']=={'14':7,'21':1}
 assert examples['6728']['retained_label_counts']=={'12':5,'13':3}
 audit={'producer':'04_analysis/compare_retained_agreement.py','producer_sha256':digest(Path(__file__)),'input_sha256':{str(f.relative_to(root)):digest(f) for f in [labels_path,sample_path,vendor_path]},'n_matched_questions':len(wide),'AI_AI':{'n_pairs':len(ai),'mean_agreement':float(ai.agreement.mean()),'min_agreement':float(ai.agreement.min()),'max_agreement':float(ai.agreement.max())},'AI_CAP':{'n_configurations':len(cap),'mean_agreement':float(cap.agreement.mean()),'min_agreement':float(cap.agreement.min()),'max_agreement':float(cap.agreement.max())},'every_AI_pair_agreement_exceeds_every_AI_CAP_agreement':True,'examples':examples,'historical_vendor_example':{'question_id':6265,'label':9,'CAP':14,'source':'recorded_disagreement','included_in_principal_eight_configuration_analysis':False},'scope':'Operational GPT-4o configurations and the same CAP benchmark on matched questions; not general AI-versus-human ability, independent corroboration, or observed human-review performance.'}
 out.mkdir(parents=True,exist_ok=True);results.to_csv(out/'retained_ai_agreement.csv',index=False);(out/'retained_ai_agreement_audit.json').write_text(json.dumps(audit,indent=2)+'\n')
 print('Verified 28 AI-AI pairs and 8 AI-CAP comparisons on 1199 matched questions; historical Immigration label is a recorded vendor disagreement.')
if __name__=='__main__':main()
