# PGD — Protocolo de Gestão Distribuída

Repositório standalone inicial do PGD, materializado a partir do handoff preservado no PGH 2.0 candidato.

**Regra central:** PGH autoriza; PGD executa.

## Identidade da execução — H01-R2

Decisão humana de 31/08/2026: este repositório `debianlima/pgd` permanece a fonte do protocolo, contratos e evidências do PGD. A implementação canônica do estado vivo de execução é `debianlima/pgh-distributed-session-control-plane`, cujo nome histórico é preservado.

Não se cria scheduler, fila, executor, lease manager, worker control plane ou runtime paralelo neste repositório para duplicar a implementação canônica. Renome, sucessão ou migração dessa linhagem exige nova decisão humana versionada.

Gate de identidade: `PGD_IDENTITY_H01_R2=PASS`.

O PGD possui estado vivo de execução: WorkSession, DAG/TaskQueue, ResourcePool/ResourceLease, workers, heartbeat, retry, checkpoint, relocation, recovery, permissões operacionais e Outcome/Efficacy.

Origem normativa: debianlima/protocolo-governanca-heterogenea@a68ba9b460bd1d2050d57873fdc1c648732ece07, documento docs/pgd/U-PGD-01-msgcd-u20-handoff.md.

## Release 1.0

PGD 1.0 é homologado somente dentro da tríade PGH 2.0 + PGD 1.0 + PGA 1.0; a evidência e os gates locais vivem em `dados/pgd-1.0/` e `tests/verify_release_1_0.py`.
