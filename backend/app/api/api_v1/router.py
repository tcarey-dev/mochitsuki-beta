from fastapi import APIRouter
from .handlers.user import user_router
from ...api.auth.jwt import auth_router
from ...api.api_v1.handlers.cards import card_router
from ...api.api_v1.handlers.decks import deck_router
from ...api.api_v1.handlers.mochi import mochi_router

router = APIRouter()


router.include_router(user_router, prefix="/user", tags=["users"])
router.include_router(auth_router, prefix="/auth", tags=["auth"])
router.include_router(card_router, prefix="/cards", tags=["cards"])
router.include_router(deck_router, prefix="/decks", tags=["decks"])
router.include_router(mochi_router, prefix="/mochi", tags=["mochi API"])



