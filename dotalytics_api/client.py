import requests

from dotalytics_api import config
from dotalytics_api.types import matches

base_url = 'https://api.steampowered.com/'
api_key = config.get('DotaAPIKey')


def get_match_history(account_id: str) -> matches.GetMatchHistoryResponse:
    url = base_url + 'IDOTA2Match_570/GetMatchHistory/V001'
    resp = requests.get(url, {'account_id': account_id, 'key': api_key})
    resp.raise_for_status()
    return resp.json()
