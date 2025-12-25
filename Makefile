up:
\tdocker compose up -d --build

down:
\tdocker compose down

logs:
\tdocker compose logs -f --tail=200

ps:
\tdocker compose ps

restart:
\tdocker compose restart

clean:
\tdocker compose down -v

migrate:
\tdocker compose exec api alembic upgrade head

makemigrations:
\tdocker compose exec api alembic revision --autogenerate -m "init"
