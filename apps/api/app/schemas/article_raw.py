from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, ConfigDict


class ArticleRawCreate(BaseModel):
    source_id: int
    url: str
    canonical_url: str | None = None
    fetched_at: datetime | None = None
    raw_text: str | None = None
    content_hash: str | None = None
    status: str | None = None


class ArticleRawRead(BaseModel):
    id: int
    source_id: int
    url: str
    canonical_url: str | None
    fetched_at: datetime | None
    raw_text: str | None
    content_hash: str | None
    status: str | None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
