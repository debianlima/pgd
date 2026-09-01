#!/usr/bin/env python3
from pathlib import Path
import yaml
R=Path(__file__).resolve().parents[1]
D=yaml.safe_load((R/'dados/pgd-1.0/U-PGD-04-lateral-delta-inventory.yaml').read_text(encoding='utf-8'))
DOC=(R/'docs/U-PGD-04-lat02-rhgd-lateral-reconciliation.md').read_text(encoding='utf-8')
STATE=(R/'estado.md').read_text(encoding='utf-8')
HANDOFF=(R/'docs/U-PGD-01-msgcd-u20-handoff.md').read_text(encoding='utf-8')
REL=yaml.safe_load((R/'dados/pgd-1.0/U-PGD-02-release-evidence.yaml').read_text(encoding='utf-8'))
assert D['lateral_delta_inventory']['DELTA_INVENTORY']=='PASS'
assert D['lateral_delta_inventory']['LEARNING_PRESERVED']=='PASS'
assert D['lateral_delta_inventory']['core_modified'] is False
assert D['lateral_delta_inventory']['rhgd_modified_by_this_side'] is False
assert D['lateral_delta_inventory']['pgd_release_reopened'] is False
rows={x['rule']:x for x in D['matrix']}
for rule in ['live_runtime_state','operational_admission','task_queue_dag','lease_and_reservation','scheduler_execution','outcome_evidence']:
    assert rule in rows
for rule in ['live_runtime_state','operational_admission','task_queue_dag','lease_and_reservation','scheduler_execution']:
    assert rows[rule]['producer']=='PGD'
assert rows['scheduler_execution']['consumer']=='RHGD_federates_not_schedules'
assert rows['lease_and_reservation']['consumer']=='RHGD_reference_only_no_mint'
assert D['gates_result']['FEDERATION_PAYLOAD_SCHEMA']=='GAP_NEW_VERSIONED_CONTRACT_REQUIRED'
assert D['handoff']['target']=='A09/MSGCD'
assert 'PGH autoriza; PGD executa' in HANDOFF
assert REL['ownership']['runtime']=='PGD' and REL['authority_chain']['runtime_lease_owner']=='PGD'
assert REL['gates']['RESOURCE_STATE_OWNED_BY_PGD']=='PASS'
assert 'RHGD federa' in DOC and 'MSGCD agrega' in DOC
assert 'não existe, no PGD standalone auditado, um schema federation-facing' in DOC
print('PGD_RHGD_LAT02=PASS MATRIX=7 OWNERSHIP=PGD FEDERATION_SCHEMA=GAP_DECLARED')
