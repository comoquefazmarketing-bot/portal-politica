from app.api.routes.articles import router as articles_router
from app.api.routes.health import router as health_router
from app.api.routes.sources import router as sources_router
from app.api.routes.stats import router as stats_router

__all__ = ["articles_router", "health_router", "sources_router", "stats_router"]
