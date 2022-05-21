import sys

from fastapi import FastAPI
import uvicorn

from dotalytics_api import client

app = FastAPI()


@app.get("/health")
def root():
    return {"message": 'up and running'}


@app.get("/matches")
def matches(account_id: str):
    match_history = client.get_match_history(account_id)

    return match_history


def main():
    uvicorn.run("dotalytics_api.main:app", host="0.0.0.0", port=8888, reload=True, log_level="info")


if __name__ == "__main__":
    sys.exit(main())