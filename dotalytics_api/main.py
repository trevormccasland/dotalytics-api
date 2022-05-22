import sys

from fastapi import FastAPI
import uvicorn

from dotalytics_api import client
from dotalytics_api.types import match_details

app = FastAPI()


@app.get("/health")
def root():
    return {"message": 'up and running'}



@app.get("/matches")
def get_matches(account_id: str):
    match_history = client.get_match_history(account_id, matches_requested=5)
    matches = []
    for match in match_history.result.matches:
        matches.append(client.get_match_details(match.match_id).result)
    heroes = client.get_heroes().result
    items = client.get_game_items().result.items
    for m in range(len(matches)):
        for p in range(len(matches[m].players)):
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
                    backpack_2_name == item.name
            for hero in heroes.heroes:
                if hero.id == matches[m].players[p].hero_id:

                    matches[m].players[p] = match_details.Player(
                        **matches[m].players[p].dict(),
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