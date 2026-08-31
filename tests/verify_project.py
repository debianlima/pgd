from pathlib import Path
import json, yaml, jsonschema
r=Path(__file__).resolve().parents[1]
req=['README.md','VERSION','manifesto.yaml','competencias.yaml','estado.md','lexico.yaml','skills/pgd/SKILL.md','docs/U-PGD-01-msgcd-u20-handoff.md','contratos/pgd-1.0/release.schema.json','dados/pgd-1.0/U-PGD-02-release-evidence.yaml','docs/U-PGD-02-release-1.0.md','tests/verify_release_1_0.py']
assert all((r/x).exists() for x in req)
assert len(list(r.glob('skills/*/SKILL.md')))==1
assert (r/'VERSION').read_text().strip()=='1.0.0'
m=yaml.safe_load((r/'manifesto.yaml').read_text(encoding='utf-8'))
assert m['versao_contrato']==2 and m['release_alvo']=='v1.0.0'
assert 'PGH autoriza; PGD executa' in (r/'docs/U-PGD-01-msgcd-u20-handoff.md').read_text(encoding='utf-8')
s=json.loads((r/'contratos/pgd-1.0/release.schema.json').read_text(encoding='utf-8'))
e=yaml.safe_load((r/'dados/pgd-1.0/U-PGD-02-release-evidence.yaml').read_text(encoding='utf-8'))
jsonschema.validate(e,s)
print('PGD_PROJECT_VERIFY=PASS VERSION=1.0.0')
