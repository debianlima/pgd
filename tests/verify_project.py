from pathlib import Path
import json, yaml, jsonschema
r=Path(__file__).resolve().parents[1]
req=['README.md','VERSION','manifesto.yaml','competencias.yaml','estado.md','lexico.yaml','skills/pgd/SKILL.md','docs/U-PGD-01-msgcd-u20-handoff.md','contratos/pgd-1.0/release.schema.json','dados/pgd-1.0/U-PGD-02-release-evidence.yaml','docs/U-PGD-02-release-1.0.md','tests/verify_release_1_0.py']
assert all((r/x).exists() for x in req)
assert len(list(r.glob('skills/*/SKILL.md')))==1
assert (r/'VERSION').read_text().strip()=='1.0.0'
m=yaml.safe_load((r/'manifesto.yaml').read_text(encoding='utf-8'))
assert isinstance(m['versao_contrato'], int) and m['versao_contrato']>=3 and m['release_alvo']=='v1.0.0'
i=m['identidade_execucao']
assert i['decisao_humana']=='H01-R2'
assert i['repositorio_protocolo']=='debianlima/pgd'
assert i['repositorio_implementacao_canonica']=='debianlima/pgh-distributed-session-control-plane'
assert i['nome_implementacao_preservado'] is True and i['runtime_paralelo_proibido'] is True and i['sucessor_novo'] is False
assert i['gate']=='PGD_IDENTITY_H01_R2=PASS'
assert 'H01-R2' in (r/'README.md').read_text(encoding='utf-8')
assert 'debianlima/pgh-distributed-session-control-plane' in (r/'README.md').read_text(encoding='utf-8')
a=m['auxiliar_construcao_conciliacao']
assert a['habilitado'] is True
assert a['natureza']=='politica_operacional_pos_release' and a['preserva_release_v1_0_0'] is True
assert a['papel']=='auxiliar' and a['ordem']==1 and a['protocolo']=='PGD'
assert a['participa_em']==['construcao','conciliacao_incremental']
assert a['gate_saida']=='PGD_AUXILIAR_RECONCILIATION=PASS' and a['proximo_protocolo']=='PGA'
assert 'nao_substitui_decisao_humana' in a['limites']
assert 'PGH autoriza; PGD executa' in (r/'docs/U-PGD-01-msgcd-u20-handoff.md').read_text(encoding='utf-8')
s=json.loads((r/'contratos/pgd-1.0/release.schema.json').read_text(encoding='utf-8'))
e=yaml.safe_load((r/'dados/pgd-1.0/U-PGD-02-release-evidence.yaml').read_text(encoding='utf-8'))
jsonschema.validate(e,s)
print('PGD_PROJECT_VERIFY=PASS VERSION=1.0.0')
