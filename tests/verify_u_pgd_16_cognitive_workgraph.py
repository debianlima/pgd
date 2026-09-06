from pathlib import Path
import json, yaml, jsonschema
R=Path(__file__).resolve().parents[1]
S=R/'contratos/pgd-1.0/cognitive-workgraph.schema.json'
E=R/'dados/pgd-1.0/U-PGD-16-cognitive-workgraph.yaml'
D=R/'docs/U-PGD-16-cognitive-workgraph.md'
T=R/'dados/pgd-1.0/U-PGD-16-telemetria-inicio.json'

def barrier_satisfied(required, completed):
    return set(required) <= set(completed)

def main():
    assert T.exists() and json.loads(T.read_text())['event']=='telemetria_inicio'
    assert S.exists() and E.exists() and D.exists()
    schema=json.loads(S.read_text(encoding='utf-8')); jsonschema.Draft202012Validator.check_schema(schema)
    ev=yaml.safe_load(E.read_text(encoding='utf-8')); jsonschema.validate(ev,schema)
    a=ev['authority']
    assert a=={'execution_owner':'PGD','scheduler_owner':'PGD','lease_authority':'PGD','ia_geral_role':'ADVISORY_PLAN_ONLY','rhgd_role':'FEDERATION_DISCOVERY_TRANSPORT_ONLY','msgcd_role':'COMPOSITION_AFTER_COMPLETION_BARRIER'}
    assert ev['source_plans']['context_segmentation_plan_ref'].startswith('ContextSegmentationPlan:')
    assert ev['source_plans']['result_aggregation_plan_ref'].startswith('ResultAggregationPlan:')
    units=ev['work_units']; assert len(units)>=3
    ids={u['work_unit_id'] for u in units}; assert len(ids)==len(units)
    for u in units:
        assert u['authorization_ref'] and u['idempotency_key'] and u['target_capability_ref']
        assert u['token_budget']>0 and u['privacy_scope'] in {'private','organization','team','public'}
        assert u['work_kind'] in {'COGNITIVE','TOOL_PREPROCESS','PHYSICAL_CHUNK'}
        assert set(u['dependency_refs']) <= ids
        assert u['lease_requested_only'] is True and u['lease_granted_by']=='PGD'
        if u['work_kind']=='TOOL_PREPROCESS':
            assert u['tool_ref'] and u['tool_authority']=='none' and u['tool_output_provenance_required'] is True
    b=ev['completion_barrier']
    assert set(b['required_segment_ids']) <= set(b['expected_segment_ids'])
    assert b['completion_owner']=='PGD' and b['composition_owner']=='MSGCD'
    assert b['reject_missing_required_segments'] is True
    assert barrier_satisfied(b['required_segment_ids'], b['proof']['before_completed_segment_ids']) is False
    assert b['proof']['before_result']=='WAIT_REQUIRED_SEGMENTS'
    assert barrier_satisfied(b['required_segment_ids'], b['proof']['after_completed_segment_ids']) is True
    assert b['proof']['after_result']=='READY_FOR_MSGCD_COMPOSITION'
    assert ev['no_second_scheduler'] is True and ev['no_inference_level_scheduler'] is True
    txt=D.read_text(encoding='utf-8')
    for m in ('ContextSegmentationPlan','ResultAggregationPlan','PGD','RHGD','MSGCD','TOOL_PREPROCESS','WAIT_REQUIRED_SEGMENTS'):
        assert m in txt
    print('PGD_U16_COGNITIVE_WORKGRAPH=PASS')
if __name__=='__main__': main()
