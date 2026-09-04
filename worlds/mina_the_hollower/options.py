from dataclasses import dataclass

from Options import DefaultOnToggle, Toggle, OptionSet, OptionDict, Choice, OptionGroup, \
    PerGameCommonOptions, Range, OptionCounter
from schema import Schema

from .data.items.traps import get_default_dict


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
    If your goal is 'Fix Generators', how many should you need to repair?.
    """
    display_name = "Generators Required"
    range_start = 1
    range_end = 6
    default = 3

class GeneratorPool(OptionSet):
    """
    This is the pool of generators that the randomizer will select X generators from, where X is your "Generators Required" Option
    **WARNING** If this pool is smaller than the number of generators to goal, this will raise an option error
    **WARNING** This cannot be empty

    Valid Options:
    - **Queensbury Crypt**
    - **Nox's Bayou**
    - **Septemburg**
    - **Bone Beach**
    - **Coltrane Peak**
    - **Astral Orrery**
    """
    display_name = "Generator Pool"
    default = ["Queensbury Crypt", "Nox's Bayou", "Septemburg", "Bone Beach", "Coltrane Peak", "Astral Orrery"]
    valid_keys = ["Queensbury Crypt", "Nox's Bayou", "Septemburg", "Bone Beach", "Coltrane Peak", "Astral Orrery"]

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
    The maximum cap of each stat. Vanilla non-NG+ is 10, maximum at the end of the NG+ is 99.
    Will be soft capped if location count is too small, as this replaces filler items in the pool
    """
    display_name = "Maximum Level for Stats"
    range_start = 10
    range_end = 99
    default = 15

class RandomizeStartingItems(Toggle):
    """
    Take all starting health, spark, vials, Magic and randomize them. This increases the difficulty tenfold and can cause some cursed starts. You have been warned.
    """
    display_name = "Randomize Starting Items"

class AbilityRando(OptionSet):
    """
    Randomize abilities (You will not be able to perform the listed actions until sent them as items).
    If there are no abilities randomized, you will start in Loner's Landing. Otherwise you will start in Ossex

    If you are ever stuck, there is a **Teleport Home** Button in the pause menu

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
    option_areaApItems = 2
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

class RandomizeAstralSwitches(DefaultOnToggle):
    """
    Instead of hitting the switches in Mirror's End yourself, make them items in the multiworld
    """
    display_name = "Randomize Mirror's End Switches"

class DeathLink(Toggle):
    """When you die a sparkless death, everyone who enabled death link dies. Of course, the reverse is true too."""
    display_name = "Death Link"
    rich_text_doc = True

class TrapPercentage(Range):
    """
    What percentage of filler do you want replaced with traps?
    """
    display_name = "Trap Percentage"
    range_start = 0
    range_end = 100
    default = 0

class TrapWeights(OptionCounter):
    """
    Change the weights of each trap

    Valid Options:
        - **Flip Controls Trap** - Invert your controls
        - **Floor Is Lava Trap** - Leave a trail of lava
        - **Giant Trap** - Mina gets larger
        - **2x Giant Trap** - Mina gets VERY large
        - **Giant Enemies Trap** - All enemies get larger
        - **2x Giant Enemies Trap** - All enemies get VERY large
        - **Invisible Trap** - Mina becomes invisible
        - **No HUD Trap** - Remove your HUD
        - **Rotate Camera Trap** - Slowly rotate your camera for a short time
        - **Rotate Camera Input Trap** - Moving now rotates your camera slowly
        - **Mirror Screen Trap** - Mirror your screen
        - **Upsidedown Screen Trap** - Mirror your screen vertically
    """
    display_name = "Trap Weights"
    default = get_default_dict()
    min = 0
    valid_keys = get_default_dict().keys()


mina_the_hollower_option_groups= [
    OptionGroup("Game Options", [
        DeathLink
    ]),
    OptionGroup("Goal Options", [
        Goal,
        NumberOfGenerators,
        GeneratorPool,
    ]),
    OptionGroup("Item Options", [
        StartingWeapon,
        RandomizeStartingItems,
        BoneUpCap,
        MaximumStatLevel,
        AbilityRando,
        KearRandomization,
        RandomizeAstralSwitches,
    ]),
    OptionGroup("Filler Options", [
        TrapPercentage,
        TrapWeights,
    ]),
]

@dataclass
class MinaTheHollowerOptions(PerGameCommonOptions):
    goal: Goal
    goal_generators: NumberOfGenerators
    generator_pool: GeneratorPool
    # goal_bosses: NumberOfBosses
    starting_weapon: StartingWeapon
    random_starting_items: RandomizeStartingItems
    ability_rando: AbilityRando
    bone_up_cap: BoneUpCap
    max_stat_level: MaximumStatLevel

    # entrance_rando: RandomizeEntrances

    kear_rando: KearRandomization
    astral_switches: RandomizeAstralSwitches
    death_link: DeathLink
    trap_percent: TrapPercentage
    trap_weights: TrapWeights
    # shuffled_sidearms: ShuffledSidearms
    # shuffle_enemy_level: ShuffleEnemyLevel
