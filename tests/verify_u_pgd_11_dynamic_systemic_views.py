#!/usr/bin/env python3
from pathlib import Path
import json,yaml,jsonschema
ROOT=Path(__file__).resolve().parents[1]
SCHEMA=ROOT/'contratos/pgd-1.0/systemic-view-sync.schema.json'
DATA=ROOT/'dados/pgd-1.0/U-PGD-11-dynamic-systemic-views.yaml'
DOC=ROOT/'docs/U-PGD-11-dynamic-systemic-views.md'
def fail(x): print('PGD_DYNAMIC_SYSTEMIC_VIEWS_U11=FAIL',x); raise SystemExit(2)
def main():
    for p in (SCHEMA,DATA,DOC):
        if not p.exists(): fail('missing:'+str(p.relative_to(ROOT)))
    schema=json.loads(SCHEMA.read_text(encoding='utf-8'))
    d=yaml.safe_load(DATA.read_text(encoding='utf-8'))
    if d.get('unit')!='U-PGD-11-DYNAMIC-SYSTEMIC-VIEWS': fail('unit')
    if d.get('contract_version')!='pgd-systemic-view-sync/1': fail('version')
    if d.get('depends_on')!=['U-PGD-09-SYSTEMIC-ONTOLOGICAL-TREES','U-PGD-10-WORK-CONTEXT-BROADCAST-NORMATIVE']: fail('deps')
    boot=d.get('project_bootstrap') or {}
    if boot.get('on_project_create_or_enable')!='materialize_macro_map_and_component_interconnections': fail('bootstrap')
    if boot.get('derive_from')!=['manifest','contracts','runtime_inventory','authority_refs','existing_tree_refs']: fail('derive')
    if boot.get('global_rescan_default') is not False: fail('global-rescan')
    maps=set((d.get('macro_maps') or {}).keys())
    if maps!={'PROJECT_MAP','INFRASTRUCTURE_MAP','RESOURCE_MAP','AUTHORIZATION_MAP','TASK_MAP'}: fail('maps')
    infra=d['macro_maps']['INFRASTRUCTURE_MAP']
    if infra.get('entrypoint')!='macro_map_then_relevant_branch': fail('infra-entrypoint')
    if set(infra.get('indexes') or []) < {'machine','resource','queue','reservation','lease','location','capability','project_ref','peer_ref'}: fail('infra-indexes')
    write=d.get('write_back') or {}
    if set(write.get('channels') or [])!={'DIRECT_STORE','WEB_EXECUTOR'}: fail('channels')
    if write.get('direct_store')!='update_canonical_graph_store_then_emit_WCB' or write.get('web_executor')!='submit_graph_mutation_to_executor_then_emit_WCB_on_commit': fail('write-back')
    if write.get('every_mutation_requires_tree_update') is not True or write.get('every_tree_update_requires_broadcast') is not True: fail('write-frequency')
    local=d.get('agent_local_view') or {}
    if local.get('shared_base_required') is not True or local.get('private_index_allowed') is not True: fail('local-view')
    if local.get('private_index_is_authority') is not False: fail('private-authority')
    if local.get('on_broadcast')!='compare_base_revision_hash_then_apply_or_refetch_impacted_branch': fail('local-sync')
    if local.get('private_index_rebase_required_on_base_change') is not True: fail('private-rebase')
    task=d.get('task_coordination') or {}
    req={'task_dependencies','allocated_agents','linked_resources','queue_refs','reservation_refs','lease_refs','project_ref','status','authority_refs'}
    if not req.issubset(set(task.get('task_node_indexes') or [])): fail('task-indexes')
    if task.get('on_task_change')!='recompute_impacted_task_branch_links_then_emit_WCB' or task.get('agent_reads_own_task_in_project_task_tree') is not True: fail('task-ritual')
    pgh=d.get('pgh_projection') or {}
    if pgh.get('consumer')!='PGH_2_0' or pgh.get('retrieval')!='macro_map_to_tree_node_to_HRAG_RAG_refs': fail('pgh-projection')
    if pgh.get('root_instruction_repeated') is not True: fail('root-instruction')
    if pgh.get('canonical_state_replacement') is not False: fail('canonical-replacement')
    security=d.get('security') or {}
    if security.get('auth_tree_secret_material') is not False or security.get('credential_value_in_broadcast') is not False: fail('secrets')
    example=d.get('example_view') or {}
    jsonschema.validate(example,schema)
    if example.get('view_kind')!='INFRASTRUCTURE_MAP' or example.get('base_revision')!=12: fail('example')
    gates=d.get('gates') or {}
    required=['DELTA_INVENTORY','LEARNING_PRESERVED','U09_TREE_CONTRACT','U10_WCB_CONTRACT','VIEW_SCHEMA','PROJECT_BOOTSTRAP','MACRO_MAPS','DIRECT_WRITE_BACK','WEB_EXECUTOR_WRITE_BACK','LOCAL_VIEW_REBASE','TASK_DYNAMIC_LINKS','PGH_HRAG_RAG_PROJECTION','AUTH_NO_SECRETS','MANDATORY_REPETITION','NO_SECOND_RUNTIME','RELEASE_IMMUTABILITY','RECONCILIATION_CLOSURE','DEPENDENCY_REFERENCES']
    if any(gates.get(k)!='PASS' for k in required): fail('gates')
    text=DOC.read_text(encoding='utf-8')
    for marker in ('mapa macro inicial','DIRECT_STORE','WEB_EXECUTOR','base_revision','private index','TaskTree','agente','recursos','dependências','HRAG/RAG','WCB','repetitivo'):
        if marker not in text: fail('doc:'+marker)
    print('PGD_DYNAMIC_SYSTEMIC_VIEWS_U11=PASS BOOTSTRAP=PASS WRITEBACK=PASS LOCAL_REBASE=PASS TASK_LINKS=PASS HRAG_RAG=PASS')
if __name__=='__main__': main()
