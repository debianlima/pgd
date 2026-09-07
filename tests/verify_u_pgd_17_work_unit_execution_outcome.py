#!/usr/bin/env python3
from __future__ import annotations

import copy
import json
from pathlib import Path

import jsonschema
import yaml

ROOT=Path(__file__).resolve().parents[1]
SCHEMA_PATH=ROOT/'contratos/pgd-1.0/work-unit-execution-outcome.schema.json'
FEDERATION_PATH=ROOT/'contratos/pgd-1.0/rhgd-federation.schema.json'


def success_outcome() -> dict:
    return {
      'schema_version':'pgd-work-unit-execution-outcome/1',
      'outcome_id':'outcome://project-final/FSWU-001/epoch-1',
      'project_ref':'project-final',
      'work_unit_id':'FSWU-001',
      'execution_ref':'pgd://execution/project-final/FSWU-001/1',
      'assignment':{'agent_id':'synth-worker','assignment_epoch':1},
      'lease_ref':None,
      'status':'SUCCEEDED',
      'retryable':False,
      'outcome_classification':'observed',
      'completion_owner':'PGD',
      'authority_effect':'NONE',
      'completed_at':'2026-09-06T23:00:00Z',
      'idempotency_key':'outcome:project-final:FSWU-001:1',
      'provenance_refs':['cogctx://task-doc','msgcd://composition/task-doc'],
      'evidence_refs':['evidence://worker/final-001'],
      'runtime_observation':{
        'model_ref':'model-synthesis-B',
        'model_version':'2',
        'host_ref':'host://worker-7',
        'transport_ref':'netmaker://peer-7'
      },
      'result':{
        'result_ref':'result://project-final/FSWU-001/1',
        'output_schema_ref':'schema://unified-documentation-result/1',
        'content_hash':'sha256:'+'a'*64,
        'payload':{'content':'documentacao final'}
      },
      'error':None
    }


def failed_outcome() -> dict:
    x=success_outcome()
    x.update({
      'outcome_id':'outcome://project-final/FSWU-001/epoch-1-failed',
      'status':'FAILED',
      'retryable':True,
      'evidence_refs':['evidence://worker/failure-001'],
      'result':None,
      'error':{
        'code':'MODEL_RUNTIME_UNAVAILABLE',
        'message':'worker perdeu o runtime antes da conclusao',
        'evidence_refs':['evidence://worker/failure-001']
      }
    })
    return x


def invalid(schema,payload,label):
    try:
        jsonschema.validate(payload,schema,format_checker=jsonschema.FormatChecker())
    except jsonschema.ValidationError:
        return
    raise AssertionError('expected invalid: '+label)


def main() -> int:
    if not SCHEMA_PATH.exists():
        print('PGD_U17_WORK_UNIT_OUTCOME=FAIL schema-missing')
        return 2
    schema=json.loads(SCHEMA_PATH.read_text(encoding='utf-8'))
    success=success_outcome(); failed=failed_outcome()
    jsonschema.validate(success,schema,format_checker=jsonschema.FormatChecker())
    jsonschema.validate(failed,schema,format_checker=jsonschema.FormatChecker())

    cases=[]
    x=copy.deepcopy(success); x['provider']='openai'; cases.append((x,'extra-provider'))
    x=copy.deepcopy(success); x['status']='RUNNING'; cases.append((x,'nonterminal'))
    x=copy.deepcopy(success); x['retryable']=True; cases.append((x,'success-retryable'))
    x=copy.deepcopy(success); x['result']=None; cases.append((x,'success-without-result'))
    x=copy.deepcopy(success); x['error']={'code':'X','message':'x','evidence_refs':['evidence://x']}; cases.append((x,'success-with-error'))
    x=copy.deepcopy(failed); x['result']=success['result']; cases.append((x,'failed-with-result'))
    x=copy.deepcopy(failed); x['error']=None; cases.append((x,'failed-without-error'))
    x=copy.deepcopy(failed); x['evidence_refs']=[]; cases.append((x,'failed-without-evidence'))
    x=copy.deepcopy(success); x['assignment']['assignment_epoch']=0; cases.append((x,'epoch-zero'))
    x=copy.deepcopy(success); x['completion_owner']='RHGD'; cases.append((x,'rhgd-cannot-complete'))
    x=copy.deepcopy(success); x['authority_effect']='EXPAND'; cases.append((x,'authority-growth'))
    x=copy.deepcopy(success); x['outcome_classification']='estimated'; cases.append((x,'not-observed'))
    x=copy.deepcopy(success); x['result']['content_hash']='a'*64; cases.append((x,'bad-hash'))
    x=copy.deepcopy(success); x['provenance_refs']=['x','x']; cases.append((x,'duplicate-provenance'))
    x=copy.deepcopy(success); x['runtime_observation']['selected_worker']='synth-worker'; cases.append((x,'runtime-cannot-select'))
    for payload,label in cases: invalid(schema,payload,label)

    federation=json.loads(FEDERATION_PATH.read_text(encoding='utf-8'))
    response=federation['properties']['response']['properties']
    statuses=response['status']['enum']
    assert 'SUCCEEDED' in statuses and 'FAILED' in statuses
    assert response['outcome_classification']['const']=='observed'
    assert set(response['outcome_evidence_ref']['type'])=={'string','null'}
    assert success['outcome_id'].startswith('outcome://')

    evidence=yaml.safe_load((ROOT/'dados/pgd-1.0/U-PGD-17-work-unit-execution-outcome.yaml').read_text(encoding='utf-8'))
    jsonschema.validate(evidence['sample_success'],schema,format_checker=jsonschema.FormatChecker())
    jsonschema.validate(evidence['sample_failure'],schema,format_checker=jsonschema.FormatChecker())
    assert evidence['boundary']['completion_owner']=='PGD'
    assert evidence['boundary']['federation_owner']=='RHGD_transport_only'
    assert evidence['boundary']['outcome_evidence_ref_semantics']=='points_to_outcome_id'
    docs=(ROOT/'docs/U-PGD-17-work-unit-execution-outcome.md').read_text(encoding='utf-8')
    assert 'Somente PGD' in docs and 'outcome_evidence_ref' in docs and 'assignment_epoch' in docs

    manifest=yaml.safe_load((ROOT/'manifesto.yaml').read_text(encoding='utf-8'))
    assert manifest['release_alvo']=='v1.0.0'
    assert manifest['identidade_execucao']['repositorio_implementacao_canonica']=='debianlima/pgh-distributed-session-control-plane'
    assert manifest['identidade_execucao']['runtime_paralelo_proibido'] is True
    assert (ROOT/'skills/pgd/SKILL.md').read_text(encoding='utf-8').split('versao: ',1)[1].splitlines()[0]=='0.2.0'

    print('PGD_U17_WORK_UNIT_OUTCOME=PASS')
    print('TERMINAL_STATUS=SUCCEEDED|FAILED')
    print('OUTCOME_CLASSIFICATION=observed')
    print('COMPLETION_OWNER=PGD')
    print('RHGD_OUTCOME_EVIDENCE_REF_COMPAT=PASS')
    print('ASSIGNMENT_FENCE=agent_id+assignment_epoch')
    print('RUNTIME_SELECTION_AUTHORITY=NONE')
    print('RELEASE_IMMUTABILITY=PASS')
    return 0


if __name__=='__main__':
    raise SystemExit(main())
