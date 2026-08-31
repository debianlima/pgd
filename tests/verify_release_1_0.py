#!/usr/bin/env python3
from pathlib import Path
import json, re, sys, yaml, jsonschema
ROOT=Path(__file__).resolve().parents[1]
def fail(x): print('PGD_RELEASE_1_0=FAIL',x); raise SystemExit(2)
S=json.loads((ROOT/'contratos/pgd-1.0/release.schema.json').read_text(encoding='utf-8'))
E=yaml.safe_load((ROOT/'dados/pgd-1.0/U-PGD-02-release-evidence.yaml').read_text(encoding='utf-8'))
jsonschema.validate(E,S)
handoff=(ROOT/'docs/U-PGD-01-msgcd-u20-handoff.md').read_text(encoding='utf-8')
required=['PGH_AUTHORIZATION_REQUIRED','NO_RUNTIME_LEASE_IN_PGH','RESOURCE_STATE_OWNED_BY_PGD','OPERATIONAL_PERMISSION_WITHIN_AUTHORIZATION','OUTCOME_EVIDENCE_OBSERVED_ONLY','SESSION_PROVENANCE_COMPLETE','HUMAN_TAKEOVER_PROVENANCE','NO_SECRET_IN_SESSION_STREAM','EFFECT_VERIFICATION_NE_PROCESS_EXIT']
if 'PGH autoriza; PGD executa' not in handoff: fail('central-boundary')
if any(g not in handoff for g in required): fail('handoff-gates')
if set(E['gates'])!=set(required) or any(E['gates'][g]!='PASS' for g in required): fail('gate-accounting')
if E['implementation_evidence']['rerun_in_this_unit'] is not False: fail('historical-evidence-relabeled')
if (ROOT/'VERSION').read_text().strip()!='1.0.0': fail('version')
m=yaml.safe_load((ROOT/'manifesto.yaml').read_text(encoding='utf-8'))
if m.get('release_alvo')!='v1.0.0' or m.get('versao_contrato')!=2: fail('manifest-release')
print('PGD_RELEASE_1_0=PASS GATES=9/9 IMPLEMENTATION_EVIDENCE=HISTORICAL_OBSERVED_REUSED')
