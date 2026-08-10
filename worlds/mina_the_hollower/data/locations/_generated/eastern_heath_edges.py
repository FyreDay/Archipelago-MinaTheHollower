# AUTO-GENERATED -- DO NOT EDIT.
# Regenerate from the spreadsheet export with:
#   python -m worlds.mina_the_hollower.tools.generate_edges <edges.csv>
# The spreadsheet is the source of truth, not this file.

from .regions import Regions
from rule_builder.rules import Has, True_, CanReachLocation
from ... import RegionConnection, Transition, DirectionType, TransitionType, RegionTypeEnum,ConnectionTypeEnum, TransitionTypeEnum
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
   RepairedGenerator, RepairedGeneratorCount,
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


class RegionConnections(ConnectionTypeEnum):
    EASTERN_HEATH_BUCKLER_S_BLUFF_CLIFF_EASTERN_HEATH_BUCKLER_S_BLUFF_BUCKLERS = ("Eastern Heath Buckler's Bluff Cliff_Eastern Heath Buckler's Bluff Bucklers", Regions.EASTERN_HEATH_BUCKLER_S_BLUFF_CLIFF, Regions.EASTERN_HEATH_BUCKLER_S_BLUFF_BUCKLERS, CanJumpTiles(distance=4, has_wall=True)),
    EASTERN_HEATH_BUCKLER_S_BLUFF_CLIFF_EASTERN_HEATH_BUCKLER_S_BLUFF_START = ("Eastern Heath Buckler's Bluff Cliff_Eastern Heath Buckler's Bluff Start", Regions.EASTERN_HEATH_BUCKLER_S_BLUFF_CLIFF, Regions.EASTERN_HEATH_BUCKLER_S_BLUFF_START, CanJumpTiles(distance=4, has_wall=True)),
    EASTERN_HEATH_BUCKLER_S_BLUFF_START_EASTERN_HEATH_BUCKLER_S_BLUFF_CLIFF = ("Eastern Heath Buckler's Bluff Start_Eastern Heath Buckler's Bluff Cliff", Regions.EASTERN_HEATH_BUCKLER_S_BLUFF_START, Regions.EASTERN_HEATH_BUCKLER_S_BLUFF_CLIFF, CanJumpTiles(distance=4, has_wall=True)),
    EASTERN_HEATH_CHOPPE_SHOPPE_ENTRY_CLIFF_EASTERN_HEATH_CLIFF_SECRET = ('Eastern Heath Choppe Shoppe Entry Cliff_Eastern Heath Cliff Secret', Regions.EASTERN_HEATH_CHOPPE_SHOPPE_ENTRY_CLIFF, Regions.EASTERN_HEATH_CLIFF_SECRET, HasKear(kear=SingleKears.EASTERN_HEATH_WATERFALL_KEAR.value)),
    EASTERN_HEATH_CHOPPE_SHOPPE_ENTRY_EASTERN_HEATH_CLIFF_SECRET = ('Eastern Heath Choppe Shoppe Entry_Eastern Heath Cliff Secret', Regions.EASTERN_HEATH_CHOPPE_SHOPPE_ENTRY, Regions.EASTERN_HEATH_CLIFF_SECRET, HasKear(kear=SingleKears.EASTERN_HEATH_WATERFALL_KEAR.value) & CanBurrow()),
    EASTERN_HEATH_CLIFF_SECRET_EASTERN_HEATH_CHOPPE_SHOPPE_ENTRY = ('Eastern Heath Cliff Secret_Eastern Heath Choppe Shoppe Entry', Regions.EASTERN_HEATH_CLIFF_SECRET, Regions.EASTERN_HEATH_CHOPPE_SHOPPE_ENTRY, HasKear(kear=SingleKears.EASTERN_HEATH_WATERFALL_KEAR.value) & CanBurrow()),
    EASTERN_HEATH_CLIFF_SECRET_EASTERN_HEATH_CHOPPE_SHOPPE_ENTRY_CLIFF = ('Eastern Heath Cliff Secret_Eastern Heath Choppe Shoppe Entry Cliff', Regions.EASTERN_HEATH_CLIFF_SECRET, Regions.EASTERN_HEATH_CHOPPE_SHOPPE_ENTRY_CLIFF, HasKear(kear=SingleKears.EASTERN_HEATH_WATERFALL_KEAR.value)),
    EASTERN_HEATH_EAST_CORNER_CLIFF_EASTERN_HEATH_EAST_CORNER = ('Eastern Heath East Corner Cliff_Eastern Heath East Corner', Regions.EASTERN_HEATH_EAST_CORNER_CLIFF, Regions.EASTERN_HEATH_EAST_CORNER, True_()),
    EASTERN_HEATH_FROZEN_PASS_EASTERN_HEATH_GRASSLAND_WATERFALL_SECOND_LEVEL = ('Eastern Heath Frozen Pass_Eastern Heath Grassland Waterfall Second Level', Regions.EASTERN_HEATH_FROZEN_PASS, Regions.EASTERN_HEATH_GRASSLAND_WATERFALL_SECOND_LEVEL, True_()),
    EASTERN_HEATH_GRASSLAND_BRIDGE_RIGHT_EASTERN_HEATH_GRASSLAND_BRIDGE_LEFT = ('Eastern Heath Grassland Bridge Right_Eastern Heath Grassland Bridge Left', Regions.EASTERN_HEATH_GRASSLAND_BRIDGE_RIGHT, Regions.EASTERN_HEATH_GRASSLAND_BRIDGE_LEFT, True_()),
    EASTERN_HEATH_GRASSLAND_WATERFALL_PIPE_EASTERN_HEATH_GRASSLAND_WATERFALL_SECOND_LEVEL = ('Eastern Heath Grassland Waterfall Pipe_Eastern Heath Grassland Waterfall Second Level', Regions.EASTERN_HEATH_GRASSLAND_WATERFALL_PIPE, Regions.EASTERN_HEATH_GRASSLAND_WATERFALL_SECOND_LEVEL, CanClimb()),
    EASTERN_HEATH_GRASSLAND_WATERFALL_SECOND_LEVEL_EASTERN_HEATH_FROZEN_PASS = ('Eastern Heath Grassland Waterfall Second Level_Eastern Heath Frozen Pass', Regions.EASTERN_HEATH_GRASSLAND_WATERFALL_SECOND_LEVEL, Regions.EASTERN_HEATH_FROZEN_PASS, CanSwim()),
    EASTERN_HEATH_POPPET_ENTRY_TOP_EASTERN_HEATH_POPPET_ENTRY = ('Eastern Heath Poppet Entry Top_Eastern Heath Poppet Entry', Regions.EASTERN_HEATH_POPPET_ENTRY_TOP, Regions.EASTERN_HEATH_POPPET_ENTRY, CanBurrow()),
    EASTERN_HEATH_POPPET_ENTRY_EASTERN_HEATH_POPPET_ENTRY_TOP = ('Eastern Heath Poppet Entry_Eastern Heath Poppet Entry Top', Regions.EASTERN_HEATH_POPPET_ENTRY, Regions.EASTERN_HEATH_POPPET_ENTRY_TOP, CanBurrow()),

class RegionTransitions(TransitionTypeEnum):
    EASTERN_HEATH_BUCKLER_S_BLUFF_BUCKLERS_WEST_TRANSITION = ("Eastern Heath Buckler's Bluff Bucklers West Transition", Regions.EASTERN_HEATH_BUCKLER_S_BLUFF_BUCKLERS, Regions.EASTERN_HEATH_GRASSLAND_WATERFALL_SECOND_LEVEL, DirectionType.WEST, TransitionType.SCREENS, True_()),
    EASTERN_HEATH_BUCKLER_S_BLUFF_START_SOUTH_KEAR_BURROW = ("Eastern Heath Buckler's Bluff Start South Kear Burrow", Regions.EASTERN_HEATH_BUCKLER_S_BLUFF_START, Regions.EASTERN_HEATH_MOURNERS_GATE, DirectionType.SOUTH, TransitionType.BURROW, CanBurrow() & HasKear(kear=SingleKears.EASTERN_HEATH_BUCKLERS_BLUFF_KEAR.value)),
    EASTERN_HEATH_BUCKLER_S_BLUFF_START_SOUTH_TRANSITION = ("Eastern Heath Buckler's Bluff Start South Transition", Regions.EASTERN_HEATH_BUCKLER_S_BLUFF_START, Regions.EASTERN_HEATH_MOURNERS_GATE, DirectionType.SOUTH, TransitionType.SCREENS, True_()),
    EASTERN_HEATH_BUSH_ROOM_NORTH_TRANSITION = ('Eastern Heath Bush Room North Transition', Regions.EASTERN_HEATH_BUSH_ROOM, Regions.EASTERN_HEATH_I_SCREEN, DirectionType.NORTH, TransitionType.SCREENS, True_()),
    EASTERN_HEATH_BUSH_ROOM_SOUTH_AREA_TRANSITION = ('Eastern Heath Bush Room South Area Transition', Regions.EASTERN_HEATH_BUSH_ROOM, Regions.SOUTHERN_OUTSKIRTS_MOONBATH, DirectionType.SOUTH, TransitionType.AREA_SCREENS, True_()),
    EASTERN_HEATH_CHOPPE_SHOPPE_ENTRY_CLIFF_EAST_TRANSITION = ('Eastern Heath Choppe Shoppe Entry Cliff East Transition', Regions.EASTERN_HEATH_CHOPPE_SHOPPE_ENTRY_CLIFF, Regions.EASTERN_HEATH_GRASSLAND_WATERFALL_FIRST_LEVEL, DirectionType.EAST, TransitionType.SCREENS, HasKear(kear=SingleKears.EASTERN_HEATH_WATERFALL_KEAR.value)),
    EASTERN_HEATH_CHOPPE_SHOPPE_ENTRY_CLIFF_GEYSER_DROP = ('Eastern Heath Choppe Shoppe Entry Cliff Geyser Drop', Regions.EASTERN_HEATH_CLIFF_SECRET, Regions.EASTERN_HEATH_HIDDEN_GROTTO, DirectionType.OVERWORLD, TransitionType.GEYSER_DOWN, True_()),
    EASTERN_HEATH_CHOPPE_SHOPPE_ENTRY_DOOR = ('Eastern Heath Choppe Shoppe Entry Door', Regions.EASTERN_HEATH_CHOPPE_SHOPPE_ENTRY, Regions.EASTERN_HEATH_CHOPPE_SHOPPE, DirectionType.NORTH, TransitionType.DOORS, HasKear(kear=SingleKears.CHOPPE_SHOPPE_KEAR.value)),
    EASTERN_HEATH_CHOPPE_SHOPPE_EXIT = ('Eastern Heath Choppe Shoppe Exit', Regions.EASTERN_HEATH_CHOPPE_SHOPPE, Regions.EASTERN_HEATH_CHOPPE_SHOPPE_ENTRY, DirectionType.SOUTH, TransitionType.DOORS, HasKear(kear=SingleKears.CHOPPE_SHOPPE_KEAR.value)),
    EASTERN_HEATH_EAST_CORNER_NORTH_TRANSITION = ('Eastern Heath East Corner North Transition', Regions.EASTERN_HEATH_EAST_CORNER, Regions.EASTERN_HEATH_MOURNERS_GATE, DirectionType.NORTH, TransitionType.SCREENS, True_()),
    EASTERN_HEATH_EAST_CORNER_SOUTH_TRANSITION = ('Eastern Heath East Corner South Transition', Regions.EASTERN_HEATH_EAST_CORNER, Regions.EASTERN_HEATH_POPPET_ENTRY, DirectionType.SOUTH, TransitionType.SCREENS, True_()),
    EASTERN_HEATH_EAST_CORNER_WEST_TRANSITION = ('Eastern Heath East Corner West Transition', Regions.EASTERN_HEATH_EAST_CORNER, Regions.EASTERN_HEATH_GRASSLAND_BRIDGE_RIGHT, DirectionType.WEST, TransitionType.SCREENS, True_()),
    EASTERN_HEATH_FROZEN_PASS_NORTH_AREA_TRANSITION = ('Eastern Heath Frozen Pass North Area Transition', Regions.EASTERN_HEATH_FROZEN_PASS, Regions.COLTRANE_PEAK_FROZEN_PASS_BOTTOM, DirectionType.NORTH, TransitionType.AREA_SCREENS, True_()),
    EASTERN_HEATH_GRASSLAND_BRIDGE_LEFT_NORTH_TRANSITION = ('Eastern Heath Grassland Bridge Left North Transition', Regions.EASTERN_HEATH_GRASSLAND_BRIDGE_LEFT, Regions.EASTERN_HEATH_GRASSLAND_WATERFALL_BOTTOM, DirectionType.NORTH, TransitionType.SCREENS, True_()),
    EASTERN_HEATH_GRASSLAND_BRIDGE_LEFT_SOUTH_TRANSITION = ('Eastern Heath Grassland Bridge Left South Transition', Regions.EASTERN_HEATH_GRASSLAND_BRIDGE_LEFT, Regions.EASTERN_HEATH_GRASSLAND_RIVERBED_TOP, DirectionType.SOUTH, TransitionType.SCREENS, True_()),
    EASTERN_HEATH_GRASSLAND_BRIDGE_LEFT_WEST_TRANSITION = ('Eastern Heath Grassland Bridge Left West Transition', Regions.EASTERN_HEATH_GRASSLAND_BRIDGE_LEFT, Regions.EASTERN_HEATH_GRASSLAND, DirectionType.WEST, TransitionType.SCREENS, True_()),
    EASTERN_HEATH_GRASSLAND_BRIDGE_RIGHT_EAST_TRANSITION = ('Eastern Heath Grassland Bridge Right East Transition', Regions.EASTERN_HEATH_GRASSLAND_BRIDGE_RIGHT, Regions.EASTERN_HEATH_EAST_CORNER, DirectionType.EAST, TransitionType.SCREENS, True_()),
    EASTERN_HEATH_GRASSLAND_BRIDGE_RIVER_NORTH_SWIM = ('Eastern Heath Grassland Bridge River North Swim', Regions.EASTERN_HEATH_GRASSLAND_BRIDGE_RIVER, Regions.EASTERN_HEATH_UNDER_THE_BRIDGE, DirectionType.NORTH, TransitionType.BURROW, CanSwim()),
    EASTERN_HEATH_GRASSLAND_BRIDGE_RIVER_SOUTH_SWIM = ('Eastern Heath Grassland Bridge River South Swim', Regions.EASTERN_HEATH_GRASSLAND_BRIDGE_RIVER, Regions.EASTERN_HEATH_GRASSLAND_RIVERBED_BOTTOM, DirectionType.SOUTH, TransitionType.BURROW, CanSwim()),
    EASTERN_HEATH_GRASSLAND_EAST_TRANSITION = ('Eastern Heath Grassland East Transition', Regions.EASTERN_HEATH_GRASSLAND, Regions.EASTERN_HEATH_GRASSLAND_BRIDGE_LEFT, DirectionType.EAST, TransitionType.SCREENS, True_()),
    EASTERN_HEATH_GRASSLAND_NORTH_TRANSITION = ('Eastern Heath Grassland North Transition', Regions.EASTERN_HEATH_GRASSLAND, Regions.EASTERN_HEATH_CHOPPE_SHOPPE_ENTRY, DirectionType.NORTH, TransitionType.SCREENS, True_()),
    EASTERN_HEATH_GRASSLAND_PIT_EAST_TRANSITION = ('Eastern Heath Grassland Pit East Transition', Regions.EASTERN_HEATH_GRASSLAND_PIT, Regions.EASTERN_HEATH_POPPET_ENTRY, DirectionType.EAST, TransitionType.SCREENS, True_()),
    EASTERN_HEATH_GRASSLAND_PIT_NORTH_TRANSITION = ('Eastern Heath Grassland Pit North Transition', Regions.EASTERN_HEATH_GRASSLAND_PIT, Regions.EASTERN_HEATH_GRASSLAND_RIVERBED_BOTTOM, DirectionType.NORTH, TransitionType.SCREENS, CanJumpTiles(distance=2)),
    EASTERN_HEATH_GRASSLAND_PIT_WEST_TRANSITION = ('Eastern Heath Grassland Pit West Transition', Regions.EASTERN_HEATH_GRASSLAND_PIT, Regions.EASTERN_HEATH_I_SCREEN, DirectionType.WEST, TransitionType.SCREENS, True_()),
    EASTERN_HEATH_GRASSLAND_POPPIT_CAVE_EAST_TRANSITION = ('Eastern Heath Grassland Poppit Cave East Transition', Regions.EASTERN_HEATH_GRASSLAND_POPPIT_CAVE, Regions.EASTERN_HEATH_POPPIT, DirectionType.EAST, TransitionType.SCREENS, True_()),
    EASTERN_HEATH_GRASSLAND_POPPIT_CAVE_NORTH_BURROW = ('Eastern Heath Grassland Poppit Cave North Burrow', Regions.EASTERN_HEATH_GRASSLAND_POPPIT_CAVE, Regions.EASTERN_HEATH_POPPIT, DirectionType.NORTH, TransitionType.BURROW, CanBurrow()),
    EASTERN_HEATH_GRASSLAND_RIVERBED_BOTTOM_SOUTH_TRANSITION = ('Eastern Heath Grassland Riverbed Bottom South Transition', Regions.EASTERN_HEATH_GRASSLAND_RIVERBED_BOTTOM, Regions.EASTERN_HEATH_GRASSLAND_PIT, DirectionType.SOUTH, TransitionType.SCREENS, CanJumpTiles(distance=2)),
    EASTERN_HEATH_GRASSLAND_RIVERBED_DIVE_EAST_TRANSITION = ('Eastern Heath Grassland Riverbed Dive East Transition', Regions.EASTERN_HEATH_GRASSLAND_RIVERBED_DIVE, Regions.EASTERN_HEATH_POPPET_ENTRY, DirectionType.EAST, TransitionType.SCREENS, True_()),
    EASTERN_HEATH_GRASSLAND_RIVERBED_DIVE_NORTH_TRANSITION_SWIM = ('Eastern Heath Grassland Riverbed Dive North Transition Swim', Regions.EASTERN_HEATH_GRASSLAND_RIVERBED_DIVE, Regions.EASTERN_HEATH_GRASSLAND_BRIDGE_RIVER, DirectionType.NORTH, TransitionType.BURROW, CanSwim()),
    EASTERN_HEATH_GRASSLAND_RIVERBED_TOP_NORTH_TRANSITION = ('Eastern Heath Grassland Riverbed Top North Transition', Regions.EASTERN_HEATH_GRASSLAND_RIVERBED_TOP, Regions.EASTERN_HEATH_GRASSLAND_BRIDGE_LEFT, DirectionType.NORTH, TransitionType.SCREENS, True_()),
    EASTERN_HEATH_GRASSLAND_RIVERBED_TOP_WEST_TRANSITION = ('Eastern Heath Grassland Riverbed Top West Transition', Regions.EASTERN_HEATH_GRASSLAND_RIVERBED_TOP, Regions.EASTERN_HEATH_I_SCREEN, DirectionType.WEST, TransitionType.SCREENS, True_()),
    EASTERN_HEATH_GRASSLAND_SOUTH_TRANSITION = ('Eastern Heath Grassland South Transition', Regions.EASTERN_HEATH_GRASSLAND, Regions.EASTERN_HEATH_I_SCREEN, DirectionType.SOUTH, TransitionType.SCREENS, True_()),
    EASTERN_HEATH_GRASSLAND_WATERFALL_BOTTOM_SOUTH_TRANSITION = ('Eastern Heath Grassland Waterfall Bottom South Transition', Regions.EASTERN_HEATH_GRASSLAND_WATERFALL_BOTTOM, Regions.EASTERN_HEATH_GRASSLAND_BRIDGE_LEFT, DirectionType.SOUTH, TransitionType.SCREENS, True_()),
    EASTERN_HEATH_GRASSLAND_WATERFALL_BOTTOM_WEST_TRANSITION = ('Eastern Heath Grassland Waterfall Bottom West Transition', Regions.EASTERN_HEATH_GRASSLAND_WATERFALL_BOTTOM, Regions.EASTERN_HEATH_CHOPPE_SHOPPE_ENTRY, DirectionType.WEST, TransitionType.SCREENS, True_()),
    EASTERN_HEATH_GRASSLAND_WATERFALL_FIRST_LEVEL_DOOR = ('Eastern Heath Grassland Waterfall First Level Door', Regions.EASTERN_HEATH_GRASSLAND_WATERFALL_FIRST_LEVEL, Regions.EASTERN_HEATH_GROTTO_LEFT, DirectionType.NORTH, TransitionType.DOORS, True_()),
    EASTERN_HEATH_GRASSLAND_WATERFALL_FIRST_LEVEL_WEST_TRANSITION = ('Eastern Heath Grassland Waterfall First Level West Transition', Regions.EASTERN_HEATH_GRASSLAND_WATERFALL_FIRST_LEVEL, Regions.EASTERN_HEATH_CHOPPE_SHOPPE_ENTRY_CLIFF, DirectionType.WEST, TransitionType.SCREENS, True_()),
    EASTERN_HEATH_GRASSLAND_WATERFALL_SECOND_LEVEL_DIVE_SOUTH = ('Eastern Heath Grassland Waterfall Second Level Dive South', Regions.EASTERN_HEATH_GRASSLAND_WATERFALL_SECOND_LEVEL, Regions.EASTERN_HEATH_UNDER_THE_BRIDGE, DirectionType.SOUTH, TransitionType.SCREENS, CanSwim()),
    EASTERN_HEATH_GRASSLAND_WATERFALL_SECOND_LEVEL_DOOR = ('Eastern Heath Grassland Waterfall Second Level Door', Regions.EASTERN_HEATH_GRASSLAND_WATERFALL_SECOND_LEVEL, Regions.EASTERN_HEATH_GROTTO_RIGHT, DirectionType.NORTH, TransitionType.DOORS, True_()),
    EASTERN_HEATH_GRASSLAND_WATERFALL_SECOND_LEVEL_EAST_TRANSITION = ('Eastern Heath Grassland Waterfall Second Level East Transition', Regions.EASTERN_HEATH_GRASSLAND_WATERFALL_SECOND_LEVEL, Regions.EASTERN_HEATH_BUCKLER_S_BLUFF_BUCKLERS, DirectionType.EAST, TransitionType.SCREENS, True_()),
    EASTERN_HEATH_GRASSLAND_WATERFALL_SECOND_LEVEL_ROPE = ('Eastern Heath Grassland Waterfall Second Level Rope', Regions.EASTERN_HEATH_GRASSLAND_WATERFALL_SECOND_LEVEL, Regions.EASTERN_HEATH_GRASSLAND_BRIDGE_RIGHT, DirectionType.SOUTH, TransitionType.DO_NOT_RANDOMIZE_ENTRANCE, CanClimb()),
    EASTERN_HEATH_GRASSLAND_WEST_AREA_TRANSITION = ('Eastern Heath Grassland West Area Transition', Regions.EASTERN_HEATH_GRASSLAND, Regions.OSSEX_HIGH_STREET_MAIN, DirectionType.WEST, TransitionType.AREA_SCREENS, True_()),
    EASTERN_HEATH_GROTTO_LEFT_EAST_TRANSITION = ('Eastern Heath Grotto Left East Transition', Regions.EASTERN_HEATH_GROTTO_LEFT, Regions.EASTERN_HEATH_GROTTO_RIGHT, DirectionType.EAST, TransitionType.BURROW, CanBurrow()),
    EASTERN_HEATH_GROTTO_LEFT_EXIT = ('Eastern Heath Grotto Left Exit', Regions.EASTERN_HEATH_GROTTO_LEFT, Regions.EASTERN_HEATH_GRASSLAND_WATERFALL_FIRST_LEVEL, DirectionType.SOUTH, TransitionType.DOORS, True_()),
    EASTERN_HEATH_GROTTO_RIGHT_EXIT = ('Eastern Heath Grotto Right Exit', Regions.EASTERN_HEATH_GROTTO_RIGHT, Regions.EASTERN_HEATH_GRASSLAND_WATERFALL_SECOND_LEVEL, DirectionType.SOUTH, TransitionType.DOORS, True_()),
    EASTERN_HEATH_GROTTO_RIGHT_WEST_BURROW = ('Eastern Heath Grotto Right West Burrow', Regions.EASTERN_HEATH_GROTTO_RIGHT, Regions.EASTERN_HEATH_GROTTO_LEFT, DirectionType.WEST, TransitionType.BURROW, CanBurrow()),
    EASTERN_HEATH_HIDDEN_GROTTO_GEYSER_UP = ('Eastern Heath Hidden Grotto Geyser Up', Regions.EASTERN_HEATH_HIDDEN_GROTTO, Regions.EASTERN_HEATH_CLIFF_SECRET, DirectionType.OVERWORLD, TransitionType.GEYSER_UP, True_()),
    EASTERN_HEATH_I_SCREEN_EAST_TRANSITION_NORTH = ('Eastern Heath I Screen East Transition North', Regions.EASTERN_HEATH_I_SCREEN, Regions.EASTERN_HEATH_GRASSLAND_RIVERBED_TOP, DirectionType.EAST, TransitionType.SCREENS, True_()),
    EASTERN_HEATH_I_SCREEN_EAST_TRANSITION_SOUTH = ('Eastern Heath I Screen East Transition South', Regions.EASTERN_HEATH_I_SCREEN, Regions.EASTERN_HEATH_GRASSLAND_PIT, DirectionType.EAST, TransitionType.SCREENS, True_()),
    EASTERN_HEATH_I_SCREEN_NORTH_TRANSITION = ('Eastern Heath I Screen North Transition', Regions.EASTERN_HEATH_I_SCREEN, Regions.EASTERN_HEATH_GRASSLAND, DirectionType.NORTH, TransitionType.SCREENS, True_()),
    EASTERN_HEATH_I_SCREEN_SOUTH_TRANSITION = ('Eastern Heath I Screen South Transition', Regions.EASTERN_HEATH_I_SCREEN, Regions.EASTERN_HEATH_BUSH_ROOM, DirectionType.SOUTH, TransitionType.SCREENS, True_()),
    EASTERN_HEATH_MOURNERS_GATE_EAST_AREA_TRANSITION = ('Eastern Heath Mourners Gate East Area Transition', Regions.EASTERN_HEATH_MOURNERS_GATE, Regions.MOURNER_S_MILE_KNIGHT_S_REST_MAIN, DirectionType.EAST, TransitionType.AREA_SCREENS, True_()),
    EASTERN_HEATH_MOURNERS_GATE_NORTH_KEAR_BURROW = ('Eastern Heath Mourners Gate North Kear Burrow', Regions.EASTERN_HEATH_MOURNERS_GATE, Regions.EASTERN_HEATH_BUCKLER_S_BLUFF_START, DirectionType.NORTH, TransitionType.BURROW, CanBurrow() & HasKear(kear=SingleKears.EASTERN_HEATH_BUCKLERS_BLUFF_KEAR.value)),
    EASTERN_HEATH_MOURNERS_GATE_SOUTH_TRANSITION = ('Eastern Heath Mourners Gate South Transition', Regions.EASTERN_HEATH_MOURNERS_GATE, Regions.EASTERN_HEATH_EAST_CORNER, DirectionType.SOUTH, TransitionType.SCREENS, True_()),
    EASTERN_HEATH_POPPET_ENTRY_NORTH_TRANSITION = ('Eastern Heath Poppet Entry North Transition', Regions.EASTERN_HEATH_POPPET_ENTRY_TOP, Regions.EASTERN_HEATH_EAST_CORNER, DirectionType.NORTH, TransitionType.SCREENS, True_()),
    EASTERN_HEATH_POPPET_ENTRY_SOUTH_BURROW = ('Eastern Heath Poppet Entry South Burrow', Regions.EASTERN_HEATH_POPPET_ENTRY, Regions.EASTERN_HEATH_GRASSLAND_POPPIT_CAVE, DirectionType.SOUTH, TransitionType.BURROW, CanBurrow()),
    EASTERN_HEATH_POPPET_ENTRY_WEST_TRANSITION_NORTH = ('Eastern Heath Poppet Entry West Transition North', Regions.EASTERN_HEATH_POPPET_ENTRY_TOP, Regions.EASTERN_HEATH_GRASSLAND_RIVERBED_DIVE, DirectionType.WEST, TransitionType.SCREENS, CanJumpTiles(distance=2, has_wall=True)),
    EASTERN_HEATH_POPPET_ENTRY_WEST_TRANSITION_SOUTH = ('Eastern Heath Poppet Entry West Transition South', Regions.EASTERN_HEATH_POPPET_ENTRY, Regions.EASTERN_HEATH_GRASSLAND_PIT, DirectionType.WEST, TransitionType.SCREENS, True_()),
    EASTERN_HEATH_POPPIT_WEST_TRANSITION = ('Eastern Heath Poppit West Transition', Regions.EASTERN_HEATH_POPPIT, Regions.EASTERN_HEATH_GRASSLAND_POPPIT_CAVE, DirectionType.WEST, TransitionType.SCREENS, True_()),
    EASTERN_HEATH_UNDER_BRIDGE_EAST_WEST_TRANSITION = ('Eastern Heath Under Bridge East West Transition', Regions.EASTERN_HEATH_UNDER_BRIDGE_EAST, Regions.EASTERN_HEATH_UNDER_THE_BRIDGE, DirectionType.WEST, TransitionType.SCREENS, True_()),
    EASTERN_HEATH_UNDER_BRIDGE_SOUTH_GEYSER_UP = ('Eastern Heath Under Bridge South Geyser Up', Regions.EASTERN_HEATH_UNDER_BRIDGE_SOUTH, Regions.EASTERN_HEATH_GRASSLAND_RIVERBED_DIVE, DirectionType.OVERWORLD, TransitionType.GEYSER_UP, True_()),
    EASTERN_HEATH_UNDER_BRIDGE_SOUTH_NORTH_TRANSITION = ('Eastern Heath Under Bridge South North Transition', Regions.EASTERN_HEATH_UNDER_BRIDGE_SOUTH, Regions.EASTERN_HEATH_UNDER_THE_BRIDGE, DirectionType.NORTH, TransitionType.SCREENS, True_()),
    EASTERN_HEATH_UNDER_BRIDGE_WEST_EAST_TRANSITION = ('Eastern Heath Under Bridge West East Transition', Regions.EASTERN_HEATH_UNDER_BRIDGE_WEST, Regions.EASTERN_HEATH_UNDER_THE_BRIDGE, DirectionType.EAST, TransitionType.SCREENS, True_()),
    EASTERN_HEATH_UNDER_THE_BRIDGE_EAST_TRANSITION = ('Eastern Heath Under the Bridge East Transition', Regions.EASTERN_HEATH_UNDER_THE_BRIDGE, Regions.EASTERN_HEATH_UNDER_BRIDGE_EAST, DirectionType.EAST, TransitionType.BURROW, CanBurrow()),
    EASTERN_HEATH_UNDER_THE_BRIDGE_SOUTH_TRANSITION = ('Eastern Heath Under the Bridge South Transition', Regions.EASTERN_HEATH_UNDER_THE_BRIDGE, Regions.EASTERN_HEATH_UNDER_BRIDGE_SOUTH, DirectionType.SOUTH, TransitionType.SCREENS, True_()),
    EASTERN_HEATH_UNDER_THE_BRIDGE_WEST_TRANSITION = ('Eastern Heath Under the Bridge West Transition', Regions.EASTERN_HEATH_UNDER_THE_BRIDGE, Regions.EASTERN_HEATH_UNDER_BRIDGE_WEST, DirectionType.WEST, TransitionType.BURROW, CanBurrow()),
    OSSEX_EASTERN_WALL_SOUTH_TRANSITION = ('Ossex Eastern Wall South Transition', Regions.OSSEX_EASTERN_WALL, Regions.OSSEX_SOUTH_EASTERN_WALL, DirectionType.SOUTH, TransitionType.SCREENS, True_()),

