from BaseClasses import LocationProgressType
from rule_builder.options import OptionFilter
from rule_builder.rules import Has, True_
from .._generated.regions import Regions
from ... import LocationTypeEnum
from ...items import SingleKears, Trinkets, Wallets, PermanentUpgrades
from ...rules.ability_rules import CanBurrow, CanBounce, CanCarry, HasFishingRod, CanClimb, HasTrinket
from ...rules.state_rules import HasKear
from ...rules.movement_rules import CanJumpTiles

class Locations(LocationTypeEnum):
    WW_SECRET_PASSAGE_CHEST = (
        "WW Secret Passage Chest",251,Regions.WESTERN_WILDS_SECRET_PASSAGEWAY_EAST,CanJumpTiles(distance=3)
    )

    WW_SECRET_PASSAGE_LOCKED_CHEST = (
        "WW Secret Passage Locked Chest",248,Regions.WESTERN_WILDS_SECRET_PASSAGEWAY_EAST,CanJumpTiles(distance=5, has_wall=True)
        & HasKear(kear=SingleKears.WESTERN_WILDS_SECRET_PASSAGE_KEAR.value),
    )

    WW_BRUTE_CHEST = (
        "WW Brute Chest",253,Regions.WESTERN_WILDS_BRUTES,
    )

    WW_LEAF_AREA_CHEST = (
        "WW Leaf Area Chest",250,Regions.WESTERN_WILDS_END,CanBurrow(),
    )

    WW_LEAF_AREA_TRINKET = (
        "WW Leaf Area Trinket",245,Regions.WESTERN_WILDS_BRUTES,(CanBurrow() & CanCarry())
        | (
            CanBurrow()
            & Has(PermanentUpgrades.TRAIN_PASS.value)
            & Has(PermanentUpgrades.SEPTEMBURG_TICKET.value)
        ),
    )  # needs kill the other leaf,

    WW_FISH_CUDDLEPUS_SHELL = (
        "WW Fish Cuddlepus Shell",259,Regions.WESTERN_WILDS_MAIN,HasFishingRod(),
    )

    WW_OCCUPIED_BRIDGE_UNDERNEATH_CHEST = (
        "WW Occupied Bridge Underneath Chest",252,Regions.WESTERN_WILDS_FOUNDRY_PATH,
    )

    WW_MOLTEN_FOUNDRY_POPPIT_TRINKET = (
        "WW Molten Foundry Poppit Trinket",256,Regions.WESTERN_WILDS_MOLTEN_FOUNDRY_DARK_POPPIT,
    )

    WW_MOLTEN_FOUNDRY_POPPIT_KEAR = (
        "WW Molten Foundry Poppit Kear",257,Regions.WESTERN_WILDS_MOLTEN_FOUNDRY_DARK_POPPIT,
    )

    WW_MOLTEN_FOUNDRY_DARK_CHEST = (
        "WW Molten Foundry Dark Chest",255,Regions.WESTERN_WILDS_MOLTEN_FOUNDRY_DARK,CanBurrow() | HasTrinket(trinket=Trinkets.POLYP_LAMP.value),
    )

    WW_MOLTEN_FOUNDRY_TRINKET = (
        "WW Molten Foundry Trinket",249,Regions.WESTERN_WILDS_MOLTEN_DUNGEON_END,
    )

    WW_FISH_GLOMPER_STALK = (
        "WW Fish Glomper Stalk",258,Regions.WESTERN_WILDS_WESTERN_POND,HasFishingRod(),
    )

    WW_BALCONY_CHEST = (
        "WW Balcony Chest",254,Regions.WESTERN_WILDS_BALCONY,HasKear(kear=SingleKears.WESTERN_WILDS_BALCONY_KEAR.value),
    )
