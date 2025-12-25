from __future__ import annotations

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes import articles_router, health_router, sources_router, stats_router
from app.core.config import settings

app = FastAPI(title="Portal Política API", version="0.1.0")

allowed_origins = [
    "http://localhost",
    "http://localhost:3000",
    "http://localhost:53000",
    "http://127.0.0.1",
    "http://127.0.0.1:3000",
    "http://127.0.0.1:53000",
]

if settings.env == "dev":
    app.add_middleware(
        CORSMiddleware,
        allow_origins=allowed_origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

app.include_router(health_router)
app.include_router(sources_router)
app.include_router(articles_router)
app.include_router(stats_router)
