#!/usr/bin/env python3
"""Run the offline release analyses in dependency order."""
from pathlib import Path
import os,subprocess,sys
ROOT=Path(__file__).resolve().parent.parent
ENV=dict(os.environ,MPLBACKEND='Agg',MPLCONFIGDIR=str(ROOT/'build/matplotlib'))
SCRIPTS=['recompute_retained_findings.py','compare_retained_agreement.py','recompute_per_category.py','recompute_calibration.py','recompute_bootstrap.py','recompute_inclusion_robustness.py','recompute_auroc.py','topic_shares_reweighted.py','build_metrics.py','build_documentary.py','make_figures.py','render_assets.py']
for script in SCRIPTS:
 print('\nRunning',script,flush=True)
 subprocess.run([sys.executable,str(ROOT/'analysis'/script)],cwd=ROOT,env=ENV,check=True)
print('Offline reproduction completed; no model calls were made.')
