from BaseClasses import LocationProgressType
from rule_builder.options import OptionFilter
from rule_builder.rules import Has, True_
from .._generated.regions import Regions
from ... import LocationTypeEnum
from ...items import SingleKears
from ...rules.ability_rules import CanBurrow, CanBounce, CanSwim, CanCarry, CanClimb, \
    HasFishingRod, PowerLevelThreshold
from ...rules.state_rules import HasKear
from ...rules.movement_rules import CanJumpTiles

class Locations(LocationTypeEnum):
    NB_FISH_SHRIMPTER_TAIL = ("NB Fish Shrimpter Tail", 50, Regions.NOXS_BAYOU_BOAT_STATION, HasFishingRod())

    NB_GUARD_ROOM_TRINKET = (
        "NB Guard Room Trinket", 47, Regions.NOXS_BAYOU_WATERFALL_TRINKET,
    )

    NB_FIRST_FLOODER_CHEST = (
        "NB First Flooder Chest", 39, Regions.NOXS_BAYOU_LILY_FULL_PUMP_ROOM,
    )

    NB_WATER_BUGS_CHEST = (
        "NB Water Bugs Chest", 38, Regions.NOXS_BAYOU_SHALLOW_POOL,
    )

    NB_LAGOON_UNFLOODED_DARK_ROOM_CHEST = (
        "NB Lagoon Unflooded Dark Room Chest", 42, Regions.NOXS_BAYOU_BIG_LAGOON_DARK,
    )

    NB_LAGOON_FLOODED_SIDE_ROOM_TRINKET = (
        "NB Lagoon Flooded Side Room Trinket", 40, Regions.NOXS_BAYOU_BIG_LAGOON_EAST_SIDE_ROOM,
    )

    NB_SWAMP_SHACK_PIT_PRESERVER = (
        "NB Swamp Shack Shop Trinket", 48, Regions.NOXS_BAYOU_SWAMP_SHACK,
    )

    NB_SWAMP_SHACK_KEAR = (
        "NB Swamp Shack Shop Kear", 49, Regions.NOXS_BAYOU_SWAMP_SHACK,
    )

    NB_SWAMP_SHACK_WEAPON_CHEST = (
        "NB Swamp Shack Weapon Chest", 45, Regions.NOXS_BAYOU_SWAMP_SHACK, HasKear(kear=SingleKears.NOXS_BAYOU_SWAMP_SHACK_KEAR.value),
    )

    NB_MOONLIT_PATH_CHEST = (
        "NB Moonlit Path Chest", 43, Regions.NOXS_BAYOU_MOONLIT_PATH,
    )

    NB_MOONLIT_HIDEAWAY_TRINKET = (
        "NB Moonlit Hideaway Trinket", 37, Regions.NOXS_BAYOU_MOONLIT_MIRROR,
    )

    NB_PLANT_POND_CAVE_CHEST = (
        "NB Plant Pond Cave Chest", 35, Regions.NOXS_BAYOU_THICK_PLANT_POND_CAVE,
    )

    NB_THICK_THICKET_CHEST = (
        "NB Thick Thicket Chest", 36, Regions.NOXS_BAYOU_TWIN_THICKET,
    )

    NB_THICKET_HIDDEN_CAVE_CHEST = (
        "NB Thicket Hidden Cave Chest", 44, Regions.NOXS_BAYOU_CANOPY_BRIDGE_CAVE,
    )

    NB_GRATE_LAKE_CHEST = (
        "NB Grate Lake Chest", 41, Regions.NOXS_BAYOU_TAINTED_LAIR_GRATE_BRIDGE,
    )

    NB_NOX_S_BEAST_FIGHT_REWARD = (
        "NB Nox's Beast Fight Reward", 34, Regions.NOXS_BAYOU_TAINTED_LAIR_ARENA, CanSwim(),
    )

    NB_GUTTER_TUNNEL_CHEST = ("NB Gutter Tunnel Chest", 46, Regions.NOXS_BAYOU_TAINTED_TUNNEL, CanBurrow(),)


class BossLocations(LocationTypeEnum):
    NB_DEFEAT_MOCK_MOON = ("NB Defeat Mock Moon", 1017, Regions.NOXS_BAYOU_MOONLIT_ARENA, PowerLevelThreshold(power=25))
    NB_DEFEAT_NOXS_BEAST = ("NB Defeat Nox's Beast", 1002, Regions.NOXS_BAYOU_TAINTED_LAIR_ARENA, PowerLevelThreshold(power=25))
    # NB_SWAMPY_GENERATOR = ("NB Swampy Generator Repaired", 6000, Regions.ASTRAL_ORRERY_STARRY_GENERATOR)

