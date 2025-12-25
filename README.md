# Portal Política

O Portal Política é uma plataforma para organizar, publicar e acompanhar informações
políticas de forma transparente e acessível.

## Stack

- FastAPI (API)
- Postgres
- Redis
- Next.js (web, planejado)
- Celery (worker, planejado)

## Como rodar com Docker

1. Copie o arquivo `.env.example` para `.env` e ajuste conforme necessário.
2. Execute:

```bash
make up
```

3. Em seguida, aplique as migrações:

```bash
make migrate
```

> **Observação:** Neste passo, apenas o backend básico foi implementado; frontend e worker ainda não existem.

## Backend (API)

- O backend lê variáveis do `.env` na raiz.
- Health check disponível em: `http://localhost:58000/health` (ou porta definida em `API_PORT`).
- Swagger disponível em: `http://localhost:58000/docs`.

## Portas padrão

| Serviço   | Porta host | Porta container |
|-----------|------------|-----------------|
| Postgres  | 55432      | 5432            |
| Redis     | 56379      | 6379            |
| API       | 58000      | 8000            |

As portas podem ser alteradas via `.env` usando as variáveis `POSTGRES_PORT`,
`REDIS_PORT` e `API_PORT`.
