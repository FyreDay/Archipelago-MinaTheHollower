from copy import deepcopy
from typing import TYPE_CHECKING

from BaseClasses import Item, Location, ItemClassification, CollectionRule
from rule_builder.rules import True_, Rule
from worlds.mina_the_hollower.data.events.events import MirrorsEndSwitches
from . import repair_generator_data
from .data.events import all_generator_data
from .data.items.kears import kear_area_lookup
from .data.locations import Regions
from .data.locations.areas import backwaters
from .world_base import MinaTheHollowerBase
from .constants import MINA_THE_HOLLOWER, ITEMS_OFFSET_PROGRESSIVES
from .data import ItemData, ItemTypeEnum, ItemFiller
from .data.items import Kear, SingleKears, AreaKears, base_items, Abilities, BoneUps, GenericBoneUp, all_filler_items, \
    PermanentUpgrades, PlayerUpgrades, upgrade_items, Trinkets, BASE_ITEM_TOTAL, \
    valid_power_types, FilledJug, FillerUpgrades, all_starting_upgrades, Weapons, AstralPlatforms, all_trap_items

from .data.rules.state_rules import sidearm_rules
from .options import BoneUpCap, KearRandomization, Goal

if TYPE_CHECKING:
    from . import MinaTheHollowerWorld


class MinaTheHollowerItem(Item):
    game: str = MINA_THE_HOLLOWER


def create_item(world: "MinaTheHollowerWorld", item: ItemData):
    for i in range(item.amount):
        world.itempool.append(world.create_item(item.type.value))


def create_single_item(world: "MinaTheHollowerWorld", item_type: ItemTypeEnum):
    world.itempool.append(world.create_item(item_type.value))


def create_items(world: "MinaTheHollowerWorld"):

    all_items: list[ItemData] = []
    trinket_types = set(Trinkets)
    bone_cap_types = {*BoneUps, GenericBoneUp.ALL_BONE_UP_CAP}
    bone_cap_cap = 4 if world.options.bone_up_cap == BoneUpCap.option_perUpgrade else 2
    trinkets_selected = 0
    bags_selected = 0
    bone_caps_selected = 0

    for item in upgrade_items:
        for _ in range(item.amount):
            all_items.append(ItemData(item.type, 1))

    for item_type in PermanentUpgrades:
        all_items.append(ItemData(item_type, 1))
    for item_type in Trinkets:
        all_items.append(ItemData(item_type, 1))
    for item_type in PlayerUpgrades:
        all_items.append(ItemData(item_type, 1))


    if world.options.bone_up_cap == BoneUpCap.option_perUpgrade:
        for item_type in BoneUps:
            for _ in range(9):
                all_items.append(ItemData(item_type, 1))
    else:
        for _ in range(9):
            all_items.append(ItemData(GenericBoneUp.ALL_BONE_UP_CAP, 1))

    starting_items: list[Item] = [] if not world.is_ut else world.starting_items

    # starting items
    if world.options.random_starting_items:
        for item in base_items:
            for _ in range(item.amount):
                all_items.append(ItemData(item.type, 1))
        if world.is_ut:
            for item in starting_items:
                item_data = next(
                    (x for x in all_items if x.type.item_id == item.code),
                    None
                )

                if item_data is None:
                    continue

                item_data.amount -= 1

                if item_data.amount <= 0:
                    all_items.remove(item_data)
        else:
            for i in range(BASE_ITEM_TOTAL):
                if i < (BASE_ITEM_TOTAL * 2) // 3:
                    candidates = [
                        item
                        for item in all_items
                        if item.type in valid_power_types
                    ]
                    if bags_selected < 2:
                        candidates += [
                            item
                            for item in all_items
                            if item.type == PlayerUpgrades.TRINKET_BAG
                        ]
                else:
                    candidates = list(all_items)

                if trinkets_selected > bags_selected:
                    filtered = [
                        item
                        for item in candidates
                        if item.type not in trinket_types
                    ]
                    if filtered:
                        candidates = filtered

                if bone_caps_selected >= bone_cap_cap:
                    filtered = [
                        item
                        for item in candidates
                        if item.type not in bone_cap_types
                    ]
                    if filtered:
                        candidates = filtered

                item_data = world.random.choice(candidates)

                starting_items.append(world.create_item(item_data.type.value))

                if item_data.type == PlayerUpgrades.TRINKET_BAG:
                    bags_selected += 1
                elif item_data.type in trinket_types:
                    trinkets_selected += 1
                elif item_data.type in bone_cap_types:
                    bone_caps_selected += 1

                item_data.amount -= 1

                if item_data.type.value == PlayerUpgrades.TRINKET_BAG.value:
                    added_trinket_pouch = True

                if item_data.amount <= 0:
                    all_items.remove(item_data)

    else:
        for item in base_items:
            for i in range(item.amount):
                starting_items.append(world.create_item(item.type.value))
    for data in all_starting_upgrades:
        for _ in range(data.amount):
            starting_items.append(world.create_item(data.type.value))

    for item_type in Abilities:
        if item_type.value in world.options.ability_rando.value:
            create_single_item(world, item_type)
        else:
            starting_items.append(world.create_item(item_type.value))

    starting_weapon = Weapons.from_item_id(ITEMS_OFFSET_PROGRESSIVES + world.options.starting_weapon.value)
    starting_items.append(world.create_item(starting_weapon.value))
    for weapon in Weapons:
        create_item(world, ItemData(weapon, 2 if starting_weapon == weapon else 3))

    for item in all_items:
        create_item(world, item)

    if world.options.kear_rando == KearRandomization.option_vanilla:
        create_item(world, ItemData(Kear.UNIVERSAL_KEAR, 42))
    if world.options.kear_rando == KearRandomization.option_vanilla:
        for i in range(8):
            world.itempool.append(MinaTheHollowerItem(
            Kear.UNIVERSAL_KEAR.value,
            ItemClassification.useful,
            Kear.UNIVERSAL_KEAR.item_id,
            world.player,
        ))
    elif world.options.kear_rando == KearRandomization.option_apItems:
        excluded_kears = [data.kear_item_type for data in all_generator_data if data.index in world.lit_generators]
        for item_type in SingleKears:
            if kear_area_lookup[item_type.value] in excluded_kears:
                starting_items.append(world.create_item(item_type.value))
                continue
            create_single_item(world, item_type)
    elif world.options.kear_rando.value == 2:# world.options.kear_rando.option_areaApItems:
        for item_type in AreaKears:
            excluded_kears = [data.kear_item_type for data in all_generator_data if data.index in world.lit_generators]
            if item_type in excluded_kears:
                starting_items.append(world.create_item(item_type.value))
                continue
            create_single_item(world, item_type)

    if world.options.astral_switches.value:
        for astral_switch in AstralPlatforms:
            create_single_item(world, astral_switch)

    total_location_count = len(world.multiworld.get_unfilled_locations(world.player))

    # print(f"total locs at start {total_location_count}")
    # print(f"total Itempool at start {len(world.itempool)}")
    _remaining = total_location_count - len(world.itempool)
    trap_count = round(_remaining * world.options.trap_percent.value / 100) if world.options.trap_percent.value > 0 else 0

    junk_count = _remaining - trap_count
    if world.options.bone_up_cap == BoneUpCap.option_perUpgrade:
        for item_type in BoneUps:
            for _ in range(world.options.max_stat_level.value-10):
                create_item(world, ItemData(item_type, 1))
                junk_count -= 1
                if junk_count <= 20:
                    break
            if junk_count <= 20:
                break
    else:
        if world.options.max_stat_level.value > 10:
            for _ in range(world.options.max_stat_level.value-10):
                create_item(world, ItemData(GenericBoneUp.ALL_BONE_UP_CAP, 1))
                junk_count -= 1
                if junk_count <= 20:
                    break
    my_trap_items = []
    if trap_count > 0:
        my_trap_items = [
            trap for trap in all_trap_items
            if trap.type.value not in world.options.disabled_traps
        ]
        if len(my_trap_items) <= 0:
            junk_count += trap_count
            trap_count = 0

    filler: list[ItemFiller] = world.random.choices(
        all_filler_items,
        weights=[item.weight for item in all_filler_items],
        k=junk_count
    )
    for item_filler in filler:
        create_single_item(world, item_filler.type)

    if trap_count > 0:
        traps: list[ItemFiller] = world.random.choices(
            my_trap_items,
            weights=[item.weight for item in my_trap_items],
            k=trap_count
        )
        for trap_filler in traps:
            create_single_item(world, trap_filler.type)

    world.multiworld.itempool += world.itempool

    return starting_items


def create_event(world: "MinaTheHollowerWorld", region_name: str, item_name: str, loc_name: str | None = None,
                 rule: CollectionRule | Rule[MinaTheHollowerBase] = True_()) -> None:
    if loc_name is None:
        loc_name = "Event " + item_name
    region = world.get_region(region_name)
    event_loc = Location(world.player, loc_name, None, region)
    world.set_rule(event_loc, rule)
    event_loc.place_locked_item(
        MinaTheHollowerItem(item_name, ItemClassification.progression, None, world.player))
    region.locations.append(event_loc)

def create_events(world: "MinaTheHollowerWorld"):

    plasma_jug_loc = world.get_location(backwaters.BossLocations.BW_DEFEAT_BUFFO_THE_FROG.value)
    plasma_jug_loc.place_locked_item(MinaTheHollowerItem(FilledJug.PLASMA_JUG.value, ItemClassification.useful, FilledJug.PLASMA_JUG.item_id, world.player))

    for itemShortcut in sidearm_rules:
        create_event(world, Regions.OSSEX_CITY_CENTER_MAIN.value, itemShortcut.type.value, rule=itemShortcut.access_rule)
        # starting_items.append(Item(item_type.value, item_type.classification, item_type.item_id, world.player))

    for data in repair_generator_data:
        create_event(world, region_name=data.type.region, item_name=data.type.event_item,
                     loc_name=data.type.value, rule=data.type.rule)
    if not world.options.astral_switches.value:
        for astral_switch in MirrorsEndSwitches:
            create_event(world, region_name=astral_switch.region, item_name=astral_switch.event_item,
                         loc_name=astral_switch.value, rule=astral_switch.rule)

    if world.options.goal.value == Goal.option_radiantManorGenerator:
        create_event(world, region_name="Radiant Manor Prime Generator",
                     item_name="Victory", loc_name="Defeat Giga Lionel")