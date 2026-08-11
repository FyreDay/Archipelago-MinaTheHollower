from BaseClasses import LocationProgressType
from rule_builder.rules import Has, CanReachLocation
from .._generated.regions import Regions
from ... import LocationTypeEnum
from ...items import SingleKears, PermanentUpgrades
from ...rules.ability_rules import CanBurrow, CanBounce, CanClimb, CanCarry, HasFishingRod
from ...rules.movement_rules import CanJumpTiles
from ...rules.state_rules import HasKear

class Locations(LocationTypeEnum):
    CTP_FRIGID_STATION_MISSED_TRAIN_CHEST = (
        "CTP Frigid Station Missed Train Chest", 113, Regions.COLTRANE_PEAK_STATION_TRACKS,
    )

    CTP_FROZEN_PASS_ROPE_CHEST = (
        "CTP Frozen Pass Rope Chest", 112, Regions.COLTRANE_PEAK_FROZEN_PASS, CanClimb(),
    )

    CTP_DEAD_MAN_S_GORGE_TRINKET = (
        "CTP Dead Man's Gorge Trinket", 110, Regions.COLTRANE_PEAK_GORGE_ICE_GAUNTLET,
    )

    CTP_DEAD_MAN_S_GORGE_RAIL_KEAR = (
        "CTP Dead Man's Gorge Rail Kear", 111, Regions.COLTRANE_PEAK_TRAIN_TRACKS_SECRET, CanBurrow(),
    )

    CTP_MIRREN_FIGHT_REWARD = (
        "CTP Mirren Fight Reward", 114, Regions.COLTRANE_PEAK_FROSTBITE_WOODS,
    )

    CTP_RAIL_YARD_BESIDE_PIPE_CHEST = (
        "CTP Rail Yard Beside Pipe Chest", 118, Regions.COLTRANE_PEAK_RAIL_YARD,
    )

    CTP_RAIL_YARD_CLIFF_CHEST = (
        "CTP Rail Yard Cliff Chest", 117, Regions.COLTRANE_PEAK_RAIL_YARD,
    )

    CTP_RAIL_YARD_WEAPON_CHEST = (
        "CTP Rail Yard Weapon Chest", 119, Regions.COLTRANE_PEAK_RAIL_YARD_CHEST,
    )

    CTP_FISH_FISHCICLE_CORE = (
        "CTP Fish Fishcicle Core", 122, Regions.COLTRANE_PEAK_FROZEN_RIVER, CanBurrow() & HasFishingRod(),
    )

    CTP_RAIL_YARD_KEAR_ROOM_RUPERT_SHOP_TRINKET = (
        "CTP Rail Yard Kear Room Rupert Shop Trinket", 120, Regions.COLTRANE_PEAK_FROZEN_RIVER, CanBurrow(),
    )

    CTP_RAIL_YARD_KEAR_ROOM_RUPERT_SHOP_KEAR = (
        "CTP Rail Yard Kear Room Rupert Shop Kear", 121, Regions.COLTRANE_PEAK_FROZEN_RIVER, CanBurrow(),
    )

    CTP_SPIRAL_SUMMIT_KEAR = (
        "CTP Spiral Summit Kear", 116, Regions.COLTRANE_PEAK_SPIRAL_SUMMIT_SECRET, CanBurrow() & CanClimb(),
    )

    CTP_AGNES_EXPRESS_MIMIC_BONESTONE = (
        "CTP Agnes Express Mimic Bonestone", 123, Regions.COLTRANE_PEAK_AGNES_EXPRESS_REAR,
    )

    CTP_LOCOMOTRESS_FIGHT_REWARD = (
        "CTP Locomotress Fight Reward", 124, Regions.COLTRANE_PEAK_AGNES_EXPRESS_ARENA,
    )

    CTP_FROZEN_PASS_CHEST = (
        "CTP Frozen Pass Chest", 232, Regions.COLTRANE_PEAK_FROZEN_PASS,
    )

    WW_BALCONY_SNOWBALL_ESCORT_TRINKET = (
        "WW Balcony Snowball Escort Trinket", 242, Regions.WESTERN_WILDS_BALCONY, HasKear(kear=SingleKears.WESTERN_WILDS_BALCONY_KEAR.value)
        & CanBurrow()
        & CanCarry()
        & CanClimb()
        & Has(PermanentUpgrades.TRAIN_PASS.value)
        & Has(PermanentUpgrades.COLTRANE_PEAK_TICKET.value),
    )

class BossLocations(LocationTypeEnum):
    CTP_DEFEAT_THORNE_2 = ("CTP Defeat Thorne 2", 1009, Regions.COLTRANE_PEAK_THORNE_ARENA)
    CTP_DEFEAT_MIRREN = ("CTP Defeat Mirren", 1025, Regions.COLTRANE_PEAK_MIRREN_ROOM)
    CTP_DEFEAT_FROZEN_HORROR = ("CTP Defeat Frozen Horror", 1015, Regions.COLTRANE_PEAK_FROZEN_HORROR_ARENA)
    CTP_DEFEAT_LOCOMOTRESS_AGNESS = ("CTP Defeat Locomotress", 1005, Regions.COLTRANE_PEAK_AGNES_EXPRESS_ARENA)
    # CTP_FROZEN_GENERATOR = ("CTP Frozen Generator Repaired", 6004, Regions.COLTRANE_PEAK_FROZEN_GENERATOR)

