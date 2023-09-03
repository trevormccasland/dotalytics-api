from typing import List, Optional

from dotalytics_api.types import match_details


class Player(match_details.Player):
    hero_name: str
    item_neutral_name: Optional[str]
    item_0_name: Optional[str]
    item_1_name: Optional[str]
    item_2_name: Optional[str]
    item_3_name: Optional[str]
    item_4_name: Optional[str]
    item_5_name: Optional[str]
    backpack_0_name: Optional[str]
    backpack_1_name: Optional[str]
    backpack_2_name: Optional[str]


class PicksBan(match_details.PicksBan):
    hero_name: str


class Match(match_details.MatchDetailsResult):
    players: List[Player]
    picks_bans: List[PicksBan]
