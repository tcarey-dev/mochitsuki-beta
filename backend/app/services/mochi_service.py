from ..core.config import settings

import json
import httpx


mochi_api_base = 'https://app.mochi.cards/api/'
key = settings.MOCHI_KEY
apikey = (key, '')
headers = {
    "Content-Type": "application/json",
    "Accept": "application/json"
}


class MochiService:

    @staticmethod
    async def list_mochi():  # -> List[Deck]:
        site = mochi_api_base + 'decks'
        async with httpx.AsyncClient() as client:
            getdeck_resp = await client.get(site, auth=apikey)
        decks = json.loads(getdeck_resp.text)
        return decks

    @staticmethod
    async def create_card(deck_in: str, content: str):
        site = mochi_api_base + 'cards'
        async with httpx.AsyncClient() as client:
            getdeck_resp = await client.get(mochi_api_base + 'decks', auth=apikey)

        deck_list = json.loads(getdeck_resp.text)

        deck = {deck['name']: deck['id'] for deck in deck_list['docs'] if deck['name'] == deck_in}
        print(deck)
        deck_id = deck[deck_in]
        print(deck_id)

        payload = {
                    "content": content,
                    "deck-id": deck_id,
                }

        httpx.post(site, auth=apikey, headers=headers, json=payload)

        return

    @staticmethod
    async def create_deck(deck_in, parent_in=None):
        site = mochi_api_base + 'decks'
        async with httpx.AsyncClient() as client:
            getdeck_resp = await client.get(site, auth=apikey)

        deck_list = json.loads(getdeck_resp.text)

        # check if deck already exists
        deck = {deck['name']: deck['id'] for deck in deck_list['docs'] if deck['name'] == deck_in}
        if deck:
            return deck[deck_in]

        # check if parent exists and create if not
        if parent_in:
            parent = {deck['name']: deck['id'] for deck in deck_list['docs'] if deck['name'] == parent_in}
            if parent:
                parent_id = parent[parent_in]
                payload = {"name": deck_in, "parent-id": parent_id}
            else:
                parent_req_payload = {"name": parent_in}
                parent_resp = httpx.post(site, auth=apikey, headers=headers, json=parent_req_payload)
                parent_resp_json = json.loads(parent_resp.text)
                parent_id = parent_resp_json['id']
                payload = {"name": deck_in, "parent-id": parent_id}
        else:
            payload = {"name": deck_in}

        # make a new deck if it doesn't exist
        resp = httpx.post(site, auth=apikey, headers=headers, json=payload)
        _deck = json.loads(resp.text)
        return _deck['id']

