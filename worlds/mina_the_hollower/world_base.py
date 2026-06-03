from BaseClasses import Tutorial
from worlds.AutoWorld import WebWorld, World
from .options import mina_the_hollower_option_groups, MinaTheHollowerOptions


class MinaTheHollowerWeb(WebWorld):
    theme = "partyTime"
    #85957132542149874884
    setup_en = Tutorial(
        tutorial_name="Multiworld Setup Guide",
        description="A guide to setting up the Mina The Hollower randomizer connected to an Archipelago Multiworld.",
        language="English",
        file_name="setup_en.md",
        link="setup/en",
        authors=["FyreDay"]
    )
    option_groups = mina_the_hollower_option_groups
    tutorials = [setup_en]

class MinaTheHollowerBase(World):


    web = MinaTheHollowerWeb()
    options_dataclass = MinaTheHollowerOptions
    options: MinaTheHollowerOptions

    def __init__(self, multiworld, player):
        super().__init__(multiworld, player)