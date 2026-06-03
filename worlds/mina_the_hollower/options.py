from dataclasses import dataclass

from Options import DeathLink, DefaultOnToggle, Toggle, OptionSet, OptionDict, Choice, OptionGroup, PerGameCommonOptions


class Goal(Choice):
    """
    Goal
    """
    display_name = "Goal"
    option_final_boss = 0

class EntranceRando(Toggle):
    """
    Randomize entrances
    """
    display_name = "Entrance Rando"

class AbilityRando(Toggle):
    """
    Randomize abilities
    """
    display_name = "Abilty Rando"


#game rando options
class ShuffledSidearms(Toggle):
    """
    Sidearms are shuffled so each type always becomes the same other type
    """
    display_name = "Auto Renovate"

class ShuffleEnemyLevel(Toggle):
    """
    Ememy attack and defense levels are randomized
    """
    display_name = "Auto Renovate"

class ShuffledItems(OptionDict):
    """
    Valid values are {"Enabled", "Disabled", "No Shops"}
    """
    display_name = "Shuffled Items"
    default = {
      "Bonestone": "Enabled",
      "Heath Roses": "Enabled",
      "Joule Boxes": "Enabled",
      "First Vial Pouch": "Enabled",
      "Vial Pouches": "Enabled",
      "Spark Container": "Enabled",
      "Trinket Bags": "Enabled",
      "Trinkets": "Enabled",
      "Train Pass": "Enabled",
      "Underlab Equipment": "Enabled",
      "Cloaks": "Enabled",
      "Fishing Upgrades": "Enabled",
      "Fish": "Enabled",
      "Kears": "Enabled",
      "Duel Sidearm": "Enabled",
      "Disturbing Dance": "Enabled",
    }

mina_the_hollower_option_groups= [
    OptionGroup("AP Options", [
        Goal,
        EntranceRando,
        AbilityRando,
        DeathLink,
    ]),
    OptionGroup("Game Options", [
        ShuffledSidearms,
        ShuffleEnemyLevel,
        ShuffledItems,
    ]),
]

@dataclass
class MinaTheHollowerOptions(PerGameCommonOptions):
    goal: Goal
    entrance_rando: EntranceRando
    ability_rando: AbilityRando
    death_link: DeathLink
    shuffled_sidearms: ShuffledSidearms
    shuffle_enemy_level: ShuffleEnemyLevel
    shuffled_items: ShuffledItems


