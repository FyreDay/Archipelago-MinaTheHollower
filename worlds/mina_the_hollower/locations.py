from BaseClasses import Region, Location, ItemClassification, LocationProgressType
from rule_builder.rules import Has
from .data.events import RADIANT_MANOR_DATA
from .data.items import BoneFiller, Abilities, PermanentUpgrades
from .data.locations import all_regions, all_region_transitions, all_internal_region_connections, \
    all_permanent_locations, dungeon_locations
from .data import LocationData, RegionConnection, Transition, matching_transition_types
from typing import TYPE_CHECKING
from .items import MinaTheHollowerItem

if TYPE_CHECKING:
    from . import MinaTheHollowerWorld


def create_location(world, name: str, data: LocationData, bonestone: bool = False):
    region = world.get_region(data.region)
    location = Location(world.player, name, data.location_id, region)
    location.progress_type = LocationProgressType.EXCLUDED if bonestone else data.progress_type
    location.item_rule = data.item_rule
    if bonestone:
        item = MinaTheHollowerItem(BoneFiller.TREASURE_SMALLEST.value, ItemClassification.filler, BoneFiller.TREASURE_SMALLEST.item_id, world.player)
        location.place_locked_item(item)
    region.locations.append(location)
    world.set_rule(location, data.rule)

def create_region(world: "MinaTheHollowerWorld", name: str, hint: str = ""):
    region = Region(name, world.player, world.multiworld)
    valid_locations: dict[str, (Location, LocationData)] = {}
    # TODO: dont loop through all locations for each region
    for loc_name, data in all_permanent_locations.items():
        if loc_name == "LL Captain's Gift" and world.options.ossex_start:
            continue
        if data.region != name:
            continue
        location = Location(world.player, loc_name, data.location_id, region)
        location.progress_type = data.progress_type
        location.item_rule = data.item_rule
        valid_locations[loc_name] = (location, data)
        region.locations.append(location)

    world.multiworld.regions.append(region)

    for loc_name, (location, data) in valid_locations.items():
        world.set_rule(location, data.rule)

    return region

def create_regions(world: "MinaTheHollowerWorld", regions: set[str]):
    # TODO: check if regions being a set introduces nondeterminism
    menu = create_region(world, "Menu")
    excluded_locations: list[int] = []
    for region in regions:
        create_region(world, region)
    for index, loc_map in dungeon_locations.items():
        for name, data in loc_map.items():
            override = index == RADIANT_MANOR_DATA.index and world.options.goal.value == world.options.goal.option_fixGenerators
            if (index in world.lit_generators) or override:
                excluded_locations.append(data.location_id)
            else:
                create_location(world, name, data)
    if world.is_ut:
        world.create_entrance(menu, create_region(world, "Burrow Region"), name="Menu To Burrow", rule=Has(Abilities.BURROW.value))
        world.create_entrance(menu, create_region(world, "Swim Region"), name="Menu To Swim", rule=Has(Abilities.SWIM.value))
        world.create_entrance(menu, create_region(world, "Carry Region"), name="Menu To Carry", rule=Has(Abilities.CARRY.value))
        world.create_entrance(menu, create_region(world, "Climb Region"), name="Menu To Climb", rule=Has(Abilities.CLIMB.value))
        world.create_entrance(menu, create_region(world, "Bounce Region"), name="Menu To Bounce", rule=Has(Abilities.BOUNCE.value))
        world.create_entrance(menu, create_region(world, "Spring Region"), name="Menu To Spring", rule=Has(Abilities.SPRING.value))

        create_location(world, "Burrow", LocationData(None, "Burrow Region", lambda _: False))
        create_location(world, "Swim", LocationData(None, "Swim Region", lambda _: False))
        create_location(world, "Carry", LocationData(None, "Carry Region", lambda _: False))
        create_location(world, "Climb", LocationData(None, "Climb Region", lambda _: False))
        create_location(world, "Bounce", LocationData(None, "Bounce Region", lambda _: False))
        create_location(world, "Spring", LocationData(None, "Spring Region", lambda _: False))

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

        create_location(world, "Train Pass", LocationData(None, "Train Pass Region", lambda _: False))
        create_location(world, "Bayou Ticket", LocationData(None, "Bayou Ticket Region", lambda _: False))
        create_location(world, "Septemburg Ticket", LocationData(None, "Septemburg Ticket Region", lambda _: False))
        create_location(world, "Bone Beach Ticket", LocationData(None, "Bone Beach Ticket Region", lambda _: False))
        create_location(world, "Coltrane Peak Ticket", LocationData(None, "Coltrane Peak Ticket Region", lambda _: False))

    return excluded_locations





def get_regions(world: "MinaTheHollowerWorld") -> set[str]:
    # TODO: logic to handle which regions are being created based on yaml
    return all_regions


def create_entrances(world: "MinaTheHollowerWorld", regions):
    menu = world.get_region("Menu")
    if world.options.ossex_start.value:
        world.create_entrance(menu, world.get_region("Ossex City Center Main"), name="Menu To Ossex")
    world.create_entrance(menu, world.get_region("Loner's Landing Shipwreck"), name="Menu To Shipwreck")
    for name, data in all_region_transitions.items():
        exiting_region = world.get_region(data.exiting_screen)
        entering_region = world.get_region(data.entering_screen)
        entrance = world.create_entrance(exiting_region, entering_region, rule=data.rule, name=name, force_creation=True)
        if data.entrance_group != 0 and world.entrance_rando:
            entrance.randomization_group = data.entrance_group
            world.disconnect_entrance_for_randomization(entrance)
    for name, data in all_internal_region_connections.items():
        exiting_region = world.get_region(data.exiting_region)
        entering_region = world.get_region(data.entering_region)
        entrance = world.create_entrance(exiting_region, entering_region, rule=data.rule, name=name,
                                         force_creation=True)
