from collections import defaultdict

from BaseClasses import Region, Location, ItemClassification, LocationProgressType, CollectionRule
from rule_builder.rules import Has, Rule, True_
from .data.events import RADIANT_MANOR_DATA
from .data.items import BoneFiller, Abilities, PermanentUpgrades
from .data.locations import all_regions, all_region_transitions, all_internal_region_connections, \
    all_permanent_locations, dungeon_locations, Regions
from .data import LocationTypeEnum, RegionTypeEnum
from typing import TYPE_CHECKING

from .data.locations.areas import loners_landing
from .items import MinaTheHollowerItem

if TYPE_CHECKING:
    from . import MinaTheHollowerWorld

class DefaultRegions(RegionTypeEnum):
    MENU = "Menu"


def create_location(world, data: LocationTypeEnum):
    region = world.get_region(data.region.value)
    location = Location(world.player, data.value, data.location_id, region)
    location.progress_type = data.progress_type
    # location.item_rule = data.item_rule

    region.locations.append(location)
    world.set_rule(location, data.rule)

def create_region(world: "MinaTheHollowerWorld", region_type: RegionTypeEnum, locations_by_region: dict[RegionTypeEnum, list[LocationTypeEnum]] | None = None):
    region = Region(region_type.value, world.player, world.multiworld)
    world.multiworld.regions.append(region)

    if locations_by_region is None:
        return region

    for data in locations_by_region[region_type]:
        if data == loners_landing.OptionalLocations.LL_CAPTAINS_GIFT and world.ossex_start:
            continue

        location = Location(world.player, data.value, data.location_id, region)
        location.progress_type = data.progress_type
        # location.item_rule = data.item_rule
        region.locations.append(location)
        world.set_rule(location, data.rule)

    return region

def is_dungeon_location_excluded(world: "MinaTheHollowerWorld", dungeon_index: int,) -> bool:
    if dungeon_index in world.lit_generators:
        return True
    return dungeon_index == RADIANT_MANOR_DATA.index and world.options.goal.value == world.options.goal.option_fixGenerators

def fill_dungeon_regions(world: "MinaTheHollowerWorld") -> list[int]:
    excluded_locations: list[int] = []
    for dungeon_index, locations in dungeon_locations.items():
        if is_dungeon_location_excluded(world, dungeon_index):
            excluded_locations.extend(
                data.location_id
                for data in locations
            )
            continue

        for data in locations:
            create_location(world, data)
    return excluded_locations

def create_event_location(world, menu: Region,
  name: str, location_rule: CollectionRule | Rule["MinaTheHollowerWorld"],
  region_name: str, region_rule: CollectionRule | Rule["MinaTheHollowerWorld"]):
    region = Region(region_name, world.player, world.multiworld)

    world.multiworld.regions.append(region)

    world.create_entrance(menu, region, name=f"Menu To {name}",rule=region_rule)
    location = Location(world.player, name, None, region)
    region.locations.append(location)
    world.set_rule(location, location_rule)


def create_regions(world: "MinaTheHollowerWorld") -> list[int]:
    menu = create_region(world, DefaultRegions.MENU)

    locations_by_region: dict[RegionTypeEnum, list[LocationTypeEnum]] = defaultdict(list)
    for _location in all_permanent_locations:
        locations_by_region[_location.region].append(_location)

    for region in Regions:
        create_region(world, region, locations_by_region)

    excluded_locations: list[int] = fill_dungeon_regions(world)

    if world.is_ut:
        create_event_location(world, menu, "Burrow", lambda _: False, "Burrow Region", Has(Abilities.BURROW.value))
        create_event_location(world, menu, "Swim", lambda _: False, "Swim Region", Has(Abilities.SWIM.value))
        create_event_location(world, menu, "Carry", lambda _: False, "Carry Region", Has(Abilities.CARRY.value))
        create_event_location(world, menu, "Climb", lambda _: False, "Climb Region", Has(Abilities.CLIMB.value))
        create_event_location(world, menu, "Bounce", lambda _: False, "Bounce Region", Has(Abilities.BOUNCE.value))
        create_event_location(world, menu, "Spring", lambda _: False, "Spring Region", Has(Abilities.SPRING.value))

        create_event_location(world, menu, "Train Pass", lambda _: False, "Train Pass Region", Has(PermanentUpgrades.TRAIN_PASS.value))
        create_event_location(world, menu, "Bayou Ticket", lambda _: False, "Bayou Ticket Region", Has(PermanentUpgrades.BAYOU_TICKET.value))
        create_event_location(world, menu, "Septemburg Ticket", lambda _: False, "Septemburg Ticket Region", Has(PermanentUpgrades.SEPTEMBURG_TICKET.value))
        create_event_location(world, menu, "Bone Beach Ticket", lambda _: False, "Bone Beach Ticket Region", Has(PermanentUpgrades.BONE_BEACH_TICKET.value))
        create_event_location(world, menu, "Coltrane Peak", lambda _: False, "Coltrane Peak Region", Has(PermanentUpgrades.COLTRANE_PEAK_TICKET.value))

    return excluded_locations


def create_entrances(world: "MinaTheHollowerWorld"):

    menu = world.get_region("Menu")
    if world.ossex_start:
        world.create_entrance(menu, world.get_region(Regions.OSSEX_CITY_CENTER_MAIN.value), name="Menu To Ossex")
    world.create_entrance(menu, world.get_region(Regions.LONERS_LANDING_SHIPWRECK.value), name="Menu To Shipwreck")

    for transition_data in all_region_transitions:
        exiting_region = world.get_region(transition_data.exiting_screen.value)
        entering_region = world.get_region(transition_data.entering_screen.value)
        entrance = world.create_entrance(exiting_region, entering_region, rule=transition_data.rule, name=transition_data.value, force_creation=True)
        if transition_data.entrance_group != 0 and world.entrance_rando:
            entrance.randomization_group = transition_data.entrance_group
            world.disconnect_entrance_for_randomization(entrance)
    for connections_data in all_internal_region_connections:
        exiting_region = world.get_region(connections_data.exiting_region.value)
        entering_region = world.get_region(connections_data.entering_region.value)
        entrance = world.create_entrance(exiting_region, entering_region, rule=connections_data.rule, name=connections_data.value, force_creation=True)
