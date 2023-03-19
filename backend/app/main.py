from fastapi import FastAPI
from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient

from .core.config import settings
from .models.user_model import User
from .api.api_v1.router import router
from .models.deck_model import Deck

from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://127.0.0.1:8080",
    "http://localhost:63342"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def app_init():
    """
    initialize application services
    """

    db_client = AsyncIOMotorClient(settings.MONGO_CONNECTION_STRING)

    await init_beanie(
        database=db_client.mochitsuki,
        document_models=[
            User,
            Deck
        ]
    )


app.include_router(router, prefix=settings.API_V1_STR)
