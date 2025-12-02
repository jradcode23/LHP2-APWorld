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

# 0 - 212
character_loc_table: Dict[str, LocationData] = {}

# 215 - 425
character_token_loc_table: Dict[str, LocationData] = {}

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

# 475 - 535 (to verify totals, I think there are actually 61)
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

# 550 - 525
house_crest_loc_table: Dict[str, LocationData] = {
    # Gryff Crests
    LocationName.dt_gc: LocationData(base_location_id + 550, RegionName.dt),
    LocationName.da_gc: LocationData(base_location_id + 551, RegionName.da),
    LocationName.foc_gc: LocationData(base_location_id + 552, RegionName.foc),
    LocationName.kd_gc: LocationData(base_location_id + 553, RegionName.kd),
    LocationName.agv_gc: LocationData(base_location_id + 554, RegionName.agv),
    LocationName.avt_gc: LocationData(base_location_id + 555, RegionName.avt),
    LocationName.oor_gc: LocationData(base_location_id + 556, RegionName.oor),
    LocationName.jd_gc: LocationData(base_location_id + 557, RegionName.jd),
    LocationName.ansmc_gc: LocationData(base_location_id + 558, RegionName.ansmc),
    LocationName.lh_gc: LocationData(base_location_id + 559, RegionName.lh),
    LocationName.ff_gc: LocationData(base_location_id + 560, RegionName.ff),
    LocationName.thath_gc: LocationData(base_location_id + 561, RegionName.thath),
    LocationName.tsh_gc: LocationData(base_location_id + 562, RegionName.tsh),
    LocationName.mim_gc: LocationData(base_location_id + 563, RegionName.mim),
    LocationName.igd_gc: LocationData(base_location_id + 564, RegionName.igd),
    LocationName.sal_gc: LocationData(base_location_id + 565, RegionName.sal),
    LocationName.ll_gc: LocationData(base_location_id + 566, RegionName.ll),
    LocationName.dob_gc: LocationData(base_location_id + 567, RegionName.dob),
    LocationName.ttd_gc: LocationData(base_location_id + 568, RegionName.ttd),
    LocationName.bts_gc: LocationData(base_location_id + 569, RegionName.bts),
    LocationName.bb_gc: LocationData(base_location_id + 570, RegionName.bb),
    LocationName.fiend_gc: LocationData(base_location_id + 571, RegionName.fiend),
    LocationName.st_gc: LocationData(base_location_id + 572, RegionName.st),
    LocationName.tfitp_gc: LocationData(base_location_id + 573, RegionName.tfitp),
    # Slyth Crests
    LocationName.dt_sc: LocationData(base_location_id + 574, RegionName.dt),
    LocationName.da_sc: LocationData(base_location_id + 575, RegionName.da),
    LocationName.foc_sc: LocationData(base_location_id + 576, RegionName.foc),
    LocationName.kd_sc: LocationData(base_location_id + 577, RegionName.kd),
    LocationName.agv_sc: LocationData(base_location_id + 578, RegionName.agv),
    LocationName.avt_sc: LocationData(base_location_id + 579, RegionName.avt),
    LocationName.oor_sc: LocationData(base_location_id + 580, RegionName.oor),
    LocationName.jd_sc: LocationData(base_location_id + 581, RegionName.jd),
    LocationName.ansmc_sc: LocationData(base_location_id + 582, RegionName.ansmc),
    LocationName.lh_sc: LocationData(base_location_id + 583, RegionName.lh),
    LocationName.ff_sc: LocationData(base_location_id + 584, RegionName.ff),
    LocationName.thath_sc: LocationData(base_location_id + 585, RegionName.thath),
    LocationName.tsh_sc: LocationData(base_location_id + 586, RegionName.tsh),
    LocationName.mim_sc: LocationData(base_location_id + 587, RegionName.mim),
    LocationName.igd_sc: LocationData(base_location_id + 588, RegionName.igd),
    LocationName.sal_sc: LocationData(base_location_id + 589, RegionName.sal),
    LocationName.ll_sc: LocationData(base_location_id + 590, RegionName.ll),
    LocationName.dob_sc: LocationData(base_location_id + 591, RegionName.dob),
    LocationName.ttd_sc: LocationData(base_location_id + 592, RegionName.ttd),
    LocationName.bts_sc: LocationData(base_location_id + 593, RegionName.bts),
    LocationName.bb_sc: LocationData(base_location_id + 594, RegionName.bb),
    LocationName.fiend_sc: LocationData(base_location_id + 595, RegionName.fiend),
    LocationName.st_sc: LocationData(base_location_id + 596, RegionName.st),
    LocationName.tfitp_sc: LocationData(base_location_id + 597, RegionName.tfitp),
    # Raven Crests
    LocationName.dt_rc: LocationData(base_location_id + 598, RegionName.dt),
    LocationName.da_rc: LocationData(base_location_id + 599, RegionName.da),
    LocationName.foc_rc: LocationData(base_location_id + 600, RegionName.foc),
    LocationName.kd_rc: LocationData(base_location_id + 601, RegionName.kd),
    LocationName.agv_rc: LocationData(base_location_id + 602, RegionName.agv),
    LocationName.avt_rc: LocationData(base_location_id + 603, RegionName.avt),
    LocationName.oor_rc: LocationData(base_location_id + 604, RegionName.oor),
    LocationName.jd_rc: LocationData(base_location_id + 605, RegionName.jd),
    LocationName.ansmc_rc: LocationData(base_location_id + 606, RegionName.ansmc),
    LocationName.lh_rc: LocationData(base_location_id + 607, RegionName.lh),
    LocationName.ff_rc: LocationData(base_location_id + 608, RegionName.ff),
    LocationName.thath_rc: LocationData(base_location_id + 609, RegionName.thath),
    LocationName.tsh_rc: LocationData(base_location_id + 610, RegionName.tsh),
    LocationName.mim_rc: LocationData(base_location_id + 611, RegionName.mim),
    LocationName.igd_rc: LocationData(base_location_id + 612, RegionName.igd),
    LocationName.sal_rc: LocationData(base_location_id + 613, RegionName.sal),
    LocationName.ll_rc: LocationData(base_location_id + 614, RegionName.ll),
    LocationName.dob_rc: LocationData(base_location_id + 615, RegionName.dob),
    LocationName.ttd_rc: LocationData(base_location_id + 616, RegionName.ttd),
    LocationName.bts_rc: LocationData(base_location_id + 617, RegionName.bts),
    LocationName.bb_rc: LocationData(base_location_id + 618, RegionName.bb),
    LocationName.fiend_rc: LocationData(base_location_id + 619, RegionName.fiend),
    LocationName.st_rc: LocationData(base_location_id + 620, RegionName.st),
    LocationName.tfitp_rc: LocationData(base_location_id + 621, RegionName.tfitp),
    # Huffle Crests
    LocationName.dt_hc: LocationData(base_location_id + 622, RegionName.dt),
    LocationName.da_hc: LocationData(base_location_id + 623, RegionName.da),
    LocationName.foc_hc: LocationData(base_location_id + 624, RegionName.foc),
    LocationName.kd_hc: LocationData(base_location_id + 625, RegionName.kd),
    LocationName.agv_hc: LocationData(base_location_id + 626, RegionName.agv),
    LocationName.avt_hc: LocationData(base_location_id + 627, RegionName.avt),
    LocationName.oor_hc: LocationData(base_location_id + 628, RegionName.oor),
    LocationName.jd_hc: LocationData(base_location_id + 629, RegionName.jd),
    LocationName.ansmc_hc: LocationData(base_location_id + 630, RegionName.ansmc),
    LocationName.lh_hc: LocationData(base_location_id + 631, RegionName.lh),
    LocationName.ff_hc: LocationData(base_location_id + 632, RegionName.ff),
    LocationName.thath_hc: LocationData(base_location_id + 633, RegionName.thath),
    LocationName.tsh_hc: LocationData(base_location_id + 634, RegionName.tsh),
    LocationName.mim_hc: LocationData(base_location_id + 635, RegionName.mim),
    LocationName.igd_hc: LocationData(base_location_id + 636, RegionName.igd),
    LocationName.sal_hc: LocationData(base_location_id + 637, RegionName.sal),
    LocationName.ll_hc: LocationData(base_location_id + 638, RegionName.ll),
    LocationName.dob_hc: LocationData(base_location_id + 639, RegionName.dob),
    LocationName.ttd_hc: LocationData(base_location_id + 640, RegionName.ttd),
    LocationName.bts_hc: LocationData(base_location_id + 641, RegionName.bts),
    LocationName.bb_hc: LocationData(base_location_id + 642, RegionName.bb),
    LocationName.fiend_hc: LocationData(base_location_id + 643, RegionName.fiend),
    LocationName.st_hc: LocationData(base_location_id + 644, RegionName.st),
    LocationName.tfitp_hc: LocationData(base_location_id + 645, RegionName.tfitp),
}

# 650 - 673
# House Crest Completed

# 675 - 698
true_wizard_loc_table: Dict[str, LocationData] = {
    LocationName.dt_tw: LocationData(base_location_id + 675, RegionName.dt),
    LocationName.da_tw: LocationData(base_location_id + 676, RegionName.da),
    LocationName.foc_tw: LocationData(base_location_id + 677, RegionName.foc),
    LocationName.kd_tw: LocationData(base_location_id + 678, RegionName.kd),
    LocationName.agv_tw: LocationData(base_location_id + 679, RegionName.agv),
    LocationName.avt_tw: LocationData(base_location_id + 680, RegionName.avt),
    LocationName.oor_tw: LocationData(base_location_id + 681, RegionName.oor),
    LocationName.jd_tw: LocationData(base_location_id + 682, RegionName.jd),
    LocationName.ansmc_tw: LocationData(base_location_id + 683, RegionName.ansmc),
    LocationName.lh_tw: LocationData(base_location_id + 684, RegionName.lh),
    LocationName.ff_tw: LocationData(base_location_id + 685, RegionName.ff),
    LocationName.thath_tw: LocationData(base_location_id + 686, RegionName.thath),
    LocationName.tsh_tw: LocationData(base_location_id + 687, RegionName.tsh),
    LocationName.mim_tw: LocationData(base_location_id + 688, RegionName.mim),
    LocationName.igd_tw: LocationData(base_location_id + 689, RegionName.igd),
    LocationName.sal_tw: LocationData(base_location_id + 690, RegionName.sal),
    LocationName.ll_tw: LocationData(base_location_id + 691, RegionName.ll),
    LocationName.dob_tw: LocationData(base_location_id + 692, RegionName.dob),
    LocationName.ttd_tw: LocationData(base_location_id + 693, RegionName.ttd),
    LocationName.bts_tw: LocationData(base_location_id + 694, RegionName.bts),
    LocationName.bb_tw: LocationData(base_location_id + 695, RegionName.bb),
    LocationName.fiend_tw: LocationData(base_location_id + 696, RegionName.fiend),
    LocationName.st_tw: LocationData(base_location_id + 697, RegionName.st),
    LocationName.tfitp_tw: LocationData(base_location_id + 698, RegionName.tfitp),
}

all_location_table = {
    **level_beaten_loc_table,
    **sip_loc_table,
    **house_crest_loc_table,
    **true_wizard_loc_table,
}


def setup_locations(options: LHP2Options):
    temp_location_table = {}
    temp_location_table.update(level_beaten_loc_table)
    temp_location_table.update(sip_loc_table)
    temp_location_table.update(house_crest_loc_table)
    temp_location_table.update(true_wizard_loc_table)
    return temp_location_table
