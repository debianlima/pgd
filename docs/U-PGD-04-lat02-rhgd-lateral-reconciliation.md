# U-PGD-04 / LAT-02 — conciliação lateral PGD ↔ RHGD

## Escopo

Este lado da dupla é **PGD**. O Core PGH 2.0 foi usado somente como referência canônica de leitura; nenhum arquivo do Core ou do RHGD foi alterado.

Referências congeladas da auditoria:
- PGD base: `366388d8c52f696d81b7277075b87e8fc144ca1b`;
- RHGD: `29194e935b838dd1c4ee4228b515911c5a0bb8e7`;
- Core de leitura: `2df5f0a98f201293fe278c54ea7fd2c483102119`.

`DELTA_INVENTORY=PASS` e `LEARNING_PRESERVED=PASS` precedem esta normalização lateral.

## Matriz regra → produtor → consumidor → implementação → teste → evidência → estado → gap/ação

| Regra | Produtor | Consumidor | Implementação | Teste | Evidência | Estado | Gap/ação |
|---|---|---|---|---|---|---|---|
| runtime vivo | **PGD** | RHGD só referencia/descobre | linhagem `pgh-distributed-session-control-plane`; Agent/Executor/WorkSession/heartbeat-status | U33 Core + release PGD | U-PGD-01, U-PGD-02, U33/U36D | PGD-owned | schema federation-facing de runtime ainda não declarado |
| admission | **PGD** | RHGD encaminha referência de trabalho já autorizado | `PGH-semantic-authorization → PGD-operational-admission → PGD-execution` | `verify_pgh_2_u33_suite_agent_control.py` | `suite-agent-control-boundary.schema.json` + U33 | PGD-owned | payload request/response RHGD→PGD não declarado |
| queue/DAG | **PGD** | RHGD **não** possui fila | TaskQueue/DAG + scheduler na linhagem PGD | U33 + `RESOURCE_STATE_OWNED_BY_PGD` | handoff PGD + fronteira RHGD | PGD-owned | RHGD só transporta referência após contrato versionado |
| lease/reservation | **PGD** | RHGD referencia; não emite | ResourceLease, ReservationToken e admission barrier PGD-owned | gates PGD 1.0 + U33 | U-PGD-01 + U33/U37 | PGD-owned | serialização federativa não declarada; RHGD não pode mintar |
| scheduler/execução | **PGD** | RHGD federa, não agenda | implementação canônica preservada por H01-R2 | U33/U36D + `PGD_IDENTITY_H01_R2=PASS` | `estado.md` PGD + fronteira RHGD | PGD-owned | ownership sem gap; adapter espera contrato |
| evidência de resultado | **PGD** | PGH primário; RHGD pode transportar preservando proveniência | `OutcomeEvidenceEnvelope` com `execution_state`/`effect_state`, candidate `observed` | gates `OUTCOME_EVIDENCE_OBSERVED_ONLY` e `EFFECT_VERIFICATION_NE_PROCESS_EXIT` | schema U20 + U-PGD-01/U-PGD-02 | schema existente | wrapper RHGD, se existir, referencia; não redefine |
| descoberta externa | **RHGD** | PGD admission / PGH contexto conforme contrato | Fase 0 RHGD ainda candidata; `KnownResourceDescriptor` é descritivo e exclui estado vivo | schema KnownResourceDescriptor + testes RHGD | U37 + fronteira RHGD | seam candidata | A02 deve criar adapter contra contrato PGD versionado, sem copiar scheduler |

## Prova de ownership

A fronteira continua inequívoca: **PGA governa; PGH autoriza/contextualiza; PGD agenda/executa; RHGD federa; MSGCD agrega.**

O PGD 1.0.0 já homologa:
- runtime = PGD;
- runtime lease owner = PGD;
- estado de recurso = PGD;
- resultado operacional = `PGD_observed_to_PGH`;
- proibição de expansão de autoridade.

O Core atual reforça a mesma divisão: U33 exige `task-dag-message-queues`, `claim-lease-retry-idempotency`, `scheduler-periodic-cycles` e `resource-reservation-lease-admission` no conjunto PGD; U37 diz explicitamente que RHGD descobre/federa executores externos usando contratos PGD, sem segundo scheduler.

## Delta lateral encontrado no RHGD

O `rhgd/estado.md` no ref auditado ainda registra que o PGD standalone não estava materializado no bootstrap. Isso é histórico obsoleto perante `debianlima/pgd` 1.0.0 e H01-R2. O lado A02/RHGD deve reconciliar essa frase e suas próximas unidades no próprio safe point; LAT-02/PGD não edita o repositório peer.

## Gap contratual deliberadamente não preenchido

O release contract PGD 1.0.0 prova ownership e gates, mas não existe, no PGD standalone auditado, um schema federation-facing que defina campos request/response para runtime vivo, admission, queue, lease/reservation e scheduler.

**Não inferir esses campos da implementação.** Antes do adapter RHGD real, deve nascer um contrato PGD novo, deliberado e versionado. Esse gap não reabre a release PGD 1.0.0; bloqueia somente a integração runtime RHGD→PGD que ainda não tem payload contratado.

## Context exchange

- **A02/RHGD:** consumir PGD 1.0.0/H01-R2; atualizar estado bootstrap; implementar somente discovery/federation; não duplicar scheduler, fila, lease ou reservation.
- **A09/MSGCD:** mostrar runtime/admission/queue/lease/reservation/scheduler como estado operacional PGD; mostrar RHGD como borda federativa; MSGCD continua agregador sem autoridade independente.
- **Agente externo do Core:** referência read-only `2df5f0a…`; nenhuma normalização ou sobrescrita LAT-02.

## Gates

- `PGD_PROJECT_VERIFY=PASS`;
- `PGD_RELEASE_1_0=PASS GATES=9/9`;
- `RHGD_PROJECT_VERIFY=PASS`;
- `RHGD unittest=8/8 PASS`;
- `PGD_OWNS_RUNTIME/ADMISSION/QUEUE_LEASE_RESERVATION/SCHEDULER_EXECUTION=PASS`;
- `RHGD_NO_DUPLICATE_SCHEDULER=PASS`;
- `CORE_READ_ONLY=PASS`;
- `FEDERATION_PAYLOAD_SCHEMA=GAP_NEW_VERSIONED_CONTRACT_REQUIRED`.

## Handoff A09 / MSGCD

Pronto para consumo com gap declarado. A visão MSGCD deve compor os estados já possuídos por PGD e a descoberta/federação RHGD, sem criar um terceiro scheduler nem nova autoridade. A futura integração runtime só avança quando existir contrato PGD versionado para o payload de federação.
