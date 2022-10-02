from functools import lru_cache
import httpx
import requests

from dotalytics_api import config
from dotalytics_api.types import items, heroes, match_details, match_history


base_url = 'https://api.steampowered.com/'
api_key = config.get('DotaAPIKey')


@lru_cache
async def get_match_history(account_id: str, matches_requested: int = 25) -> match_history.GetMatchHistoryResponse:
    url = base_url + 'IDOTA2Match_570/GetMatchHistory/v1'
    async with httpx.AsyncClient() as client:
        resp = await client.get(url, params={'account_id': account_id, 'key': api_key, 'matches_requested': matches_requested})
        resp.raise_for_status()
        return match_history.GetMatchHistoryResponse(**resp.json())



@lru_cache
async def get_match_details(match_id: int) -> match_details.GetMatchDetailsResponse:
    url =  base_url + 'IDOTA2Match_570/GetMatchDetails/v1'
    resp = await requests.get(url, {'match_id': match_id, 'key': api_key})
    resp.raise_for_status()
    return match_details.GetMatchDetailsResponse(**resp.json())


@lru_cache
async def get_heroes() -> heroes.GetHeroesResponse:
    url =  base_url + 'IEconDOTA2_570/GetHeroes/v1'
    resp = await requests.get(url, {'key': api_key})resp.raise_for_status()
    return heroes.GetHeroesResponse(**resp.json())


@lru_cache
async def get_game_items() -> items.GetGameItemsResponse:
    url =  base_url + 'IEconDOTA2_570/GetGameItems/v1'
    resp = await requests.get(url, {'key': api_key})resp.raise_for_status()
    return items.GetGameItemsResponse(**resp.json())
