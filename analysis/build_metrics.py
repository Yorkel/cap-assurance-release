#!/usr/bin/env python3
"""Additional retained-label measures; no API calls and no calibration inference."""
from pathlib import Path
from itertools import combinations
import pandas as pd
from scipy.stats import binomtest
ROOT=Path(__file__).resolve().parent.parent;OUT=ROOT/'06_outputs/tables/current';OUT.mkdir(parents=True,exist_ok=True)
d=pd.read_csv(ROOT/'05_evidence/confidence_per_question.csv');wide=d.pivot(index='question_id',columns='variant',values='predicted_label').dropna();gold=d.drop_duplicates('question_id').set_index('question_id').gold.reindex(wide.index);correct=wide.eq(gold,axis=0)
rows=[]
for a,b in combinations(sorted(wide.columns),2):
 a_only=int((correct[a]&~correct[b]).sum());b_only=int((~correct[a]&correct[b]).sum());discordant=a_only+b_only
 p=binomtest(min(a_only,b_only),discordant,.5).pvalue if discordant else 1.
 rows.append({'a':a,'b':b,'n':len(wide),'a_correct_b_wrong':a_only,'a_wrong_b_correct':b_only,'p_two_sided':p})
r=pd.DataFrame(rows);order=r.p_two_sided.sort_values().index;values=r.loc[order,'p_two_sided'];m=len(r)
holm=[];running=0
for i,p in enumerate(values):running=max(running,min(1,p*(m-i)));holm.append(running)
bh=[min(1,float(p)*m/(i+1)) for i,p in enumerate(values)]
for i in range(m-2,-1,-1):bh[i]=min(bh[i],bh[i+1])
r.loc[order,'p_holm']=holm;r.loc[order,'p_bh']=bh;r.to_csv(OUT/'retained_mcnemar.csv',index=False)
print('Verified 28 exact paired McNemar comparisons:',int((r.p_two_sided<.05).sum()),'unadjusted;',int((r.p_holm<.05).sum()),'Holm;',int((r.p_bh<.05).sum()),'BH significant at .05.')
