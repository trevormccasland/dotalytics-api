import requests

from dotalytics_api import config
from dotalytics_api.types import match_history
from dotalytics_api.types import match_details
from dotalytics_api.types import heroes

base_url = 'https://api.steampowered.com/'
api_key = config.get('DotaAPIKey')


def get_match_history(account_id: str, matches_requested: int = 25) -> match_history.GetMatchHistoryResponse:
    url = base_url + 'IDOTA2Match_570/GetMatchHistory/v1'
    resp = requests.get(url, {'account_id': account_id, 'key': api_key, 'matches_requested': matches_requested})
    resp.raise_for_status()
    return match_history.GetMatchHistoryResponse(**resp.json())


def get_match_details(match_id: int) -> match_details.GetMatchDetailsResponse:
    url = base_url + 'IDOTA2Match_570/GetMatchDetails/v1'
    resp = requests.get(url, {'match_id': match_id, 'key': api_key})
    resp.raise_for_status()
    return match_details.GetMatchDetailsResponse(**resp.json())


def get_heroes() -> heroes.GetHeroesResponse:
    url = base_url + 'IEconDOTA2_570/GetHeroes/v1'
    resp = requests.get(url, {'key': api_key})
    resp.raise_for_status()
    return heroes.GetHeroesResponse(**resp.json())
