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
    KINDLEWOOD_FARM_CROSSING_ENTRANCE_KINDLEWOOD_FARM_CROSSING = ('Kindlewood Farm Crossing Entrance_Kindlewood Farm Crossing', Regions.KINDLEWOOD_FARM_CROSSING_ENTRANCE, Regions.KINDLEWOOD_FARM_CROSSING, CanBurrow()),
    KINDLEWOOD_FARM_CROSSING_ENTRANCE_KINDLEWOOD_FARM_CROSSING_PUMPKIN_PATCH = ('Kindlewood Farm Crossing Entrance_Kindlewood Farm Crossing Pumpkin Patch', Regions.KINDLEWOOD_FARM_CROSSING_ENTRANCE, Regions.KINDLEWOOD_FARM_CROSSING_PUMPKIN_PATCH, CanBurrow()),
    KINDLEWOOD_FARM_CROSSING_PUMPKIN_PATCH_KINDLEWOOD_FARM_CROSSING_ENTRANCE = ('Kindlewood Farm Crossing Pumpkin Patch_Kindlewood Farm Crossing Entrance', Regions.KINDLEWOOD_FARM_CROSSING_PUMPKIN_PATCH, Regions.KINDLEWOOD_FARM_CROSSING_ENTRANCE, CanBurrow()),
    KINDLEWOOD_FARM_CROSSING_SHACK_OUTSIDE_KINDLEWOOD_FARM_TOMATO = ('Kindlewood Farm Crossing Shack Outside_Kindlewood Farm Tomato', Regions.KINDLEWOOD_FARM_CROSSING_SHACK_OUTSIDE, Regions.KINDLEWOOD_FARM_TOMATO, HasKear(kear=SingleKears.KINDLEWOOD_TOMATO_PATCH_KEAR.value)),
    KINDLEWOOD_FARM_CROSSING_KINDLEWOOD_FARM_CROSSING_ENTRANCE = ('Kindlewood Farm Crossing_Kindlewood Farm Crossing Entrance', Regions.KINDLEWOOD_FARM_CROSSING, Regions.KINDLEWOOD_FARM_CROSSING_ENTRANCE, CanBurrow()),
    KINDLEWOOD_FARM_TOMATO_KINDLEWOOD_FARM_CROSSING_SHACK_OUTSIDE = ('Kindlewood Farm Tomato_Kindlewood Farm Crossing Shack Outside', Regions.KINDLEWOOD_FARM_TOMATO, Regions.KINDLEWOOD_FARM_CROSSING_SHACK_OUTSIDE, HasKear(kear=SingleKears.KINDLEWOOD_TOMATO_PATCH_KEAR.value)),
    KINDLEWOOD_FARM_TOMATO_KINDLEWOOD_TRAIN_TRACKS = ('Kindlewood Farm Tomato_Kindlewood Train Tracks', Regions.KINDLEWOOD_FARM_TOMATO, Regions.KINDLEWOOD_TRAIN_TRACKS, CanBurrow()),
    KINDLEWOOD_OVERGROWTH_BEHIND_RESIDENCE_LAWN_KINDLEWOOD_OVERGROWTH_BEHIND_RESIDENCE = ('Kindlewood Overgrowth Behind Residence Lawn_Kindlewood Overgrowth Behind Residence', Regions.KINDLEWOOD_OVERGROWTH_BEHIND_RESIDENCE_LAWN, Regions.KINDLEWOOD_OVERGROWTH_BEHIND_RESIDENCE, CanCarry()),
    KINDLEWOOD_OVERGROWTH_BEHIND_RESIDENCE_KINDLEWOOD_OVERGROWTH_BEHIND_RESIDENCE_LAWN = ('Kindlewood Overgrowth Behind Residence_Kindlewood Overgrowth Behind Residence Lawn', Regions.KINDLEWOOD_OVERGROWTH_BEHIND_RESIDENCE, Regions.KINDLEWOOD_OVERGROWTH_BEHIND_RESIDENCE_LAWN, True_()),
    KINDLEWOOD_OVERGROWTH_BONFIRE_LEFT_KINDLEWOOD_OVERGROWTH_BONFIRE_MAIN = ('Kindlewood Overgrowth Bonfire Left_Kindlewood Overgrowth Bonfire Main', Regions.KINDLEWOOD_OVERGROWTH_BONFIRE_LEFT, Regions.KINDLEWOOD_OVERGROWTH_BONFIRE_MAIN, CanBurrow()),
    KINDLEWOOD_OVERGROWTH_BONFIRE_MAIN_KINDLEWOOD_OVERGROWTH_BONFIRE_LEFT = ('Kindlewood Overgrowth Bonfire Main_Kindlewood Overgrowth Bonfire Left', Regions.KINDLEWOOD_OVERGROWTH_BONFIRE_MAIN, Regions.KINDLEWOOD_OVERGROWTH_BONFIRE_LEFT, CanBurrow()),
    KINDLEWOOD_OVERGROWTH_BONFIRE_TOP_KINDLEWOOD_OVERGROWTH_BONFIRE_LEFT = ('Kindlewood Overgrowth Bonfire Top_Kindlewood Overgrowth Bonfire Left', Regions.KINDLEWOOD_OVERGROWTH_BONFIRE_TOP, Regions.KINDLEWOOD_OVERGROWTH_BONFIRE_LEFT, CanBurrow()),
    KINDLEWOOD_OVERGROWTH_ENTRY_MAIN_KINDLEWOOD_OVERGROWTH_ENTRY_UPPER_LEFT = ('Kindlewood Overgrowth Entry Main_Kindlewood Overgrowth Entry Upper Left', Regions.KINDLEWOOD_OVERGROWTH_ENTRY_MAIN, Regions.KINDLEWOOD_OVERGROWTH_ENTRY_UPPER_LEFT, True_()),
    KINDLEWOOD_OVERGROWTH_RESIDENCE_BARN_BURROW_KINDLEWOOD_OVERGROWTH_RESIDENCE_BARN = ('Kindlewood Overgrowth Residence Barn Burrow_Kindlewood Overgrowth Residence Barn', Regions.KINDLEWOOD_OVERGROWTH_RESIDENCE_BARN_BURROW, Regions.KINDLEWOOD_OVERGROWTH_RESIDENCE_BARN, CanClimb()),
    KINDLEWOOD_OVERGROWTH_RESIDENCE_BARN_KINDLEWOOD_OVERGROWTH_RESIDENCE_BARN_BURROW = ('Kindlewood Overgrowth Residence Barn_Kindlewood Overgrowth Residence Barn Burrow', Regions.KINDLEWOOD_OVERGROWTH_RESIDENCE_BARN, Regions.KINDLEWOOD_OVERGROWTH_RESIDENCE_BARN_BURROW, CanCarry()),
    KINDLEWOOD_RAIL_TUNNEL_TRACKS_KINDLEWOOD_RAIL_TUNNEL = ('Kindlewood Rail Tunnel Tracks_Kindlewood Rail Tunnel', Regions.KINDLEWOOD_RAIL_TUNNEL_TRACKS, Regions.KINDLEWOOD_RAIL_TUNNEL, CanBurrow() & CanClimb()),
    KINDLEWOOD_RAIL_TUNNEL_KINDLEWOOD_RAIL_TUNNEL_TRACKS = ('Kindlewood Rail Tunnel_Kindlewood Rail Tunnel Tracks', Regions.KINDLEWOOD_RAIL_TUNNEL, Regions.KINDLEWOOD_RAIL_TUNNEL_TRACKS, CanBurrow() & CanClimb()),
    KINDLEWOOD_WALLOWERS_PATH_END_KINDLEWOOD_WALLOWERS_PATH = ('Kindlewood Wallowers Path End_Kindlewood Wallowers Path', Regions.KINDLEWOOD_WALLOWERS_PATH_END, Regions.KINDLEWOOD_WALLOWERS_PATH, CanBurrow()),
    KINDLEWOOD_WALLOWERS_PATH_KINDLEWOOD_WALLOWER_S_PATH_CLIFF_BUSH = ("Kindlewood Wallowers Path_Kindlewood Wallower's Path Cliff Bush", Regions.KINDLEWOOD_WALLOWERS_PATH, Regions.KINDLEWOOD_WALLOWER_S_PATH_CLIFF_BUSH, CanBurrow()),
    KINDLEWOOD_WALLOWERS_PATH_KINDLEWOOD_WALLOWERS_PATH_END = ('Kindlewood Wallowers Path_Kindlewood Wallowers Path End', Regions.KINDLEWOOD_WALLOWERS_PATH, Regions.KINDLEWOOD_WALLOWERS_PATH_END, HasTrinket(trinket=Trinkets.WALLOWERS_GAUNTLETS.value) | CanJumpTiles(distance=7, has_wall=True)),

class RegionTransitions(TransitionTypeEnum):
    KINDLEWOOD_BEHIND_MADD_HOUSE_SOUTH_BURROW = ('Kindlewood Behind Madd House South Burrow', Regions.KINDLEWOOD_BEHIND_MADD_HOUSE, Regions.KINDLEWOOD_OVERGROWTH_MADD_ARENA, DirectionType.SOUTH, TransitionType.BURROW, PowerLevelThreshold(power=25)),
    KINDLEWOOD_FARM_CROSSING_ABOVE_SCHOOL_EAST_BURROW = ('Kindlewood Farm Crossing Above School East Burrow', Regions.KINDLEWOOD_FARM_CROSSING_ABOVE_SCHOOL, Regions.KINDLEWOOD_FARM_CROSSING_PUMPKIN_PATCH, DirectionType.EAST, TransitionType.BURROW, CanBurrow()),
    KINDLEWOOD_FARM_CROSSING_DO_NOT_RANDOMIZE_ENTRANCE = ('Kindlewood Farm Crossing Do_Not_Randomize_Entrance', Regions.KINDLEWOOD_FARM_CROSSING, Regions.OSSEX_TRAIN_CABOOSE, DirectionType.OVERWORLD, TransitionType.DO_NOT_RANDOMIZE_ENTRANCE, Has(PermanentUpgrades.TRAIN_PASS.value)),
    KINDLEWOOD_FARM_CROSSING_PUMPKIN_PATCH_NORTH_BURROW = ('Kindlewood Farm Crossing Pumpkin Patch North Burrow', Regions.KINDLEWOOD_FARM_CROSSING_PUMPKIN_PATCH, Regions.KINDLEWOOD_FARM_CROSSING_SHACK, DirectionType.NORTH, TransitionType.BURROW, CanBurrow()),
    KINDLEWOOD_FARM_CROSSING_PUMPKIN_PATCH_WEST_BURROW = ('Kindlewood Farm Crossing Pumpkin Patch West Burrow', Regions.KINDLEWOOD_FARM_CROSSING_PUMPKIN_PATCH, Regions.KINDLEWOOD_FARM_CROSSING_ABOVE_SCHOOL, DirectionType.WEST, TransitionType.BURROW, CanBurrow()),
    KINDLEWOOD_FARM_CROSSING_SHACK_EAST_BURROW = ('Kindlewood Farm Crossing Shack East Burrow', Regions.KINDLEWOOD_FARM_CROSSING_SHACK, Regions.KINDLEWOOD_FARM_CROSSING_SHACK_OUTSIDE, DirectionType.EAST, TransitionType.BURROW, CanBurrow()),
    KINDLEWOOD_FARM_CROSSING_SHACK_OUTSIDE_WEST_BURROW = ('Kindlewood Farm Crossing Shack Outside West Burrow', Regions.KINDLEWOOD_FARM_CROSSING_SHACK_OUTSIDE, Regions.KINDLEWOOD_FARM_CROSSING_SHACK, DirectionType.WEST, TransitionType.BURROW, CanBurrow()),
    KINDLEWOOD_FARM_CROSSING_SHACK_SOUTH_BURROW = ('Kindlewood Farm Crossing Shack South Burrow', Regions.KINDLEWOOD_FARM_CROSSING_SHACK, Regions.KINDLEWOOD_FARM_CROSSING_PUMPKIN_PATCH, DirectionType.SOUTH, TransitionType.BURROW, CanBurrow()),
    KINDLEWOOD_FARM_CROSSING_SOUTH_BURROW = ('Kindlewood Farm Crossing South Burrow', Regions.KINDLEWOOD_FARM_CROSSING, Regions.KINDLEWOOD_WALLOWERS_PATH, DirectionType.SOUTH, TransitionType.BURROW, True_()),
    KINDLEWOOD_FARM_CROSSING_WEST_TRANSITION = ('Kindlewood Farm Crossing West Transition', Regions.KINDLEWOOD_FARM_CROSSING, Regions.KINDLEWOOD_SCHOOL_YARD, DirectionType.WEST, TransitionType.SCREENS, True_()),
    KINDLEWOOD_FARM_TOMATO_PIPE = ('Kindlewood Farm Tomato Pipe', Regions.KINDLEWOOD_FARM_TOMATO, Regions.KINDLEWOOD_FARM_CROSSING_PUMPKIN_PATCH, DirectionType.OVERWORLD, TransitionType.DO_NOT_RANDOMIZE_ENTRANCE, True_()),
    KINDLEWOOD_OVERGROWTH_BEHIND_RESIDENCE_LAWN_SOUTH_BURROW = ('Kindlewood Overgrowth Behind Residence Lawn South Burrow', Regions.KINDLEWOOD_OVERGROWTH_BEHIND_RESIDENCE_LAWN, Regions.KINDLEWOOD_OVERGROWTH_RESIDENCE_BARN_BURROW, DirectionType.SOUTH, TransitionType.BURROW, CanBurrow()),
    KINDLEWOOD_OVERGROWTH_BEHIND_RESIDENCE_WEST_TRANSITION = ('Kindlewood Overgrowth Behind Residence West Transition', Regions.KINDLEWOOD_OVERGROWTH_BEHIND_RESIDENCE, Regions.KINDLEWOOD_OVERGROWTH_BONFIRE_TOP, DirectionType.WEST, TransitionType.SCREENS, True_()),
    KINDLEWOOD_OVERGROWTH_BONFIRE_LEFT_SOUTH_BURROW = ('Kindlewood Overgrowth Bonfire Left South Burrow', Regions.KINDLEWOOD_OVERGROWTH_BONFIRE_LEFT, Regions.KINDLEWOOD_OVERGROWTH_ENTRY_UPPER_LEFT, DirectionType.SOUTH, TransitionType.BURROW, CanBurrow()),
    KINDLEWOOD_OVERGROWTH_BONFIRE_LEFT_WEST_BURROW = ('Kindlewood Overgrowth Bonfire Left West Burrow', Regions.KINDLEWOOD_OVERGROWTH_BONFIRE_LEFT, Regions.KINDLEWOOD_WALLOWER_S_PATH_CLIFF_BUSH, DirectionType.WEST, TransitionType.BURROW, CanBurrow()),
    KINDLEWOOD_OVERGROWTH_BONFIRE_MAIN_EAST_TRANSITION = ('Kindlewood Overgrowth Bonfire Main East Transition', Regions.KINDLEWOOD_OVERGROWTH_BONFIRE_MAIN, Regions.KINDLEWOOD_OVERGROWTH_RESIDENCE_YARD, DirectionType.EAST, TransitionType.SCREENS, True_()),
    KINDLEWOOD_OVERGROWTH_BONFIRE_TOP_EAST_TRANSITION = ('Kindlewood Overgrowth Bonfire Top East Transition', Regions.KINDLEWOOD_OVERGROWTH_BONFIRE_TOP, Regions.KINDLEWOOD_OVERGROWTH_BEHIND_RESIDENCE, DirectionType.EAST, TransitionType.SCREENS, True_()),
    KINDLEWOOD_OVERGROWTH_BONFIRE_TOP_NORTH_TRANSITION = ('Kindlewood Overgrowth Bonfire Top North Transition', Regions.KINDLEWOOD_OVERGROWTH_BONFIRE_TOP, Regions.KINDLEWOOD_OVERGROWTH_MADD_ARENA, DirectionType.NORTH, TransitionType.SCREENS, True_()),
    KINDLEWOOD_OVERGROWTH_ENTRY_MAIN_EAST_AREA_TRANSITION = ('Kindlewood Overgrowth Entry Main East Area Transition', Regions.KINDLEWOOD_OVERGROWTH_ENTRY_MAIN, Regions.WESTERN_WILDS_BRUTES, DirectionType.EAST, TransitionType.AREA_SCREENS, CanBurrow()),
    KINDLEWOOD_OVERGROWTH_ENTRY_UPPER_LEFT_NORTH_BURROW = ('Kindlewood Overgrowth Entry Upper Left North Burrow', Regions.KINDLEWOOD_OVERGROWTH_ENTRY_UPPER_LEFT, Regions.KINDLEWOOD_OVERGROWTH_BONFIRE_LEFT, DirectionType.NORTH, TransitionType.BURROW, CanBurrow()),
    KINDLEWOOD_OVERGROWTH_MADD_ARENA_BOTTOM_WEST_TRANSITION = ('Kindlewood Overgrowth Madd Arena Bottom West Transition', Regions.KINDLEWOOD_OVERGROWTH_MADD_ARENA, Regions.KINDLEWOOD_FARM_CROSSING_ENTRANCE, DirectionType.WEST, TransitionType.SCREENS, PowerLevelThreshold(power=25)),
    KINDLEWOOD_OVERGROWTH_MADD_ARENA_DOORS = ('Kindlewood Overgrowth Madd Arena Doors', Regions.KINDLEWOOD_OVERGROWTH_MADD_ARENA, Regions.KINDLEWOOD_OVERGROWTH_MADD_HOUSE, DirectionType.NORTH, TransitionType.DOORS, PowerLevelThreshold(power=25)),
    KINDLEWOOD_OVERGROWTH_MADD_ARENA_NORTH_BURROW = ('Kindlewood Overgrowth Madd Arena North Burrow', Regions.KINDLEWOOD_OVERGROWTH_MADD_ARENA, Regions.KINDLEWOOD_BEHIND_MADD_HOUSE, DirectionType.NORTH, TransitionType.BURROW, CanCarry() & CanBurrow() & HasAccessToTorch() & PowerLevelThreshold(power=25)),
    KINDLEWOOD_OVERGROWTH_MADD_ARENA_SOUTH_TRANSITION = ('Kindlewood Overgrowth Madd Arena South Transition', Regions.KINDLEWOOD_OVERGROWTH_MADD_ARENA, Regions.KINDLEWOOD_OVERGROWTH_BONFIRE_TOP, DirectionType.SOUTH, TransitionType.SCREENS, PowerLevelThreshold(power=25)),
    KINDLEWOOD_OVERGROWTH_MADD_ARENA_TOP_WEST_TRANSITION = ('Kindlewood Overgrowth Madd Arena Top West Transition', Regions.KINDLEWOOD_OVERGROWTH_MADD_ARENA, Regions.KINDLEWOOD_FARM_CROSSING_ENTRANCE, DirectionType.WEST, TransitionType.SCREENS, PowerLevelThreshold(power=25)),
    KINDLEWOOD_OVERGROWTH_MADD_HOUSE_DOORS = ('Kindlewood Overgrowth Madd House Doors', Regions.KINDLEWOOD_OVERGROWTH_MADD_HOUSE, Regions.KINDLEWOOD_OVERGROWTH_MADD_ARENA, DirectionType.SOUTH, TransitionType.DOORS, True_()),
    KINDLEWOOD_OVERGROWTH_RESIDENCE_BARN_BURROW_NORTH_BURROW = ('Kindlewood Overgrowth Residence Barn Burrow North Burrow', Regions.KINDLEWOOD_OVERGROWTH_RESIDENCE_BARN_BURROW, Regions.KINDLEWOOD_OVERGROWTH_BEHIND_RESIDENCE_LAWN, DirectionType.NORTH, TransitionType.BURROW, CanBurrow()),
    KINDLEWOOD_OVERGROWTH_RESIDENCE_BARN_DOORS = ('Kindlewood Overgrowth Residence Barn Doors', Regions.KINDLEWOOD_OVERGROWTH_RESIDENCE_BARN, Regions.KINDLEWOOD_OVERGROWTH_RESIDENCE_YARD, DirectionType.SOUTH, TransitionType.DOORS, True_()),
    KINDLEWOOD_OVERGROWTH_RESIDENCE_BARN_GEYSER_DOWN = ('Kindlewood Overgrowth Residence Barn Geyser_Down', Regions.KINDLEWOOD_OVERGROWTH_RESIDENCE_BARN, Regions.KINDLEWOOD_OVERGROWTH_RESIDENCE_BASEMENT, DirectionType.OVERWORLD, TransitionType.GEYSER_DOWN, CanCarry()),
    KINDLEWOOD_OVERGROWTH_RESIDENCE_BASEMENT_GEYSER_UP = ('Kindlewood Overgrowth Residence Basement Geyser_Up', Regions.KINDLEWOOD_OVERGROWTH_RESIDENCE_BASEMENT, Regions.KINDLEWOOD_OVERGROWTH_RESIDENCE_BARN, DirectionType.OVERWORLD, TransitionType.GEYSER_UP, True_()),
    KINDLEWOOD_OVERGROWTH_RESIDENCE_YARD_DOORS = ('Kindlewood Overgrowth Residence Yard Doors', Regions.KINDLEWOOD_OVERGROWTH_RESIDENCE_YARD, Regions.KINDLEWOOD_OVERGROWTH_RESIDENCE_BARN, DirectionType.NORTH, TransitionType.DOORS, True_()),
    KINDLEWOOD_OVERGROWTH_RESIDENCE_YARD_WEST_TRANSITION = ('Kindlewood Overgrowth Residence Yard West Transition', Regions.KINDLEWOOD_OVERGROWTH_RESIDENCE_YARD, Regions.KINDLEWOOD_OVERGROWTH_BONFIRE_MAIN, DirectionType.WEST, TransitionType.SCREENS, True_()),
    KINDLEWOOD_RAIL_TUNNEL_TRACKS_WEST_TRANSITION = ('Kindlewood Rail Tunnel Tracks West Transition', Regions.KINDLEWOOD_RAIL_TUNNEL_TRACKS, Regions.KINDLEWOOD_TRAIN_TRACKS, DirectionType.WEST, TransitionType.SCREENS, True_()),
    KINDLEWOOD_SCHOOL_BACKYARD_DOORS = ('Kindlewood School Backyard Doors', Regions.KINDLEWOOD_SCHOOL_BACKYARD, Regions.KINDLEWOOD_SCHOOL_SIDE, DirectionType.NORTH, TransitionType.DOORS, True_()),
    KINDLEWOOD_SCHOOL_BACKYARD_STAIRS = ('Kindlewood School Backyard Stairs', Regions.KINDLEWOOD_SCHOOL_BACKYARD, Regions.SEPTEMBURG_WASTEWATER_CANAL_WELL_ENTRANCE, DirectionType.NORTH, TransitionType.STAIRS, CanClimb()),
    KINDLEWOOD_SCHOOL_DOORS = ('Kindlewood School Doors', Regions.KINDLEWOOD_SCHOOL, Regions.KINDLEWOOD_SCHOOL_YARD, DirectionType.SOUTH, TransitionType.DOORS, True_()),
    KINDLEWOOD_SCHOOL_SIDE_DOORS = ('Kindlewood School Side Doors', Regions.KINDLEWOOD_SCHOOL_SIDE, Regions.KINDLEWOOD_SCHOOL_BACKYARD, DirectionType.SOUTH, TransitionType.DOORS, True_()),
    KINDLEWOOD_SCHOOL_SIDE_EAST_BURROW = ('Kindlewood School Side East Burrow', Regions.KINDLEWOOD_SCHOOL_SIDE, Regions.KINDLEWOOD_SCHOOL, DirectionType.EAST, TransitionType.BURROW, True_()),
    KINDLEWOOD_SCHOOL_WEST_BURROW = ('Kindlewood School West Burrow', Regions.KINDLEWOOD_SCHOOL, Regions.KINDLEWOOD_SCHOOL_SIDE, DirectionType.WEST, TransitionType.BURROW, True_()),
    KINDLEWOOD_SCHOOL_YARD_DOORS = ('Kindlewood School Yard Doors', Regions.KINDLEWOOD_SCHOOL_YARD, Regions.KINDLEWOOD_SCHOOL, DirectionType.NORTH, TransitionType.DOORS, True_()),
    KINDLEWOOD_SCHOOL_YARD_EAST_TRANSITION = ('Kindlewood School Yard East Transition', Regions.KINDLEWOOD_SCHOOL_YARD, Regions.KINDLEWOOD_FARM_CROSSING, DirectionType.EAST, TransitionType.SCREENS, True_()),
    KINDLEWOOD_SCHOOL_YARD_WEST_AREA_TRANSITION = ('Kindlewood School Yard West Area Transition', Regions.KINDLEWOOD_SCHOOL_YARD, Regions.SEPTEMBURG_WITHERED_FARMS_START_EAST, DirectionType.WEST, TransitionType.AREA_SCREENS, True_()),
    KINDLEWOOD_TRAIN_TRACKS_EAST_TRANSITION = ('Kindlewood Train Tracks East Transition', Regions.KINDLEWOOD_TRAIN_TRACKS, Regions.KINDLEWOOD_RAIL_TUNNEL_TRACKS, DirectionType.EAST, TransitionType.SCREENS, True_()),
    KINDLEWOOD_WALLOWER_S_PATH_CLIFF_BUSH_EAST_BURROW = ("Kindlewood Wallower's Path Cliff Bush East Burrow", Regions.KINDLEWOOD_WALLOWER_S_PATH_CLIFF_BUSH, Regions.KINDLEWOOD_OVERGROWTH_BONFIRE_LEFT, DirectionType.EAST, TransitionType.BURROW, True_()),
    KINDLEWOOD_WALLOWERS_PATH_NORTH_BURROW = ('Kindlewood Wallowers Path North Burrow', Regions.KINDLEWOOD_WALLOWERS_PATH, Regions.KINDLEWOOD_FARM_CROSSING, DirectionType.NORTH, TransitionType.BURROW, True_()),

