from dataclasses import dataclass
from typing import List
from Options import DefaultOnToggle, Range, Choice, PerGameCommonOptions, OptionList, OptionDict
from .Names import ItemName


class EndGoal(Choice):
    """
    Determine the goal for the seed

    Defeat Voldemort: Collect the 7 Horcruxes and defeat Voldemort
    The Collector: Collect items from throughout the multiworld to win
    """
    display_name = "Goal"
    option_defeat_voldemort = 0
    option_the_collector = 1
    default = 0


class CollectibleQuantity(OptionDict):
    """
    The number of each collectible you need to beat the seed. Does nothing if the collector is your not win con.

    Valid Keys:
    - Gold Brick
    - Student in Peril
    - True Wizard
    - Character Token
    - House Crest Completed
    """
    display_name = "Collectibles Required"
    min = 0
    max_values_dict: dict[str, int] = {
        ItemName.gb: 201,
        ItemName.sip: 61,
        ItemName.tw: 24,
        ItemName.ct: 200,
        ItemName.hcgb: 24,
    }


@dataclass
class LHP2Options(PerGameCommonOptions):
    EndGoal: EndGoal
    CollectibleQuantity: CollectibleQuantity
