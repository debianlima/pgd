# U-PGD-17 — WorkUnit Execution Outcome

A U-PGD-17 formaliza o objeto terminal de evidência observado após a execução física de uma WorkUnit. Ela não cria runtime no repositório PGD e não altera o release `v1.0.0`; a implementação canônica continua em `debianlima/pgh-distributed-session-control-plane` conforme H01-R2.

## Lacuna fechada

`pgd-rhgd-federation/1` já possuía estados `SUCCEEDED|FAILED` e os campos `execution_ref`, `lease_ref`, `outcome_evidence_ref`, `retryable` e `outcome_classification=observed`, porém não existia um objeto canônico para o `outcome_evidence_ref` apontar.

O novo contrato é `pgd-work-unit-execution-outcome/1`. Seu `outcome_id` é o identificador referenciável pela resposta federada como `outcome_evidence_ref`.

## Autoridade

O resultado é **evidência**, não grant de autoridade:

- `outcome_classification=observed`;
- `completion_owner=PGD`;
- `authority_effect=NONE`.

Worker e RHGD podem produzir/transportar o relato. Somente PGD, após conferir o estado runtime corrente, pode aceitar esse relato como completion da WorkUnit.

RHGD continua responsável apenas por `capability_discovery`, `federation_transport` e `interdomain_provenance`. Não recebe scheduler, assignment, lease ou completion authority.

## Fence de assignment

O contrato carrega os fences que o runtime canônico efetivamente possui hoje:

- `project_ref`;
- `work_unit_id`;
- `assignment.agent_id`;
- `assignment.assignment_epoch`.

`lease_ref` é obrigatório como campo, porém pode ser `null`. Isso preserva compatibilidade com `pgd-rhgd-federation/1` sem inventar um identificador de lease que o claim atual não emite: o Control Plane usa `assignment_epoch` e opcionalmente `lease_until` no assignment canônico.

Uma futura implementação de completion deve comparar `agent_id + assignment_epoch` com o assignment vivo antes de alterar `TASK_MAP`.

## Estados terminais

O contrato aceita somente:

- `SUCCEEDED`;
- `FAILED`.

Estados intermediários permanecem no contrato de runtime/federação e não são outcomes terminais.

### SUCCEEDED

Exige:

- `retryable=false`;
- `result` não nulo;
- `error=null`.

O resultado contém `result_ref`, `output_schema_ref`, `content_hash` e `payload`. O payload é deliberadamente opaco ao PGD: o schema esperado pertence à WorkUnit/contrato da tarefa.

### FAILED

Exige:

- `result=null`;
- objeto `error` com `code`, `message` e evidências;
- ao menos uma `evidence_ref` no outcome.

`retryable` pode ser verdadeiro ou falso; a decisão posterior de retry continua propriedade PGD.

## Modelo e host são observação, não seleção

`runtime_observation` pode registrar `model_ref`, `model_version`, `host_ref` e `transport_ref` observados após a execução. Esses campos não autorizam nem selecionam o executor. O schema fechado rejeita propriedades como `selected_worker`.

Isso preserva a arquitetura model-independent demonstrada pela U293 do Control Plane: trocar o modelo não altera o plano/WorkUnit; o outcome apenas registra qual runtime realmente produziu aquela execução.

## Próximo consumidor

O consumidor canônico esperado é uma nova unidade do Control Plane. Ela deverá:

1. receber `pgd-work-unit-execution-outcome/1`;
2. localizar a WorkUnit/assignment corrente;
3. fencear `agent_id + assignment_epoch` e schema/hash de saída;
4. aplicar completion idempotente no `TASK_MAP` somente se os fences passarem;
5. tornar o resultado final disponível ao canal de resposta sem transformar `/v1/chat/completions` em scheduler ou hardcode de modelo.

Essa materialização é futura e não faz parte da U-PGD-17.
