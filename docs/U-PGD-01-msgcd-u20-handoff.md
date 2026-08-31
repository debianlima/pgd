# U-PGD-01 — Integração MSGCD com PGH U20

## Estado
Handoff versionado para o futuro repositório canônico do **PGD — Protocolo de Gestão Distribuída**. Enquanto não existir repositório standalone identificável, esta unidade permanece preservada no repositório do PGH e vinculada ao Issue #14.

## Dependência upstream
PGH 2.0 U20 — MSGCD Knowledge Boundary Alignment.

## Contratos PGH a consumir
- `KnowledgeScope` — informa escopo organizacional/tenant/ambiente do conhecimento;
- `GovernanceContextBinding` — referencia snapshot PGA aplicável;
- `KnownResourceDescriptor` — descreve recurso conhecido sem estado operacional vivo;
- `AuthorizationGrant` — autorização semântica; não é lease runtime;
- `OutcomeEvidenceEnvelope` — retorno PGD → PGH;
- `RuntimeObservationSurface` / `RuntimeInteractionAttestation` — observação/interação já definidas pela U19;
- `GovernedRequestEnvelope` / `DelegationGrant` — requests entre agentes/sessões.

## Propriedade normativa do PGD
PGD é responsável por:
- WorkSession;
- scheduler/TaskQueue/DAG;
- Resource/ResourcePool/ResourceLease;
- OperationalPermissionBinding;
- escolha operacional de transporte e endpoint;
- materialização runtime de credencial via cofre/broker sem expor segredo;
- MCP/SSH/REST/OAuth/terminal/VM execution;
- monitoramento e estado vivo;
- retry/checkpoint/resume/relocation;
- HumanControlLease;
- alertas/incidentes;
- Outcome/Efficacy Engine (`funcionou?`).

## Mudança U20 relevante
A função histórica U18 que chamava transport adapter continua preservada como protótipo/evidência, mas a propriedade normativa final é:

> **PGH autoriza; PGD executa.**

O PGD deve receber uma decisão `AUTHORIZED` e então decidir, sob suas regras operacionais, se há recurso, credencial disponível, rede, capacidade e transport homologado para materializar a execução.

## Recurso conhecido versus recurso operacional
`KnownResourceDescriptor` PGH pode dizer que uma GPU/VM/servidor existe, quais capacidades possui e quais métodos a conhecem.

PGD mantém o estado mutável: utilização, saúde, fila, reserva, lease, temperatura, capacidade livre, executor atual e prioridade.

## Outcome/Efficacy
Ao terminar uma ação, PGD não deve marcar conhecimento homologado. Deve produzir `OutcomeEvidenceEnvelope` com:
- `execution_session_ref`;
- projeto/tarefa;
- efeitos esperados/observados;
- `execution_state`;
- `effect_state`;
- evidências e proveniência.

`knowledge_candidate_status` é obrigatoriamente `observed`. PGH decide posteriormente se a evidência pode virar conhecimento homologado.

## Permissões
Separação obrigatória:
- PGA: política/autoridade organizacional;
- PGH: `AuthorizationGrant` semântico;
- PGD: `OperationalPermissionBinding` + `ResourceLease` temporários.

PGD nunca amplia escopo recebido do PGH/PGA.

## Gates futuros PGD
- `PGH_AUTHORIZATION_REQUIRED`
- `NO_RUNTIME_LEASE_IN_PGH`
- `RESOURCE_STATE_OWNED_BY_PGD`
- `OPERATIONAL_PERMISSION_WITHIN_AUTHORIZATION`
- `OUTCOME_EVIDENCE_OBSERVED_ONLY`
- `SESSION_PROVENANCE_COMPLETE`
- `HUMAN_TAKEOVER_PROVENANCE`
- `NO_SECRET_IN_SESSION_STREAM`
- `EFFECT_VERIFICATION_NE_PROCESS_EXIT`

## Migração
Quando o repositório standalone PGD existir, esta unidade deve ser migrada preservando referência ao commit U20 original e ao Issue #14; não copiar silenciosamente como documento sem linhagem.

## U33 — gestão de agentes e executores
A decisão humana de 30/08/2026 fixa a gestão **runtime** de agentes/executores no PGD. O HEAD commitado `pgh-distributed-session-control-plane@3ec7f1f0cc79f5eef2edfe11cbf567ca51f7ff34` (2.3.1) é reutilizado como evidência da linhagem de implementação: diretório vivo de agentes, workers persistentes por chat, perfis/runtime, rotação/handoff, scheduler, filas, claims, leases, retries e API de controle.

A propriedade normativa acrescentada ao PGD inclui `AgentInstance`, `ExecutorInstance`, worker lifecycle, runtime profile/rotation/handoff, live heartbeat/status e admission/reservation. O `WorkProfile` PGH continua semântico/cognitivo e não é renomeado para representar estado vivo.

Para a futura integração AIP/UMRP/SGLang, `ReservationToken`, resource lease e admission barrier pertencem ao PGD. AIP planeja; PGD reserva; Residency/UMRP decide objeto/tier; ATU move; SGLang executa.

U33 não cria runtime paralelo e não renomeia o repositório/símbolos existentes. A unidade U-235 em andamento no control-plane foi excluída da evidência até homologação própria.
