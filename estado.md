# Estado — PGD 1.0.0 — contrato v2

## Decisões vigentes
- PGH autoriza; PGD executa.
- PGD possui estado runtime vivo, scheduler, filas, leases, workers, heartbeat, recovery e Outcome/Efficacy.
- PGD não amplia autoridade recebida de PGA/PGH.
- Decisão humana de 31/08/2026: o papel `auxiliar` participa da construção e da conciliação incremental do PGD; concluído `PGD_AUXILIAR_RECONCILIATION=PASS`, a sequência habilita o auxiliar no PGA.

## Decisões superadas
- PGD 0.1.0 como estado de repouso standalone — superado pela unidade U-PGD-02 de release 1.0.

## Decisões humanas pendentes
- Nenhuma.

## Pendências técnicas não humanas
- Nenhuma local para U-PGD-03 após o gate auxiliar. A sequência seguinte pertence ao PGA e só abre depois de `PGD_AUXILIAR_RECONCILIATION=PASS`.

## Trabalho compartilhado
- ponteiro: `manifesto.yaml.trabalho_compartilhado` — vazio; U-PGD-03 encerrada após `PGD_AUXILIAR_RECONCILIATION=PASS`.

## Competências ativas nesta unidade
- `pgd-project@0.1.0` — skill de projeto; não alterada, pois a homologação não produziu novo aprendizado de skill.
- `desenvolvedor-de-software@15`.
- `github-incremental-reconciliation@7`.

## Divergências da última reconciliação
- corrigidas: política operacional pós-release registra o auxiliar na construção/conciliação do PGD sem transferir autoridade nem alterar o contrato/release 1.0.0; sequência PGD → PGA tornada verificável por gate.
- pendentes de autorização: nenhuma.

## Entradas aceitas
- 1–13.

## Próxima unidade
- PGA: incluir o mesmo papel auxiliar em construção/conciliação somente após `PGD_AUXILIAR_RECONCILIATION=PASS`.
