from BaseClasses import LocationProgressType
from rule_builder.options import OptionFilter
from rule_builder.rules import Has, True_
from .._generated.regions import Regions
from ... import TransitionType, DirectionType, LocationTypeEnum
from ...items import Wallets
from ...rules.ability_rules import CanBurrow, CanBounce, HasVialsCount, CanClimb, CanCarry, HasFishingRod
from ...rules.state_rules import RepairedGeneratorCount
from ...rules.movement_rules import CanJumpTiles

class Locations(LocationTypeEnum):
    SO_COMMONS_OSSEX_ENTRY_WALL_LEFT_CHEST = (
        "SO Commons Ossex Entry Wall Left Chest",270,Regions.OSSEX_ENTRY_WESTERN_WALL_CHEST,CanJumpTiles(distance=5, has_wall=True),
    )

    SO_COMMONS_OSSEX_ENTRY_WALL_RIGHT_CHEST = (
        "SO Commons Ossex Entry Wall Right Chest",266,Regions.OSSEX_ENTRY_EASTERN_WALL_CHEST,
    )

    SO_COMMONS_BOUNCE_CHEST = (
        "SO Commons Bounce Chest",264,Regions.SOUTHERN_OUTSKIRTS_COMMONS_MAIN,CanBurrow() & CanBounce(),
    )

    SO_FISH_CRUMBLEFIN_HEAD = (
        "SO Fish Crumblefin Head",274,Regions.SOUTHERN_OUTSKIRTS_COMMONS_MAIN,HasFishingRod() & CanCarry(),
    )

    SO_CAVE_NETWORK_CHEST = (
        "SO Cave Network Chest",265,Regions.SOUTHERN_OUTSKIRTS_CAVE_NETWORK_DEEP_EXIT,
    )

    SO_CAVE_NETWORK_SIDE_ROOM_CHEST = (
        "SO Cave Network Side Room Chest",268,Regions.SOUTHERN_OUTSKIRTS_CAVE_DEEP_ARENA,
    )

    SO_POPPIT_KERI = (
        "SO Poppit Keri",272,Regions.SOUTHERN_OUTSKIRTS_POPPIT,
    )

    SO_POPPIT_KEAR = (
        "SO Poppit Kear",273,Regions.SOUTHERN_OUTSKIRTS_POPPIT,
    )

    SO_PIT_ROOM_BONESTONE = (
        "SO Pit Room Bonestone",261,Regions.SOUTHERN_OUTSKIRTS_COMMONS_SOUTHERN_PIT_ROOM_MAIN,CanJumpTiles(distance=5, has_wall=True) & CanBurrow(),
    )

    SO_WESTERN_WILDS_ENTRANCE_CHEST = (
        "SO Western Wilds Entrance Chest",267,Regions.SOUTHERN_OUTSKIRTS_COMMONS_WESTERN_PIT_ROOM_MAIN
    )

    SO_THORNE_RESIDENCE_BASEMENT_TRINKET = (
        "SO Thorne Residence Basement Trinket",269,Regions.SOUTHERN_OUTSKIRTS_RESIDENCE_BASEMENT
    )

    SO_MINING_PASSAGE_CHEST = (
        "SO Mining Passage Chest",331,Regions.SOUTHERN_OUTSKIRTS_MINING_PASSAGE_SECRET,CanBurrow() & CanBounce() & HasVialsCount(count=2),
    )

    DUGIN_FIGHT_2_TRINKET = (
        "Dugin Fight 2 Trinket",263,Regions.SOUTHERN_OUTSKIRTS_MOONBATH,RepairedGeneratorCount(count=2),
    )

    SO_FOUR_FLOWERS_CHEST = (
        "SO Four Flowers Chest",271,Regions.SOUTHERN_OUTSKIRTS_FOUR_FLOWERS_SHORTCUT,CanBounce(),
    )
class BossLocations(LocationTypeEnum):
    SO_DEFEAT_DUGIN_2 = ("Defeat Dugin 2", 1016, Regions.SOUTHERN_OUTSKIRTS_MOONBATH,RepairedGeneratorCount(count=2))
