# Portal Política

O Portal Política é uma plataforma para organizar, publicar e acompanhar informações
políticas de forma transparente e acessível.

## Stack

- Next.js (web)
- FastAPI (API)
- Celery (worker)
- Postgres
- Redis

## Como rodar com Docker

1. Copie o arquivo `.env.example` para `.env` e ajuste conforme necessário.
2. Execute:

```bash
make up
```

> **Observação:** Neste passo, a app ainda não foi implementada; apenas infra e estrutura.

## Portas padrão

| Serviço   | Porta host | Porta container |
|-----------|------------|-----------------|
| Postgres  | 55432      | 5432            |
| Redis     | 56379      | 6379            |
| API       | 58000      | 8000            |
| Web       | 53000      | 3000            |

As portas podem ser alteradas via `.env` usando as variáveis `POSTGRES_PORT`,
`REDIS_PORT`, `API_PORT` e `WEB_PORT`.
