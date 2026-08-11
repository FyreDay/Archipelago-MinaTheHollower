from BaseClasses import LocationProgressType
from rule_builder.rules import Has, CanReachLocation
from .._generated.regions import Regions
from ... import LocationTypeEnum
from ...items import Trinkets, SingleKears
from ...rules.ability_rules import CanBurrow, CanBounce, CanClimb, CanCarry, \
    HasReachingSideArm, HasFishingRod, HasTrinket
from ...rules.state_rules import HasKear, ShopPrice
from ...rules.movement_rules import CanJumpTiles

class Locations(LocationTypeEnum):
    KW_CAMPFIRE_CHEST = (
        "KW Campfire Chest", 340, Regions.KINDLEWOOD_OVERGROWTH_BONFIRE_MAIN,
    )

    KW_RESIDENCE_BASEMENT_CHEST = (
        "KW Residence Basement Chest", 341, Regions.KINDLEWOOD_OVERGROWTH_RESIDENCE_BASEMENT,
    )

    KW_MADD_HOUSE_DRAINING_BEASTIUM = (
        "KW Madd House Draining Beastium", 348, Regions.KINDLEWOOD_OVERGROWTH_MADD_HOUSE,
    )

    KW_MADD_HOUSE_OOZING_ORGAN = (
        "KW Madd House Oozing Organ", 347, Regions.KINDLEWOOD_OVERGROWTH_MADD_HOUSE,
    )

    KW_MADD_HOUSE_VOLTAIC_GUARD = (
        "KW Madd House Voltaic Guard", 349, Regions.KINDLEWOOD_OVERGROWTH_MADD_HOUSE,
    )

    KW_MADD_HOUSE_KEAR = (
        "KW Madd House Kear", 350, Regions.KINDLEWOOD_OVERGROWTH_MADD_HOUSE,
    )

    KW_TORCH_ESCORT_BONESTONE = (
        "KW Torch Escort Bonestone", 339, Regions.KINDLEWOOD_BEHIND_MADD_HOUSE, CanBurrow() & CanCarry(),
    )

    KW_GOURDAN_OOZING_ORGAN_REWARD = (
        "KW Gourdan Oozing Organ Reward", 335, Regions.KINDLEWOOD_FARM_CROSSING_PUMPKIN_PATCH, HasTrinket(trinket=Trinkets.OOZING_ORGAN.value),
    )

    KW_FISH_GAZEWORM_EYE = (
        "KW Fish Gazeworm Eye", 104, Regions.KINDLEWOOD_FARM_CROSSING_PUMPKIN_PATCH, HasFishingRod(),
    )

    KW_TRAIN_STATION_LEDGE_CHEST = (
        "KW Train Station Ledge Chest", 346, Regions.KINDLEWOOD_FARM_CROSSING_PUMPKIN_PATCH, CanBurrow(),
    )

    KW_SHACK_CHEST = (
        "KW Shack Chest", 342, Regions.KINDLEWOOD_FARM_CROSSING_SHACK, HasReachingSideArm() & CanBurrow(),
    )

    KW_WALLOWER_S_ROOM_TRINKET = (
        "KW Wallower's Room Trinket", 344, Regions.KINDLEWOOD_WALLOWERS_PATH, HasKear(kear=SingleKears.KINDLEWOOD_WALLOWERS_PATH_TRINKET_KEAR.value),
    )  # needs kear, burrow,

    KW_WALLOWER_S_ROOM_CHEST = (
        "KW Wallower's Room Chest", 345, Regions.KINDLEWOOD_WALLOWERS_PATH, (
            CanBurrow()
            & HasTrinket(trinket=Trinkets.WALLOWERS_GAUNTLETS.value)
        )
        | (
            CanJumpTiles(distance=7)
            & HasTrinket(trinket=Trinkets.BRIDGE_WEAVER.value)
        ),
    )

    KW_RAIL_TUNNEL_VIAL_POUCH = (
        "KW Rail Tunnel Vial Pouch", 343, Regions.KINDLEWOOD_RAIL_TUNNEL, CanBurrow()
        & CanCarry()
        & HasKear(kear=SingleKears.KINDLEWOOD_TRAIN_TUNNEL_KEAR.value),
    )
class BossLocations(LocationTypeEnum):
    KW_DEFEAT_MADD_HOUSE = ("KW Defeat Madd House", 1012, Regions.KINDLEWOOD_OVERGROWTH_MADD_HOUSE)

