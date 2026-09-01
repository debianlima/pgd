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
