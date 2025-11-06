from typing import NamedTuple, Optional, Dict

from BaseClasses import Item, ItemClassification
from .Names import ItemName
from .Options import LHP2Options


# from .Options import LHP2Options


class LHP2Item(Item):
    game: str = "Lego Harry Potter 5-7"


class LHP2ItemData(NamedTuple):
    code: Optional[int] = None
    qty: int = 0
    classification: ItemClassification = ItemClassification.progression_deprioritized_skip_balancing
   

base_item_id = 400000

# 0 - 199
character_item_table: Dict[str, LHP2ItemData] = {}

# 200 - 399
character_token_loc_table: Dict[str, LHP2ItemData] = {}

# 400 - 408 Spells, 409 - 418 Unlockable abilities 419 - 424 Extra abilities
spell_loc_table: Dict[str, LHP2ItemData] = {}

# 425 - 443
joke_shop_loc_table: Dict[str, LHP2ItemData] = {}

# 450 - 473
level_unlock_loc_table: Dict[str, LHP2ItemData] = {
    ItemName.dt_unlock: LHP2ItemData(base_item_id + 450, ItemClassification.progression),
    ItemName.da_unlock: LHP2ItemData(base_item_id + 451, ItemClassification.progression),
    ItemName.foc_unlock: LHP2ItemData(base_item_id + 452, ItemClassification.progression),
    ItemName.kd_unlock: LHP2ItemData(base_item_id + 453, ItemClassification.progression),
    ItemName.agv_unlock: LHP2ItemData(base_item_id + 454, ItemClassification.progression),
    ItemName.avt_unlock: LHP2ItemData(base_item_id + 455, ItemClassification.progression),
    ItemName.oor_unlock: LHP2ItemData(base_item_id + 456, ItemClassification.progression),
    ItemName.jd_unlock: LHP2ItemData(base_item_id + 457, ItemClassification.progression),
    ItemName.ansmc_unlock: LHP2ItemData(base_item_id + 458, ItemClassification.progression),
    ItemName.lh_unlock: LHP2ItemData(base_item_id + 459, ItemClassification.progression),
    ItemName.ff_unlock: LHP2ItemData(base_item_id + 460, ItemClassification.progression),
    ItemName.thath_unlock: LHP2ItemData(base_item_id + 461, ItemClassification.progression),
    ItemName.tsh_unlock: LHP2ItemData(base_item_id + 462, ItemClassification.progression),
    ItemName.mim_unlock: LHP2ItemData(base_item_id + 463, ItemClassification.progression),
    ItemName.igd_unlock: LHP2ItemData(base_item_id + 464, ItemClassification.progression),
    ItemName.sal_unlock: LHP2ItemData(base_item_id + 465, ItemClassification.progression),
    ItemName.ll_unlock: LHP2ItemData(base_item_id + 466, ItemClassification.progression),
    ItemName.dob_unlock: LHP2ItemData(base_item_id + 467, ItemClassification.progression),
    ItemName.ttd_unlock: LHP2ItemData(base_item_id + 468, ItemClassification.progression),
    ItemName.bts_unlock: LHP2ItemData(base_item_id + 469, ItemClassification.progression),
    ItemName.bb_unlock: LHP2ItemData(base_item_id + 470, ItemClassification.progression),
    ItemName.fiend_unlock: LHP2ItemData(base_item_id + 471, ItemClassification.progression),
    ItemName.st_unlock: LHP2ItemData(base_item_id + 472, ItemClassification.progression),
    ItemName.tfitp_unlock: LHP2ItemData(base_item_id + 473, ItemClassification.progression),
}

# 475 - 435 (to verify totals since there are extras)
sip_item_table: Dict[str, LHP2ItemData] = {
    ItemName.sip: LHP2ItemData(base_item_id + 475, 24)
}


item_data_table = {
    **level_unlock_loc_table,
    **sip_item_table,
}


def setup_items(options: LHP2Options):
    temp_item_table = {}
    temp_item_table.update(level_unlock_loc_table)
    return temp_item_table
