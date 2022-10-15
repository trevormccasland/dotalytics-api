import asyncio
from http import HTTPStatus
from typing import Dict, List

from fastapi import FastAPI, HTTPException
from fastapi.middleware import Middleware
from fastapi.middleware.cors import CORSMiddleware
import uvicorn


from dotalytics_api import client
from dotalytics_api.types import match, match_history

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


async def get_hero_map() -> Dict[str, str]:
    try:
        res = (await client.get_heroes()).result.heroes
        return {r.id: r.name for r in res}
    except Exception as error:
        raise HTTPException(status_code=HTTPStatus.BAD_REQUEST,
                            detail="Bad request %s" % error)


async def get_items_map() -> Dict[str, str]:
    try:
        res = (await client.get_game_items()).result.items
        return {r.id: r.name for r in res}
    except Exception as error:
        raise HTTPException(status_code=HTTPStatus.BAD_REQUEST,
                            detail="Bad request %s" % error)


async def get_match_history(account_id: str, matches_requested: int) -> List[match_history.Match]:
    try:
        history = await client.get_match_history(
            account_id, matches_requested=matches_requested)
        return history.result.matches
    except Exception as error:
        raise HTTPException(status_code=HTTPStatus.BAD_REQUEST,
                            detail="Bad request %s" % error)


@app.get("/healthz")
def root():
    return {"message": "up and running"}


@app.get("/matches", response_model=List[match.Match])
async def get_matches(account_id: str, matches_requested: int = 5):

    match_details = None

    heroes, items, history = await asyncio.gather(
        get_hero_map(), get_items_map(), get_match_history(account_id, matches_requested))
    try:
        # Unfortunately, we receive a 429 (Too Many Requests) error when we get match details with asyncio.gather
        match_details = [
            (await client.get_match_details(game.match_id)).result for game in history
        ]
    except Exception as error:
        raise HTTPException(status_code=HTTPStatus.BAD_REQUEST,
                            detail="Bad request %s" % error)
    matches: List[match.Match] = []
    for m in match_details:
        picks_bans: List[match.PicksBan] = []
        for pb in m.picks_bans:
            picks_bans.append(
                match.PicksBan(**pb.dict(), hero_name=heroes.get(pb.hero_id))
            )
        players: List[match.Player] = []
        for p in m.players:
            players.append(
                match.Player(
                    **p.dict(),
                    hero_name=heroes.get(p.hero_id),
                    item_neutral_name=items.get(p.item_neutral),
                    item_0_name=items.get(p.item_0),
                    item_1_name=items.get(p.item_1),
                    item_2_name=items.get(p.item_2),
                    item_3_name=items.get(p.item_3),
                    item_4_name=items.get(p.item_4),
                    item_5_name=items.get(p.item_5),
                    backpack_0_name=items.get(p.backpack_0),
                    backpack_1_name=items.get(p.backpack_1),
                    backpack_2_name=items.get(p.backpack_2),
                )
            )
        game = m.dict()
        del game['players']
        del game['picks_bans']
        matches.append(
            match.Match(
                **game,
                players=players,
                picks_bans=picks_bans
            )
        )

    return matches


async def amain():
    config = uvicorn.Config("dotalytics_api.main:app", host="0.0.0.0", port=8888, reload=True, log_level="info")
    server = uvicorn.Server(config)
    await server.serve()


def main():
    asyncio.run(amain())


if __name__ == "__main__":
    main()
