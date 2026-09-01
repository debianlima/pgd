# U-PGD-14 — Incremental Runtime Information Exchange

## Objetivo

Formalizar consulta de informação entre agentes **sem interromper a unidade em execução**. O mecanismo reutiliza `pgh-work-context-broadcast/1`; não cria fila, broker, scheduler ou runtime paralelo.

## Procedimento repetitivo

1. O solicitante cria `InformationRequest` com `request_id`, pergunta, termos de recuperação, evidência desejada e `required_for_gate`.
2. O PGD envia a consulta como WCB direcionado, preferencialmente piggyback no envelope normal.
3. O solicitante **continua imediatamente todo trabalho independente**; consulta não vira espera implícita.
4. O respondente recebe a consulta sem trocar sua unidade principal. Faz microavaliação read-only/bounded, localiza refs/evidência e emite `InformationResponse` por WCB.
5. O respondente continua a unidade original. Responder não equivale a claim, preempção, nova lease ou troca de owner.
6. O solicitante pode concluir outros passos enquanto a resposta trafega.
7. Quando a resposta chega, ela entra como **evidência observada**, não autoridade. O solicitante compara revisão/hash/refs com o estado canônico e executa reconciliação incremental somente do delta afetado.
8. Resposta stale é descartada ou rebaseada; duplicata é idempotente; divergência na mesma revisão exige reconciliação ou `HUMAN_BLOCKED`.
9. Somente se `required_for_gate=true` e o agente alcançar exatamente o gate dependente sem resposta, esse gate entra em `WAITING_FOR_INFORMATION`. Trabalho não relacionado continua elegível.

## Mesma zona

O `CommunicationGraph` resolve os destinos e o WCB entrega request/response. O agente consultado não abandona a TaskTree nem perde claim/lease da unidade corrente.

## Zonas heterogêneas

A semântica é idêntica. O WCB continua sendo contrato PGD e a travessia de peer usa referência/federação RHGD. RHGD transporta/descobre; **PGD continua owner de fila, lease, retry, runtime e watermark**. Nenhum segundo scheduler nasce no peer.

## Relação com Operational Context Forest

A consulta deve começar pelo ramo conhecido (`SystemNavigatorGraph` → grafo especializado → refs) e pedir ao outro agente somente o que não está disponível/fresco localmente. A resposta pode fornecer refs para o receptor atualizar apenas o ramo stale. Consulta não substitui navegação, provenance/freshness ou fonte canônica.

## Anti-padrões proibidos

- parar todos os agentes aguardando uma resposta;
- interromper/preemptar a unidade do consultado para responder;
- usar resposta textual como autorização;
- reenviar histórico bruto quando refs estruturadas bastam;
- criar scheduler/broker de pesquisa paralelo;
- aplicar resposta stale sem conferir revisão/hash;
- transformar pesquisa opcional em blocker global.

## Gate

`NON_BLOCKING_DEFAULT=PASS`, `REQUEST_RESPONSE_CORRELATION=PASS`, `SAME_ZONE=PASS`, `HETEROGENEOUS_ZONE=PASS`, `NO_PREEMPTION=PASS`, `EVIDENCE_NOT_AUTHORITY=PASS`, `INCREMENTAL_RECONCILIATION=PASS`, `NO_SECOND_RUNTIME=PASS`, `RECONCILIATION_CLOSURE=PASS`, `DEPENDENCY_REFERENCES=PASS`.
