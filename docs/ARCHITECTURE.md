# Arquitetura

Visão geral do monorepo do Portal Política:

## Componentes

- **Frontend (apps/web)**: aplicação Next.js para a interface pública e administrativa.
- **API (apps/api)**: serviço FastAPI responsável pela camada de negócio e exposição de dados.
- **Worker (apps/worker)**: serviço Celery para ingestão, processamento e tarefas assíncronas.
- **Shared (packages/shared)**: biblioteca de tipos/utilidades compartilhadas.

## Pipeline (alto nível)

1. Usuários acessam o frontend para consultar e administrar conteúdo.
2. O frontend consome a API para leitura e escrita de dados.
3. O worker executa ingestões e processamentos assíncronos, persistindo resultados no banco.
