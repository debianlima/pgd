# U-PGD-12 — Operational Context Forest

A Operational Context Forest é a raiz de navegação operacional compartilhada do PGD/PGH 2.0. Ela reduz buscas globais e obriga o agente a começar por um mapa conhecido, versionado e verificável.

## SystemNavigatorGraph

`SystemNavigatorGraph` é a raiz. A intenção seleciona o grafo apropriado antes da expansão de qualquer ramo. Infraestrutura vai para ResourceGraph/StateHealthGraph; tarefa para TaskGraph; “quem pode executar?” para CapabilityRoutingGraph; conhecimento para KnowledgeGraph; identidade/acesso para IdentityAuthorizationGraph; freshness para ProvenanceFreshnessGraph.

## Grafos especializados

A floresta contém 12 grafos: SystemNavigatorGraph, ProjectGraph, TaskGraph, ResourceGraph, IdentityAuthorizationGraph, CapabilityRoutingGraph, KnowledgeGraph, ArtifactGraph, StateHealthGraph, CommunicationGraph, ProvenanceFreshnessGraph e PeerFederationGraph. A visão é DAG e usa relações tipadas com **backlinks** obrigatórios.

## Recursos e competências associadas

ResourceGraph indexa máquina/localização, fila, reserva, lease, projeto/tarefa, capabilities, **competências associadas**, `skill_refs` e peer. Ao abrir um recurso, o agente resolve as capabilities e competências associadas e só então carrega as skills necessárias.

O recurso não é autoridade de skill. `CapabilityRoutingGraph` liga tarefa/requisito → capability → competency → agente/recurso. A versão carregável de uma skill é resolvida exclusivamente pela `linha_homologada` do catálogo; o inventário de recurso só fornece referências.

## Conhecimento e proveniência

KnowledgeGraph liga contrato, documentação, evidência, skill, ontologia, HRAG, RAG, B+ e artefato. ProvenanceFreshnessGraph exige `source_ref`, revision, content hash, observed_at e authority_ref. Visão stale precisa sincronizar antes de dirigir mutação.

O caminho padrão é `SystemNavigatorGraph → macro graph → node → canonical refs → HRAG/RAG se necessário`. Isso evita busca global repetitiva.

## Federação e comunicação

PeerFederationGraph mantém refs de peers, tipos de grafo oferecidos, revision/hash, capabilities, query_ref, autoridade e validade. Replicação total não é padrão: busca-se apenas o ramo impactado.

CommunicationGraph liga chats/agentes/supervisores/projetos/tarefas a watermarks WCB para calcular quem precisa ser sincronizado.

## Autorização

IdentityAuthorizationGraph contém identidade, role, capability, grant, escopo, authority_ref, validade, `credential_ref` e `resolver_ref`. Valor de **credencial** ou segredo nunca entra no grafo nem no broadcast.

## Sincronização

Toda mutação efetiva atualiza os grafos atingidos e emite WCB `GraphDelta + graph_revision + content_hash + refs`. O receptor compara revisão/hash, aplica o delta ou refaz apenas o ramo stale; índices privados são invalidados/rebaseados.

A raiz repete ao agente: esta é uma visão sistêmica compartilhada; navegue pelo SystemNavigatorGraph, confirme revision/hash/proveniência, use refs canônicas e resolva skills pela linha_homologada antes de agir.
