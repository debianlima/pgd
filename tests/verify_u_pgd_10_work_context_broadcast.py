#!/usr/bin/env python3
from pathlib import Path
import hashlib,json,yaml,jsonschema
ROOT=Path(__file__).resolve().parents[1]
SCHEMA=ROOT/'contratos/pgd-1.0/work-context-broadcast.schema.json'
DATA=ROOT/'dados/pgd-1.0/U-PGD-10-work-context-broadcast-normative.yaml'
DOC=ROOT/'docs/U-PGD-10-work-context-broadcast-normative.md'
RUNTIME_SCHEMA_SHA='d585dcc3fd8e180e4a8fb8bf65bc9a5662bf734b2b5a80557010af630760f456'
RUNTIME_POLICY_SHA='c8e521df62b7b53fa3cdd29a4ccb9fc3c65a39109edc6c7f80401f6e7d1117ed'
def fail(x): print('PGD_WCB_U10=FAIL',x); raise SystemExit(2)
def main():
    for p in (SCHEMA,DATA,DOC):
        if not p.exists(): fail('missing:'+str(p.relative_to(ROOT)))
    raw=SCHEMA.read_bytes(); schema=json.loads(raw.decode('utf-8'))
    d=yaml.safe_load(DATA.read_text(encoding='utf-8'))
    if d.get('unit')!='U-PGD-10-WORK-CONTEXT-BROADCAST-NORMATIVE': fail('unit')
    if d.get('contract_version')!='pgh-work-context-broadcast/1': fail('contract-version')
    refs=d.get('runtime_reference') or {}
    if refs.get('closure_commit')!='f5047f72914c6634982df30c8ce0f8747af5cfb3': fail('runtime-closure')
    if refs.get('schema_sha256')!=RUNTIME_SCHEMA_SHA or refs.get('policy_sha256')!=RUNTIME_POLICY_SHA: fail('runtime-fingerprint')
    if hashlib.sha256(raw).hexdigest()!=RUNTIME_SCHEMA_SHA: fail('schema-byte-equivalence')
    if schema.get('properties',{}).get('schema_version',{}).get('const')!='pgh-work-context-broadcast/1': fail('schema-id')
    inv=d.get('normative_invariants') or {}
    required_true=['every_botv2_update','fallback_generation_required','self_delivery','canonical_verification_required','no_second_broker','no_second_scheduler','piggyback_next_order','standalone_when_no_actionable_work','watermark_per_destination','coalescing_preserves_event_ids']
    if any(inv.get(k) is not True for k in required_true): fail('invariants')
    if inv.get('agent_relevance_decision') is not False: fail('agent-relevance')
    nc=d.get('no_change') or {}
    if nc.get('audit_required') is not True or nc.get('fanout') is not False or nc.get('purpose')!='prevent_feedback_loop': fail('no-change')
    wm=d.get('watermark') or {}
    if wm.get('same_revision_same_payload')!='IDEMPOTENT' or wm.get('same_revision_different_payload')!='CONFLICT' or wm.get('older_revision')!='STALE': fail('watermark')
    ritual=d.get('mandatory_ritual') or {}
    if ritual.get('every_work_completion') is not True or ritual.get('every_sync_update') is not True: fail('ritual-frequency')
    if ritual.get('agent_may_skip') is not False: fail('ritual-skip')
    if ritual.get('explicit_delta_preferred') is not True or ritual.get('fallback_if_missing') is not True: fail('fallback')
    if ritual.get('after_receive_only_no_new_work')!='emit_NO_CHANGE_audit_without_fanout': fail('anti-echo')
    trees=d.get('systemic_tree_integration') or {}
    if trees.get('consumer_unit')!='U-PGD-09-SYSTEMIC-ONTOLOGICAL-TREES' or trees.get('tree_delta_over_wcb') is not True: fail('tree-integration')
    if d.get('runtime_owner')!='debianlima/pgh-distributed-session-control-plane' or d.get('runtime_parallel_created') is not False: fail('runtime-boundary')
    if d.get('project_skill_change_required')!='NO_IMMUTABLE_U08': fail('skill-boundary')
    gates=d.get('gates') or {}
    required=['DELTA_INVENTORY','LEARNING_PRESERVED','WCB_RUNTIME_CLOSED','WCB_SCHEMA_EQUIVALENCE','WCB_MANDATORY_RITUAL','WCB_FALLBACK','WCB_NO_CHANGE_ANTI_ECHO','WCB_SELF_DELIVERY','WCB_WATERMARK','WCB_COALESCING','WCB_PIGGYBACK','WCB_STANDALONE','NO_SECOND_RUNTIME','SYSTEMIC_TREE_INTEGRATION','RELEASE_IMMUTABILITY','RECONCILIATION_CLOSURE','DEPENDENCY_REFERENCES']
    if any(gates.get(k)!='PASS' for k in required): fail('gates')
    text=DOC.read_text(encoding='utf-8')
    for marker in ('pgh-work-context-broadcast/1','toda atualização/finalização','NO_CHANGE','self-origin','watermark','piggyback','15 minutos','U-PGD-09','não cria segundo scheduler'):
        if marker not in text: fail('doc:'+marker)
    print('PGD_WCB_U10=PASS SCHEMA_EQUIVALENCE=PASS RITUAL=PASS ANTI_ECHO=PASS TREE_INTEGRATION=PASS')
if __name__=='__main__': main()
