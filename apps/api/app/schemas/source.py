from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, ConfigDict


class SourceBase(BaseModel):
    name: str
    domain: str
    type: str
    allowlisted: bool = False
    trust_score_base: float = 0
    is_primary: bool = False
    notes: str | None = None


class SourceCreate(SourceBase):
    pass


class SourceRead(SourceBase):
    id: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
