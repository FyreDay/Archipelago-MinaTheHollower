from collections import defaultdict

from BaseClasses import Region, Location, ItemClassification, LocationProgressType
from rule_builder.rules import Has
from .data.events import RADIANT_MANOR_DATA
from .data.items import BoneFiller, Abilities, PermanentUpgrades
from .data.locations import all_regions, all_region_transitions, all_internal_region_connections, \
    all_permanent_locations, dungeon_locations, Regions
from .data import EventData, matching_transition_types, LocationTypeEnum, RegionTypeEnum
from typing import TYPE_CHECKING
from .items import MinaTheHollowerItem

if TYPE_CHECKING:
    from . import MinaTheHollowerWorld

def create_event_location(world, name: str, data: EventData):
    region = world.get_region(data.region)
    location = Location(world.player, name, data.location_id, region)
    location.progress_type = data.progress_type
    region.locations.append(location)
    world.set_rule(location, data.rule)

def create_location(world, data: LocationTypeEnum):
    region = world.get_region(data.region.value)
    location = Location(world.player, data.value, data.location_id, region)
    location.progress_type = data.progress_type
    # location.item_rule = data.item_rule

    region.locations.append(location)
    world.set_rule(location, data.rule)

def create_region(world: "MinaTheHollowerWorld", regionType: RegionTypeEnum, hint: str = ""):
    region = Region(regionType.value, world.player, world.multiworld)
    valid_locations: dict[LocationTypeEnum, Location] = {}
    # TODO: dont loop through all locations for each region
    for data in all_permanent_locations:
        if data.value == "LL Captain's Gift" and world.options.ossex_start:
            continue
        if data.region != regionType:
            continue

        location = Location(world.player, data.value, data.location_id, region)
        location.progress_type = data.progress_type
        # location.item_rule = data.item_rule
        valid_locations[data] = location
        region.locations.append(location)

    world.multiworld.regions.append(region)

    for data, location in valid_locations.items():
        world.set_rule(location, data.rule)

    return region

class DefaultRegions(RegionTypeEnum):
    MENU = "Menu"
    BURROW_REGION = "Burrow Region"

def create_regions(world: "MinaTheHollowerWorld"):
    menu = create_region(world, DefaultRegions.MENU)
    excluded_locations: list[int] = []
    for region in Regions:
        create_region(world, region)
    for index, loc_map in dungeon_locations.items():
        for data in loc_map:
            override = index == RADIANT_MANOR_DATA.index and world.options.goal.value == world.options.goal.option_fixGenerators
            if (index in world.lit_generators) or override:
                excluded_locations.append(data.location_id)
            else:
                create_location(world, data)
    if world.is_ut:
        world.create_entrance(menu, create_region(world, DefaultRegions.BURROW_REGION), name="Menu To Burrow", rule=Has(Abilities.BURROW.value))
        world.create_entrance(menu, create_region(world, "Swim Region"), name="Menu To Swim", rule=Has(Abilities.SWIM.value))
        world.create_entrance(menu, create_region(world, "Carry Region"), name="Menu To Carry", rule=Has(Abilities.CARRY.value))
        world.create_entrance(menu, create_region(world, "Climb Region"), name="Menu To Climb", rule=Has(Abilities.CLIMB.value))
        world.create_entrance(menu, create_region(world, "Bounce Region"), name="Menu To Bounce", rule=Has(Abilities.BOUNCE.value))
        world.create_entrance(menu, create_region(world, "Spring Region"), name="Menu To Spring", rule=Has(Abilities.SPRING.value))

        create_event_location(world, "Burrow", EventData(None, "Burrow Region", lambda _: False))
        create_event_location(world, "Swim", EventData(None, "Swim Region", lambda _: False))
        create_event_location(world, "Carry", EventData(None, "Carry Region", lambda _: False))
        create_event_location(world, "Climb", EventData(None, "Climb Region", lambda _: False))
        create_event_location(world, "Bounce", EventData(None, "Bounce Region", lambda _: False))
        create_event_location(world, "Spring", EventData(None, "Spring Region", lambda _: False))

        world.create_entrance(menu, create_region(world, "Train Pass Region"), name="Menu To Train Pass",
                              rule=Has(PermanentUpgrades.TRAIN_PASS.value))
        world.create_entrance(menu, create_region(world, "Bayou Ticket Region"), name="Menu To Bayou Ticket",
                              rule=Has(PermanentUpgrades.BAYOU_TICKET.value))
        world.create_entrance(menu, create_region(world, "Septemburg Ticket Region"), name="Menu To Septemburg Ticket",
                              rule=Has(PermanentUpgrades.SEPTEMBURG_TICKET.value))
        world.create_entrance(menu, create_region(world, "Bone Beach Ticket Region"), name="Menu To Bone Beach Ticket",
                              rule=Has(PermanentUpgrades.BONE_BEACH_TICKET.value))
        world.create_entrance(menu, create_region(world, "Coltrane Peak Ticket Region"), name="Menu To Coltrane Peak Ticket",
                              rule=Has(PermanentUpgrades.COLTRANE_PEAK_TICKET.value))

        create_event_location(world, "Train Pass", EventData(None, "Train Pass Region", lambda _: False))
        create_event_location(world, "Bayou Ticket", EventData(None, "Bayou Ticket Region", lambda _: False))
        create_event_location(world, "Septemburg Ticket", EventData(None, "Septemburg Ticket Region", lambda _: False))
        create_event_location(world, "Bone Beach Ticket", EventData(None, "Bone Beach Ticket Region", lambda _: False))
        create_event_location(world, "Coltrane Peak Ticket", EventData(None, "Coltrane Peak Ticket Region", lambda _: False))

    return excluded_locations


def create_entrances(world: "MinaTheHollowerWorld"):
    entrance_sources = defaultdict(list)

    for data in all_region_transitions:
        entrance_sources[data.value].append(
            f"RegionTransitions.{data.name}"
        )

    for data in all_internal_region_connections:
        entrance_sources[data.value].append(
            f"RegionConnections.{data.name}"
        )

    for name, sources in entrance_sources.items():
        if len(sources) > 1:
            print(f"Duplicate entrance: {name}")
            for source in sources:
                print(f"    {source}")

    menu = world.get_region("Menu")
    if world.options.ossex_start.value:
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
