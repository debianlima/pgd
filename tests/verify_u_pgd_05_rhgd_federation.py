#!/usr/bin/env python3
from pathlib import Path
import json, yaml, jsonschema
ROOT=Path(__file__).resolve().parents[1]
SCHEMA=ROOT/'contratos/pgd-1.0/rhgd-federation.schema.json'
DATA=ROOT/'dados/pgd-1.0/U-PGD-05-rhgd-federation.yaml'
def fail(msg):
    print('PGD_RHGD_U05=FAIL',msg); raise SystemExit(2)
def main():
    schema=json.loads(SCHEMA.read_text(encoding='utf-8-sig'))
    data=yaml.safe_load(DATA.read_text(encoding='utf-8-sig'))
    jsonschema.validate(data['contract_example'],schema)
    g=data['gates']
    for k in ('DELTA_INVENTORY','LEARNING_PRESERVED','PGH_AUTHORIZATION_REQUIRED','RESOURCE_STATE_OWNED_BY_PGD','NO_DUPLICATE_PGD_RUNTIME','OUTCOME_EVIDENCE_OBSERVED_ONLY','FEDERATION_PAYLOAD_SCHEMA'):
        if g.get(k)!='PASS': fail(k)
    ex=data['contract_example']
    if not ex['request']['authorization_ref']: fail('authorization-ref')
    if ex['runtime_mapping']['pgd_owns'] != ['admission','queue','lease','scheduler','retry','recovery','runtime_state']: fail('pgd-ownership')
    if 'scheduler' in ex['runtime_mapping']['rhgd_owns'] or 'lease' in ex['runtime_mapping']['rhgd_owns']: fail('duplicate-runtime')
    if ex['response']['outcome_classification']!='observed': fail('outcome-classification')
    print('PGD_RHGD_U05=PASS FEDERATION_PAYLOAD_SCHEMA=PASS OWNERSHIP=PGD')
    return 0
if __name__=='__main__': raise SystemExit(main())
