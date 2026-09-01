#!/usr/bin/env python3
from pathlib import Path
import json,yaml,jsonschema
ROOT=Path(__file__).resolve().parents[1]
SCHEMA=ROOT/'contratos/pgd-1.0/systemic-tree.schema.json'
DATA=ROOT/'dados/pgd-1.0/U-PGD-09-systemic-ontological-trees.yaml'
DOC=ROOT/'docs/U-PGD-09-systemic-ontological-trees.md'
def fail(x): print('PGD_SYSTEMIC_TREES_U09=FAIL',x); raise SystemExit(2)
def main():
    for p in (SCHEMA,DATA,DOC):
        if not p.exists(): fail('missing:'+str(p.relative_to(ROOT)))
    schema=json.loads(SCHEMA.read_text(encoding='utf-8'))
    d=yaml.safe_load(DATA.read_text(encoding='utf-8'))
    if d.get('unit')!='U-PGD-09-SYSTEMIC-ONTOLOGICAL-TREES': fail('unit')
    if d.get('contract_version')!='pgd-systemic-tree/1': fail('contract-version')
    if d.get('wcb_dependency')!='f5047f72914c6634982df30c8ce0f8747af5cfb3': fail('wcb-ref')
    kinds=set((d.get('tree_kinds') or {}).keys())
    if kinds!={'PROJECT_TREE','RESOURCE_TREE','AUTH_TREE','TASK_TREE'}: fail('tree-kinds')
    tt=d['tree_kinds']['TASK_TREE']
    if tt.get('cardinality')!='one_per_enabled_project': fail('task-tree-cardinality')
    for name in ('PROJECT_TREE','RESOURCE_TREE','AUTH_TREE','TASK_TREE'):
        k=d['tree_kinds'][name]
        if k.get('internal_model')!='typed_DAG': fail('dag:'+name)
        if k.get('visual_projection')!='hierarchical_A_plus': fail('visual:'+name)
    auth=d['tree_kinds']['AUTH_TREE']
    if auth.get('secret_material_allowed') is not False: fail('auth-secret')
    required_node_types={'project','task','resource','agent','machine','queue','reservation','lease','capability','auth_binding','peer'}
    if not required_node_types.issubset(set(d.get('node_types') or [])): fail('node-types')
    required_edges={'HAS_TASK','DEPENDS_ON','HAS_RESOURCE','QUEUED_IN','RESERVED_BY','LEASED_TO','AUTHORIZED_BY','LOCATED_AT','ASSIGNED_TO_PROJECT','RUNS_ON','PEER_REF','DERIVED_FROM'}
    if not required_edges.issubset(set(d.get('edge_predicates') or [])): fail('edge-predicates')
    remote=d.get('remote_subtrees') or {}
    for k in ('peer_id','tree_kind','tree_ref','revision','content_hash','authority_ref','last_verified_at'):
        if k not in remote.get('required_fields',[]): fail('remote-field:'+k)
    rag=d.get('rag_navigation') or {}
    if rag.get('node_rag_refs_required') is not True or rag.get('retrieval_terms_required') is not True: fail('rag')
    instruction=str(rag.get('agent_instruction') or '')
    if 'árvore de visão sistêmica' not in instruction or 'RAG' not in instruction or 'nó' not in instruction: fail('instruction')
    ritual=d.get('mandatory_ritual') or {}
    if ritual.get('before_decision')!='compare_local_tree_revision_with_latest_applied_WCB_then_sync_if_stale': fail('before-decision')
    if ritual.get('after_mutation')!='update_impacted_tree_nodes_then_emit_WCB_tree_delta': fail('after-mutation')
    if ritual.get('every_work_completion') is not True or ritual.get('every_broadcast_receive') is not True: fail('ritual-frequency')
    delta=d.get('wcb_tree_delta') or {}
    required_delta={'tree_id','tree_kind','from_revision','to_revision','tree_hash','delta_ref','changed_node_ids','invalidated_node_ids','remote_refs_changed','canonical_verification_required'}
    if set(delta.get('required_fields') or [])!=required_delta: fail('delta-fields')
    storage=d.get('storage_model') or {}
    if storage.get('canonical')!='SQLite_relational_graph_projection' or storage.get('local_cache')!='SQLite_plus_RAG_refs': fail('storage')
    if storage.get('indexing')!='B_tree_indices_plus_ontology_edges': fail('indexing')
    if storage.get('raw_secret_storage') is not False: fail('raw-secret-storage')
    example=d.get('example_resource_tree') or {}
    jsonschema.validate(example,schema)
    # Resource example must encode queue/reservation/project/peer relations.
    node_types={n['node_type'] for n in example['nodes']}
    if not {'resource','queue','reservation','project','peer'}.issubset(node_types): fail('resource-example-nodes')
    preds={e['predicate'] for e in example['edges']}
    if not {'QUEUED_IN','RESERVED_BY','ASSIGNED_TO_PROJECT','PEER_REF'}.issubset(preds): fail('resource-example-edges')
    gates=d.get('gates') or {}
    required=['DELTA_INVENTORY','LEARNING_PRESERVED','WCB_DEPENDENCY','TREE_SCHEMA','PROJECT_TREE','RESOURCE_TREE','AUTH_TREE','TASK_TREE','REMOTE_PEER_REFS','RAG_NAVIGATION','AUTH_NO_SECRETS','MANDATORY_TREE_RITUAL','RECONCILIATION_CLOSURE','DEPENDENCY_REFERENCES']
    if any(gates.get(k)!='PASS' for k in required): fail('gates')
    skill=(ROOT/'skills/pgd/SKILL.md').read_text(encoding='utf-8')
    if 'versao: 0.2.0' not in skill: fail('ratified-skill-version')
    if d.get('project_skill_change_required')!='NO_IMMUTABLE_U08': fail('skill-boundary')
    text=DOC.read_text(encoding='utf-8')
    for marker in ('ProjectTree','ResourceTree','AuthTree','TaskTree','remote_subtrees','árvore de visão sistêmica','RAG','WCB','segredos'):
        if marker not in text: fail('doc:'+marker)
    print('PGD_SYSTEMIC_TREES_U09=PASS TREES=4 DAG=PASS REMOTE_PEERS=PASS RAG=PASS AUTH_NO_SECRETS=PASS')
if __name__=='__main__': main()
