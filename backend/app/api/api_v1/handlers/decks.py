from typing import List
from uuid import UUID

from fastapi import APIRouter, Depends
from ....schemas.deck_schema import DeckOut, DeckCreate
from ....models.user_model import User
from ....models.deck_model import Deck
from ....api.deps.user_deps import get_current_user
from ....services.deck_service import DeckService, DeckUpdate


deck_router = APIRouter()


@deck_router.get('/', summary="Get all the decks of the user", response_model=List[DeckOut])
async def list_decks(current_user: User = Depends(get_current_user)):
    """Retrieve a list of all existing decks"""
    return await DeckService.list_decks(current_user)


@deck_router.post('/create', summary="Create a deck", response_model=Deck)
async def create_deck(data: DeckCreate, current_user: User = Depends(get_current_user)):
    return await DeckService.create_deck(data, current_user)


@deck_router.get('/{deck_id}', summary="Get deck by deck_id", response_model=DeckOut)
async def retrieve(deck_id: UUID, current_user: User = Depends(get_current_user)):
    return await DeckService.retrieve_deck(deck_id, current_user)


@deck_router.put('/{deck_id}', summary="Update deck by deck_id", response_model=DeckOut)
async def update(deck_id: UUID, data: DeckUpdate, current_user: User = Depends(get_current_user)):
    return await DeckService.update_deck(deck_id, data, current_user)


@deck_router.delete('/{deck_id}', summary="Delete deck by deck_id")
async def delete(deck_id: UUID, current_user: User = Depends(get_current_user)):
    await DeckService.delete_deck(deck_id, current_user)
    return None
