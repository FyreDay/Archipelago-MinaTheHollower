from dataclasses import dataclass

from Options import DeathLink, DefaultOnToggle, Toggle, OptionSet, OptionDict, Choice, OptionGroup, \
    PerGameCommonOptions, Range


class Goal(Choice):
    """
    Goal
    """
    display_name = "Goal"
    option_radiantManorGenerator = 0
    option_fixGenerators = 1
    # option_killBosses = 2
    default = 1

class BoneUpCap(Choice):
    """
    How do you want your Bone Up Cap Items. A progressive each for attack, defense and Sidearms OR One progressive item for all
    """
    display_name = "Bone Up Cap Type"
    option_perUpgrade = 1
    option_allUpgrade = 0
    default = 0

class NumberOfGenerators(Range):
    """
    The number of generators required to goal.
    """
    display_name = "Generators Required"
    range_start = 1
    range_end = 6
    default = 3

class NumberOfBosses(Range):
    """
    The number of bosses required to goal.
    """
    display_name = "Bosses Required"
    range_start = 1
    range_end = 26
    default = 26

class MaximumStatLevel(Range):
    """
    The maximum cap of each stat. Vanilla non-NG+ is 10, maximum at the end of the NG+es is 99.
    Will be soft capped if location count is too small
    """
    display_name = "Maximum Stat Caps"
    range_start = 10
    range_end = 99
    default = 15

class OssexStart(DefaultOnToggle):
    """
    Start In Ossex
    """
    display_name = "Ossex Start"

class RandomizeStartingItems(Toggle):
    """
    Take all starting health, spark, vials, Magic and randomize them. This increases the difficulty tenfold and can cause some cursed starts. You have been warned.
    """
    display_name = "Randomize Starting Items"

class AbilityRando(OptionSet):
    """
    Randomize abilities (You will not be able to perform the listed actions until sent them as items). You will always start in Ossex.

    Valid Options:
    - **Burrow** - The ability to burrow. You will still be able to enter Underlabs.
    - **Swim** - The ability to swim (burrow in deep water).
    - **Climb** - The ability to climb ropes.
    - **Bounce** - The ability to bounce on bounce plants and springboards.
    - **Spring** - The ability to be launched by springboards.
    - **Carry** - The ability to carry objects.
    """
    display_name = "Abilty Rando"
    default = ["Swim", "Climb", "Bounce", "Carry", "Spring"]
    valid_keys = ["Burrow", "Swim", "Climb", "Bounce", "Carry", "Spring"]


ABILITY_RANDO_SLOT_KEYS = {
    "Burrow": ["burrow_rando"],
    "Swim": ["swim_rando"],
    "Climb": ["rope_rando"],
    "Bounce": ["puff_rando"],
    "Carry": ["carry_rando"],
    "Spring": ["spring_rando"]
}

class RandomizeEntrances(OptionSet):
    """
    Currently there are no valid keys. Only give this []

    - **Doors** - Randomizes All Doors between eachother
    - **Stairs** - Randomizes All Stairs between eachother
    - **Area Transitions** - Randomizes All Screen transitions that change areas
    - **Screen Transitions** - Randomizes All Screen transitions
    """
    display_name = "Entrance Randomization"
    valid_keys = []

    # valid_keys = ["Doors", "Stairs", "Area Transitions", "Screen Transitions"]

class KearRandomization(Choice):
    """
    Vanilla: Universal Kears are in the multiworld. Every Kear Lock you open before receiving every single Kear will be OUT OF LOGIC
    AP Items: Each Kear Lock is removed by a unique AP item
    Area AP Items: All Kear Locks in an area are removed by a single AP Item
    """
    display_name = "Kear Rando"
    option_vanilla = 0
    option_apItems = 1
    # option_areaApItems = 2
    default = 1

class ShuffledSidearms(Toggle):
    """
    Sidearms are shuffled so each type always becomes the same other type
    """
    display_name = "Shuffled Sidearms"

class StartingWeapon(Choice):
    """
    Select your starting weapon.
    """
    display_name = "Starting Weapon"
    option_NightStar = 0
    option_BlastStrike_Maul = 1
    option_Whisper_And_Vesper = 2
    option_Battery_Buster = 3
    option_Guardian_Casket = 4
    default = 'random'


mina_the_hollower_option_groups= [
    OptionGroup("AP Options", [
        Goal,
        BoneUpCap,
        NumberOfGenerators,
        StartingWeapon,
        # NumberOfBosses,
        MaximumStatLevel,
        OssexStart,
        KearRandomization,
        RandomizeStartingItems,
        # RandomizeEntrances,
        AbilityRando,
        DeathLink,
    ]),
]

@dataclass
class MinaTheHollowerOptions(PerGameCommonOptions):
    goal: Goal
    goal_generators: NumberOfGenerators
    # goal_bosses: NumberOfBosses
    ossex_start: OssexStart
    starting_weapon: StartingWeapon
    kear_rando: KearRandomization
    # excluded_areas : ExcludedAreas
    bone_up_cap: BoneUpCap
    max_stat_level: MaximumStatLevel
    random_starting_items: RandomizeStartingItems
    # entrance_rando: RandomizeEntrances
    ability_rando: AbilityRando
    death_link: DeathLink
    # shuffled_sidearms: ShuffledSidearms
    # shuffle_enemy_level: ShuffleEnemyLevel
