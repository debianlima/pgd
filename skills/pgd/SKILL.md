---
name: pgd-project
versao: 0.2.0
description: Skill de projeto do PGD standalone candidato.
tipo_competencia: projeto
origem:
  projeto_de_origem: protocolo-governanca-heterogenea
  commit_divergencia: a68ba9b460bd1d2050d57873fdc1c648732ece07
---
# PGD Project Skill

PGD possui scheduler, DAG, filas, leases, workers, heartbeat, recovery, transport e estado operacional vivo. Nunca amplia autorização recebida de PGA/PGH. Resultado operacional retorna como evidência observada, não conhecimento homologado.

## Federação RHGD
RHGD pode descobrir capacidade e transportar WorkUnits, mas não possui admission, fila, lease, scheduler, retry, recovery nem estado runtime. Toda WorkUnit federada exige `authorization_ref` PGH, idempotência, orçamento de contexto, privacidade e capacidades requeridas. Lease solicitado é intenção; somente PGD concede. Resultado retorna como evidência `observed`. Contrato: `pgd-rhgd-federation/1`.
