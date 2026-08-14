from BaseClasses import LocationProgressType
from rule_builder.options import OptionFilter
from rule_builder.rules import Has, True_, CanReachLocation
from .._generated.regions import Regions
from ... import TransitionType, DirectionType, LocationTypeEnum
from ...items import Trinkets, SingleKears, PermanentUpgrades, Wallets, PlayerUpgrades, Sidearms
from ...rules.ability_rules import CanBurrow, CanBounce, HasReachingSideArm, CanClimb, \
    CanSwim, HasFishingRod, PowerLevelThreshold
from ...rules.state_rules import HasKear, RepairedGeneratorCount
from ...rules.movement_rules import CanJumpTiles

class Locations(LocationTypeEnum):
    EH_MAXI_FIGHT_REWARD = (
        "EH Maxi Fight Reward", 221, Regions.EASTERN_HEATH_GRASSLAND, RepairedGeneratorCount(count=1),
    )

    EH_FISH_DORK_EYES = (
        "EH Fish Dork Eyes", 241, Regions.EASTERN_HEATH_GRASSLAND_BRIDGE_LEFT, HasFishingRod(),
    )  # needs fishing rod,

    EH_OSSEX_ENTRY_CHEST = (
        "EH Ossex Entry Chest", 231, Regions.EASTERN_HEATH_I_SCREEN, CanBurrow(),
    )

    EH_BUSH_ROOM_LOCKED_BONESTONE = (
        "EH Bush Room Locked Bonestone", 236, Regions.EASTERN_HEATH_BUSH_ROOM, HasKear(kear=SingleKears.EASTERN_HEATH_GRASSLAND_BUSHROOM_KEAR.value),
    )  # needs kear,

    EH_RIVERBED_CHEST = (
        "EH Riverbed Chest", 233, Regions.EASTERN_HEATH_GRASSLAND_RIVERBED_BOTTOM
    )

    EH_CHOPPE_SHOPPE_TRINKET = (
        "EH Choppe Shoppe Trinket", 226, Regions.EASTERN_HEATH_CHOPPE_SHOPPE,
    )

    EH_HIDDEN_SLIME_CAVE_CHEST = (
        "EH Hidden Slime Cave Chest", 228, Regions.EASTERN_HEATH_HIDDEN_GROTTO,
    )

    EH_BESIDE_KITE_CHEST = (
        "EH Beside Kite Chest", 234, Regions.EASTERN_HEATH_GRASSLAND_WATERFALL_SECOND_LEVEL,
    )

    EH_KITE_TRINKET = (
        "EH Kite Trinket", 223, Regions.EASTERN_HEATH_GRASSLAND_WATERFALL_SECOND_LEVEL, HasReachingSideArm()
        & (
            CanJumpTiles(distance=4, has_wall=True, no_sidearms=True)
            | (
                CanJumpTiles(distance=4, has_wall=True)
                & Has(PermanentUpgrades.DOUBLE_SIDEARM_PERMIT.value)
            )
            | (CanBurrow() & CanClimb())
            | (
                CanBurrow()
                & HasKear(kear=SingleKears.EASTERN_HEATH_WATERFALL_KEAR.value)
            )
            | (
                Has(PermanentUpgrades.COLTRANE_PEAK_TICKET.value)
                & Has(PermanentUpgrades.TRAIN_PASS.value)
                & CanClimb()
            )
        ),
    )

    EH_MIMIC_CHEST = (
        "EH Mimic Chest", 230, Regions.EASTERN_HEATH_UNDER_BRIDGE_WEST,
    )

    EH_BUCKLER_S_BLUFF_JOULE_BOX = (
        "EH Buckler's Bluff Joule Box", 229, Regions.EASTERN_HEATH_BUCKLERS_BLUFF_CLIFF, CanClimb()
        & (
            Has(PlayerUpgrades.JOULE_BOX.value, count=2)
            & Has(Sidearms.DRIVER_DRILL.value)
        ),
    )

    EH_POPPIT_CAVE_CHEST = (
        "EH Poppit Cave Chest", 235, Regions.EASTERN_HEATH_GRASSLAND_POPPIT_CAVE,
    )

    EH_POPPIT_CAVE_WILLOW = (
        "EH Poppit Cave Shop Trinket", 239, Regions.EASTERN_HEATH_POPPIT,
    )

    EH_POPPIT_CAVE_KEAR = (
        "EH Poppit Cave Shop Kear", 240, Regions.EASTERN_HEATH_POPPIT,
    )

    EH_FROZEN_PASS_TRINKET = (
        "EH Frozen Pass Trinket", 237, Regions.COLTRANE_PEAK_FROZEN_PASS_BOTTOM,
    )

class BossLocations(LocationTypeEnum):
    EH_DEFEAT_MAXI = ("EH Defeat Maxi", 1018, Regions.EASTERN_HEATH_GRASSLAND, RepairedGeneratorCount(count=1) & PowerLevelThreshold(power=25))
