import json
from pathlib import Path

from worlds.mina_the_hollower import MinaTheHollowerWorld
from worlds.mina_the_hollower.data.locations import all_collectables
from worlds.mina_the_hollower.test.bases import MinaTestBase


def test_all_collectables_have_sections(base):
    locations_folder = Path(__file__).parent.parent / "tracker" / "locations"
    all_section_names = set()

    for location_file in locations_folder.glob("*.json"):
        try:
            with open(location_file, 'r') as f:
                locations = json.load(f)

            for location in locations:
                for section in location.get("sections", []):
                    section_name = section.get("name")
                    if section_name:
                        all_section_names.add(section_name)
        except json.JSONDecodeError:
            base.fail(f"Invalid JSON in {location_file}")

    # Check if all collectable keys exist as section names
    missing_collectables = []
    for collectable_key in all_collectables:
        if collectable_key.value not in all_section_names:
            missing_collectables.append(collectable_key.value)

    if missing_collectables:
        print(f"\nCollectable keys without matching section names:")
        for key in sorted(missing_collectables):
            print(f"  - {key}")

    base.assertEqual(len(missing_collectables), 0,
                     f"Found {len(missing_collectables)} collectable keys without matching section names")


def test_all_map_names_exist(base):
    maps_folder = Path(__file__).parent.parent / "tracker" / "maps"
    maps_file = maps_folder / "maps.json"

    try:
        with open(maps_file, 'r') as f:
            maps_data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        base.fail(f"Could not load maps.json: {e}")

    available_maps = {map_entry.get("name") for map_entry in maps_data if map_entry.get("name")}

    locations_folder = Path(__file__).parent.parent / "tracker" / "locations"
    missing_maps = set()

    for location_file in locations_folder.glob("*.json"):
        try:
            with open(location_file, 'r') as f:
                locations = json.load(f)

            for location in locations:
                for map_location in location.get("map_locations", []):
                    map_name = map_location.get("map")
                    if map_name and map_name not in available_maps:
                        missing_maps.add(map_name)
        except json.JSONDecodeError:
            base.fail(f"Invalid JSON in {location_file}")

    if missing_maps:
        print(f"\nMap names that don't exist in maps.json:")
        for map_name in sorted(missing_maps):
            print(f"  - {map_name}")
        print(f"\nAvailable maps in maps.json:")
        for map_name in sorted(available_maps):
            print(f"  - {map_name}")

    base.assertEqual(len(missing_maps), 0,
                     f"Found {len(missing_maps)} map names that don't exist in maps.json")


class TestCollectablesHaveSections(MinaTestBase):
    """Test that all collectable keys have matching section names in location files."""

    def test_collectables_have_matching_sections(self):
        test_all_collectables_have_sections(self)


class TestMapNamesExist(MinaTestBase):
    """Test that all map names referenced in locations exist in maps.json."""

    def test_map_names_in_maps_json(self):
        test_all_map_names_exist(self)