from pydantic import BaseModel

from typing import List, Optional


class PicksBan(BaseModel):
    hero_id: int
    is_pick: bool
    order: int
    team: int


class AbilityUpgrade(BaseModel):
    ability: int
    level: int
    time: int


class Player(BaseModel):
    ability_upgrades: List[AbilityUpgrade]
    account_id: int
    aghanims_scepter: int
    aghanims_shard: int
    assists: int
    backpack_0: int
    backpack_1: int
    backpack_2: int
    deaths: int
    denies: int
    gold: int
    gold_per_min: int
    gold_spent: int
    hero_damage: int
    hero_healing: int
    hero_id: int
    item_0: int
    item_1: int
    item_2: int
    item_3: int
    item_4: int
    item_5: int
    item_neutral: int
    kills: int
    last_hits: int
    leaver_status: int
    level: int
    moonshard: int
    net_worth: int
    player_slot: int
    scaled_hero_damage: int
    scaled_hero_healing: int
    scaled_tower_damage: int
    team_number: int
    team_slot: int
    tower_damage: int
    xp_per_min: int


class MatchDetailsResult(BaseModel):
    barracks_status_dire: int
    barracks_status_radiant: int
    cluster: int
    dire_score: int
    duration: int
    engine: int
    first_blood_time: int
    flags: int
    game_mode: int
    human_players: int
    leagueid: int
    lobby_type: int
    match_id: int
    match_seq_num: int
    picks_bans: List[PicksBan]
    players: List[Player]
    pre_game_duration: int
    radiant_score: int
    radiant_win: bool
    start_time: int
    tower_status_dire: int
    tower_status_radiant: int


class GetMatchDetailsResponse(BaseModel):
    result: MatchDetailsResult
