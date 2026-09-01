#!/usr/bin/env python3
from pathlib import Path
from datetime import datetime
import subprocess,yaml
R=Path(__file__).resolve().parents[1]
D=yaml.safe_load((R/'dados/pgd-1.0/U-PGD-08-human-reconciliation-ratification.yaml').read_text(encoding='utf-8'))
assert D['authority']['decision_id']=='HUMAN-RECONCILIATION-TOTAL-GENERAL-20260901'
assert datetime.fromisoformat(D['authority']['decision_at'].replace('Z','+00:00')) > datetime.fromisoformat(D['temporal_provenance']['u_pgd_05_commit_at'])
assert D['temporal_provenance']['historical_authority_reclassified'] is False
assert D['temporal_provenance']['ratification_effect']=='prospective_from_decision_at'
for p,h in D['immutable_blobs'].items(): assert subprocess.check_output(['git','hash-object',str(R/p)],text=True).strip()==h
assert all(v=='PASS' for v in D['gates'].values())
assert D['preserved_boundaries']['PGD']=='runtime_scheduler_execution'
assert D['preserved_boundaries']['RHGD']=='federation_discovery_no_second_scheduler'
print('PGD_HUMAN_RECONCILIATION_U08=PASS PROSPECTIVE_RATIFICATION=PASS')
