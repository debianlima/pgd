# Estado — PGD 1.0.0 — contrato v3

## Decisões vigentes
- PGH autoriza; PGD executa.
- PGD possui estado runtime vivo, scheduler, filas, leases, workers, heartbeat, recovery e Outcome/Efficacy.
- PGD não amplia autoridade recebida de PGA/PGH.
- H01-R2, decisão humana de 31/08/2026: `debianlima/pgd` permanece protocolo/contratos/evidências; `debianlima/pgh-distributed-session-control-plane` é a implementação canônica de execução do PGD, com o nome histórico preservado e sem runtime sucessor/paralelo.
- Decisão humana de 31/08/2026: o papel `auxiliar` participa da construção e da conciliação incremental do PGD; concluído `PGD_AUXILIAR_RECONCILIATION=PASS`, a sequência habilita o auxiliar no PGA.

## Decisões superadas
- PGD 0.1.0 como estado de repouso standalone — superado pela unidade U-PGD-02 de release 1.0.

## Decisões humanas pendentes
- Nenhuma.


## Decisões fechadas nesta emenda
- H01-R2 — manter `pgh-distributed-session-control-plane` como nome da implementação canônica do PGD e manter `pgd` como protocolo/especificação separado. Gate: `PGD_IDENTITY_H01_R2=PASS`.

## Pendências técnicas não humanas
- Nenhuma local no PGD: `PGD_AUXILIAR_RECONCILIATION=PASS` já estava fechado e H01-R2 fixa a identidade com `PGD_IDENTITY_H01_R2=PASS`. A sequência seguinte pertence ao PGA.

## Trabalho compartilhado
- ponteiro: `manifesto.yaml.trabalho_compartilhado` — vazio; T-016/H01-R2 encerrada após `PGD_IDENTITY_H01_R2=PASS`.

## Competências ativas nesta unidade
- `pgd-project@0.1.0` — skill de projeto; não alterada, pois a homologação não produziu novo aprendizado de skill.
- `desenvolvedor-de-software@15`.
- `github-incremental-reconciliation@7`.

## Divergências da última reconciliação
- corrigidas: H01-R2 materializado sem renome/migração: `pgd` fica como protocolo e `pgh-distributed-session-control-plane` como implementação canônica de execução; runtime paralelo explicitamente proibido; release 1.0.0 preservada.
- pendentes de autorização: nenhuma.

## Entradas aceitas
- 1–13.

## Próxima unidade
- PGA: continuar construção/conciliação com a dependência PGD fixada por `PGD_AUXILIAR_RECONCILIATION=PASS` + `PGD_IDENTITY_H01_R2=PASS`.
