from rule_builder.rules import Has
from worlds.mina_the_hollower import CanJumpTiles
from .._generated.regions import Regions
from ... import  LocationTypeEnum
from ...items import SingleKears, AstralPlatforms
from ...rules.ability_rules import CanBurrow, HasFishingRod, CanCarry
from ...rules.state_rules import HasKear

class Locations(LocationTypeEnum):
    AO_MIRROR_S_END_RED_SWITCH_CHEST = (
        "AO Mirror's End Red Switch Chest", 281, Regions.ASTRAL_ORRERY_MIRRORS_END, Has(AstralPlatforms.RED_ASTRAL_PLATFORMS.value) & CanBurrow(),
    )

    AO_MIRROR_S_END_DR_NAUGHT_REWARD = (
        "AO Mirror's End Dr. Naught Reward", 276, Regions.ASTRAL_ORRERY_MIRRORS_END, CanJumpTiles(distance=3)
        & CanCarry()
        & HasKear(
            kear=SingleKears.ASTRAL_ORREY_MIRROR_ROOM_RIGHT_SIDE_KEAR.value
        )
    )

    AO_MIRROR_S_END_LOCKED_TRINKET_BAG = (
        "AO Mirror's End Locked Trinket Bag", 279, Regions.ASTRAL_ORRERY_MIRRORS_END, HasKear(
            kear=SingleKears.ASTRAL_ORREY_MIRROR_ROOM_LEFT_SIDE_KEAR.value
        )
        & (
            (
                CanBurrow()
                & Has(AstralPlatforms.YELLOW_ASTRAL_PLATFORMS.value)
            )
            | (
                (
                    Has(AstralPlatforms.RED_ASTRAL_PLATFORMS.value)
                    | Has(AstralPlatforms.GREEN_ASTRAL_PLATFORMS.value)
                    | Has(AstralPlatforms.BLUE_ASTRAL_PLATFORMS.value)
                )
                & CanJumpTiles(distance=4)
            )
        ),
    )

    AO_MIRROR_S_END_FISH_TRUNKSTAR_CORE = (
        "AO Mirror's End Fish Trunkstar Core", 282, Regions.ASTRAL_ORRERY_MIRRORS_END, HasFishingRod(),
    )

    AO_MIRROR_S_END_BLUE_SWITCH_PATH_CHEST = (
        "AO Mirror's End Blue Switch Path Chest", 280, Regions.ASTRAL_ORRERY_MIRRORS_END_BLUE_CHEST,
    )