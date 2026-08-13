from BaseClasses import LocationProgressType
from rule_builder.rules import Has, CanReachLocation
from .._generated.regions import Regions
from ... import LocationTypeEnum
from ...events import BONE_BEACH_DATA
from ...rules.ability_rules import CanBurrow, CanBounce, CanClimb, CanCarry, CanSwim, \
    HasFishingRod, PowerLevelThreshold
from ...rules.movement_rules import CanJumpTiles
from ...rules.state_rules import RepairedGenerator

class Locations(LocationTypeEnum):
    BB_FISH_GOREMAW_FANG = (
        "BB Fish Goremaw Fang", 88, Regions.BONE_BEACH_AQUATIC, HasFishingRod() & CanSwim(),
    )

    BB_BEHIND_FURGUS_TUNNEL_CHEST = (
        "BB Behind Furgus Tunnel Chest", 354, Regions.BONE_BEACH_BONE_RUSH_MINE,
    )

    BB_ENTRANCE_PIT_HANDLE_BONESTONE = (
        "BB Entrance Pit Handle Bonestone", 71, Regions.BONE_BEACH_BONE_RUSH_DROP,
    )

    BB_CONVEYER_JUMP_BONESTONE = (
        "BB Conveyer Jump Bonestone", 70, Regions.BONE_BEACH_BONE_RUSH_CONVEYOR_TOP, CanBounce(),
    )

    BB_BOUNCE_CONVEYER_CHALLENGE_CHEST = (
        "BB Bounce Conveyer Challenge Chest", 78, Regions.BONE_BEACH_WORMS_BACK_SPLIT, CanJumpTiles(distance=2),
    )

    BB_MESSAGE_IN_A_BOTTLE_CHEST = (
        "BB Message In a Bottle Chest", 73, Regions.BONE_BEACH_AQUATIC_CONVEYOR, CanBurrow(),
    )

    BB_BRAC_S_TENT_TRINKET = (
        "BB Brac's Tent Trinket", 80, Regions.BONE_BEACH_BRACS_TENT,
    )

    BB_BRAC_S_TENT_KEAR = (
        "BB Brac's Tent Kear", 81, Regions.BONE_BEACH_BRACS_TENT,
    )

    BB_SECRET_SHOALS_TRINKET = (
        "BB Secret Shoals Trinket", 74, Regions.BONE_BEACH_SECRET_SHOALS, CanSwim(),
    )

    BB_CALCIFIED_CAVES_KEAR = (
        "BB Calcified Caves Kear", 79, Regions.BONE_BEACH_CALCIFIED_CAVES,
    )

    BB_CALCIFIED_CAVES_JAIL_BONESTONE = (
        "BB Calcified Caves Jail Bonestone", 76, Regions.BONE_BEACH_CALCIFIED_CAGE,
    )

    BB_SUBMERGED_HANDLES_CHEST = (
        "BB Submerged Handles Chest", 77, Regions.BONE_BEACH_SUBMERGED_HANDLES, CanSwim(),
    )

    BB_PULSING_TRACT_HIDDEN_BONESTONE = (
        "BB Pulsing Tract Hidden Bonestone", 86, Regions.BONE_BEACH_PULSING_TRACT_MOVING_TOP, CanJumpTiles(distance=2),
    )

    BB_WORM_S_BACK_WEAPON_CHEST = (
        "BB Worm's Back Weapon Chest", 75, Regions.BONE_BEACH_WORMS_BACK_CHEST, CanBounce(),
    )

    BB_WORM_S_BACK_BONESTONE = (
        "BB Worm's Back Bonestone", 72, Regions.BONE_BEACH_WORMS_BACK_RIGHT, CanBurrow(),
    )

    BB_STOMACH_MINE_KEAR = (
        "BB Stomach Mine Kear", 84, Regions.BONE_BEACH_STOMACH_MINE_LOWER, CanBurrow() & CanBounce(),
    )

    BB_GUT_DEPTHS_MOVING_STAIRS_BONESTONE = (
        "BB Gut Depths Moving Stairs Bonestone", 85, Regions.BONE_BEACH_GUT_DEPTHS_HIDDEN, CanBounce(),
    )

    BB_GUT_DEPTHS_PASSAGE_CHEST = (
        "BB Gut Depths Passage Chest", 87, Regions.BONE_BEACH_GUT_DEPTHS_DARK,
    )

    BB_MINED_MIND_FIGHT_REWARD = (
        "BB Mined Mind Fight Reward", 83, Regions.BONE_BEACH_BRAIN_ALCOVE,
    )

    OS_COUPLE_S_QUARTER_TRINKET = (
        "OS Couple's Quarter Trinket", 147, Regions.BONE_BEACH_CALCIFIED_CAGE,
    )

    SF_MITE_FIGHT_REWARD = (
        "SF Mite Fight Reward", 319, Regions.SANDFALLS_SIFTED_SANDS, RepairedGenerator(event=BONE_BEACH_DATA),
    )

class BossLocations(LocationTypeEnum):
    BB_DEFEAT_MINED_MIND = ("BB Defeat Mined Mind", 1004, Regions.BONE_BEACH_BRAIN_ALCOVE, PowerLevelThreshold(power=40))
    # BB_SHORELINE_GENERATOR = ("BB Shoreline Generator Repaired", 6003, Regions.BONE_BEACH_SHORELINE_GENERATOR)