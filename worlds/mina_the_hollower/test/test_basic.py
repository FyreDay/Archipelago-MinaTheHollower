from BaseClasses import ItemClassification
from collections import Counter

from .. import options, MinaTheHollowerWorld
from .bases import MinaTestBase


class TestBasic(MinaTestBase):
    options = {}
    world: MinaTheHollowerWorld

    def test_can_beat_game(self):
        self.collect_all_but([])
        self.assertBeatable(True)

# class TestFromDict(MinaTestBase):
#     options = {}
#     world: MinaTheHollowerWorld
#
#     def test_can_call(self):
#         entrance_rule = {"children":[{"args":{"count":1.0,"item_name":"Burrow"},"options":[],"rule":"Has"},{"args":{"count":1.0,"item_name":"Climb"},"options":[],"rule":"Has"}],"options":[],"rule":"And"}
#
#         rule = self.world.rule_from_dict(entrance_rule)
#
#         print(rule)

