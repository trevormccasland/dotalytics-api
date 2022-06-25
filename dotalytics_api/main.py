from http import HTTPStatus
import sys

from fastapi import FastAPI, HTTPException
import uvicorn

from dotalytics_api import client
from dotalytics_api.types import player
from fastapi.middleware import Middleware
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(middleware=[
    Middleware(
        CORSMiddleware,
        allow_origins=['*'],
        allow_credentials=True,
        allow_methods=['*'],
        allow_headers=['*']
    )
])


@app.get("/healthz")
def root():
    return {"message": 'up and running'}


@app.get("/matches")
def get_matches(account_id: str, matches_requested: int = 5):

    match_history = None
    matches = None
    heroes = None
    items = None

    try:
        match_history = client.get_match_history(
            account_id, matches_requested=matches_requested)
        matches = [client.get_match_details(match.match_id).result for match in match_history.result.matches]
        heroes = client.get_heroes().result
        items = client.get_game_items().result.items
    except Exception:
        raise HTTPException(status_code=HTTPStatus.BAD_REQUEST,
                            detail="Bad request")

    for m in range(len(matches)):
        for p in range(len(matches[m].players)):
            item_neutral_name = ''
            item_neutral = matches[m].players[p].item_neutral
            item_0 = matches[m].players[p].item_0
            item_0_name = ''
            item_1 = matches[m].players[p].item_1
            item_1_name = ''
            item_2 = matches[m].players[p].item_2
            item_2_name = ''
            item_3 = matches[m].players[p].item_3
            item_3_name = ''
            item_4 = matches[m].players[p].item_4
            item_4_name = ''
            item_5 = matches[m].players[p].item_5
            item_5_name = ''
            backpack_0 = matches[m].players[p].backpack_0
            backpack_0_name = ''
            backpack_1 = matches[m].players[p].backpack_1
            backpack_1_name = ''
            backpack_2 = matches[m].players[p].backpack_2
            backpack_2_name = ''
            for item in items:
                if item_neutral == item.id:
                    item_neutral_name = item.name
                if item_0 == item.id:
                    item_0_name = item.name
                elif item_1 == item.id:
                    item_1_name = item.name
                elif item_2 == item.id:
                    item_2_name = item.name
                elif item_3 == item.id:
                    item_3_name = item.name
                elif item_4 == item.id:
                    item_4_name = item.name
                elif item_5 == item.id:
                    item_5_name = item.name
                elif backpack_0 == item.id:
                    backpack_0_name = item.name
                elif backpack_1 == item.id:
                    backpack_1_name = item.name
                elif backpack_2 == item.id:
                    backpack_2_name = item.name
            for hero in heroes.heroes:
                if hero.id == matches[m].players[p].hero_id:
                    matches[m].players[p] = player.Player(
                        player_slot=matches[m].players[p].player_slot,
                        team_number=matches[m].players[p].team_number,
                        hero_id=matches[m].players[p].hero_id,
                        item_0=matches[m].players[p].item_0,
                        item_1=matches[m].players[p].item_1,
                        item_2=matches[m].players[p].item_2,
                        item_3=matches[m].players[p].item_3,
                        item_4=matches[m].players[p].item_4,
                        item_5=matches[m].players[p].item_5,
                        item_neutral=matches[m].players[p].item_neutral,
                        backpack_0=matches[m].players[p].backpack_0,
                        backpack_1=matches[m].players[p].backpack_1,
                        backpack_2=matches[m].players[p].backpack_2,
                        item_netral=matches[m].players[p].item_neutral,
                        kills=matches[m].players[p].kills,
                        deaths=matches[m].players[p].deaths,
                        assists=matches[m].players[p].assists,
                        leaver_status=matches[m].players[p].leaver_status,
                        last_hits=matches[m].players[p].last_hits,
                        denies=matches[m].players[p].denies,
                        gold_per_min=matches[m].players[p].gold_per_min,
                        xp_per_min=matches[m].players[p].xp_per_min,
                        level=matches[m].players[p].level,
                        net_worth=matches[m].players[p].net_worth,
                        aghanims_scepter=matches[m].players[p].aghanims_scepter,
                        aghanims_shard=matches[m].players[p].aghanims_shard,
                        moonshard=matches[m].players[p].moonshard,
                        hero_damage=matches[m].players[p].hero_damage,
                        tower_damage=matches[m].players[p].tower_damage,
                        hero_healing=matches[m].players[p].hero_healing,
                        gold=matches[m].players[p].gold,
                        gold_spent=matches[m].players[p].gold_spent,
                        scaled_hero_damage=matches[m].players[p].scaled_hero_damage,
                        scaled_tower_damage=matches[m].players[p].scaled_tower_damage,
                        scaled_hero_healing=matches[m].players[p].scaled_hero_healing,
                        item_neutral_name=item_neutral_name,
                        hero_name=hero.name,
                        item_0_name=item_0_name,
                        item_1_name=item_1_name,
                        item_2_name=item_2_name,
                        item_3_name=item_3_name,
                        item_4_name=item_4_name,
                        item_5_name=item_5_name,
                        backpack_0_name=backpack_0_name,
                        backpack_1_name=backpack_1_name,
                        backpack_2_name=backpack_2_name,
                    )
                    break

    return matches


def main():
    uvicorn.run("dotalytics_api.main:app", host="0.0.0.0", port=8888, reload=True, log_level="info")


if __name__ == "__main__":
    sys.exit(main())
