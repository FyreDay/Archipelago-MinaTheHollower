from typing import ClassVar, Dict, Any, Optional

from BaseClasses import Tutorial, ItemClassification
from worlds.mina_the_hollower import locations, items, tracker
from worlds.mina_the_hollower.items import MinaTheHollowerItem,create_items, get_all_items
from worlds.mina_the_hollower.regions import connect_random_entrances, connect_entrances, create_regions
from worlds.mina_the_hollower.rules import set_rules

from .world_base import MinaTheHollowerBase

class MinaTheHollowerWorld(MinaTheHollowerBase):

    item_name_to_id: ClassVar[Dict[str, int]] = {item_name: item_data.code for item_name, item_data in get_all_items().items()}

    location_name_to_id: ClassVar[Dict[str, int]] = {item_name: item_code for item_name, item_code in locations.get_all_locations().items()}

    ut_can_gen_without_yaml = True
    tracker_world: ClassVar = {
        "map_page_folder": "tracker",
        "map_page_maps": "maps/maps.json",
        "map_page_locations": "locations/locations.json",
        "map_page_index": tracker.map_page_index,
        "map_page_setting_key": "mina_the_hollower_map_{team}_{player}",
    }

    @staticmethod
    def interpret_slot_data(slot_data: Dict[str, Any]) -> Dict[str, Any]:
        return slot_data

    def __init__(self, multiworld, player):
        self.itempool = []

        self.hints = {}

        super().__init__(multiworld, player)

    def generate_early(self) -> None:
        self.set_rule()
        self.handle_ut_yamless(None)

    def create_regions(self):
        create_regions(self)
        if not self.options.entrance_rando.value:
            connect_entrances(self)

    def connect_entrances(self) -> None:
        if self.options.entrance_rando.value:
            connect_random_entrances(self)

    def create_item(self, item: str) -> MinaTheHollowerItem:
        if item in items.get_filler():
            return MinaTheHollowerItem(item, ItemClassification.filler, self.item_name_to_id[item], self.player)
        return MinaTheHollowerItem(item, ItemClassification.progression, self.item_name_to_id[item], self.player)

    def create_items(self):
        starting_items = create_items(self)
        for item in starting_items:
            # print(item.name)
            self.push_precollected(item)

    def set_rules(self):
        set_rules(self)

    def fill_slot_data(self) -> id:
        #print("Filling Slot Data")
        return {
            "sem_ver": "0.1.0",
            "goal" : self.options.goal.value,
            "entrance_rando" : self.options.entrance_rando.value,
            "death_link" : self.options.death_link.value,
            "shuffled_sidearms" : self.options.shuffled_sidearms.value,
            "shuffle_enemy_level" : self.options.shuffle_enemy_level.value,
            "shuffled_items" : self.options.shuffled_items.value,
        }

    def extend_hint_information(self, hint_data: Dict[int, Dict[int, str]]):
        hint_data[self.player] = self.hints

    def handle_ut_yamless(self, slot_data: Optional[Dict[str, Any]]) -> Optional[Dict[str, Any]]:

        if not slot_data \
                and hasattr(self.multiworld, "re_gen_passthrough") \
                and isinstance(self.multiworld.re_gen_passthrough, dict) \
                and self.game in self.multiworld.re_gen_passthrough:
            slot_data = self.multiworld.re_gen_passthrough[self.game]

        if not slot_data:
            return None

        self.options.goal.value = slot_data["goal"]
        self.options.death_link.value = slot_data["death_link"]
        self.options.entrance_rando.value = slot_data["entrance_rando"]
        self.options.shuffled_sidearms.value = slot_data["shuffled_sidearms"]
        self.options.shuffle_enemy_level.value = slot_data["shuffle_enemy_level"]
        self.options.shuffled_items.value = slot_data["shuffled_items"]

        return slot_data