from pathlib import Path
import re
r=Path(__file__).resolve().parents[1]
req=['README.md','VERSION','manifesto.yaml','competencias.yaml','estado.md','lexico.yaml','skills/pgd/SKILL.md','docs/U-PGD-01-msgcd-u20-handoff.md']
assert all((r/x).exists() for x in req)
assert len(list(r.glob('skills/*/SKILL.md')))==1
assert (r/'VERSION').read_text().strip()=='0.1.0'
assert 'PGH autoriza; PGD executa' in (r/'docs/U-PGD-01-msgcd-u20-handoff.md').read_text(encoding='utf-8')
print('PGD_PROJECT_VERIFY=PASS')
