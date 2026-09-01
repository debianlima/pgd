# U-PGD-13 — reconciliação do fechamento RHGD

Esta unidade consome o fechamento estável da RHGD sem reescrever as evidências históricas U-PGD-04/U-PGD-05 e sem alterar a release PGD 1.0.0.

## Referências finais consumidas

- PGD base pós-U12: `3f7d70e974271a0ee316df9425d5e955225fddd4`.
- RHGD reconciliada: `ee24a3916e964c7ec624b666daa035aa6f4e97c5`.
- PGA: `c151e58adf05339eee7f762fa0a96b401e4b6985`.
- PGH base canônica: `304b9914ae44b0ac4240d912bd81f7be87d5a708`.
- runtime/control-plane no safe point fechado U260: `6c3708aeff692c6eac5ce2a39d134afd64f616df`.
- catálogo após RHGD Project-Skill 0.0.7: `07b6f5ef067873f0f6e77896a477184fb9dd53db`.

## Fronteira reconciliada

**PGA governa; PGH autoriza/contextualiza; PGD agenda/executa; RHGD federa.** O contrato `pgd-rhgd-federation/1` continua sendo a fronteira operacional. `FederatedDestinationMatcher` na RHGD apenas filtra e ranqueia destinos federados; `CognitiveScheduler` é alias legado de compatibilidade e não possui fila, admission, lease, retry, recovery ou estado runtime.

U-PGD-04 e U-PGD-05 preservam os hashes RHGD que observaram no momento histórico. U-PGD-13 acrescenta a referência corrente em vez de normalizar retroativamente essas evidências.

A tag/release `v1.0.0` do PGD permanece imutável; esta é reconciliação pós-release de dependências.
