# U-PGD-10 — homologação normativa do PGD Work Context Broadcast

## Contrato

O PGD homologa `pgh-work-context-broadcast/1` como protocolo operacional obrigatório de sincronização de contexto entre agentes. O schema normativo deste repositório é byte-equivalente ao schema do runtime fechado em `debianlima/pgh-distributed-session-control-plane@f5047f72914c6634982df30c8ce0f8747af5cfb3`.

A implementação canônica continua no control-plane. Esta unidade **não cria segundo scheduler**, broker, store ou runtime PGD.

## Ritual obrigatório

Em **toda atualização/finalização** de trabalho distribuído, um Work Context Broadcast é produzido. O agente não decide se a mudança “parece relevante”. Um `work_context_delta` explícito é preferido; se ausente, o runtime gera fallback determinístico a partir do `context_exchange`.

O delta transporta um resumo compacto, referências, impactos, itens resolvidos/remanescentes e hipóteses invalidadas. Histórico textual bruto não é a continuidade operacional.

Se o turno apenas recebeu/aplicou uma janela WCB e não produziu trabalho novo, `NO_CHANGE` continua sendo auditado, mas sem novo fanout. Essa regra impede eco infinito sem tornar o procedimento opcional.

## Broadcast, self-origin e fencing

O broadcast é global e inclui o próprio emissor (`self-origin`). O watermark/fencing usa origem, revisão e chave de coalescing: mesma revisão/mesmo payload é idempotente; mesma revisão/payload divergente é conflito; revisão anterior é stale.

Coalescing mantém o último estado efetivo sem perder os `event_id` necessários para recibo e auditoria.

## Entrega

A via preferida é **piggyback** na próxima entrega Supervisor/humano/fallback/op-reconciliation. Quando não há trabalho acionável para piggyback, a janela pode sair standalone após **15 minutos** pelo mesmo reconcile loop; não nasce scheduler paralelo.

## Integração com U-PGD-09

`U-PGD-09-SYSTEMIC-ONTOLOGICAL-TREES` permanece homologada e passa a ter sua dependência WCB formalmente satisfeita pelo contrato PGD. `ProjectTree`, `ResourceTree`, `AuthTree` e `TaskTree` emitem `WCB Tree Delta` por ramo afetado, com revisão/hash e refs remotas; o consumidor sincroniza somente o ramo necessário.

A árvore continua uma visão operacional/RAG verificável, nunca substituta de Git, manifesto, contratos, banco operacional, locks ou autoridade.

## Release e skill

PGD continua em `1.0.0` e `v1.0.0` permanece imutável. `pgd-project@0.2.0` não é reescrita porque U-PGD-08 congelou a skill histórica; o ritual repetitivo vive no contrato normativo, nas raízes das árvores e na injeção runtime.

## Gates

`DELTA_INVENTORY=PASS`, `LEARNING_PRESERVED=PASS`, `WCB_RUNTIME_CLOSED=PASS`, `WCB_SCHEMA_EQUIVALENCE=PASS`, `WCB_MANDATORY_RITUAL=PASS`, `WCB_FALLBACK=PASS`, `WCB_NO_CHANGE_ANTI_ECHO=PASS`, `WCB_SELF_DELIVERY=PASS`, `WCB_WATERMARK=PASS`, `WCB_COALESCING=PASS`, `WCB_PIGGYBACK=PASS`, `WCB_STANDALONE=PASS`, `NO_SECOND_RUNTIME=PASS`, `SYSTEMIC_TREE_INTEGRATION=PASS`, `RELEASE_IMMUTABILITY=PASS`, `RECONCILIATION_CLOSURE=PASS` e `DEPENDENCY_REFERENCES=PASS`.
