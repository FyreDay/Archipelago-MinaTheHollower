from BaseClasses import LocationProgressType
from rule_builder.rules import Has, CanReachLocation
from .._generated.regions import Regions
from ... import LocationTypeEnum
from ...items import AstralPlatforms, SingleKears
from ...rules.ability_rules import CanBurrow, CanBounce, CanClimb, CanCarry, HasFishingRod, PowerLevelThreshold
from ...rules.state_rules import HasKear
from ...rules.movement_rules import CanJumpTiles

class Locations(LocationTypeEnum):
    AO_STELLARIUM_EAST_CHEST = (
        "AO Stellarium East Chest", 129, Regions.ASTRAL_ORRERY_STELLARIUM, HasKear(kear=SingleKears.ASTRAL_ORRERY_STELLARIUM_KEAR.value),
    )

    AO_TUBERT_TRINKET = (
        "AO Tubert Trinket", 137, Regions.ASTRAL_ORRERY_STELLARIUM_MUTANT_SWITCH,
    )

    AO_TUBERT_KEAR = (
        "AO Tubert Kear", 138, Regions.ASTRAL_ORRERY_STELLARIUM_MUTANT_SWITCH,
    )

    AO_GRAVITY_ZONE_LONG_HALLWAY_CHEST = (
        "AO Gravity Zone Long Hallway Chest", 133, Regions.ASTRAL_ORRERY_GRAVITY_ZONE, CanJumpTiles(distance=2),
    )

    AO_GRAVITY_ZONE_AFTER_PURPLE_SWITCH_KEAR = (
        "AO Gravity Zone After Purple Switch Kear", 134, Regions.ASTRAL_ORRERY_GRAVITY_ZONE,
    )

    AO_GRAVITY_ZONE_BELOW_GREEN_SWITCH_CHEST = (
        "AO Gravity Zone Below Green Switch Chest", 128, Regions.ASTRAL_ORRERY_GRAVITY_ZONE, CanBurrow(),
    )

    AO_COG_CHAMBER_WEST_SECRET_ROOM_CHEST = (
        "AO Cog Chamber West Secret Room Chest", 130, Regions.ASTRAL_ORRERY_COG_CHAMBER, CanBurrow() & CanCarry(),
    )

    AO_COG_CHAMBER_EAST_SECRET_ROOM_KEAR = (
        "AO Cog Chamber East Secret Room Kear", 135, Regions.ASTRAL_ORRERY_COG_CHAMBER, CanBurrow() & CanCarry(),
    )

    AO_MUTANT_LAB_EAST_SECRET_ROOM_CHEST = (
        "AO Mutant Lab East Secret Room Chest", 131, Regions.ASTRAL_ORRERY_MUTANT_LAB, CanBurrow(),
    )

    AO_MUTANT_LAB_WEST_SECRET_ROOM_TRINKET = (
        "AO Mutant Lab West Secret Room Trinket", 132, Regions.ASTRAL_ORRERY_MUTANT_LAB, CanBurrow(),
    )

    AO_HALL_OF_SCHOLARS_BELOW_BOSS_CHAMBER_BONESTONE = (
        "AO Hall of Scholars Below Boss Chamber Bonestone", 126, Regions.ASTRAL_ORRERY_HALL_OF_SCHOLARS,
    )

    AO_HALL_OF_SCHOLARS_EXIT_CHEST = (
        "AO Hall of Scholars Exit Chest", 136, Regions.ASTRAL_ORRERY_HALL_OF_SCHOLARS_END, CanBurrow(),
    )

    AO_THE_CONGEALED_FIGHT_REWARD = (
        "AO The Congealed Fight Reward", 125, Regions.ASTRAL_ORRERY_SEALED_ARCHIVE_CONGEALED_CHAMBER,
    )

class BossLocations(LocationTypeEnum):
    AO_DEFEAT_LUMENARKS = ("AO Defeat Lumenarks", 1014, Regions.ASTRAL_ORRERY_HALL_OF_SCHOLARS, PowerLevelThreshold(power=40))
    AO_DEFEAT_THE_CONGEALED = ("AO Defeat The Congealed", 1006, Regions.ASTRAL_ORRERY_SEALED_ARCHIVE_CONGEALED_CHAMBER, PowerLevelThreshold(power=45))
    # AO_STARRY_GENERATOR = ("AO Starry Generator Repaired", 6005, Regions.ASTRAL_ORRERY_STARRY_GENERATOR)


