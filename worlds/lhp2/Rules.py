from BaseClasses import MultiWorld, Location
from worlds.generic.Rules import set_rule
from worlds.AutoWorld import CollectionState

from .Names import LocationName, ItemName, RegionName
from .Options import LHP2Options, EndGoal


def set_rules(world: MultiWorld, options: LHP2Options, player: int):
    set_entrance_rules(world, options, player)
    set_win_con(world, options, player)


def set_entrance_rules(world: MultiWorld, options: LHP2Options, player: int):
    set_rule(world.get_entrance(RegionName.leak + " -> " + RegionName.dt, player),
             lambda state: state.has(ItemName.dt_unlock, player))
    set_rule(world.get_entrance(RegionName.leak + " -> " + RegionName.da, player),
             lambda state: state.has(ItemName.da_unlock, player))
    set_rule(world.get_entrance(RegionName.leak + " -> " + RegionName.foc, player),
             lambda state: state.has(ItemName.foc_unlock, player))
    set_rule(world.get_entrance(RegionName.leak + " -> " + RegionName.kd, player),
             lambda state: state.has(ItemName.kd_unlock, player))
    set_rule(world.get_entrance(RegionName.leak + " -> " + RegionName.agv, player),
             lambda state: state.has(ItemName.agv_unlock, player))
    set_rule(world.get_entrance(RegionName.leak + " -> " + RegionName.avt, player),
             lambda state: state.has(ItemName.avt_unlock, player))
    set_rule(world.get_entrance(RegionName.leak + " -> " + RegionName.oor, player),
             lambda state: state.has(ItemName.oor_unlock, player))
    set_rule(world.get_entrance(RegionName.leak + " -> " + RegionName.jd, player),
             lambda state: state.has(ItemName.jd_unlock, player))
    set_rule(world.get_entrance(RegionName.leak + " -> " + RegionName.ansmc, player),
             lambda state: state.has(ItemName.ansmc_unlock, player))
    set_rule(world.get_entrance(RegionName.leak + " -> " + RegionName.lh, player),
             lambda state: state.has(ItemName.lh_unlock, player))
    set_rule(world.get_entrance(RegionName.leak + " -> " + RegionName.ff, player),
             lambda state: state.has(ItemName.ff_unlock, player))
    set_rule(world.get_entrance(RegionName.leak + " -> " + RegionName.thath, player),
             lambda state: state.has(ItemName.thath_unlock, player))
    set_rule(world.get_entrance(RegionName.leak + " -> " + RegionName.tsh, player),
             lambda state: state.has(ItemName.tsh_unlock, player))
    set_rule(world.get_entrance(RegionName.leak + " -> " + RegionName.mim, player),
             lambda state: state.has(ItemName.mim_unlock, player))
    set_rule(world.get_entrance(RegionName.leak + " -> " + RegionName.igd, player),
             lambda state: state.has(ItemName.igd_unlock, player))
    set_rule(world.get_entrance(RegionName.leak + " -> " + RegionName.sal, player),
             lambda state: state.has(ItemName.sal_unlock, player))
    set_rule(world.get_entrance(RegionName.leak + " -> " + RegionName.ll, player),
             lambda state: state.has(ItemName.ll_unlock, player))
    set_rule(world.get_entrance(RegionName.leak + " -> " + RegionName.dob, player),
             lambda state: state.has(ItemName.dob_unlock, player))
    set_rule(world.get_entrance(RegionName.leak + " -> " + RegionName.ttd, player),
             lambda state: state.has(ItemName.ttd_unlock, player))
    set_rule(world.get_entrance(RegionName.leak + " -> " + RegionName.bts, player),
             lambda state: state.has(ItemName.bts_unlock, player))
    set_rule(world.get_entrance(RegionName.leak + " -> " + RegionName.bb, player),
             lambda state: state.has(ItemName.bb_unlock, player))
    set_rule(world.get_entrance(RegionName.leak + " -> " + RegionName.fiend, player),
             lambda state: state.has(ItemName.fiend_unlock, player))
    set_rule(world.get_entrance(RegionName.leak + " -> " + RegionName.st, player),
             lambda state: state.has(ItemName.st_unlock, player))
    set_rule(world.get_entrance(RegionName.leak + " -> " + RegionName.tfitp, player),
             lambda state: state.has(ItemName.tfitp_unlock, player))


def set_win_con(world: MultiWorld, options: LHP2Options, player: int):
    if options.EndGoal == EndGoal.option_defeat_voldemort:
        world.completion_condition[player] = lambda state: state.can_reach_location(LocationName.tfitp_beat, player)
    # if options.EndGoal == EndGoal.option_the_collector:
    #     world.completion_condition[player] =
