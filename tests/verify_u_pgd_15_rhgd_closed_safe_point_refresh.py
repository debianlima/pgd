#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, subprocess
from pathlib import Path
import yaml

ROOT=Path(__file__).resolve().parents[1]
DATA=ROOT/'dados/pgd-1.0/U-PGD-15-rhgd-closed-safe-point-refresh.yaml'
DOC=ROOT/'docs/U-PGD-15-rhgd-closed-safe-point-refresh.md'
RHGD_SAFE='c74daa217f307b1fb8d78e10fe5218d8e496dbd8'
RHGD_ACTIVE_UNIT='U-RHGD-12-LIVE-CAPABILITY-DISCOVERY-CONTRACT'
PGD_FED='contratos/pgd-1.0/rhgd-federation.schema.json'
PGD_FED_SHA='3135f6cee8de163d55c9782b1b1de300359a0e2936f79f2a243a03941fefdc52'

def fail(x):
    print('PGD_U15_RHGD_CLOSED_SAFE_POINT_REFRESH=FAIL',x)
    raise SystemExit(2)

def git(repo,*args):
    return subprocess.check_output(['git','-C',str(repo),*args],text=True).strip()

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--suite-root',type=Path); args=ap.parse_args()
    if not DATA.exists(): fail('missing-data')
    if not DOC.exists(): fail('missing-doc')
    d=yaml.safe_load(DATA.read_text(encoding='utf-8'))
    if d.get('schema')!='pgd-rhgd-closed-safe-point-refresh/1': fail('schema')
    if d.get('unit')!='U-PGD-15-RHGD-CLOSED-SAFE-POINT-REFRESH': fail('unit')
    refs=d['refs']
    if refs['RHGD_CLOSED_SAFE_POINT']!=RHGD_SAFE: fail('safe-point')
    if refs['RHGD_PROJECT_SKILL']!='0.0.10': fail('skill')
    if refs['PGD_FEDERATION_CONTRACT_SHA256']!=PGD_FED_SHA: fail('pgd-contract-hash')
    observed=d['observed']
    if observed['rhgd_active_unit']!=RHGD_ACTIVE_UNIT: fail('active-unit')
    if observed['rhgd_active_unit_consumed'] is not False: fail('active-unit-consumed')
    if observed['consumer_rule']!='consume_last_closed_safe_point_not_in_progress_head': fail('consumer-rule')
    if d['authority']!={'PGD':'runtime_scheduler_execution','RHGD':'discovery_federation_transport_no_scheduler'}: fail('authority')
    gates=d['gates']
    expected={
      'DELTA_INVENTORY':'PASS','LEARNING_PRESERVED':'PASS','RHGD_SAFE_POINT_CLOSED':'PASS',
      'RHGD_SAFE_POINT_ANCESTOR':'PASS','RHGD_U12_ACTIVE_NOT_CONSUMED':'PASS','PGD_FEDERATION_CONTRACT_IDENTITY':'PASS',
      'NO_DUPLICATE_RUNTIME':'PASS','HISTORICAL_EVIDENCE_IMMUTABLE':'PASS','RELEASE_IMMUTABILITY':'PASS',
      'FUNCTIONAL_PGD_CHANGE_REQUIRED':'NO'
    }
    if gates!=expected: fail('gates')
    text=DOC.read_text(encoding='utf-8')
    for marker in ('c74daa217f30','U-RHGD-12','safe point fechado','não consome','execution_ref','v1.0.0'):
        if marker not in text: fail('doc:'+marker)
    if args.suite_root:
        rhgd=args.suite_root/'rhgd'
        if not rhgd.joinpath('.git').exists(): fail('missing-rhgd')
        subprocess.check_call(['git','-C',str(rhgd),'merge-base','--is-ancestor',RHGD_SAFE,'HEAD'])
        safe_manifest=yaml.safe_load(git(rhgd,'show',f'{RHGD_SAFE}:manifesto.yaml'))
        if safe_manifest.get('trabalho_compartilhado'): fail('safe-point-not-closed')
        if safe_manifest.get('versao_contrato')!=4: fail('safe-contract-version')
        entries={e['id']:e for e in safe_manifest.get('entradas',[])}
        if any(entries[i]['status']!='aceito' for i in (44,45,46,47)): fail('u11-not-accepted')
        skill=git(rhgd,'show',f'{RHGD_SAFE}:skills/rhgd/SKILL.md')
        if 'versao: 0.0.10' not in skill: fail('safe-skill-version')
        observed_active=refs['RHGD_OBSERVED_ACTIVE_HEAD']
        subprocess.check_call(['git','-C',str(rhgd),'merge-base','--is-ancestor',observed_active,'HEAD'])
        observed_manifest=yaml.safe_load(git(rhgd,'show',f'{observed_active}:manifesto.yaml'))
        observed_sw=observed_manifest.get('trabalho_compartilhado') or {}
        if observed_sw.get('unidade')!=RHGD_ACTIVE_UNIT: fail('observed-u12-not-active')
        if hashlib.sha256((ROOT/PGD_FED).read_bytes()).hexdigest()!=PGD_FED_SHA: fail('pgd-fed-local-hash')
        print('RHGD_CLOSED_SAFE_POINT_EXTERNAL=PASS')
    print('PGD_U15_RHGD_CLOSED_SAFE_POINT_REFRESH=PASS')
if __name__=='__main__': main()
