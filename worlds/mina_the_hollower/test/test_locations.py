from BaseClasses import ItemClassification
from collections import Counter

from .. import options, MinaTheHollowerWorld
from .bases import MinaTestBase
from ..data.locations import all_collectables
from ..data.locations.areas import loners_landing


def test_all_locations(base):
    world_location_names = {location.name for location in base.world.get_locations()}

    for location in all_collectables:
        base.assertIn(location.value, world_location_names)
    if base.world.ossex_start:
        base.assertNotIn(loners_landing.OptionalLocations.LL_CAPTAINS_GIFT.value, world_location_names)
        base.assertNotIn(loners_landing.OptionalLocations.LL_HULK_TROOPER.value, world_location_names)
        base.assertNotIn(loners_landing.OptionalLocations.LL_THORNE_1.value, world_location_names)
    else:
        base.assertIn(loners_landing.OptionalLocations.LL_CAPTAINS_GIFT.value, world_location_names)
        base.assertNotIn(loners_landing.OptionalLocations.LL_HULK_TROOPER.value, world_location_names)
        base.assertNotIn(loners_landing.OptionalLocations.LL_THORNE_1.value, world_location_names)

class TestCollectablesNoOssexStart(MinaTestBase):
    options = {
        "Abilty Rando": [],
        "goal": "radiantManorGenerator"
    }

    def test_all_locations_loaded(self):
        test_all_locations(self)


class TestCollectablesOssexStart(MinaTestBase):
    options = {
        "Abilty Rando": [],
        "goal": "radiantManorGenerator",
    }

    def test_all_locations_loaded(self):
        test_all_locations(self)
