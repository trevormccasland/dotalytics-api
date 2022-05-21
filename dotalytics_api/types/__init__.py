from pydantic import BaseModel


class Player(BaseModel):
    account_id: str
    player_slot: int
    hero_id: int


class Match(BaseModel):
    match_id: int
    match_seq_num: int
    start_time: int
    lobby_type: int
    radiant_team_id: int
    dire_team_id: int
    players: list[Player]


class MatchesResponse(BaseModel):
    status: int
    num_results: int
    total_results: int
    results_remaining: int
    matches: list[Match]


class GetMatchHistoryResponse(BaseModel):
    result: MatchesResponse

