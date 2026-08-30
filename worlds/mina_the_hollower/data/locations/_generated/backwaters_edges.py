# AUTO-GENERATED -- DO NOT EDIT.
# Regenerate from the spreadsheet export with:
#   python -m worlds.mina_the_hollower.tools.generate_edges <edges.csv>
# The spreadsheet is the source of truth, not this file.

from .regions import Regions
from rule_builder.rules import Has, True_, CanReachLocation
from ... import DirectionType, TransitionType, ConnectionTypeEnum, TransitionTypeEnum
from ...rules.ability_rules import (
    CanBurrow, CanCarry, CanClimb, CanSwim, CanBounce, PowerLevelThreshold,
    HasVialsCount, HasReachingSideArm, HasFishingRod, CanSpring, HasTrinket 
)
from ...rules.movement_rules import (
    CanJumpTiles, 
)
from ...rules.state_rules import (
   HasLadder, HasAccessToTorch, StartedInOssex, 
   AnyThreeAstralPlatforms, HasKear, HasSparks, 
   RepairedGenerator, RepairedGeneratorCount, IsGeneratorRequired, 
)
from ...events import (
   QUEENSBURY_CRYPT_DATA, NOXS_BAYOU_DATA, SEPTEMBURG_DATA, 
   BONE_BEACH_DATA, COLTRANE_PEAK_DATA, ASTRAL_ORRERY_DATA, 
)
from ...items.game_items import (
   PermanentUpgrades, PlayerUpgrades, Trinkets, Sidearms
)
from ...items.kears import (
   SingleKears,
)
from ...items.blockers import (
   AstralPlatforms,
)
from ....constants import *

class RegionConnections(ConnectionTypeEnum):
    BACKWATERS_BAYOU_FALLS_EAST_BACKWATERS_BAYOU_FALLS_WEST = ('Backwaters Bayou Falls East_Backwaters Bayou Falls West', Regions.BACKWATERS_BAYOU_FALLS_EAST, Regions.BACKWATERS_BAYOU_FALLS_WEST, CanSwim())
    BACKWATERS_BAYOU_FALLS_WEST_BACKWATERS_BAYOU_FALLS_EAST = ('Backwaters Bayou Falls West_Backwaters Bayou Falls East', Regions.BACKWATERS_BAYOU_FALLS_WEST, Regions.BACKWATERS_BAYOU_FALLS_EAST, CanJumpTiles(distance=2, over_water=True) | CanSwim())
    BACKWATERS_LOWER_SWAMP_BAYOU_ENTRANCE_BACKWATERS_LOWER_SWAMP_SHANTY_BAND = ('Backwaters Lower Swamp Bayou Entrance_Backwaters Lower Swamp Shanty Band', Regions.BACKWATERS_LOWER_SWAMP_BAYOU_ENTRANCE, Regions.BACKWATERS_LOWER_SWAMP_SHANTY_BAND, True_())
    BACKWATERS_LOWER_SWAMP_FISHING_BACKWATERS_LOWER_SWAMP = ('Backwaters Lower Swamp Fishing_Backwaters Lower Swamp', Regions.BACKWATERS_LOWER_SWAMP_FISHING, Regions.BACKWATERS_LOWER_SWAMP, CanJumpTiles(distance=5, over_water=True) | HasKear(kear=SingleKears.BACKWATERS_FISHING_KEAR.value))
    BACKWATERS_LOWER_SWAMP_SHANTY_BAND_BACKWATERS_LOWER_SWAMP = ('Backwaters Lower Swamp Shanty Band_Backwaters Lower Swamp', Regions.BACKWATERS_LOWER_SWAMP_SHANTY_BAND, Regions.BACKWATERS_LOWER_SWAMP, CanSwim())
    BACKWATERS_LOWER_SWAMP_SHANTY_BAND_BACKWATERS_LOWER_SWAMP_BAYOU_ENTRANCE = ('Backwaters Lower Swamp Shanty Band_Backwaters Lower Swamp Bayou Entrance', Regions.BACKWATERS_LOWER_SWAMP_SHANTY_BAND, Regions.BACKWATERS_LOWER_SWAMP_BAYOU_ENTRANCE, CanJumpTiles(distance=4, over_water=True) | CanSwim())
    BACKWATERS_LOWER_SWAMP_STATION_ENTRANCE_BACKWATERS_LOWER_SWAMP = ('Backwaters Lower Swamp Station Entrance_Backwaters Lower Swamp', Regions.BACKWATERS_LOWER_SWAMP_STATION_ENTRANCE, Regions.BACKWATERS_LOWER_SWAMP, CanJumpTiles(distance=2, over_water=True) | CanSwim())
    BACKWATERS_LOWER_SWAMP_STATION_ENTRANCE_BACKWATERS_LOWER_SWAMP_BAYOU_ENTRANCE = ('Backwaters Lower Swamp Station Entrance_Backwaters Lower Swamp Bayou Entrance', Regions.BACKWATERS_LOWER_SWAMP_STATION_ENTRANCE, Regions.BACKWATERS_LOWER_SWAMP_BAYOU_ENTRANCE, CanBurrow() | CanSwim())
    BACKWATERS_LOWER_SWAMP_BACKWATERS_LOWER_SWAMP_BAYOU_ENTRANCE = ('Backwaters Lower Swamp_Backwaters Lower Swamp Bayou Entrance', Regions.BACKWATERS_LOWER_SWAMP, Regions.BACKWATERS_LOWER_SWAMP_BAYOU_ENTRANCE, CanSwim())
    BACKWATERS_LOWER_SWAMP_BACKWATERS_LOWER_SWAMP_FISHING = ('Backwaters Lower Swamp_Backwaters Lower Swamp Fishing', Regions.BACKWATERS_LOWER_SWAMP, Regions.BACKWATERS_LOWER_SWAMP_FISHING, CanJumpTiles(distance=5, over_water=True) | HasKear(kear=SingleKears.BACKWATERS_FISHING_KEAR.value))
    BACKWATERS_LOWER_SWAMP_BACKWATERS_LOWER_SWAMP_SHANTY_BAND = ('Backwaters Lower Swamp_Backwaters Lower Swamp Shanty Band', Regions.BACKWATERS_LOWER_SWAMP, Regions.BACKWATERS_LOWER_SWAMP_SHANTY_BAND, CanSwim())
    BACKWATERS_LOWER_SWAMP_BACKWATERS_LOWER_SWAMP_STATION_ENTRANCE = ('Backwaters Lower Swamp_Backwaters Lower Swamp Station Entrance', Regions.BACKWATERS_LOWER_SWAMP, Regions.BACKWATERS_LOWER_SWAMP_STATION_ENTRANCE, CanJumpTiles(distance=2, over_water=True) | CanSwim())
    BACKWATERS_PINKY_BACK_POND_BOARD_BACKWATERS_PINKY_BACK_POND_LAWN = ('Backwaters Pinky Back Pond Board_Backwaters Pinky Back Pond Lawn', Regions.BACKWATERS_PINKY_BACK_POND_BOARD, Regions.BACKWATERS_PINKY_BACK_POND_LAWN, CanJumpTiles(distance=3, has_wall=True, over_water=True) | CanSwim())
    BACKWATERS_PINKY_BACK_POND_LAWN_BACKWATERS_PINKY_BACK_POND_BOARD = ('Backwaters Pinky Back Pond Lawn_Backwaters Pinky Back Pond Board', Regions.BACKWATERS_PINKY_BACK_POND_LAWN, Regions.BACKWATERS_PINKY_BACK_POND_BOARD, CanJumpTiles(distance=3, has_wall=True, over_water=True) | CanSwim())
    BACKWATERS_PINKY_FRONT_LAWN_EAST_BACKWATERS_PINKY_FRONT_LAWN_WEST = ('Backwaters Pinky Front Lawn East_Backwaters Pinky Front Lawn West', Regions.BACKWATERS_PINKY_FRONT_LAWN_EAST, Regions.BACKWATERS_PINKY_FRONT_LAWN_WEST, CanBurrow())
    BACKWATERS_PINKY_FRONT_LAWN_WEST_BACKWATERS_PINKY_FRONT_LAWN_EAST = ('Backwaters Pinky Front Lawn West_Backwaters Pinky Front Lawn East', Regions.BACKWATERS_PINKY_FRONT_LAWN_WEST, Regions.BACKWATERS_PINKY_FRONT_LAWN_EAST, CanBurrow())
    BACKWATERS_PINKY_SHOP_BACK_BACKWATERS_PINKY_SHOP = ('Backwaters Pinky Shop Back_Backwaters Pinky Shop', Regions.BACKWATERS_PINKY_SHOP_BACK, Regions.BACKWATERS_PINKY_SHOP, True_())
    BACKWATERS_THALESSIAN_WAY_LOWER_BACKWATERS_THALESSIAN_WAY_UPPER = ('Backwaters Thalessian Way Lower_Backwaters Thalessian Way Upper', Regions.BACKWATERS_THALESSIAN_WAY_LOWER, Regions.BACKWATERS_THALESSIAN_WAY_UPPER, HasFishingRod() & HasReachingSideArm())
    BACKWATERS_THALESSIAN_WAY_UPPER_BACKWATERS_THALESSIAN_WAY_LOWER = ('Backwaters Thalessian Way Upper_Backwaters Thalessian Way Lower', Regions.BACKWATERS_THALESSIAN_WAY_UPPER, Regions.BACKWATERS_THALESSIAN_WAY_LOWER, True_())
    BACKWATERS_UPPER_LANTERN_PAD_BACKWATERS_UPPER_SWAMP_EAST = ('Backwaters Upper Lantern Pad_Backwaters Upper Swamp East', Regions.BACKWATERS_UPPER_LANTERN_PAD, Regions.BACKWATERS_UPPER_SWAMP_EAST, CanJumpTiles(distance=3, over_water=True) | CanSwim())
    BACKWATERS_UPPER_LANTERN_PAD_BACKWATERS_UPPER_SWAMP_ENTRANCE_EXIT = ('Backwaters Upper Lantern Pad_Backwaters Upper Swamp Entrance Exit', Regions.BACKWATERS_UPPER_LANTERN_PAD, Regions.BACKWATERS_UPPER_SWAMP_ENTRANCE_EXIT, CanBurrow())
    BACKWATERS_UPPER_SWAMP_BACK_BACKWATERS_UPPER_SWAMP_ENTRANCE = ('Backwaters Upper Swamp Back_Backwaters Upper Swamp Entrance', Regions.BACKWATERS_UPPER_SWAMP_BACK, Regions.BACKWATERS_UPPER_SWAMP_ENTRANCE, CanJumpTiles(distance=2, over_water=True))
    BACKWATERS_UPPER_SWAMP_BACK_BACKWATERS_UPPER_SWAMP_FENCED = ('Backwaters Upper Swamp Back_Backwaters Upper Swamp Fenced', Regions.BACKWATERS_UPPER_SWAMP_BACK, Regions.BACKWATERS_UPPER_SWAMP_FENCED, CanJumpTiles(distance=4, has_wall=True, over_water=True) | CanSwim())
    BACKWATERS_UPPER_SWAMP_EAST_BACKWATERS_UPPER_LANTERN_PAD = ('Backwaters Upper Swamp East_Backwaters Upper Lantern Pad', Regions.BACKWATERS_UPPER_SWAMP_EAST, Regions.BACKWATERS_UPPER_LANTERN_PAD, CanJumpTiles(distance=3, over_water=True) | CanSwim())
    BACKWATERS_UPPER_SWAMP_EAST_BACKWATERS_UPPER_SWAMP_LILY = ('Backwaters Upper Swamp East_Backwaters Upper Swamp Lily', Regions.BACKWATERS_UPPER_SWAMP_EAST, Regions.BACKWATERS_UPPER_SWAMP_LILY, CanJumpTiles(distance=2, over_water=True) | CanSwim())
    BACKWATERS_UPPER_SWAMP_ENTRANCE_EXIT_BACKWATERS_UPPER_SWAMP_ENTRANCE = ('Backwaters Upper Swamp Entrance Exit_Backwaters Upper Swamp Entrance', Regions.BACKWATERS_UPPER_SWAMP_ENTRANCE_EXIT, Regions.BACKWATERS_UPPER_SWAMP_ENTRANCE, True_())
    BACKWATERS_UPPER_SWAMP_ENTRANCE_BACKWATERS_UPPER_SWAMP_WATERFALL = ('Backwaters Upper Swamp Entrance_Backwaters Upper Swamp Waterfall', Regions.BACKWATERS_UPPER_SWAMP_ENTRANCE, Regions.BACKWATERS_UPPER_SWAMP_WATERFALL, True_())
    BACKWATERS_UPPER_SWAMP_FENCED_BACKWATERS_UPPER_LANTERN_PAD = ('Backwaters Upper Swamp Fenced_Backwaters Upper Lantern Pad', Regions.BACKWATERS_UPPER_SWAMP_FENCED, Regions.BACKWATERS_UPPER_LANTERN_PAD, CanJumpTiles(distance=4, over_water=True) | (CanSwim() & CanBurrow()))
    BACKWATERS_UPPER_SWAMP_FENCED_BACKWATERS_UPPER_SWAMP_BACK = ('Backwaters Upper Swamp Fenced_Backwaters Upper Swamp Back', Regions.BACKWATERS_UPPER_SWAMP_FENCED, Regions.BACKWATERS_UPPER_SWAMP_BACK, CanJumpTiles(distance=5, over_water=True) | (CanSwim() & CanBurrow()))
    BACKWATERS_UPPER_SWAMP_LILY_BACKWATERS_UPPER_LANTERN_PAD = ('Backwaters Upper Swamp Lily_Backwaters Upper Lantern Pad', Regions.BACKWATERS_UPPER_SWAMP_LILY, Regions.BACKWATERS_UPPER_LANTERN_PAD, CanSwim())
    BACKWATERS_UPPER_SWAMP_LILY_BACKWATERS_UPPER_SWAMP_EAST = ('Backwaters Upper Swamp Lily_Backwaters Upper Swamp East', Regions.BACKWATERS_UPPER_SWAMP_LILY, Regions.BACKWATERS_UPPER_SWAMP_EAST, CanJumpTiles(distance=2, over_water=True) | CanSwim())
    BACKWATERS_UPPER_SWAMP_WATERFALL_BACKWATERS_UPPER_SWAMP_BACK = ('Backwaters Upper Swamp Waterfall_Backwaters Upper Swamp Back', Regions.BACKWATERS_UPPER_SWAMP_WATERFALL, Regions.BACKWATERS_UPPER_SWAMP_BACK, CanJumpTiles(distance=2, over_water=True))

class RegionTransitions(TransitionTypeEnum):
    BACKWATERS_BAYOU_FALLS_EAST_EAST_TRANSITION = ('Backwaters Bayou Falls East East Transition', Regions.BACKWATERS_BAYOU_FALLS_EAST, Regions.BACKWATERS_LOWER_SWAMP_BAYOU_ENTRANCE, DirectionType.EAST, TransitionType.SCREENS, True_())
    BACKWATERS_BAYOU_FALLS_WEST_AREA_TRANSITION = ('Backwaters Bayou Falls West Area Transition', Regions.BACKWATERS_BAYOU_FALLS_WEST, Regions.NOXS_BAYOU_BOAT_STATION_PATH, DirectionType.WEST, TransitionType.AREA_SCREENS, True_())
    BACKWATERS_FISHING_HOLE_EAST_TRANSITION = ('Backwaters Fishing Hole East Transition', Regions.BACKWATERS_FISHING_HOLE, Regions.BACKWATERS_THALESSIAN_WAY_LOWER, DirectionType.EAST, TransitionType.SCREENS, True_())
    BACKWATERS_FISHING_HOLE_WEST_TRANSITION = ('Backwaters Fishing Hole West Transition', Regions.BACKWATERS_FISHING_HOLE, Regions.BACKWATERS_LOWER_SWAMP_FISHING, DirectionType.WEST, TransitionType.SCREENS, True_())
    BACKWATERS_LOWER_SWAMP_BAYOU_ENTRANCE_LUCKY_BURROW = ('Backwaters Lower Swamp Bayou Entrance Lucky Burrow', Regions.BACKWATERS_LOWER_SWAMP_BAYOU_ENTRANCE, Regions.BACKWATERS_LUCKYS_LAIR, DirectionType.NORTH, TransitionType.BURROW, CanBurrow())
    BACKWATERS_LOWER_SWAMP_BAYOU_ENTRANCE_WEST_TRANSITION = ('Backwaters Lower Swamp Bayou Entrance West Transition', Regions.BACKWATERS_LOWER_SWAMP_BAYOU_ENTRANCE, Regions.BACKWATERS_BAYOU_FALLS_EAST, DirectionType.WEST, TransitionType.SCREENS, True_())
    BACKWATERS_LOWER_SWAMP_FISHING_EAST_TRANSITION = ('Backwaters Lower Swamp Fishing East Transition', Regions.BACKWATERS_LOWER_SWAMP_FISHING, Regions.BACKWATERS_FISHING_HOLE, DirectionType.EAST, TransitionType.SCREENS, True_())
    BACKWATERS_LOWER_SWAMP_NORTH_TRANSITION = ('Backwaters Lower Swamp North Transition', Regions.BACKWATERS_LOWER_SWAMP, Regions.BACKWATERS_UPPER_SWAMP_LILY, DirectionType.NORTH, TransitionType.SCREENS, True_())
    BACKWATERS_LOWER_SWAMP_SHANTY_BAND_SECRET_NORTH_TRANSITION = ('Backwaters Lower Swamp Shanty Band Secret North Transition', Regions.BACKWATERS_LOWER_SWAMP_SHANTY_BAND, Regions.BACKWATERS_UPPER_SWAMP_BACK, DirectionType.NORTH, TransitionType.SCREENS, CanSwim())
    BACKWATERS_LOWER_SWAMP_STATION_ENTRANCE_EAST_TRANSITION = ('Backwaters Lower Swamp Station Entrance East Transition', Regions.BACKWATERS_LOWER_SWAMP_STATION_ENTRANCE, Regions.BACKWATERS_LOWER_SWAMP_STATION, DirectionType.EAST, TransitionType.SCREENS, True_())
    BACKWATERS_LOWER_SWAMP_STATION_SOUTH_AREA_TRANSITION = ('Backwaters Lower Swamp Station South Area Transition', Regions.BACKWATERS_LOWER_SWAMP_STATION, Regions.LONERS_LANDING_BAY, DirectionType.SOUTH, TransitionType.AREA_SCREENS, True_())
    BACKWATERS_LOWER_SWAMP_STATION_TRAIN = ('Backwaters Lower Swamp Station Train', Regions.BACKWATERS_LOWER_SWAMP_STATION, Regions.OSSEX_TRAIN_CABOOSE, DirectionType.OVERWORLD, TransitionType.DO_NOT_RANDOMIZE_ENTRANCE, Has(PermanentUpgrades.TRAIN_PASS.value))
    BACKWATERS_LUCKYS_LAIR_BURROW_EXIT = ("Backwaters Lucky's Lair Burrow Exit", Regions.BACKWATERS_LUCKYS_LAIR, Regions.BACKWATERS_LOWER_SWAMP_BAYOU_ENTRANCE, DirectionType.SOUTH, TransitionType.BURROW, CanBurrow())
    BACKWATERS_PINKY_BACK_POND_BOARD_SOUTH_TRANSITION = ('Backwaters Pinky Back Pond Board South Transition', Regions.BACKWATERS_PINKY_BACK_POND_BOARD, Regions.BACKWATERS_PINKY_FRONT_LAWN_WEST, DirectionType.SOUTH, TransitionType.SCREENS, True_())
    BACKWATERS_PINKY_BACK_POND_LAWN_WEST_SHOP_ENTRANCE = ('Backwaters Pinky Back Pond Lawn West Shop Entrance', Regions.BACKWATERS_PINKY_BACK_POND_LAWN, Regions.BACKWATERS_PINKY_SHOP_BACK, DirectionType.WEST, TransitionType.SCREENS, HasKear(kear=SingleKears.PINKY_BACK_KEAR.value))
    BACKWATERS_PINKY_FRONT_LAWN_EAST_WEST_TRANSITION = ('Backwaters Pinky Front Lawn East West Transition', Regions.BACKWATERS_PINKY_FRONT_LAWN_EAST, Regions.BACKWATERS_PINKY_OUTSIDE, DirectionType.WEST, TransitionType.SCREENS, True_())
    BACKWATERS_PINKY_FRONT_LAWN_WEST_NORTH_TRANSITION = ('Backwaters Pinky Front Lawn West North Transition', Regions.BACKWATERS_PINKY_FRONT_LAWN_WEST, Regions.BACKWATERS_PINKY_BACK_POND_BOARD, DirectionType.NORTH, TransitionType.SCREENS, True_())
    BACKWATERS_PINKY_OUTSIDE_EAST_TRANSITION = ('Backwaters Pinky Outside East Transition', Regions.BACKWATERS_PINKY_OUTSIDE, Regions.BACKWATERS_PINKY_FRONT_LAWN_EAST, DirectionType.EAST, TransitionType.SCREENS, True_())
    BACKWATERS_PINKY_OUTSIDE_SHOP_DOOR = ('Backwaters Pinky Outside Shop Door', Regions.BACKWATERS_PINKY_OUTSIDE, Regions.BACKWATERS_PINKY_SHOP, DirectionType.NORTH, TransitionType.DOORS, True_())
    BACKWATERS_PINKY_OUTSIDE_WEST_LOCKED_TRANSITION = ('Backwaters Pinky Outside West Locked Transition', Regions.BACKWATERS_PINKY_OUTSIDE, Regions.BACKWATERS_UPPER_SWAMP_LILY, DirectionType.WEST, TransitionType.SCREENS, HasKear(kear=SingleKears.PINKY_KEAR.value))
    BACKWATERS_PINKY_SHOP_BACK_EAST_EXIT = ('Backwaters Pinky Shop Back East Exit', Regions.BACKWATERS_PINKY_SHOP_BACK, Regions.BACKWATERS_PINKY_BACK_POND_LAWN, DirectionType.EAST, TransitionType.SCREENS, HasKear(kear=SingleKears.PINKY_BACK_KEAR.value))
    BACKWATERS_PINKY_SHOP_EXIT = ('Backwaters Pinky Shop Exit', Regions.BACKWATERS_PINKY_SHOP, Regions.BACKWATERS_PINKY_OUTSIDE, DirectionType.SOUTH, TransitionType.DOORS, True_())
    BACKWATERS_THALESSIAN_LILLIES_WEST_TRANSITION = ('Backwaters Thalessian Lillies West Transition', Regions.BACKWATERS_THALESSIAN_LILLIES, Regions.BACKWATERS_THALESSIAN_WAY_UPPER, DirectionType.WEST, TransitionType.SCREENS, True_())
    BACKWATERS_THALESSIAN_WAY_LOWER_WEST_TRANSITION = ('Backwaters Thalessian Way Lower West Transition', Regions.BACKWATERS_THALESSIAN_WAY_LOWER, Regions.BACKWATERS_FISHING_HOLE, DirectionType.WEST, TransitionType.SCREENS, True_())
    BACKWATERS_THALESSIAN_WAY_UPPER_EAST_TRANSITION = ('Backwaters Thalessian Way Upper East Transition', Regions.BACKWATERS_THALESSIAN_WAY_UPPER, Regions.BACKWATERS_THALESSIAN_LILLIES, DirectionType.EAST, TransitionType.SCREENS, True_())
    BACKWATERS_UPPER_LANTERN_CAVE_BACKWATERS_UPPER_LANTERN_PAD = ('Backwaters Upper Lantern Cave_Backwaters Upper Lantern Pad', Regions.BACKWATERS_UPPER_LANTERN_CAVE, Regions.BACKWATERS_UPPER_LANTERN_PAD, DirectionType.SOUTH, TransitionType.DOORS, True_())
    BACKWATERS_UPPER_LANTERN_PAD_BACKWATERS_UPPER_LANTERN_CAVE = ('Backwaters Upper Lantern Pad_Backwaters Upper Lantern Cave', Regions.BACKWATERS_UPPER_LANTERN_PAD, Regions.BACKWATERS_UPPER_LANTERN_CAVE, DirectionType.NORTH, TransitionType.DOORS, HasSparks(count=2) & HasLadder())
    BACKWATERS_UPPER_SWAMP_BACK_EAST_TRANSITION = ('Backwaters Upper Swamp Back East Transition', Regions.BACKWATERS_UPPER_SWAMP_BACK, Regions.BACKWATERS_UPPER_SWAMP_SECRET_ROOM, DirectionType.EAST, TransitionType.SCREENS, True_())
    BACKWATERS_UPPER_SWAMP_ENTRANCE_NORTH_AREA_TRANSITION = ('Backwaters Upper Swamp Entrance North Area Transition', Regions.BACKWATERS_UPPER_SWAMP_ENTRANCE, Regions.WESTERN_WILDS_WESTERN_POND, DirectionType.NORTH, TransitionType.AREA_SCREENS, True_())
    BACKWATERS_UPPER_SWAMP_LILY_EAST_LOCKED_TRANSITION = ('Backwaters Upper Swamp Lily East Locked Transition', Regions.BACKWATERS_UPPER_SWAMP_LILY, Regions.BACKWATERS_PINKY_OUTSIDE, DirectionType.EAST, TransitionType.SCREENS, HasKear(kear=SingleKears.PINKY_KEAR.value))
    BACKWATERS_UPPER_SWAMP_LILY_SOUTH_TRANSITION = ('Backwaters Upper Swamp Lily South Transition', Regions.BACKWATERS_UPPER_SWAMP_LILY, Regions.BACKWATERS_LOWER_SWAMP, DirectionType.SOUTH, TransitionType.SCREENS, True_())
    BACKWATERS_UPPER_SWAMP_SECRET_ROOM_WEST_TRANSITION = ('Backwaters Upper Swamp Secret Room West Transition', Regions.BACKWATERS_UPPER_SWAMP_SECRET_ROOM, Regions.BACKWATERS_UPPER_SWAMP_BACK, DirectionType.WEST, TransitionType.SCREENS, True_())

