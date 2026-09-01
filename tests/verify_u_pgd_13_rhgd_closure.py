#!/usr/bin/env python3
from pathlib import Path
import yaml
R=Path(__file__).resolve().parents[1]
D=R/'dados/pgd-1.0/U-PGD-13-rhgd-closure-reconciliation.yaml'
DOC=R/'docs/U-PGD-13-rhgd-closure-reconciliation.md'

def bad(x): print('PGD_U13_RHGD_CLOSURE=FAIL',x); raise SystemExit(2)
def main():
 if not D.exists(): bad('missing-data')
 if not DOC.exists(): bad('missing-doc')
 d=yaml.safe_load(D.read_text(encoding='utf-8'))
 if d.get('schema')!='pgd-rhgd-closure-reconciliation/1': bad('schema')
 refs=d.get('refs') or {}
 expected={'PGD_BASE':'3f7d70e974271a0ee316df9425d5e955225fddd4','RHGD_CLOSURE':'b57baf3381a9c0e28fcfaba0faa7fd2e14cebb9c','PGA':'c151e58adf05339eee7f762fa0a96b401e4b6985','PGH':'304b9914ae44b0ac4240d912bd81f7be87d5a708','RUNTIME_SAFE_POINT':'6c3708aeff692c6eac5ce2a39d134afd64f616df'}
 for k,v in expected.items():
  if refs.get(k)!=v: bad('ref:'+k)
 facts=d.get('facts') or {}
 if facts.get('historical_u04_u05_refs_preserved') is not True: bad('history')
 if facts.get('rhgd_peer_gap_closed') is not True: bad('peer-gap')
 if facts.get('federation_contract')!='pgd-rhgd-federation/1': bad('contract')
 if facts.get('pgd_runtime_owner') is not True: bad('runtime-owner')
 if facts.get('rhgd_second_scheduler') is not False: bad('second-scheduler')
 gates=d.get('gates') or {}
 for k in ('DELTA_INVENTORY','LEARNING_PRESERVED','RHGD_CLOSURE_REF','PGH_REF','PGA_REF','RUNTIME_SAFE_POINT','HISTORICAL_EVIDENCE_IMMUTABLE','AUTHORITY_BOUNDARY','NO_DUPLICATE_RUNTIME','RELEASE_IMMUTABILITY'):
  if gates.get(k)!='PASS': bad('gate:'+k)
 for k in ('RECONCILIATION_CLOSURE','DEPENDENCY_REFERENCES'):
  if gates.get(k) not in ('PENDING','PASS'): bad('gate:'+k)
 state=(R/'estado.md').read_text(encoding='utf-8')
 if 'RHGD peer reconciliado em `b57baf3381a9c0e28fcfaba0faa7fd2e14cebb9c`' not in state: bad('state-peer')
 old=(R/'dados/pgd-1.0/U-PGD-04-lateral-delta-inventory.yaml').read_text(encoding='utf-8')
 if '29194e935b838dd1c4ee4228b515911c5a0bb8e7' not in old: bad('historical-u04-mutated')
 old5=(R/'dados/pgd-1.0/U-PGD-05-rhgd-federation.yaml').read_text(encoding='utf-8')
 if '29194e935b838dd1c4ee4228b515911c5a0bb8e7' not in old5: bad('historical-u05-mutated')
 print('PGD_U13_RHGD_CLOSURE=PASS')
if __name__=='__main__': main()
