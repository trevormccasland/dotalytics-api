from async_lru import alru_cache
import asyncio
import httpx

from dotalytics_api import config
from dotalytics_api.types import items, heroes, match_details, match_history, steam_user


base_url = 'https://api.steampowered.com/'
api_key = config.get('DotaAPIKey')


@alru_cache
async def get_match_history(account_id: str, matches_requested: int = 25) -> match_history.GetMatchHistoryResponse:
    url = base_url + 'IDOTA2Match_570/GetMatchHistory/v1'
    async with httpx.AsyncClient() as client:
        resp = await client.get(url, params={'account_id': account_id, 'key': api_key, 'matches_requested': matches_requested})
        resp.raise_for_status()
        return match_history.GetMatchHistoryResponse(**resp.json())


@alru_cache
async def get_match_details(match_id: int) -> match_details.GetMatchDetailsResponse:
    url = base_url + 'IDOTA2Match_570/GetMatchDetails/v1'
    async with httpx.AsyncClient() as client:
        resp = await client.get(url, params={'match_id': match_id, 'key': api_key})
        resp.raise_for_status()
        return match_details.GetMatchDetailsResponse(**resp.json())


@alru_cache
async def get_heroes() -> heroes.GetHeroesResponse:
    url = base_url + 'IEconDOTA2_570/GetHeroes/v1'
    async with httpx.AsyncClient() as client:
        resp = await client.get(url, params={'key': api_key})
        resp.raise_for_status()
        return heroes.GetHeroesResponse(**resp.json())


@alru_cache
async def get_game_items() -> items.GetGameItemsResponse:
    url = base_url + 'IEconDOTA2_205790/GetGameItems/v1'
    async with httpx.AsyncClient() as client:
        resp = await client.get(url, params={'key': api_key})
        resp.raise_for_status()
        return items.GetGameItemsResponse(**resp.json())


@alru_cache
async def get_steam_id(vanity_url: str) -> steam_user.ResolveVanityUrlResponse:
    url = base_url + 'ISteamUser/ResolveVanityURL/v0001/'
    async with httpx.AsyncClient() as client:
        resp = await client.get(url, params={'key': api_key, 'vanityurl': vanity_url})
        resp.raise_for_status()
        return steam_user.ResolveVanityUrlResponse(**resp.json())
