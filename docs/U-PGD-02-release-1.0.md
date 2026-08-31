# U-PGD-02 — Homologação PGD 1.0

PGD 1.0 formaliza a fronteira já decidida no handoff U20: **PGH autoriza; PGD executa**. A release não cria nova autoridade e não move scheduler, leases, heartbeat, workers ou estado operacional vivo para PGH/PGA.

## Classificação da evidência

Os nove gates desta unidade são gates de **conformidade do protocolo**. A implementação runtime é evidência separada e pinada em `debianlima/pgh-distributed-session-control-plane@85652710ac7514772b7b89043645697bae1519d6`, registrada pela U36D como `376/376_PASS`. Esta unidade não afirma ter reexecutado esse pytest no fallback wireguard.

## Invariantes

- autorização semântica PGH é obrigatória antes da materialização operacional;
- `OperationalPermissionBinding` e `ResourceLease` pertencem ao PGD e permanecem dentro da autorização recebida;
- `OutcomeEvidenceEnvelope` retorna como `observed`, nunca como conhecimento homologado automático;
- stream/sessão preserva proveniência e não carrega segredo;
- takeover humano exige proveniência;
- efeito observado é diferente de mero exit code do processo.

## Dependência da tríade

Esta release só é publicada como parte da homologação T-019/T-020 com PGH 2.0 e PGA 1.0. O tag final é criado somente depois do gate conjunto.
