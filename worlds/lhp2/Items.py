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
    # TODO: not sure why gen fails if everything but level unlocks is filler


base_item_id = 400000

# 0 - 199
character_item_table: Dict[str, LHP2ItemData] = {}

# 200 - 399
character_token_item_table: Dict[str, LHP2ItemData] = {}

# 400 - 408 Spells, 409 - 418 Unlockable abilities 419 - 424 Extra abilities
spell_item_table: Dict[str, LHP2ItemData] = {}

# 425 - 443
joke_shop_item_table: Dict[str, LHP2ItemData] = {}

# 450 - 473
level_unlock_item_table: Dict[str, LHP2ItemData] = {
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

# 475 - 535 (to verify totals since there are extras)
sip_item_table: Dict[str, LHP2ItemData] = {
    ItemName.dt_sip: LHP2ItemData(base_item_id + 475),
    ItemName.da_sip: LHP2ItemData(base_item_id + 476),
    ItemName.foc_sip: LHP2ItemData(base_item_id + 477),
    ItemName.kd_sip: LHP2ItemData(base_item_id + 478),
    ItemName.agv_sip: LHP2ItemData(base_item_id + 479),
    ItemName.avt_sip: LHP2ItemData(base_item_id + 480),
    ItemName.oor_sip: LHP2ItemData(base_item_id + 481),
    ItemName.jd_sip: LHP2ItemData(base_item_id + 482),
    ItemName.ansmc_sip: LHP2ItemData(base_item_id + 483),
    ItemName.lh_sip: LHP2ItemData(base_item_id + 484),
    ItemName.ff_sip: LHP2ItemData(base_item_id + 485),
    ItemName.thath_sip: LHP2ItemData(base_item_id + 486),
    ItemName.tsh_sip: LHP2ItemData(base_item_id + 487),
    ItemName.mim_sip: LHP2ItemData(base_item_id + 488),
    ItemName.igd_sip: LHP2ItemData(base_item_id + 489),
    ItemName.sal_sip: LHP2ItemData(base_item_id + 490),
    ItemName.ll_sip: LHP2ItemData(base_item_id + 491),
    ItemName.dob_sip: LHP2ItemData(base_item_id + 492),
    ItemName.ttd_sip: LHP2ItemData(base_item_id + 493),
    ItemName.bts_sip: LHP2ItemData(base_item_id + 494),
    ItemName.bb_sip: LHP2ItemData(base_item_id + 495),
    ItemName.fiend_sip: LHP2ItemData(base_item_id + 496),
    ItemName.st_sip: LHP2ItemData(base_item_id + 497),
    ItemName.tfitp_sip: LHP2ItemData(base_item_id + 498),
}

# 550 - 525
house_crest_item_table: Dict[str, LHP2ItemData] = {
    # Gryff Crests
    ItemName.dt_gc: LHP2ItemData(base_item_id + 550),
    ItemName.da_gc: LHP2ItemData(base_item_id + 551),
    ItemName.foc_gc: LHP2ItemData(base_item_id + 552),
    ItemName.kd_gc: LHP2ItemData(base_item_id + 553),
    ItemName.agv_gc: LHP2ItemData(base_item_id + 554),
    ItemName.avt_gc: LHP2ItemData(base_item_id + 555),
    ItemName.oor_gc: LHP2ItemData(base_item_id + 556),
    ItemName.jd_gc: LHP2ItemData(base_item_id + 557),
    ItemName.ansmc_gc: LHP2ItemData(base_item_id + 558),
    ItemName.lh_gc: LHP2ItemData(base_item_id + 559),
    ItemName.ff_gc: LHP2ItemData(base_item_id + 560),
    ItemName.thath_gc: LHP2ItemData(base_item_id + 561),
    ItemName.tsh_gc: LHP2ItemData(base_item_id + 562),
    ItemName.mim_gc: LHP2ItemData(base_item_id + 563),
    ItemName.igd_gc: LHP2ItemData(base_item_id + 564),
    ItemName.sal_gc: LHP2ItemData(base_item_id + 565),
    ItemName.ll_gc: LHP2ItemData(base_item_id + 566),
    ItemName.dob_gc: LHP2ItemData(base_item_id + 567),
    ItemName.ttd_gc: LHP2ItemData(base_item_id + 568),
    ItemName.bts_gc: LHP2ItemData(base_item_id + 569),
    ItemName.bb_gc: LHP2ItemData(base_item_id + 570),
    ItemName.fiend_gc: LHP2ItemData(base_item_id + 571),
    ItemName.st_gc: LHP2ItemData(base_item_id + 572),
    ItemName.tfitp_gc: LHP2ItemData(base_item_id + 573),
    # Slyth Crests
    ItemName.dt_sc: LHP2ItemData(base_item_id + 574),
    ItemName.da_sc: LHP2ItemData(base_item_id + 575),
    ItemName.foc_sc: LHP2ItemData(base_item_id + 576),
    ItemName.kd_sc: LHP2ItemData(base_item_id + 577),
    ItemName.agv_sc: LHP2ItemData(base_item_id + 578),
    ItemName.avt_sc: LHP2ItemData(base_item_id + 579),
    ItemName.oor_sc: LHP2ItemData(base_item_id + 580),
    ItemName.jd_sc: LHP2ItemData(base_item_id + 581),
    ItemName.ansmc_sc: LHP2ItemData(base_item_id + 582),
    ItemName.lh_sc: LHP2ItemData(base_item_id + 583),
    ItemName.ff_sc: LHP2ItemData(base_item_id + 584),
    ItemName.thath_sc: LHP2ItemData(base_item_id + 585),
    ItemName.tsh_sc: LHP2ItemData(base_item_id + 586),
    ItemName.mim_sc: LHP2ItemData(base_item_id + 587),
    ItemName.igd_sc: LHP2ItemData(base_item_id + 588),
    ItemName.sal_sc: LHP2ItemData(base_item_id + 589),
    ItemName.ll_sc: LHP2ItemData(base_item_id + 590),
    ItemName.dob_sc: LHP2ItemData(base_item_id + 591),
    ItemName.ttd_sc: LHP2ItemData(base_item_id + 592),
    ItemName.bts_sc: LHP2ItemData(base_item_id + 593),
    ItemName.bb_sc: LHP2ItemData(base_item_id + 594),
    ItemName.fiend_sc: LHP2ItemData(base_item_id + 595),
    ItemName.st_sc: LHP2ItemData(base_item_id + 596),
    ItemName.tfitp_sc: LHP2ItemData(base_item_id + 597),
    # Raven Crests
    ItemName.dt_rc: LHP2ItemData(base_item_id + 598),
    ItemName.da_rc: LHP2ItemData(base_item_id + 599),
    ItemName.foc_rc: LHP2ItemData(base_item_id + 600),
    ItemName.kd_rc: LHP2ItemData(base_item_id + 601),
    ItemName.agv_rc: LHP2ItemData(base_item_id + 602),
    ItemName.avt_rc: LHP2ItemData(base_item_id + 603),
    ItemName.oor_rc: LHP2ItemData(base_item_id + 604),
    ItemName.jd_rc: LHP2ItemData(base_item_id + 605),
    ItemName.ansmc_rc: LHP2ItemData(base_item_id + 606),
    ItemName.lh_rc: LHP2ItemData(base_item_id + 607),
    ItemName.ff_rc: LHP2ItemData(base_item_id + 608),
    ItemName.thath_rc: LHP2ItemData(base_item_id + 609),
    ItemName.tsh_rc: LHP2ItemData(base_item_id + 610),
    ItemName.mim_rc: LHP2ItemData(base_item_id + 611),
    ItemName.igd_rc: LHP2ItemData(base_item_id + 612),
    ItemName.sal_rc: LHP2ItemData(base_item_id + 613),
    ItemName.ll_rc: LHP2ItemData(base_item_id + 614),
    ItemName.dob_rc: LHP2ItemData(base_item_id + 615),
    ItemName.ttd_rc: LHP2ItemData(base_item_id + 616),
    ItemName.bts_rc: LHP2ItemData(base_item_id + 617),
    ItemName.bb_rc: LHP2ItemData(base_item_id + 618),
    ItemName.fiend_rc: LHP2ItemData(base_item_id + 619),
    ItemName.st_rc: LHP2ItemData(base_item_id + 620),
    ItemName.tfitp_rc: LHP2ItemData(base_item_id + 621),
    # Huffle Crests
    ItemName.dt_hc: LHP2ItemData(base_item_id + 622),
    ItemName.da_hc: LHP2ItemData(base_item_id + 623),
    ItemName.foc_hc: LHP2ItemData(base_item_id + 624),
    ItemName.kd_hc: LHP2ItemData(base_item_id + 625),
    ItemName.agv_hc: LHP2ItemData(base_item_id + 626),
    ItemName.avt_hc: LHP2ItemData(base_item_id + 627),
    ItemName.oor_hc: LHP2ItemData(base_item_id + 628),
    ItemName.jd_hc: LHP2ItemData(base_item_id + 629),
    ItemName.ansmc_hc: LHP2ItemData(base_item_id + 630),
    ItemName.lh_hc: LHP2ItemData(base_item_id + 631),
    ItemName.ff_hc: LHP2ItemData(base_item_id + 632),
    ItemName.thath_hc: LHP2ItemData(base_item_id + 633),
    ItemName.tsh_hc: LHP2ItemData(base_item_id + 634),
    ItemName.mim_hc: LHP2ItemData(base_item_id + 635),
    ItemName.igd_hc: LHP2ItemData(base_item_id + 636),
    ItemName.sal_hc: LHP2ItemData(base_item_id + 637),
    ItemName.ll_hc: LHP2ItemData(base_item_id + 638),
    ItemName.dob_hc: LHP2ItemData(base_item_id + 639),
    ItemName.ttd_hc: LHP2ItemData(base_item_id + 640),
    ItemName.bts_hc: LHP2ItemData(base_item_id + 641),
    ItemName.bb_hc: LHP2ItemData(base_item_id + 642),
    ItemName.fiend_hc: LHP2ItemData(base_item_id + 643),
    ItemName.st_hc: LHP2ItemData(base_item_id + 644),
    ItemName.tfitp_hc: LHP2ItemData(base_item_id + 645),
}

# 650 - 673
# House Crest Completed

# 675 - 698
true_wizard_item_table: Dict[str, LHP2ItemData] = {
    ItemName.dt_tw: LHP2ItemData(base_item_id + 675),
    ItemName.da_tw: LHP2ItemData(base_item_id + 676),
    ItemName.foc_tw: LHP2ItemData(base_item_id + 677),
    ItemName.kd_tw: LHP2ItemData(base_item_id + 678),
    ItemName.agv_tw: LHP2ItemData(base_item_id + 679),
    ItemName.avt_tw: LHP2ItemData(base_item_id + 680),
    ItemName.oor_tw: LHP2ItemData(base_item_id + 681),
    ItemName.jd_tw: LHP2ItemData(base_item_id + 682),
    ItemName.ansmc_tw: LHP2ItemData(base_item_id + 683),
    ItemName.lh_tw: LHP2ItemData(base_item_id + 684),
    ItemName.ff_tw: LHP2ItemData(base_item_id + 685),
    ItemName.thath_tw: LHP2ItemData(base_item_id + 686),
    ItemName.tsh_tw: LHP2ItemData(base_item_id + 687),
    ItemName.mim_tw: LHP2ItemData(base_item_id + 688),
    ItemName.igd_tw: LHP2ItemData(base_item_id + 689),
    ItemName.sal_tw: LHP2ItemData(base_item_id + 690),
    ItemName.ll_tw: LHP2ItemData(base_item_id + 691),
    ItemName.dob_tw: LHP2ItemData(base_item_id + 692),
    ItemName.ttd_tw: LHP2ItemData(base_item_id + 693),
    ItemName.bts_tw: LHP2ItemData(base_item_id + 694),
    ItemName.bb_tw: LHP2ItemData(base_item_id + 695),
    ItemName.fiend_tw: LHP2ItemData(base_item_id + 696),
    ItemName.st_tw: LHP2ItemData(base_item_id + 697),
    ItemName.tfitp_tw: LHP2ItemData(base_item_id + 698),
}

item_data_table = {
    **level_unlock_item_table,
    **sip_item_table,
    **house_crest_item_table,
    **true_wizard_item_table,
}


def setup_items(options: LHP2Options):
    temp_item_table = {}
    temp_item_table.update(level_unlock_item_table)
    temp_item_table.update(sip_item_table)
    temp_item_table.update(house_crest_item_table)
    temp_item_table.update(true_wizard_item_table)
    return temp_item_table
