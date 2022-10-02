import asyncio
from http import HTTPStatus
from typing import Dict

from fastapi import FastAPI, HTTPException
from fastapi.middleware import Middleware
from fastapi.middleware.cors import CORSMiddleware
import uvicorn


from dotalytics_api import client
from dotalytics_api.types import player

app = FastAPI(
    middleware=[
        Middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )
    ]
)


<<<<<<< HEAD
async def get_hero_map() -> Dict:
=======
def get_heroes_map() -> Dict:
>>>>>>> 3aba7ff (clean up indices)
    try:
        res = (await client.get_heroes()).result.heroes
        return {r.id: r.name for r in res}
    except Exception as error:
        raise HTTPException(status_code=HTTPStatus.BAD_REQUEST,
                            detail="Bad request %s" % error)


def get_items_map() -> Dict:
    try:
        res = client.get_game_items().result.items
        return {r.id: r.name for r in res}
    except Exception:
        raise HTTPException(status_code=HTTPStatus.BAD_REQUEST, detail="Bad request")


@app.get("/healthz")
def root():
    return {"message": "up and running"}


@app.get("/matches")
async def get_matches(account_id: str, matches_requested: int = 5):

    match_history = None
    matches = None

<<<<<<< HEAD
    hero_map = await get_hero_map()
=======
    hero_map = get_heroes_map()
    item_map = get_items_map()

    print(item_map)
>>>>>>> 3aba7ff (clean up indices)

    try:
        match_history = await client.get_match_history(
            account_id, matches_requested=matches_requested)
        # Unfortunately, we receive a 429 (Too Many Requests) error when we get match details with asyncio.gather
        matches = [
            (await client.get_match_details(match.match_id)).result for match in match_history.result.matches
        ]
<<<<<<< HEAD
        heroes, items = await asyncio.gather(client.get_heroes(), client.get_game_items())
        heroes = heroes.result
        items = items.result.items
    except Exception as error:
        raise HTTPException(status_code=HTTPStatus.BAD_REQUEST,
                            detail="Bad request %s" % error)
=======

    except Exception:
        raise HTTPException(status_code=HTTPStatus.BAD_REQUEST, detail="Bad request")
>>>>>>> 3aba7ff (clean up indices)

    for m in matches:
        for pb in m.picks_bans:
            pb.hero_name = hero_map.get(pb.hero_id)

        for p in m.players:
            p.hero_name = hero_map.get(p.hero_id)
            p.item_neutral_name = item_map.get(p.item_neutral)
            p.item_0_name = item_map.get(p.item_0)
            p.item_1_name = item_map.get(p.item_1)
            p.item_2_name = item_map.get(p.item_2)
            p.item_3_name = item_map.get(p.item_3)
            p.item_4_name = item_map.get(p.item_4)
            p.item_5_name = item_map.get(p.item_5)
            p.backpack_0_name = item_map.get(p.backpack_0)
            p.backpack_1_name = item_map.get(p.backpack_1)
            p.backpack_2_name = item_map.get(p.backpack_2)
    return matches


async def amain():
    config = uvicorn.Config("dotalytics_api.main:app", host="0.0.0.0", port=8888, reload=True, log_level="info")
    server = uvicorn.Server(config)
    await server.serve()


def main():
    asyncio.run(amain())


if __name__ == "__main__":
    main()
