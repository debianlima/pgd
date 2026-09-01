# Estado — PGD 1.0.0 — contrato v3

## Decisões vigentes
- PGH autoriza; PGD executa.
- PGD possui estado runtime vivo, scheduler, filas, leases, workers, heartbeat, recovery e Outcome/Efficacy.
- PGD não amplia autoridade recebida de PGA/PGH.
- H01-R2, decisão humana de 31/08/2026: `debianlima/pgd` permanece protocolo/contratos/evidências; `debianlima/pgh-distributed-session-control-plane` é a implementação canônica de execução do PGD, com o nome histórico preservado e sem runtime sucessor/paralelo.
- Decisão humana de 31/08/2026: o papel `auxiliar` participa da construção e da conciliação incremental do PGD; concluído `PGD_AUXILIAR_RECONCILIATION=PASS`, a sequência habilita o auxiliar no PGA.
- LAT-02/U-PGD-04 preserva a fronteira da suíte: PGA governa; PGH autoriza/contextualiza; PGD agenda/executa; RHGD federa; MSGCD agrega.

## Decisões superadas
- PGD 0.1.0 como estado de repouso standalone — superado pela unidade U-PGD-02 de release 1.0.

## Decisões humanas pendentes
- Nenhuma local no PGD nesta unidade lateral.

## Decisões fechadas nesta emenda
- H01-R2 permanece materializada sem renome/migração: `pgd` é protocolo/especificação e `pgh-distributed-session-control-plane` é a implementação canônica de execução. Gate histórico preservado: `PGD_IDENTITY_H01_R2=PASS`.
- U-PGD-04/LAT-02 confirmou, sem tocar o Core, que runtime vivo, admission, queue/DAG, lease/reservation e scheduler/execução continuam propriedade PGD; RHGD apenas descobre/federa e referencia os contratos PGD.

## Pendências técnicas não humanas
- `PGD_RHGD_FEDERATION_PAYLOAD_SCHEMA`: FECHADO por U-PGD-05 com `pgd-rhgd-federation/1`; `v1.0.0` permanece imutável. RHGD transporta WorkUnit autorizada e PGD conserva admission/fila/lease/scheduler/retry/recovery/runtime state.
- No peer RHGD `29194e935b838dd1c4ee4228b515911c5a0bb8e7`, `estado.md` ainda afirma que o PGD standalone não estava materializado no bootstrap. Essa frase virou delta lateral do peer e deve ser conciliada pelo A02/RHGD no próprio safe point.

## Trabalho compartilhado
- ponteiro: `manifesto.yaml.trabalho_compartilhado` — vazio após fechamento de U-PGD-04/LAT-02.

## Competências ativas nesta unidade
- `pgd-project@0.2.0` — Project-Skill única; sem alteração porque a homologação lateral não produziu novo aprendizado de skill, apenas confirmou ownership já vigente e registrou gap de interface.
- `desenvolvedor-de-software@15`.
- `github-incremental-reconciliation@7`.
- `telemetry-data-visualization@2` — macro global de telemetria da unidade.

## Divergências da última reconciliação
- corrigidas: cópia de auditoria PGD antiga (`47615dbf…`) não foi promovida; a unidade partiu do remoto canônico `366388d8…` e publicou incremento sobre ele.
- preservadas: release PGD 1.0.0, contrato v3, H01-R2, `pgd-project@0.2.0` e implementação Core externa permaneceram imutáveis nesta unidade.
- peer RHGD: estado bootstrap obsoleto identificado e encaminhado ao A02; nenhum arquivo RHGD foi escrito pelo lado PGD.
- Core PGH 2.0: usado somente como referência canônica de leitura em `2df5f0a98f201293fe278c54ea7fd2c483102119`; nenhuma normalização/sobrescrita LAT-02.
- pendentes de autorização: nenhuma local; o schema de federação exige nova unidade contratual deliberada antes de implementação, não preenchimento por inferência.

## Portões da unidade U-PGD-04/LAT-02
- `DELTA_INVENTORY=PASS`.
- `LEARNING_PRESERVED=PASS`.
- `PGD_PROJECT_VERIFY=PASS`.
- `PGD_RELEASE_1_0=PASS GATES=9/9`.
- `RHGD_PROJECT_VERIFY=PASS` e `RHGD_UNITTESTS=PASS 8/8` no ref auditado.
- `PGD_RHGD_LAT02=PASS MATRIX=7 OWNERSHIP=PGD FEDERATION_SCHEMA=GAP_DECLARED`.
- `CORE_READ_ONLY=PASS`.

## Entradas aceitas
- 1–17.

## Próxima unidade
- Aguardar a conciliação peer do A02/RHGD e, somente se o consumidor exigir integração runtime, abrir uma nova unidade contratual PGD para definir de forma versionada o payload federation-facing. Até lá, RHGD não cria scheduler, queue, ResourceLease ou ReservationToken próprios.

## Portões da unidade U-PGD-05
- `DELTA_INVENTORY=PASS`.
- `LEARNING_PRESERVED=PASS`.
- `PGD_RHGD_U05=PASS`.
- `FEDERATION_PAYLOAD_SCHEMA=PASS`.
- `RESOURCE_STATE_OWNED_BY_PGD=PASS`.
- `NO_DUPLICATE_PGD_RUNTIME=PASS`.
- `CORE_CHANGE_REQUIRED=NO`.

## Próxima unidade após U-PGD-05
- RHGD: implementar/conciliar o adapter `ContextEnvelope -> pgd-rhgd-federation/1` e capability discovery sem duplicar scheduler/lease PGD.

## U-PGD-06-CORE-SYSTEM-CONTEXT — interrupção governada por dependência
- `DELTA_INVENTORY=PASS` e `LEARNING_PRESERVED=PASS`: identidade/base do componente e fronteiras da suíte foram inventariadas sem normalização.
- `UPSTREAM_CORE_SAFE_POINT=BLOCKED`: o PGH Core está sob reserva viva `U250-U255-HUMAN-APPROVED-RECONCILIATION` em `b4852d9c13c463cfe171771e59ac0e3767bc2260`, e o runtime PGD está sob `U250-OPERATIONAL-RECONCILIATION-MATERIALIZATION`; a semântica U250/U255 ainda pode alterar referências que esta unidade deve consumir.
- Resultado desta unidade: `BLOCKED_DEPENDENCY`; nenhuma normalização, bump de release, mudança de autoridade, tag ou runtime foi executada.
- Reserva liberada para não manter exclusão inútil.
- Próximo gate: safe point final U250/U255 + U250 runtime; então abrir unidade sucessora com refs finais e rerodar os gates.

## U-PGD-07-CORE-SYSTEM-CONTEXT-RECONCILIATION — unidade sucessora aberta
- `telemetria_inicio=2026-09-01T13:32:42Z`; a dependência U250/U255/runtime que bloqueou U-PGD-06 foi encerrada em safe point final.
- Escopo: reconciliar somente refs/ownership/evidência PGD; `VERSION=1.0.0` e tag `v1.0.0` permanecem imutáveis; nenhum runtime paralelo será criado.

## U-PGD-07-CORE-SYSTEM-CONTEXT-RECONCILIATION — PASS
- Bloqueio U-PGD-06 removido por safe point final U250/U255/runtime; refs finais consumidas sem normalização destrutiva.
- `DELTA_INVENTORY=PASS`; `LEARNING_PRESERVED=PASS`; `UPSTREAM_CORE_SAFE_POINT=PASS`.
- `PGD_CORE_SYSTEM_CONTEXT_U07=PASS`; `AUTHORITY_BOUNDARY=PASS`; `CONTEXT_SYNC_BOUNDARY=PASS`; `NO_DUPLICATE_PGD_RUNTIME=PASS`.
- `RECONCILIATION_CLOSURE=PASS`; `DEPENDENCY_REFERENCES=PASS`; `RELEASE_IMMUTABILITY=PASS`; `VERSION=1.0.0` e tag `v1.0.0` preservadas.
- `trabalho_compartilhado` liberado; próxima dependência habilitada: reconciliação sucessora da PGA contra este HEAD PGD.


## U-PGD-08-HUMAN-RECONCILIATION-RATIFICATION — PASS
- Decisão humana direta: `HUMAN-RECONCILIATION-TOTAL-GENERAL-20260901`, RouterStore `rowid=4915`, `decision_at=2026-09-01T05:51:28.063002Z`: “A reconciliação está aprovada, total e geral.”
- Efeito: ratificação **prospectiva** do estado reconciliado atual; `historical_authority_reclassified=false`. U-PGD-05 (`abf929598c1eeb50fa09c90c3f039d4bc8bb1f79`) antecede a decisão e não foi reescrita/reclassificada.
- `pgd-rhgd-federation/1` permanece homologado: PGD possui runtime/scheduler/execution; RHGD federa/descobre sem segundo scheduler.
- U-PGD-07 Core/System Context permanece PASS e imutável nesta unidade.
- A aprovação não cria `context-sync`, `browser-qa`, `simulation` ou identidade de máquina; tampouco autoriza operações destrutivas de árvore, persistência de segredos ou expansão de autoridade entre camadas.
- `DELTA_INVENTORY=PASS`; `LEARNING_PRESERVED=PASS`; `HUMAN_DECISION_PROVENANCE=PASS`; `TEMPORAL_NON_RETROACTIVITY=PASS`; `CURRENT_STATE_RATIFIED=PASS`; `RELEASE_IMMUTABILITY=PASS`; `AUTHORITY_BOUNDARY=PASS`.
- `trabalho_compartilhado` liberado; próxima conciliação deve consumir este HEAD e respeitar locks/safe points/capabilities reais.

## U-PGD-09-SYSTEMIC-ONTOLOGICAL-TREES — unidade aberta
- `telemetria_inicio=2026-09-01T14:58:57Z`; decisão humana: árvores sistêmicas compartilhadas para projetos, recursos, autenticação e tarefas, sincronizadas por WCB e navegáveis via refs RAG.
- Visualização pode ser hierárquica/A+, mas modelo interno é DAG tipado para representar dependências cruzadas e peers remotos sem duplicação de identidade.

## U-PGD-09-SYSTEMIC-ONTOLOGICAL-TREES — PASS
- `ProjectTree`, `ResourceTree`, `AuthTree` e `TaskTree` contratadas como projeções hierárquicas sobre DAG tipado; `TaskTree` é uma por projeto habilitado.
- ResourceTree indexa fila/reserva/lease/localização/projeto/capability/peer; `remote_subtrees` usam ref+revision+hash+authority.
- AuthTree contém somente bindings/escopos/refs; `AUTH_NO_SECRETS=PASS`.
- Todo nó possui refs RAG/termos; ritual obrigatório: comparar revisão com WCB antes de decidir, atualizar ramo afetado e emitir delta WCB após mutação.
- `pgd-project@0.2.0` preservada por `U-PGD-08 immutable_blobs`; o ritual repetitivo vive no contrato/raiz das árvores e será injetado pelo runtime. `RECONCILIATION_CLOSURE=PASS`; `DEPENDENCY_REFERENCES=PASS`; `trabalho_compartilhado={}`; `v1.0.0` permanece imutável.

## U-PGD-10-WORK-CONTEXT-BROADCAST-NORMATIVE — unidade aberta
- `telemetria_inicio=2026-09-01T15:05:37Z`; objetivo: homologar no PGD o contrato WCB runtime `f5047f72914c6634982df30c8ce0f8747af5cfb3` sem duplicar runtime.

## U-PGD-10-WORK-CONTEXT-BROADCAST-NORMATIVE — PASS
- `pgh-work-context-broadcast/1` homologado no PGD com schema byte-equivalente ao runtime `f5047f72914c6634982df30c8ce0f8747af5cfb3`.
- Ritual obrigatório: toda atualização/finalização gera WCB; fallback determinístico se delta explícito ausente; `NO_CHANGE` auditado sem fanout; self-origin, watermark, coalescing, piggyback e standalone 15 min preservados.
- `SYSTEMIC_TREE_INTEGRATION=PASS`: U-PGD-09 usa WCB Tree Delta com revisão/hash por ramo.
- `NO_SECOND_RUNTIME=PASS`; `RELEASE_IMMUTABILITY=PASS`; `RECONCILIATION_CLOSURE=PASS`; `DEPENDENCY_REFERENCES=PASS`; `trabalho_compartilhado={}`.

## U-PGD-11-DYNAMIC-SYSTEMIC-VIEWS — unidade aberta
- `telemetria_inicio=2026-09-01T15:08:52Z`; objetivo: transformar U09+U10 em ciclo vivo de mapas/visões ontológicas, com atualização repetitiva e verificável a cada mutação.

## U-PGD-11-DYNAMIC-SYSTEMIC-VIEWS — PASS
- Mapas macro iniciais e interconexões por projeto contratados; navegação começa no domínio/mapa aplicável e expande apenas o ramo necessário.
- `DIRECT_STORE` e `WEB_EXECUTOR` são os únicos canais de write-back; toda mutação efetiva atualiza revisão/hash e emite WCB.
- Visões locais preservam base compartilhada; índice privado é derivado/não autoritativo e exige rebase quando a base muda.
- TaskTree indexa agente, recursos, dependências, fila/reserva/lease e refs de autoridade; mudança recalcula somente ramo afetado.
- `PGH_HRAG_RAG_PROJECTION=PASS`; `AUTH_NO_SECRETS=PASS`; `RECONCILIATION_CLOSURE=PASS`; `DEPENDENCY_REFERENCES=PASS`; `trabalho_compartilhado={}`.
