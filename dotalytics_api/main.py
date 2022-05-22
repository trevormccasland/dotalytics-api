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
    for m in range(len(matches)):
        for p in range(len(matches[m].players)):
            for hero in heroes.heroes:
                if hero.id == matches[m].players[p].hero_id:
                    matches[m].players[p] = match_details.Player(**matches[m].players[p].dict(), hero_name=hero.name)
                    break

    return matches


def main():
    uvicorn.run("dotalytics_api.main:app", host="0.0.0.0", port=8888, reload=True, log_level="info")


if __name__ == "__main__":
    sys.exit(main())