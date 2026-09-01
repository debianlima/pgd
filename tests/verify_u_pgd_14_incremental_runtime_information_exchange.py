from pathlib import Path
import json, yaml
ROOT=Path(__file__).resolve().parents[1]
s=json.loads((ROOT/'contratos/pgd-1.0/incremental-information-exchange.schema.json').read_text())
d=yaml.safe_load((ROOT/'dados/pgd-1.0/U-PGD-14-incremental-runtime-information-exchange.yaml').read_text())
doc=(ROOT/'docs/U-PGD-14-incremental-runtime-information-exchange.md').read_text()
man=yaml.safe_load((ROOT/'manifesto.yaml').read_text())
assert s['properties']['schema_version']['const']=='pgd-incremental-information-exchange/1'
c=s['properties']['continuation']['properties']
assert c['requester_continues_work']['const'] is True
assert c['responder_preserves_current_unit']['const'] is True
assert c['preemption_forbidden']['const'] is True
assert c['default_blocking']['const'] is False
assert s['properties']['transport']['properties']['carrier']['const']=='pgh-work-context-broadcast/1'
assert s['properties']['transport']['properties']['no_second_scheduler']['const'] is True
r=s['properties']['reconciliation']['properties']
assert r['on_arrival']['const']=='INCREMENTAL_RECONCILIATION'
assert r['response_is_evidence_not_authority']['const'] is True
assert d['status']=='PASS'
assert d['principios']['only_required_gate_can_wait'] is True
assert d['zonas']['SAME_ZONE']['carrier']=='PGD_WCB'
assert d['zonas']['HETEROGENEOUS_ZONE']['pgd_remains_runtime_owner'] is True
assert d['fencing']['duplicate_response']=='IDEMPOTENT'
assert d['blocking_rule']['unrelated_work_never_waits_for_information'] is True
for token in ['continua imediatamente','microavaliação read-only','evidência observada','WAITING_FOR_INFORMATION','Nenhum segundo scheduler']:
    assert token in doc, token
entries={e['caminho']:e for e in man['entradas']}
for p in ['contratos/pgd-1.0/incremental-information-exchange.schema.json','dados/pgd-1.0/U-PGD-14-incremental-runtime-information-exchange.yaml','docs/U-PGD-14-incremental-runtime-information-exchange.md','tests/verify_u_pgd_14_incremental_runtime_information_exchange.py']:
    assert entries[p]['status']=='aceito', p
print('PGD_U14_INCREMENTAL_INFORMATION_EXCHANGE=PASS')
