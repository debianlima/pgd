# U-PGD-16 — Cognitive WorkGraph and aggregation barrier

PGH 2.2 entrega ao PGD um `ContextSegmentationPlan` advisory. O PGD é quem converte a decomposição autorizada em WorkUnits/DAG executáveis e continua sendo o único dono de fila, admission, scheduler, assignment, lease, retry, recovery e completion.

Cada WorkUnit preserva `authorization_ref`, idempotência, privacy scope, budget de tokens, capability alvo, dependências e referências de contexto. O contrato admite `COGNITIVE`, `TOOL_PREPROCESS` e `PHYSICAL_CHUNK`; isso não cria scheduler por inferência. Uma etapa `TOOL_PREPROCESS`, como Marker antes de um worker documentador, continua sendo trabalho PGD: a ferramenta tem `tool_authority=none`, só solicita execução e a saída exige proveniência.

RHGD pode descobrir destino e transportar a WorkUnit, mas não concede lease ou assignment. O `ResultAggregationPlan` é consumido como barrier: enquanto faltar qualquer segmento obrigatório o resultado é `WAIT_REQUIRED_SEGMENTS`. Somente quando o PGD prova completion dos segmentos requeridos emite `READY_FOR_MSGCD_COMPOSITION`; então o MSGCD pode compor/deduplicar/preservar conflitos e proveniência.

Este contrato não implementa runtime paralelo no repositório `pgd`. A implementação canônica permanece `debianlima/pgh-distributed-session-control-plane`, conforme H01-R2. A próxima integração runtime deve materializar este contrato no Control Plane existente, nunca criar segundo scheduler.

## Project-Skill imutável por ratificação humana U08
A U08 sela `skills/pgd/SKILL.md` no blob `28a453019c254475380924ff05f70c9e4f096b90`. Portanto U16 **não** incrementa a Project-Skill nem altera esse arquivo; fazê-lo quebraria `verify_u_pgd_08_human_ratification.py`. O aprendizado U16 permanece preservado no contrato versionado `pgd-cognitive-workgraph/1`, nesta documentação, evidência/estado e na implementação canônica futura do Control Plane.
