import json
from importlib.resources import files
from typing import Any, ClassVar, override

from BaseClasses import ItemClassification, Location, Tutorial, CollectionState
from NetUtils import JSONMessagePart
from Options import OptionError
from entrance_rando import bake_target_group_lookup, randomize_entrances

from Utils import visualize_regions
from rule_builder.rules import Has
from .data.events import repair_generator_data
from .data.rules.ability_rules import PowerLevelThreshold
from .data.rules.movement_rules import CanJumpTiles, max_jump
from .data.rules.state_rules import repair_generator_lookup
from .rules import set_goal

from ..AutoWorld import WebWorld
from . import items, locations, tracker
from .constants import *
from .data import get_target_groups
from .data.items import all_filler_items, all_items
from .data.locations import all_locations
from .items import MinaTheHollowerItem
from .options import ABILITY_RANDO_SLOT_KEYS, mina_the_hollower_option_groups, Goal
from .world_base import MinaTheHollowerBase


class MinaTheHollowerWeb(WebWorld):
    theme = "partyTime"
    setup_en = Tutorial(
        tutorial_name="Multiworld Setup Guide",
        description="A guide to setting up the Mina The Hollower randomizer connected to an Archipelago Multiworld.",
        language="English",
        file_name="setup_en.md",
        link="setup/en",
        authors=["FyreDay"],
    )
    option_groups = mina_the_hollower_option_groups
    tutorials = [setup_en]


def load_manifest():
    return json.loads(
        files(__package__).joinpath("archipelago.json").read_text("utf-8")
    )


class MinaTheHollowerWorld(MinaTheHollowerBase):

    manifest = load_manifest()

    game = MINA_THE_HOLLOWER
    web = MinaTheHollowerWeb()

    item_name_to_id: ClassVar[dict[str, int]] = {
        item.value: item.item_id for item in all_items
    }
    location_name_to_id: ClassVar[dict[str, int]] = {
        loc.value: loc.location_id for loc in all_locations
    }

    item_lookup = {item.value: item for item in all_items}

    ut_can_gen_without_yaml = True

    tracker_world: ClassVar = {
        "map_page_folder": "tracker",
        "map_page_maps": "maps/maps.json",
        "map_page_locations": {
            "locations/eastern_heath.json",
            "locations/ossex.json",
            "locations/loners_landing.json",
            "locations/southern_outskirts.json",
            "locations/backwaters.json",
            "locations/western_wilds.json",
            "locations/bayou.json",
            "locations/mourners_mile.json",
            "locations/queensbury.json",
            "locations/kindlewood.json",
            "locations/septemburg.json",
            "locations/sandfalls.json",
            "locations/bone_beach.json",
            "locations/coltrane_peak.json",
            "locations/astral_orrery.json",
            "locations/radiant_manor.json",
            "locations/overview.json",

        },
        "map_page_index": tracker.map_page_index,
        "map_page_setting_key": "MTH_level_{team}_{player}",
    }

    @staticmethod
    def interpret_slot_data(slot_data: dict[str, Any]) -> dict[str, Any]:
        return slot_data

    regions: set[str]
    itempool: list[MinaTheHollowerItem]
    entrance_rando: bool
    hints: dict[int, str]
    starting_items: list[MinaTheHollowerItem]

    def __init__(self, multiworld, player):
        self.regions = set()
        self.itempool = []
        self.entrance_rando = False
        self.hints = {}
        self.starting_items = []
        self.lit_generators:list[int] = []
        self.broken_generators:list[int] = []
        self.removed_locations: list[int] = []
        self.is_ut = False
        super().__init__(multiworld, player)

    def generate_early(self) -> None:

        if self.options.goal.value == self.options.goal.option_fixGenerators:

            if self.options.goal_generators.value <= 2 and self.options.max_stat_level.value > 20:
                self.options.max_stat_level.value = 20

            if self.options.goal_generators.value <= 3:
                valid_generators = [QUEENSBURY_CRYPT, NOXS_BAYOU, SEPTEMBURG, BONE_BEACH]
                if self.options.goal_generators == 1:
                    self.options.max_stat_level.value = 6
                elif self.options.goal_generators == 2:
                    self.options.max_stat_level.value = 10
            elif self.options.goal_generators.value < 5:
                valid_generators = [QUEENSBURY_CRYPT, NOXS_BAYOU, SEPTEMBURG, BONE_BEACH,
                                    self.random.choice([COLTRANE_PEAK, ASTRAL_ORRERY])]
            else:
                valid_generators = [QUEENSBURY_CRYPT, NOXS_BAYOU, SEPTEMBURG, BONE_BEACH, COLTRANE_PEAK, ASTRAL_ORRERY]
            selected_generators = self.random.sample(valid_generators, self.options.goal_generators.value)
            self.broken_generators =[gen.index for gen in repair_generator_data if gen.gen_name in selected_generators]
            self.lit_generators = [gen.index for gen in repair_generator_data if gen.gen_name not in selected_generators]
        elif self.options.goal.value == self.options.goal.option_radiantManorGenerator:
            self.options.goal_generators.value = 6
            valid_generators = [QUEENSBURY_CRYPT, NOXS_BAYOU, SEPTEMBURG, BONE_BEACH, COLTRANE_PEAK, ASTRAL_ORRERY]
            selected_generators = self.random.sample(valid_generators, self.options.goal_generators.value)
            self.broken_generators = [gen.index for gen in repair_generator_data if gen.gen_name in selected_generators]

        if len(self.options.ability_rando.value) != 0:
            self.options.ossex_start.value = self.options.ossex_start.option_true


        self.is_ut = (hasattr(self.multiworld, "re_gen_passthrough")
            and isinstance(self.multiworld.re_gen_passthrough, dict)
            and self.game in self.multiworld.re_gen_passthrough)
        self.handle_ut_yamless(None)

    def create_regions(self):
        self.removed_locations = locations.create_regions(self)
        items.create_events(self)
        locations.create_entrances(self)

    def connect_entrances(self) -> None:
        if self.entrance_rando:
            target_group_lookup = bake_target_group_lookup(self, get_target_groups)
            randomize_entrances(self, False, target_group_lookup)

    def create_item(self, item: str) -> MinaTheHollowerItem:
        item_enum = self.item_lookup[item]

        return MinaTheHollowerItem(
            item,
            item_enum.classification,
            item_enum.item_id,
            self.player,
        )

    def create_items(self):
        self.starting_items = items.create_items(self)
        for item in self.starting_items:
            self.push_precollected(item)

    def set_rules(self):
        set_goal(self)


    # def generate_output(self, output_directory: str):
    #     print("Generating Output")
    #     visualize_regions(
    #         self.multiworld.get_region("Menu", self.player),
    #         f"Player{self.player}_output.puml",
    #         show_entrance_names=True,
    #         regions_to_highlight=self.multiworld.get_all_state(
    #             self.player
    #         ).reachable_regions[self.player],
    #     )

    def fill_slot_data(self) -> id:
        ability_rando = self.options.ability_rando.value
        return {
            "sem_ver": self.manifest["mod_version"],
            "goal_config": self.options.goal.value,
            "goal_generators": self.options.goal_generators.value,
            "goal_bosses": 0, #self.options.goal_bosses.value,
            "ossex_start": self.options.ossex_start.value,
            "kear_rando": self.options.kear_rando.value,
            "max_stat_level": self.options.max_stat_level.value,
            "wallet_cap": False,
            "lit_generators" : self.lit_generators,
            "broken_generators" : self.broken_generators,
            # "entrance_rando" : self.options.entrance_rando.value,
            "death_link": self.options.death_link.value,
            # The client disables each ability while its "*_rando" key is nonzero.
            **{
                slot_key: int(option_key in ability_rando)
                for option_key, slot_keys in ABILITY_RANDO_SLOT_KEYS.items()
                for slot_key in slot_keys
            },
            "starting_items": [
                item.name
                for item in self.starting_items
            ],
            "removed_locations": self.removed_locations
        }

    @override
    def explain_rule(self, dest_name: str, state: CollectionState, *_: Any, **__: Any) -> list[JSONMessagePart] | None:
        if dest_name == "help" or dest_name == "Help" :
            return [
                {
                    "type": "color",
                    "color": "green",
                    "text": f"Max Jump, Generators\n",
                },
            ]
        if dest_name == "Max Jump" or dest_name == "max jump":
            pure_distance, pure_loadout = max_jump(state, self.player, False, False, False)
            wall_distance, wall_loadout = max_jump(state, self.player, True, False, False)
            no_sides_distance, no_sides_loadout = max_jump(state, self.player, True, True, False)
            swim_distance, swim_loadout = max_jump(state, self.player, False, False, True)

            pure_loadout_message = "" if  pure_loadout is None else f" Loadout is {", ".join([x.value for x in pure_loadout])}"
            wall_loadout_message = "" if  wall_loadout is None else f" Loadout is {", ".join([x.value for x in wall_loadout])}"
            no_sides_loadout_message = "" if  no_sides_loadout is None else f" Loadout is {", ".join([x.value for x in no_sides_loadout])}"
            swim_loadout_message = "" if  swim_loadout is None else f" Loadout is {", ".join([x.value for x in swim_loadout])}"
            return [
                {"type": "color", "color": "green", "text": f"Can Jump {pure_distance} Tiles.{pure_loadout_message}\n"},
                {"type": "color", "color": "green", "text": f"Can Jump With Wallower {wall_distance} Tiles.{wall_loadout_message}\n"},
                {"type": "color", "color": "green", "text": f"Can Jump With No Sidarms {no_sides_distance} Tiles.{no_sides_loadout_message}\n"},
                {"type": "color", "color": "green", "text": f"Can Jump Over Water {swim_distance} Tiles.{swim_loadout_message}\n"},
            ]
        if dest_name == "Generators" or dest_name == "generators":
            repairable_generators = [
                repair_generator_lookup[i].type.name for i in self.broken_generators
                if state.has(repair_generator_lookup[i].type.event_item, self.player)
            ]

            unreachable_generators = [
                repair_generator_lookup[i].type.name for i in self.broken_generators
                if not state.has(repair_generator_lookup[i].type.event_item, self.player)
            ]

            return [
                {
                    "type": "color",
                    "color": "green",
                    "text": f"Repairable Generators: {', '.join(repairable_generators) or 'None'}\n",
                },
                {
                    "type": "color",
                    "color": "salmon",
                    "text": f"Unreachable Generators: {', '.join(unreachable_generators) or 'None'}\n",
                },
            ]
        return None


    def extend_hint_information(self, hint_data: dict[int, dict[int, str]]):
        hint_data[self.player] = self.hints

    def handle_ut_yamless(
        self, slot_data: dict[str, Any] | None
    ) -> dict[str, Any] | None:
        if self.is_ut and not slot_data:
            slot_data = self.multiworld.re_gen_passthrough[self.game]
        if not slot_data:
            return None

        self.options.goal.value = slot_data["goal_config"]
        self.options.goal_generators.value = slot_data["goal_generators"]
        # self.options.goal_bosses.value = slot_data["goal_bosses"]
        self.options.death_link.value = slot_data["death_link"]
        self.options.kear_rando.value = slot_data["kear_rando"]
        self.options.ossex_start.value = slot_data["ossex_start"]
        self.options.max_stat_level.value = slot_data["max_stat_level"]
        self.lit_generators = slot_data["lit_generators"]
        self.broken_generators = slot_data["broken_generators"]
        self.options.ability_rando.value = {
            option_key
            for option_key, slot_keys in ABILITY_RANDO_SLOT_KEYS.items()
            if any(slot_data.get(slot_key) for slot_key in slot_keys)
        }
        # self.options.entrance_rando.value = slot_data["entrance_rando"]
        # self.options.shuffled_sidearms.value = slot_data["shuffled_sidearms"]
        # self.options.shuffle_enemy_level.value = slot_data["shuffle_enemy_level"]
        # self.options.shuffled_items.value = slot_data["shuffled_items"]

        for item_name in slot_data["starting_items"]:
            self.starting_items.append(MinaTheHollowerItem(item_name, ItemClassification.progression, self.item_name_to_id[item_name], self.player))
        return slot_data
