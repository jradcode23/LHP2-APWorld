from typing import Dict, NamedTuple

from BaseClasses import Location
from .Options import LHP2Options
from .Names import LocationName, RegionName


class LHP2Location(Location):
    game: str = "Lego Harry Potter 5-7"


class LocationData(NamedTuple):
    id: int = 0
    region: str = ""
    price: int = 0


base_location_id = 400000

# 0 - 199
character_loc_table: Dict[str, LocationData] = {}

# 200 - 399
character_token_loc_table: Dict[str, LocationData] = {}

# 400 - 408 Spells, 409 - 418 Unlockable abilities 419 - 424 Extra abilities
spell_loc_table: Dict[str, LocationData] = {}

# 425 - 443
joke_shop_loc_table: Dict[str, LocationData] = {}

# 450 - 473
level_beaten_loc_table: Dict[str, LocationData] = {
    LocationName.dt_beat: LocationData(base_location_id + 450, RegionName.dt),
    LocationName.da_beat: LocationData(base_location_id + 451, RegionName.da),
    LocationName.foc_beat: LocationData(base_location_id + 452, RegionName.foc),
    LocationName.kd_beat: LocationData(base_location_id + 453, RegionName.kd),
    LocationName.agv_beat: LocationData(base_location_id + 454, RegionName.agv),
    LocationName.avt_beat: LocationData(base_location_id + 455, RegionName.avt),
    LocationName.oor_beat: LocationData(base_location_id + 456, RegionName.oor),
    LocationName.jd_beat: LocationData(base_location_id + 457, RegionName.jd),
    LocationName.ansmc_beat: LocationData(base_location_id + 458, RegionName.ansmc),
    LocationName.lh_beat: LocationData(base_location_id + 459, RegionName.lh),
    LocationName.ff_beat: LocationData(base_location_id + 460, RegionName.ff),
    LocationName.thath_beat: LocationData(base_location_id + 461, RegionName.thath),
    LocationName.tsh_beat: LocationData(base_location_id + 462, RegionName.tsh),
    LocationName.mim_beat: LocationData(base_location_id + 463, RegionName.mim),
    LocationName.igd_beat: LocationData(base_location_id + 464, RegionName.igd),
    LocationName.sal_beat: LocationData(base_location_id + 465, RegionName.sal),
    LocationName.ll_beat: LocationData(base_location_id + 466, RegionName.ll),
    LocationName.dob_beat: LocationData(base_location_id + 467, RegionName.dob),
    LocationName.ttd_beat: LocationData(base_location_id + 468, RegionName.ttd),
    LocationName.bts_beat: LocationData(base_location_id + 469, RegionName.bts),
    LocationName.bb_beat: LocationData(base_location_id + 470, RegionName.bb),
    LocationName.fiend_beat: LocationData(base_location_id + 471, RegionName.fiend),
    LocationName.st_beat: LocationData(base_location_id + 472, RegionName.st),
    LocationName.tfitp_beat: LocationData(base_location_id + 473, RegionName.tfitp),
}

# 475 - 435 (to verify totals, I think there are actually 61)
sip_loc_table: Dict[str, LocationData] = {
    LocationName.dt_sip: LocationData(base_location_id + 475, RegionName.dt),
    LocationName.da_sip: LocationData(base_location_id + 476, RegionName.da),
    LocationName.foc_sip: LocationData(base_location_id + 477, RegionName.foc),
    LocationName.kd_sip: LocationData(base_location_id + 478, RegionName.kd),
    LocationName.agv_sip: LocationData(base_location_id + 479, RegionName.agv),
    LocationName.avt_sip: LocationData(base_location_id + 480, RegionName.avt),
    LocationName.oor_sip: LocationData(base_location_id + 481, RegionName.oor),
    LocationName.jd_sip: LocationData(base_location_id + 482, RegionName.jd),
    LocationName.ansmc_sip: LocationData(base_location_id + 483, RegionName.ansmc),
    LocationName.lh_sip: LocationData(base_location_id + 484, RegionName.lh),
    LocationName.ff_sip: LocationData(base_location_id + 485, RegionName.ff),
    LocationName.thath_sip: LocationData(base_location_id + 486, RegionName.thath),
    LocationName.tsh_sip: LocationData(base_location_id + 487, RegionName.tsh),
    LocationName.mim_sip: LocationData(base_location_id + 488, RegionName.mim),
    LocationName.igd_sip: LocationData(base_location_id + 489, RegionName.igd),
    LocationName.sal_sip: LocationData(base_location_id + 490, RegionName.sal),
    LocationName.ll_sip: LocationData(base_location_id + 491, RegionName.ll),
    LocationName.dob_sip: LocationData(base_location_id + 492, RegionName.dob),
    LocationName.ttd_sip: LocationData(base_location_id + 493, RegionName.ttd),
    LocationName.bts_sip: LocationData(base_location_id + 494, RegionName.bts),
    LocationName.bb_sip: LocationData(base_location_id + 495, RegionName.bb),
    LocationName.fiend_sip: LocationData(base_location_id + 496, RegionName.fiend),
    LocationName.st_sip: LocationData(base_location_id + 497, RegionName.st),
    LocationName.tfitp_sip: LocationData(base_location_id + 498, RegionName.tfitp),
}

all_location_table = {
    **level_beaten_loc_table,
    **sip_loc_table,
}


def setup_locations(options: LHP2Options):
    temp_location_table = {}
    temp_location_table.update(level_beaten_loc_table)
    temp_location_table.update(sip_loc_table)
    return temp_location_table
