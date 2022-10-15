from pydantic import BaseModel

from typing import List, Optional


class AbilityUpgrade(BaseModel):
    ability: int
    time: int
    level: int


class AdditionalUnit(BaseModel):
    unitname: str
    item_0: int
    item_1: int
    item_2: int
    item_3: int
    item_4: int
    item_5: int
    backpack_0: int
    backpack_1: int
    backpack_2: int
    item_neutral: int


class PlayerResult(BaseModel):
    account_id: int
    player_slot: int
    team_number: int
    team_slot: int
    hero_id: int
    item_0: int
    item_1: int
    item_2: int
    item_3: int
    item_4: int
    item_5: int
    backpack_0: int
    backpack_1: int
    backpack_2: int
    item_neutral: int
    kills: int
    deaths: int
    assists: int
    leaver_status: int
    last_hits: int
    denies: int
    gold_per_min: int
    xp_per_min: int
    level: int
    net_worth: int
    aghanims_scepter: int
    aghanims_shard: int
    moonshard: int
    hero_damage: Optional[int]
    tower_damage: Optional[int]
    hero_healing: Optional[int]
    gold: Optional[int]
    gold_spent: Optional[int]
    scaled_hero_damage: Optional[int]
    scaled_tower_damage: Optional[int]
    scaled_hero_healing: Optional[int]
    ability_upgrades: Optional[List[AbilityUpgrade]]
    additional_units: Optional[List[AdditionalUnit]] = None


class PicksBan(BaseModel):
    is_pick: bool
    hero_id: int
    team: int
    order: int


class BaseMatchDetailsResult(BaseModel):
    radiant_win: bool
    duration: int
    pre_game_duration: int
    start_time: int
    match_id: int
    match_seq_num: int
    tower_status_radiant: int
    tower_status_dire: int
    barracks_status_radiant: int
    barracks_status_dire: int
    cluster: int
    first_blood_time: int
    lobby_type: int
    human_players: int
    leagueid: int
    positive_votes: int
    negative_votes: int
    game_mode: int
    flags: int
    engine: int
    radiant_score: int
    dire_score: int


class MatchDetailsResult(BaseMatchDetailsResult):
    players: List[PlayerResult]
    picks_bans: List[PicksBan]


class GetMatchDetailsResponse(BaseModel):
    result: MatchDetailsResult
