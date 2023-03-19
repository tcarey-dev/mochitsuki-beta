from datetime import datetime
from typing import Optional
from uuid import UUID
from pydantic import BaseModel, Field


class DeckCreate(BaseModel):
    title: str = Field(..., title='Title', max_length=55, min_length=1)
    description: Optional[str] = Field(..., title='Title', max_length=755, min_length=1)
    parent_id: Optional[UUID] = None


class DeckUpdate(BaseModel):
    title: Optional[str] = Field(None, title='Title', max_length=55, min_length=1)
    description: Optional[str] = Field(None, title='Title', max_length=755, min_length=1)
    parent_id: Optional[UUID] = None


class DeckOut(BaseModel):
    deck_id: UUID
    parent_id: Optional[UUID]
    title: str
    description: Optional[str]
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)