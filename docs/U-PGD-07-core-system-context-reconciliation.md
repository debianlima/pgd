# U-PGD-07 — reconciliação PGD com U250/U255

## Resultado

A dependência que interrompeu U-PGD-06 foi removida: U250/U255 foram fechadas no PGH e o runtime U250 foi fechado no `pgh-distributed-session-control-plane`. Esta unidade reconcilia o PGD pós-release sem reabrir nem mover `v1.0.0`.

A fronteira permanece: **PGH autoriza/contextualiza; PGD executa**. U250 adiciona o invariante de reconciliação operacional, mas não transfere o scheduler ao PGH. O `OperationalReconciliationCoordinator` vive na implementação canônica PGD/control-plane em `f033b622ce6a3e59f4a3d2d29f903b3f4a267b32`.

## Ownership reconciliado

- PGH: triggers, invariantes, semântica, evidência e proveniência.
- PGA: política, autoridade e gates.
- PGD: assignment, dispatch, filas, leases, scheduler, retry/recovery e estado runtime vivo.
- RHGD: federação sem segundo scheduler.
- Supervisor: transporte de ordens preconstruídas, sem replanning por padrão.

O ciclo operacional padrão de 60 minutos reutiliza `RouterStore.scheduler_state`; fencing de assignment reutiliza `DynamicSyncCoordinator.task_assignments.assignment_epoch`; Bot V2 preserva `command_id + round_id + base_revision`.

## Context-sync e visão sistêmica

`PGH-SUITE-SYSTEM-VISION-1` é orientação arquitetural compartilhada, não nova autoridade. `context-sync` reutiliza `pgh.dynamic-sync`: PGH mantém autoridade semântica; PGD aplica transporte/estado operacional; PGA governa política. Não foi criado broker ou scheduler paralelo.

A decisão posterior PGDMD×PGA não altera esta fronteira: PGDMD é protocolo acessório de governança de domínio sob PGA e não assume tarefas, filas, leases ou runtime do PGD.

## Release e compatibilidade

O release permanece `1.0.0`; a tag `v1.0.0` continua apontando para `366388d8c52f696d81b7277075b87e8fc144ca1b`. A unidade é pós-release e somente adiciona reconciliação/evidência. A skill `pgd-project@0.2.0` já declara scheduler, DAG, filas, leases, workers, heartbeat, recovery, transport e runtime, portanto nenhum bump artificial de skill é necessário.

## Gates

`DELTA_INVENTORY=PASS`, `LEARNING_PRESERVED=PASS`, `UPSTREAM_CORE_SAFE_POINT=PASS`, `U250_OPERATIONAL_RECONCILIATION=PASS`, `U255_SYSTEM_VISION=PASS`, `AUTHORITY_BOUNDARY=PASS`, `CONTEXT_SYNC_BOUNDARY=PASS`, `NO_DUPLICATE_PGD_RUNTIME=PASS`, `RELEASE_IMMUTABILITY=PASS`, `RECONCILIATION_CLOSURE=PASS` e `DEPENDENCY_REFERENCES=PASS`.
