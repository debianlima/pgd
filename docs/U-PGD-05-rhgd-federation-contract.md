# U-PGD-05 — contrato RHGD → PGD

## Objetivo
Fechar o gap `PGD_RHGD_FEDERATION_PAYLOAD_SCHEMA` sem reabrir `v1.0.0` e sem duplicar runtime no RHGD.

## Fronteira
PGA governa; PGH autoriza/contextualiza; PGD agenda e executa; RHGD descobre/federa; MSGCD agrega. O RHGD pode selecionar um executor e transportar uma `WorkUnit`, porém admission, fila, lease, scheduler, retry, recovery e estado runtime continuam exclusivamente no PGD.

## Identidades reconciliadas
- PGH Core vivo: `3bc2b30df75d5a622fbdae3ee9e201d5113c94bc`, contrato `CT-PGH2-CORE-RECONCILIATION@1.0.0`.
- PGD base desta unidade: `a4a60387f75b89be5bbb22120349291d06acfeb0`.
- implementação estável: `pgh-distributed-session-control-plane:v2.3.2`, commit `cfd68602a4491d61658f564b86d550f4b498f06f`.
- RHGD consumidor auditado: `29194e935b838dd1c4ee4228b515911c5a0bb8e7`.

## Mapeamento operacional
O envelope de federação não substitui `pgh-message/1`. Ele é o payload lógico entre RHGD e PGD; o adapter PGD o materializa no transporte durável da implementação estável, preservando correlação, idempotência, ACK e lease.

O request exige `authorization_ref`: federação nunca amplia autoridade. `context_tokens`, `privacy_level`, `required_capabilities` e política de expansão permitem ao RHGD selecionar um nó sem adquirir o scheduler. `requested_lease_seconds` é pedido, não concessão: somente PGD concede lease.

A resposta classifica resultado como `observed`. Homologação de conhecimento permanece responsabilidade PGH.

## Consequência para o Core
Nenhuma mudança no PGH 2.0 é necessária nesta unidade. U45 já suporta referência viva e a autorização semântica existente cobre o `authorization_ref`. Capability discovery continua dado operacional RHGD/PGD até existir aprendizado que exija um objeto normativo novo no Core.
