#!/usr/bin/env python3
from pathlib import Path
import json,yaml,jsonschema
ROOT=Path(__file__).resolve().parents[1]
SCHEMA=ROOT/'contratos/pgd-1.0/operational-context-forest.schema.json'
DATA=ROOT/'dados/pgd-1.0/U-PGD-12-operational-context-forest.yaml'
DOC=ROOT/'docs/U-PGD-12-operational-context-forest.md'
def fail(x): print('PGD_OPERATIONAL_CONTEXT_FOREST_U12=FAIL',x); raise SystemExit(2)
def main():
    for p in (SCHEMA,DATA,DOC):
        if not p.exists(): fail('missing:'+str(p.relative_to(ROOT)))
    schema=json.loads(SCHEMA.read_text(encoding='utf-8'))
    d=yaml.safe_load(DATA.read_text(encoding='utf-8'))
    if d.get('unit')!='U-PGD-12-OPERATIONAL-CONTEXT-FOREST': fail('unit')
    if d.get('contract_version')!='pgd-operational-context-forest/1': fail('version')
    if d.get('depends_on')!=['U-PGD-09-SYSTEMIC-ONTOLOGICAL-TREES','U-PGD-10-WORK-CONTEXT-BROADCAST-NORMATIVE','U-PGD-11-DYNAMIC-SYSTEMIC-VIEWS']: fail('deps')
    graphs=d.get('graphs') or {}
    required={'SYSTEM_NAVIGATOR','PROJECT','TASK','RESOURCE','AUTHORIZATION','CAPABILITY_ROUTING','KNOWLEDGE','ARTIFACT','STATE_HEALTH','COMMUNICATION','PROVENANCE_FRESHNESS','PEER_FEDERATION'}
    if set(graphs)!=required: fail('graphs')
    nav=graphs['SYSTEM_NAVIGATOR']
    if nav.get('root') is not True or nav.get('intent_to_graph_routing') is not True or nav.get('global_scan_default') is not False: fail('navigator')
    res=graphs['RESOURCE']
    if set(res.get('indexes') or []) < {'resource','machine','location','queue','reservation','lease','project_ref','task_ref','capability_refs','competency_refs','skill_refs','peer_ref'}: fail('resource-indexes')
    cap=graphs['CAPABILITY_ROUTING']
    if cap.get('route')!='task_or_requirement_to_capability_to_competency_to_agent_or_resource': fail('capability-route')
    if cap.get('resource_load_resolves_associated_competencies') is not True: fail('resource-competency-load')
    if cap.get('skill_authority')!='catalog_linha_homologada_only': fail('skill-authority')
    if cap.get('resource_inventory_is_skill_authority') is not False: fail('resource-skill-authority')
    know=graphs['KNOWLEDGE']
    if set(know.get('indexes') or []) < {'contract','documentation','evidence','skill_ref','ontology_ref','hrag_ref','rag_ref','bplus_ref','artifact_ref'}: fail('knowledge')
    prov=graphs['PROVENANCE_FRESHNESS']
    if set(prov.get('required_fields') or []) < {'source_ref','revision','content_hash','observed_at','authority_ref'}: fail('freshness-fields')
    if prov.get('stale_must_sync_before_mutation') is not True: fail('freshness-gate')
    peer=graphs['PEER_FEDERATION']
    if peer.get('full_replication_default') is not False or peer.get('fetch_impacted_branch_only') is not True: fail('peer')
    auth=graphs['AUTHORIZATION']
    if auth.get('secret_material') is not False or auth.get('credential_ref_only') is not True or auth.get('resolver_ref_required') is not True: fail('auth-security')
    task=graphs['TASK']
    if set(task.get('indexes') or []) < {'dependencies','allocated_agents','linked_resources','required_capabilities','competency_refs','queue_refs','reservation_refs','lease_refs','status'}: fail('task')
    edges=d.get('edge_policy') or {}
    if edges.get('backlinks_required') is not True or edges.get('typed_edges_only') is not True: fail('edges')
    if 'PROVIDES_CAPABILITY' not in edges.get('predicates',[]) or 'ASSOCIATED_COMPETENCY' not in edges.get('predicates',[]): fail('capability-edges')
    sync=d.get('synchronization') or {}
    if sync.get('protocol')!='pgh-work-context-broadcast/1' or sync.get('payload')!='GraphDelta+graph_revision+content_hash+refs': fail('sync')
    if sync.get('every_effective_mutation')!='update_impacted_graphs_then_emit_WCB': fail('sync-frequency')
    retrieval=d.get('retrieval') or {}
    if retrieval.get('default_path')!='SystemNavigatorGraph_to_macro_graph_to_node_to_canonical_refs_to_HRAG_RAG_if_needed': fail('retrieval-path')
    if retrieval.get('repeat_root_instruction') is not True: fail('repeat')
    security=d.get('security') or {}
    if security.get('secret_in_graph') is not False or security.get('secret_in_broadcast') is not False: fail('security')
    example=d.get('example_forest') or {}
    jsonschema.validate(example,schema)
    gates=d.get('gates') or {}
    required_gates=['DELTA_INVENTORY','LEARNING_PRESERVED','SYSTEM_NAVIGATOR','GRAPH_COVERAGE','RESOURCE_COMPETENCY_LINKS','CAPABILITY_ROUTING','KNOWLEDGE_ROUTING','PROVENANCE_FRESHNESS','PEER_FEDERATION','BACKLINKS','WCB_GRAPH_DELTA','AUTH_NO_SECRETS','CATALOG_SKILL_AUTHORITY','RELEASE_IMMUTABILITY','RECONCILIATION_CLOSURE','DEPENDENCY_REFERENCES']
    if any(gates.get(k)!='PASS' for k in required_gates): fail('gates')
    text=DOC.read_text(encoding='utf-8')
    for marker in ('SystemNavigatorGraph','CapabilityRoutingGraph','KnowledgeGraph','ProvenanceFreshnessGraph','PeerFederationGraph','competências associadas','linha_homologada','GraphDelta','backlinks','credencial'):
        if marker not in text: fail('doc:'+marker)
    print('PGD_OPERATIONAL_CONTEXT_FOREST_U12=PASS GRAPHS=12 RESOURCE_COMPETENCY_LINKS=PASS CAPABILITY_ROUTING=PASS FRESHNESS=PASS PEERS=PASS')
if __name__=='__main__': main()
