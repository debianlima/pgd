# U-PGD-09 — árvores sistêmicas ontológicas sincronizadas por WCB

## Modelo

O agente vê uma projeção hierárquica **A+** para reduzir custo cognitivo, mas o estado interno é um DAG tipado. Assim uma mesma tarefa, máquina, fila, lease ou peer pode participar de várias relações sem ganhar identidades duplicadas.

As quatro vistas são:

- **ProjectTree** — portfólio/projetos habilitados e relações de elegibilidade/prioridade;
- **ResourceTree** — recursos, máquinas, filas, reservas, leases, capacidades, localização, projeto consumidor e peers;
- **AuthTree** — bindings, escopos e autoridade por referência; **segredos nunca são persistidos na árvore**;
- **TaskTree** — uma por projeto habilitado, contendo ramos independentes e dependências cruzadas.

## Ritual repetitivo

O procedimento não depende da memória episódica do agente. Em **toda** conclusão/atualização de trabalho ele atualiza os nós/arestas impactados e emite um delta pelo **WCB**. Em toda recepção WCB ele compara `revision + content_hash` das árvores que usa. Antes de decidir/alocar, se a revisão local não corresponde ao último WCB aplicado, sincroniza primeiro.

O agente reavalia somente o ramo afetado pelo delta. Full rescan do portfólio não é o default.

## Árvore de recursos

Um nó como `resource:work34` pode ser navegado ontologicamente para:

`recurso -> fila -> reserva/lease -> agente/projeto -> localização -> peer -> capacidades`.

Portanto perguntas como “onde está o recurso?”, “quem reservou?”, “qual fila?”, “qual projeto está usando?” e “qual peer conhece o estado remoto?” são resolvidas por relações tipadas, não por busca textual livre no histórico.

## Peers e árvores remotas

Cada árvore pode carregar `remote_subtrees` com `peer_id`, `tree_ref`, `revision`, `content_hash`, `authority_ref` e `last_verified_at`. O WCB distribui a **referência e o delta**, não a árvore remota inteira. O consumidor busca a subárvore somente quando o ramo é necessário e valida revisão/hash antes de usá-la.

Isso permite que um peer remoto exponha seu estado de fila/recurso/projeto sem transformar o broadcast em cópia massiva de contexto.

## RAG e repetição ativa

Todo nó tem `rag_refs` e `retrieval_terms`. A instrução que acompanha a raiz é deliberadamente repetitiva:

> **Esta é uma árvore de visão sistêmica que permite acesso ao banco RAG e navegação ontológica entre recursos disponíveis de cada nó; antes de decidir, confirme o nó, suas relações, revisão/hash e referências canônicas.**

O agente carrega a raiz e expande só o ramo necessário. O RAG fornece detalhes/evidências; a árvore fornece estrutura e localização sem substituir contratos, Git, locks, grants ou autoridade.

## Persistência

O contrato recomenda SQLite com projeção relacional de grafo, índices B-tree maduros e refs RAG. Não é necessário inventar um banco de árvore próprio. A mesma representação serve ao cache local e à sincronização distribuída.

## WCB Tree Delta

Cada mutação produz um delta compacto com `tree_id`, tipo, revisão anterior/nova, hash, `delta_ref`, nós alterados/invalidados e refs remotas alteradas. `NO_CHANGE` continua auditável sem fanout, preservando a proteção contra eco já homologada no WCB.
