from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, ConfigDict


class ArticleCreate(BaseModel):
    source_id: int
    title: str
    subtitle: str | None = None
    summary: str | None = None
    content: str | None = None
    author: str | None = None
    original_published_at: datetime | None = None
    topic: str | None = None
    tags: list[str] | None = None
    canonical_url: str | None = None
    status: str | None = None


class ArticleRead(BaseModel):
    id: int
    source_id: int
    title: str
    subtitle: str | None
    summary: str | None
    content: str | None
    author: str | None
    original_published_at: datetime | None
    topic: str | None
    tags: list[str] | None
    canonical_url: str | None
    status: str | None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)
