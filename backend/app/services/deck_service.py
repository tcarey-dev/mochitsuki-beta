from typing import List
from uuid import UUID

from ..models.user_model import User
from ..models.deck_model import Deck
from ..schemas.deck_schema import DeckCreate, DeckUpdate


class DeckService:
    @staticmethod
    async def list_decks(user: User) -> List[Deck]:
        decks = await Deck.find(Deck.owner_id == user.user_id).to_list()
        return decks

    @staticmethod
    async def create_deck(data: DeckCreate, user: User) -> Deck:
        deck = Deck(**data.dict(), owner_id=user.user_id)
        return await deck.insert()


    @staticmethod
    async def retrieve_deck(deck_id: UUID, current_user: User):
        deck = await Deck.find_one(Deck.deck_id == deck_id, Deck.owner_id == current_user.user_id)
        return deck


    @staticmethod
    async def update_deck(deck_id: UUID, data: DeckUpdate, current_user: User):
        deck = await DeckService.retrieve_deck(deck_id, current_user)
        await deck.update({"$set": data.dict(exclude_unset=True)})
        await deck.save()
        return deck

    @staticmethod
    async def delete_deck(deck_id: UUID, current_user: User):
        deck = await DeckService.retrieve_deck(deck_id, current_user)
        if deck:
            await deck.delete()
        return None


