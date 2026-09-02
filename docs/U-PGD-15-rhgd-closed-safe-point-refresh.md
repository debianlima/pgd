# U-PGD-15 — refresh do safe point RHGD fechado

O PGD reconcilia o peer RHGD sem consumir HEAD de unidade ainda em andamento.

## Safe point consumido

O último **safe point fechado** do RHGD antes da U12 é U-RHGD-11, commit `c74daa217f307b1fb8d78e10fe5218d8e496dbd8`, contrato estrutural v4 e `rhgd-project@0.0.10`. Nesse commit `trabalho_compartilhado={}` e as entradas U11 44–47 estão aceitas.

O HEAD RHGD observado depois dele é `397e03821954ebeb88780b6658efec95ecb095b7`, sob `U-RHGD-12-LIVE-CAPABILITY-DISCOVERY-CONTRACT`. A U15 **não consome** essa U-RHGD-12 enquanto a zona permanece ativa; apenas prova que U11 é ancestral do HEAD corrente.

## Contrato PGD preservado

`pgd-rhgd-federation/1` continua byte-idêntico, SHA-256 `3135f6cee8de163d55c9782b1b1de300359a0e2936f79f2a243a03941fefdc52`.

A fronteira permanece:

- PGD possui runtime, admission, fila, scheduler, lease, retry e recovery;
- RHGD possui discovery/federação/transporte e não cria segundo scheduler;
- o request federado exige autorização PGH e capacidades requeridas;
- a resposta PGD fornece `execution_ref`; um transporte RHGD posterior referencia esse `execution_ref`, não inventa `assignment_ref` nem lease.

Não há mudança funcional necessária no PGD para consumir o safe point U11. A futura conclusão da U-RHGD-12 deverá ser reconciliada em nova unidade somente depois de fechar o próprio safe point.

## Release

A release PGD `v1.0.0` permanece imutável; esta unidade apenas atualiza a referência reconciliada do peer e não promove release, runtime ou autoridade.
