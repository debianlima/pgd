# U-PGD-11 — visões sistêmicas dinâmicas

U09 definiu as árvores/DAGs; U10 homologou o WCB. U11 define como essas estruturas viram uma visão operacional viva durante a produção.

## Bootstrap do projeto

Ao criar ou habilitar um projeto, o PGD materializa um **mapa macro inicial** a partir de manifesto, contratos, inventário runtime, refs de autoridade e árvores já existentes. O mapa registra as interconexões específicas daquele projeto. Contexto interprojeto escolhe primeiro o mapa macro aplicável e só depois expande o ramo necessário.

Exemplo: para infraestrutura, o agente começa pelo `INFRASTRUCTURE_MAP`; não faz varredura ontológica global. Dali navega máquina → recurso → fila/reserva/lease/localização/capability/projeto/peer e, quando necessário, segue refs **HRAG/RAG**.

## Write-back obrigatório

Toda mutação relevante usa exatamente um dos canais:

- `DIRECT_STORE`: agente com acesso direto atualiza o store canônico, incrementa revisão/hash e então emite WCB.
- `WEB_EXECUTOR`: agente WebCX envia a mutação ao executor; somente após commit no store canônico o executor emite WCB.

Toda mutação atualiza o ramo afetado e toda atualização efetiva da árvore gera WCB. O procedimento é **repetitivo** e não depende de o agente lembrar se “vale a pena” sincronizar.

## Visão compartilhada e private index

Cada agente mantém uma base compartilhada identificada por `base_revision + base_hash + last_wcb_epoch`. Um **private index** local é permitido para acelerar navegação, mas nunca é autoridade. Quando a base muda, o índice privado precisa ser invalidado/rebaseado antes de dirigir nova mutação.

Ao receber WCB, o agente compara revisão/hash; aplica o delta ou busca novamente somente o ramo impactado. Self-origin também é reaplicado idempotentemente para manter a mesma visão coletiva.

## TaskTree e coordenação

O agente enxerga a própria tarefa dentro do `TaskTree` do projeto. Cada nó de tarefa indexa **agente** alocado, **recursos** vinculados, **dependências**, filas, reservas, leases, projeto, estado e refs de autoridade.

Mudou tarefa, alocação de agente ou recurso: recalcula somente as ligações do ramo afetado e emite WCB. A próxima tarefa vem da fronteira READY da árvore; não exige reavaliar o projeto inteiro.

## PGH 2.0 / RAG

A projeção para PGH 2.0 é `mapa macro → nó de árvore → refs HRAG/RAG`. A raiz repete a instrução operacional: esta é uma visão sistêmica compartilhada/versionada; confirme revisão/hash e refs canônicas antes de mutar, expanda só o ramo necessário e sincronize via WCB se stale.

A visão não substitui banco operacional, Git, manifesto, contratos, locks ou gates. Autorização usa somente refs; segredos e valores de credencial não entram na árvore nem no broadcast.
