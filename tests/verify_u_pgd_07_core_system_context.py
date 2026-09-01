#!/usr/bin/env python3
from pathlib import Path
import yaml
ROOT=Path(__file__).resolve().parents[1]
DATA=ROOT/'dados/pgd-1.0/U-PGD-07-core-system-context-reconciliation.yaml'
DOC=ROOT/'docs/U-PGD-07-core-system-context-reconciliation.md'
def fail(x): print('PGD_CORE_SYSTEM_CONTEXT_U07=FAIL',x); raise SystemExit(2)
def main():
    if not DATA.exists(): fail('missing-data')
    if not DOC.exists(): fail('missing-doc')
    d=yaml.safe_load(DATA.read_text(encoding='utf-8'))
    if d.get('unit')!='U-PGD-07-CORE-SYSTEM-CONTEXT-RECONCILIATION': fail('unit')
    refs=d.get('refs') or {}
    expected={
      'pgd_base':'3f23a2d5a83446e4b7f0ba2abeee4f63dddf738e',
      'pgh_main':'edbfefa6ef4d0bd2e6581e6781e82e167c583b96',
      'pgh_candidate':'78ec019c5ba0f4e72c878aa3c18baea2639a350b',
      'runtime':'f033b622ce6a3e59f4a3d2d29f903b3f4a267b32',
      'system_vision_catalog':'c1f208fb3470eeced0fd3da96d948efa196cb38c'}
    for k,v in expected.items():
        if refs.get(k)!=v: fail('ref:'+k)
    if refs.get('system_vision_sha256')!='d35189c2a1e1b1cd8d5ae62c036e752f6c2dfa8495fa00bd0d92204bdee65e7d': fail('vision-hash')
    if d.get('pgh_contract')!='CT-PGH2-OPERATIONAL-RECONCILIATION@1.0.0': fail('u250-contract')
    if d.get('system_vision_id')!='PGH-SUITE-SYSTEM-VISION-1': fail('vision-id')
    a=d.get('authority') or {}
    if a.get('PGH')!='triggers_invariants_semantics_evidence': fail('pgh-authority')
    if a.get('PGD')!='assignment_dispatch_queues_leases_scheduler_runtime_state': fail('pgd-authority')
    if a.get('PGA')!='policy_authority_gates': fail('pga-authority')
    if a.get('RHGD')!='federation_without_second_scheduler': fail('rhgd-authority')
    if a.get('supervisor')!='transport_preconstructed_orders_without_default_replanning': fail('supervisor-boundary')
    cs=d.get('context_sync') or {}
    if cs.get('runtime')!='pgh.dynamic-sync' or cs.get('semantic_authority')!='PGH' or cs.get('runtime_authority')!='PGD': fail('context-sync-boundary')
    if cs.get('second_broker_created') is not False or cs.get('second_scheduler_created') is not False: fail('context-sync-duplicate-runtime')
    rel=d.get('release') or {}
    if rel.get('version')!='1.0.0' or rel.get('tag')!='v1.0.0' or rel.get('tag_commit')!='366388d8c52f696d81b7277075b87e8fc144ca1b' or rel.get('immutable') is not True: fail('release')
    if d.get('core_change_required')!='NO' or d.get('project_skill_change_required')!='NO': fail('unnecessary-change')
    gates=d.get('gates') or {}
    required=['DELTA_INVENTORY','LEARNING_PRESERVED','UPSTREAM_CORE_SAFE_POINT','U250_OPERATIONAL_RECONCILIATION','U255_SYSTEM_VISION','PGD_RUNTIME_REFERENCE','AUTHORITY_BOUNDARY','CONTEXT_SYNC_BOUNDARY','NO_DUPLICATE_PGD_RUNTIME','RELEASE_IMMUTABILITY','RECONCILIATION_CLOSURE','DEPENDENCY_REFERENCES']
    if any(gates.get(k)!='PASS' for k in required): fail('gates')
    text=DOC.read_text(encoding='utf-8')
    for marker in ('PGH autoriza/contextualiza; PGD executa','OperationalReconciliationCoordinator','PGH-SUITE-SYSTEM-VISION-1','f033b622ce6a3e59f4a3d2d29f903b3f4a267b32','v1.0.0'):
        if marker not in text: fail('doc:'+marker)
    print('PGD_CORE_SYSTEM_CONTEXT_U07=PASS U250=PASS U255=PASS AUTHORITY=PASS RELEASE_IMMUTABLE=PASS')
    return 0
if __name__=='__main__': raise SystemExit(main())
