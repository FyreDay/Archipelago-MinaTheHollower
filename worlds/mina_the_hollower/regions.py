from BaseClasses import LocationProgressType, Location, Region


def create_location(world, region, name: str, code: int, excluded: bool = False):
    location = Location(world.player, name, code, region)
    if excluded:
        location.progress_type = LocationProgressType.EXCLUDED
    region.locations.append(location)

def add_locations(world, region, locations_dict):
    for (key, code) in locations_dict.items():
        create_location(world, region, key, code, False)


def create_region(world, name: str, hint: str, locations_dict):
    region = Region(name, world.player, world.multiworld)
    add_locations(world, region, locations_dict)
    world.multiworld.regions.append(region)
    return region


def create_regions(world):
    print("Create regions")

def connect_entrances(world):
    print("connect entrances as game intended")

def connect_random_entrances(world):
    print("connect entrances randomly based on groups")