from BaseClasses import LocationProgressType
from rule_builder.options import OptionFilter
from rule_builder.rules import Has, True_
from .._generated.regions import Regions
from ... import LocationTypeEnum
from ...items import Trinkets, SingleKears, Sidearms, FishingUpgrades, Wallets
from ...rules.ability_rules import CanBurrow, CanBounce, CanSwim, CanCarry, CanClimb, \
    HasFishingRod, PowerLevelThreshold, HasTrinket
from ...rules.state_rules import HasLadder, HasKear, RepairedGeneratorCount
from ...rules.movement_rules import CanJumpTiles

class Locations(LocationTypeEnum):
    BW_BUFFO_THE_FROG_GIFT = (
        "BW Buffo The Frog Gift", 289, Regions.BACKWATERS_UPPER_SWAMP_WATERFALL,
    )

    BW_SIDE_ROOM_CHEST = (
        "BW Side Room Chest", 296, Regions.BACKWATERS_UPPER_SWAMP_SECRET_ROOM,
        CanSwim() & (
            (
                CanJumpTiles(distance=2, no_sidearms=True)
                | CanJumpTiles(distance=4, has_wall=True)
                | CanBurrow()
            )
            | (CanBurrow() & HasTrinket(trinket=Trinkets.WALLOWERS_GAUNTLETS.value))
        ),
    )

    BW_LANTERN_CAVE_BONESTONE = (
        "BW Lantern Cave Bonestone", 287, Regions.BACKWATERS_UPPER_LANTERN_CAVE,
    )

    BW_LANTERN_CAVE_VIAL_POUCH = (
        "BW Lantern Cave Vial Pouch", 295, Regions.BACKWATERS_UPPER_LANTERN_CAVE,
    )

    BW_PINKYS_PARLOR_TRINKET = (
        "BW Pinky's Parlor Trinket", 297, Regions.BACKWATERS_PINKY_SHOP,
    )

    BW_PINKYS_PARLOR_KEAR = (
        "BW Pinky's Parlor Kear", 298, Regions.BACKWATERS_PINKY_SHOP,
    )

    BW_PINKYS_PARLOR_JOULE_BOX = (
        "BW Pinky's Parlor Joule Box", 286, Regions.BACKWATERS_PINKY_SHOP_BACK, HasLadder(),
    )

    BW_FISHING_HOLE_ENTRANCE_LOCKED_CHEST = (
        "BW Fishing Hole Entrance Locked Chest", 293, Regions.BACKWATERS_LOWER_SWAMP_FISHING, HasKear(kear=SingleKears.BACKWATERS_FISHING_KEAR.value)
        & (CanSwim() | CanJumpTiles(distance=4)),
    )

    BW_LADDER_TRINKET = (
        "BW Ladder Trinket", 294, Regions.BACKWATERS_LOWER_SWAMP_STATION_ENTRANCE, HasLadder(),
    )

    BW_LADDER_BONESTONE = (
        "BW Ladder Bonestone", 288, Regions.BACKWATERS_LOWER_SWAMP_STATION_ENTRANCE, HasLadder(),
    )

    BW_RESCUE_CLIFF_BAND_REWARD = (
        "BW Rescue Cliff Band Reward", 291, Regions.BACKWATERS_LOWER_SWAMP_SHANTY_BAND, CanCarry() & CanBurrow() & CanSwim() & CanClimb(),
    )

    BW_LUCKY_S_LAIR_GIFT = (
        "BW Lucky's Lair Gift", 292, Regions.BACKWATERS_LUCKYS_LAIR, CanBurrow() & CanCarry(),
    )

    BW_FISHING_HOLE_FISHING_ROD = (
        "BW Fishing Hole Fishing Rod", 300, Regions.BACKWATERS_FISHING_HOLE,
    )

    BW_FISH_FLEEPER_HEAD = (
        "BW Fish Fleeper Head", 299, Regions.BACKWATERS_FISHING_HOLE, HasFishingRod(),
    )

    BW_FISHING_HOLE_THALASSIAN_PEARL = (
        "BW Fishing Hole Thalassian Pearl", 302, Regions.BACKWATERS_FISHING_HOLE, PowerLevelThreshold(power=40)
        & HasFishingRod()
        & CanSwim()
        & (
            HasTrinket(trinket=Trinkets.TUNNELING_CODEX.value)
            | Has(FishingUpgrades.FISHING_ROD.value, count=2)
        ),
    )

    BW_FISHING_HOLE_GILDED_ROD = (
        "BW Fishing Hole Gilded Rod", 301, Regions.BACKWATERS_FISHING_HOLE, RepairedGeneratorCount(count=6)
        & HasFishingRod()
        & CanSwim()
        & (
            HasTrinket(trinket=Trinkets.TUNNELING_CODEX.value)
            | Has(FishingUpgrades.FISHING_ROD.value, count=2)
        ),
    )

class BossLocations(LocationTypeEnum):
    BW_DEFEAT_BUFFO_THE_FROG = ("BW Buffo The Frog Fight Plasma Jug", 290, Regions.BACKWATERS_UPPER_SWAMP_WATERFALL, HasTrinket(trinket=Trinkets.EMPTY_JUG.value) & PowerLevelThreshold(power=24))

