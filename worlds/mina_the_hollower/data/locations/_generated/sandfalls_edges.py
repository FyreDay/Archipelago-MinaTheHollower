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
    SANDFALLS_BONE_JUNCTION_SANDS_SANDFALLS_SIFTED_SANDS = ('Sandfalls Bone Junction Sands_Sandfalls Sifted Sands', Regions.SANDFALLS_BONE_JUNCTION_SANDS, Regions.SANDFALLS_SIFTED_SANDS, True_())
    SANDFALLS_BONE_JUNCTION_STAIR_SANDFALLS_BONE_JUNCTION = ('Sandfalls Bone Junction Stair_Sandfalls Bone Junction', Regions.SANDFALLS_BONE_JUNCTION_STAIR, Regions.SANDFALLS_BONE_JUNCTION, CanBurrow() & RepairedGenerator(event=BONE_BEACH_DATA) & CanCarry())
    SANDFALLS_BONE_JUNCTION_SANDFALLS_BONE_JUNCTION_STAIR = ('Sandfalls Bone Junction_Sandfalls Bone Junction Stair', Regions.SANDFALLS_BONE_JUNCTION, Regions.SANDFALLS_BONE_JUNCTION_STAIR, CanBurrow() & RepairedGenerator(event=BONE_BEACH_DATA) & CanCarry())
    SANDFALLS_MINERS_DEN_ENTRANCE_TOP_SANDFALLS_MINERS_DEN_ENTRANCE = ('Sandfalls Miners Den Entrance Top_Sandfalls Miners Den Entrance', Regions.SANDFALLS_MINERS_DEN_ENTRANCE_TOP, Regions.SANDFALLS_MINERS_DEN_ENTRANCE, CanClimb())
    SANDFALLS_MINERS_DEN_ENTRANCE_SANDFALLS_MINERS_DEN_ENTRANCE_TOP = ('Sandfalls Miners Den Entrance_Sandfalls Miners Den Entrance Top', Regions.SANDFALLS_MINERS_DEN_ENTRANCE, Regions.SANDFALLS_MINERS_DEN_ENTRANCE_TOP, CanClimb())
    SANDFALLS_PAYLOAD_PASSAGE_BOTTOM_SANDFALLS_PAYLOAD_PASSAGE_CHEST = ('Sandfalls Payload Passage Bottom_Sandfalls Payload Passage Chest', Regions.SANDFALLS_PAYLOAD_PASSAGE_BOTTOM, Regions.SANDFALLS_PAYLOAD_PASSAGE_CHEST, CanJumpTiles(distance=2))
    SANDFALLS_PAYLOAD_PASSAGE_CHEST_SANDFALLS_PAYLOAD_PASSAGE_BOTTOM = ('Sandfalls Payload Passage Chest_Sandfalls Payload Passage Bottom', Regions.SANDFALLS_PAYLOAD_PASSAGE_CHEST, Regions.SANDFALLS_PAYLOAD_PASSAGE_BOTTOM, CanJumpTiles(distance=5, has_wall=True))
    SANDFALLS_SIFTED_SANDS_FUNNEL_SANDFALLS_SIFTED_SANDS = ('Sandfalls Sifted Sands Funnel_Sandfalls Sifted Sands', Regions.SANDFALLS_SIFTED_SANDS_FUNNEL, Regions.SANDFALLS_SIFTED_SANDS, CanClimb())
    SANDFALLS_SIFTED_SANDS_HIDDEN_LEFT_BOMB_SANDFALLS_SIFTED_SANDS = ('Sandfalls Sifted Sands Hidden Left Bomb_Sandfalls Sifted Sands', Regions.SANDFALLS_SIFTED_SANDS_HIDDEN_LEFT_BOMB, Regions.SANDFALLS_SIFTED_SANDS, CanCarry())
    SANDFALLS_SIFTED_SANDS_SANDFALLS_SIFTED_SANDS_FUNNEL = ('Sandfalls Sifted Sands_Sandfalls Sifted Sands Funnel', Regions.SANDFALLS_SIFTED_SANDS, Regions.SANDFALLS_SIFTED_SANDS_FUNNEL, True_())

class RegionTransitions(TransitionTypeEnum):
    SANDFALLS_BONE_JUNCTION_BURROW_EAST = ('Sandfalls Bone Junction Burrow East', Regions.SANDFALLS_BONE_JUNCTION, Regions.BONE_BEACH_BONE_RUSH_MINE, DirectionType.EAST, TransitionType.BURROW, CanBurrow() & RepairedGenerator(event=BONE_BEACH_DATA) & CanCarry())
    SANDFALLS_BONE_JUNCTION_EAST_TRANSITION = ('Sandfalls Bone Junction East Transition', Regions.SANDFALLS_BONE_JUNCTION, Regions.BONE_BEACH_SHORELINE_GENERATOR, DirectionType.EAST, TransitionType.SCREENS, True_())
    SANDFALLS_BONE_JUNCTION_NORTH_TRANSITION = ('Sandfalls Bone Junction North Transition', Regions.SANDFALLS_BONE_JUNCTION_STAIR, Regions.SANDFALLS_BONE_JUNCTION_PLANK, DirectionType.NORTH, TransitionType.SCREENS, True_())
    SANDFALLS_BONE_JUNCTION_PLANK_SOUTH_TRANSITION = ('Sandfalls Bone Junction Plank South Transition', Regions.SANDFALLS_BONE_JUNCTION_PLANK, Regions.SANDFALLS_BONE_JUNCTION_STAIR, DirectionType.SOUTH, TransitionType.SCREENS, True_())
    SANDFALLS_BONE_JUNCTION_PLANK_WEST_AREA_TRANSITION = ('Sandfalls Bone Junction Plank West Area Transition', Regions.SANDFALLS_BONE_JUNCTION_PLANK, Regions.MOURNERS_MILE_SPIKE_HELL_SANDFALL, DirectionType.WEST, TransitionType.AREA_SCREENS, True_())
    SANDFALLS_BONE_JUNCTION_SANDS_EAST_TRANSITION = ('Sandfalls Bone Junction Sands East Transition', Regions.SANDFALLS_BONE_JUNCTION_SANDS, Regions.SANDFALLS_BONE_JUNCTION, DirectionType.OVERWORLD, TransitionType.DO_NOT_RANDOMIZE_ENTRANCE, True_())
    SANDFALLS_BONE_JUNCTION_WEST_TRANSITION = ('Sandfalls Bone Junction West Transition', Regions.SANDFALLS_BONE_JUNCTION, Regions.SANDFALLS_BONE_JUNCTION_SANDS, DirectionType.OVERWORLD, TransitionType.DO_NOT_RANDOMIZE_ENTRANCE, True_())
    SANDFALLS_MINERS_DEN_ENTRANCE_EAST_TRANSITION = ('Sandfalls Miners Den Entrance East Transition', Regions.SANDFALLS_MINERS_DEN_ENTRANCE, Regions.SANDFALLS_MINERS_DEN_PATH, DirectionType.EAST, TransitionType.SCREENS, True_())
    SANDFALLS_MINERS_DEN_ENTRANCE_EXIT = ('Sandfalls Miners Den Entrance Exit', Regions.SANDFALLS_MINERS_DEN_ENTRANCE_TOP, Regions.SANDFALLS_SIFTED_SANDS, DirectionType.NORTH, TransitionType.STAIRS, CanClimb())
    SANDFALLS_MINERS_DEN_NORTH_TRANSITION = ('Sandfalls Miners Den North Transition', Regions.SANDFALLS_MINERS_DEN, Regions.SANDFALLS_MINERS_DEN_PATH, DirectionType.NORTH, TransitionType.SCREENS, True_())
    SANDFALLS_MINERS_DEN_OUTSKIRT_NORTH_TRANSITION = ('Sandfalls Miners Den Outskirt North Transition', Regions.SANDFALLS_MINERS_DEN_OUTSKIRT, Regions.SANDFALLS_MINERS_DEN, DirectionType.NORTH, TransitionType.SCREENS, True_())
    SANDFALLS_MINERS_DEN_OUTSKIRT_STAIRS = ('Sandfalls Miners Den Outskirt Stairs', Regions.SANDFALLS_MINERS_DEN_OUTSKIRT, Regions.BONE_BEACH_BONE_RUSH_MINE, DirectionType.NORTH, TransitionType.STAIRS, True_())
    SANDFALLS_MINERS_DEN_PATH_SOUTH_TRANSITION = ('Sandfalls Miners Den Path South Transition', Regions.SANDFALLS_MINERS_DEN_PATH, Regions.SANDFALLS_MINERS_DEN, DirectionType.SOUTH, TransitionType.SCREENS, True_())
    SANDFALLS_MINERS_DEN_PATH_WEST_TRANSITION = ('Sandfalls Miners Den Path West Transition', Regions.SANDFALLS_MINERS_DEN_PATH, Regions.SANDFALLS_MINERS_DEN_ENTRANCE, DirectionType.WEST, TransitionType.SCREENS, True_())
    SANDFALLS_MINERS_DEN_SOUTH_TRANSITION = ('Sandfalls Miners Den South Transition', Regions.SANDFALLS_MINERS_DEN, Regions.SANDFALLS_MINERS_DEN_OUTSKIRT, DirectionType.SOUTH, TransitionType.SCREENS, True_())
    SANDFALLS_MINING_OUTLOOK = ('Sandfalls Mining Outlook', Regions.SANDFALLS_MINING_OUTLOOK, Regions.SOUTHERN_OUTSKIRTS_FOUR_FLOWERS_SANDFALL, DirectionType.WEST, TransitionType.AREA_SCREENS, True_())
    SANDFALLS_MINING_OUTLOOK_CAVE_STAIRS = ('Sandfalls Mining Outlook Cave Stairs', Regions.SANDFALLS_MINING_OUTLOOK, Regions.SOUTHERN_OUTSKIRTS_MINING_PASSAGE_EXIT, DirectionType.NORTH, TransitionType.STAIRS, True_())
    SANDFALLS_MINING_OUTLOOK_SANDFALLS_SIFTED_SANDS = ('Sandfalls Mining Outlook_Sandfalls Sifted Sands', Regions.SANDFALLS_MINING_OUTLOOK, Regions.SANDFALLS_SIFTED_SANDS, DirectionType.SOUTH, TransitionType.SCREENS, True_())
    SANDFALLS_PACHINKO_EXIT = ('Sandfalls Pachinko Exit', Regions.SANDFALLS_PACHINKO, Regions.SANDFALLS_SIFTED_SANDS, DirectionType.SOUTH, TransitionType.DOORS, True_())
    SANDFALLS_PAYLOAD_PASSAGE_BOTTOM_BURROW_WEST = ('Sandfalls Payload Passage Bottom Burrow West', Regions.SANDFALLS_PAYLOAD_PASSAGE_BOTTOM, Regions.SANDFALLS_SANDWATER_JUNCTION_TOP, DirectionType.WEST, TransitionType.BURROW, CanBurrow() & HasKear(kear=SingleKears.SANDFALLS_PAYLOAD_PASSAGE_BOTTOM_KEAR.value))
    SANDFALLS_PAYLOAD_PASSAGE_CHEST_EAST_BURROW = ('Sandfalls Payload Passage Chest East Burrow', Regions.SANDFALLS_PAYLOAD_PASSAGE_CHEST, Regions.SANDFALLS_SIFTED_SANDS, DirectionType.EAST, TransitionType.BURROW, CanBurrow())
    SANDFALLS_PAYLOAD_PASSAGE_EAST_BURROW_1 = ('Sandfalls Payload Passage East Burrow 1', Regions.SANDFALLS_PAYLOAD_PASSAGE, Regions.SANDFALLS_SIFTED_SANDS, DirectionType.EAST, TransitionType.BURROW, CanBurrow())
    SANDFALLS_PAYLOAD_PASSAGE_EAST_BURROW_2 = ('Sandfalls Payload Passage East Burrow 2', Regions.SANDFALLS_PAYLOAD_PASSAGE, Regions.SANDFALLS_SIFTED_SANDS, DirectionType.EAST, TransitionType.BURROW, CanBurrow())
    SANDFALLS_RING_DIVE_PARLOR_GEYSER_UP = ('Sandfalls Ring Dive Parlor Geyser Up', Regions.SANDFALLS_RING_DIVE_PARLOR, Regions.SANDFALLS_SIFTED_SANDS_FUNNEL, DirectionType.OVERWORLD, TransitionType.GEYSER_UP, True_())
    SANDFALLS_SANDWATER_JUNCTION_NORTH_ROPE = ('Sandfalls Sandwater Junction North Rope', Regions.SANDFALLS_SANDWATER_JUNCTION, Regions.SANDFALLS_SANDWATER_JUNCTION_TOP, DirectionType.NORTH, TransitionType.SCREENS, CanClimb())
    SANDFALLS_SANDWATER_JUNCTION_SOUTH_ROPE = ('Sandfalls Sandwater Junction South Rope', Regions.SANDFALLS_SANDWATER_JUNCTION, Regions.LONERS_LANDING_BOARDWALK_SANDFALLS_LEDGE, DirectionType.SOUTH, TransitionType.SCREENS, CanClimb())
    SANDFALLS_SANDWATER_JUNCTION_SOUTH_TRANSITION = ('Sandfalls Sandwater Junction South Transition', Regions.SANDFALLS_SANDWATER_JUNCTION, Regions.LONERS_LANDING_BOARDWALK_SANDFALLS_LAKE, DirectionType.SOUTH, TransitionType.SCREENS, True_())
    SANDFALLS_SANDWATER_JUNCTION_TOP_BURROW_EAST = ('Sandfalls Sandwater Junction Top Burrow East', Regions.SANDFALLS_SANDWATER_JUNCTION_TOP, Regions.SANDFALLS_PAYLOAD_PASSAGE_BOTTOM, DirectionType.EAST, TransitionType.BURROW, CanBurrow() & HasKear(kear=SingleKears.SANDFALLS_PAYLOAD_PASSAGE_BOTTOM_KEAR.value))
    SANDFALLS_SANDWATER_JUNCTION_TOP_SOUTH_ROPE = ('Sandfalls Sandwater Junction Top South Rope', Regions.SANDFALLS_SANDWATER_JUNCTION_TOP, Regions.SANDFALLS_SANDWATER_JUNCTION, DirectionType.SOUTH, TransitionType.SCREENS, CanClimb())
    SANDFALLS_SANDY_STATION_NORTH_TRANSITION = ('Sandfalls Sandy Station North Transition', Regions.SANDFALLS_SANDY_STATION, Regions.SANDFALLS_SIFTED_SANDS, DirectionType.NORTH, TransitionType.SCREENS, True_())
    SANDFALLS_SANDY_STATION_TRAIN = ('Sandfalls Sandy Station Train', Regions.SANDFALLS_SANDY_STATION, Regions.OSSEX_TRAIN_CABOOSE, DirectionType.OVERWORLD, TransitionType.DO_NOT_RANDOMIZE_ENTRANCE, Has(PermanentUpgrades.TRAIN_PASS.value))
    SANDFALLS_SHIFTY_SECLUSION_EXIT = ('Sandfalls Shifty Seclusion Exit', Regions.SANDFALLS_SHIFTY_SECLUSION, Regions.SANDFALLS_SIFTED_SANDS, DirectionType.SOUTH, TransitionType.DOORS, True_())
    SANDFALLS_SIFTED_SANDS_BURROW_WEST = ('Sandfalls Sifted Sands Burrow West', Regions.SANDFALLS_SIFTED_SANDS, Regions.SANDFALLS_PAYLOAD_PASSAGE_CHEST, DirectionType.WEST, TransitionType.BURROW, CanBurrow() & CanCarry())
    SANDFALLS_SIFTED_SANDS_DEN_DOOR = ('Sandfalls Sifted Sands Den Door', Regions.SANDFALLS_SIFTED_SANDS, Regions.SANDFALLS_MINERS_DEN_ENTRANCE_TOP, DirectionType.NORTH, TransitionType.STAIRS, HasVialsCount(count=3) & CanBurrow() & CanCarry())
    SANDFALLS_SIFTED_SANDS_EAST_MOVING_BURROW = ('Sandfalls Sifted Sands East Moving Burrow', Regions.SANDFALLS_SIFTED_SANDS, Regions.SANDFALLS_SIFTED_SANDS_HIDDEN_CAVE, DirectionType.EAST, TransitionType.BURROW, CanBurrow())
    SANDFALLS_SIFTED_SANDS_FUNNEL_GEYSER_DOWN = ('Sandfalls Sifted Sands Funnel Geyser Down', Regions.SANDFALLS_SIFTED_SANDS_FUNNEL, Regions.SANDFALLS_RING_DIVE_PARLOR, DirectionType.OVERWORLD, TransitionType.GEYSER_DOWN, True_())
    SANDFALLS_SIFTED_SANDS_HIDDEN_LEFT_BOMB_SOUTH_TRANSITION = ('Sandfalls Sifted Sands Hidden Left Bomb South Transition', Regions.SANDFALLS_SIFTED_SANDS_HIDDEN_LEFT_BOMB, Regions.SANDFALLS_SPIKE_SQUARES, DirectionType.SOUTH, TransitionType.SCREENS, True_())
    SANDFALLS_SIFTED_SANDS_NORTH_TRANSITION = ('Sandfalls Sifted Sands North Transition', Regions.SANDFALLS_SIFTED_SANDS, Regions.SANDFALLS_MINING_OUTLOOK, DirectionType.NORTH, TransitionType.SCREENS, True_())
    SANDFALLS_SIFTED_SANDS_PACHINKO_CAVE = ('Sandfalls Sifted Sands Pachinko Cave', Regions.SANDFALLS_SIFTED_SANDS, Regions.SANDFALLS_PACHINKO, DirectionType.NORTH, TransitionType.DOORS, HasKear(kear=SingleKears.SANDFALL_CAVE_KEAR.value))
    SANDFALLS_SIFTED_SANDS_PAYLOAD_WEST_BURROW_1 = ('Sandfalls Sifted Sands Payload West Burrow 1', Regions.SANDFALLS_SIFTED_SANDS, Regions.SANDFALLS_PAYLOAD_PASSAGE, DirectionType.WEST, TransitionType.BURROW, CanBurrow())
    SANDFALLS_SIFTED_SANDS_PAYLOAD_WEST_BURROW_2 = ('Sandfalls Sifted Sands Payload West Burrow 2', Regions.SANDFALLS_SIFTED_SANDS, Regions.SANDFALLS_PAYLOAD_PASSAGE, DirectionType.WEST, TransitionType.BURROW, CanBurrow())
    SANDFALLS_SIFTED_SANDS_SHIFTY_CAVE = ('Sandfalls Sifted Sands Shifty Cave', Regions.SANDFALLS_SIFTED_SANDS, Regions.SANDFALLS_SHIFTY_SECLUSION, DirectionType.NORTH, TransitionType.DOORS, CanBurrow() & CanCarry())
    SANDFALLS_SIFTED_SANDS_SOUTH_BURROW = ('Sandfalls Sifted Sands South Burrow', Regions.SANDFALLS_SIFTED_SANDS, Regions.SANDFALLS_SPIKE_SQUARES, DirectionType.SOUTH, TransitionType.BURROW, CanBurrow())
    SANDFALLS_SIFTED_SANDS_SOUTH_TRANSITION = ('Sandfalls Sifted Sands South Transition', Regions.SANDFALLS_SIFTED_SANDS, Regions.SANDFALLS_SANDY_STATION, DirectionType.SOUTH, TransitionType.SCREENS, CanBurrow() & CanCarry())
    SANDFALLS_SIFTED_SANDS_UNDER_BURROW_EAST = ('Sandfalls Sifted Sands Under Burrow East', Regions.SANDFALLS_SIFTED_SANDS_HIDDEN_CAVE, Regions.SANDFALLS_SIFTED_SANDS, DirectionType.EAST, TransitionType.BURROW, CanBurrow())
    SANDFALLS_SIFTED_SANDS_UNDER_BURROW_WEST = ('Sandfalls Sifted Sands Under Burrow West', Regions.SANDFALLS_SIFTED_SANDS_HIDDEN_CAVE, Regions.SANDFALLS_SIFTED_SANDS, DirectionType.WEST, TransitionType.BURROW, CanBurrow())
    SANDFALLS_SIFTED_SANDS_WEST_MOVING_BURROW = ('Sandfalls Sifted Sands West Moving Burrow', Regions.SANDFALLS_SIFTED_SANDS, Regions.SANDFALLS_SIFTED_SANDS_HIDDEN_CAVE, DirectionType.WEST, TransitionType.BURROW, CanBurrow())
    SANDFALLS_SPIKE_SQUARES_NORTH_BURROW = ('Sandfalls Spike Squares North Burrow', Regions.SANDFALLS_SPIKE_SQUARES, Regions.SANDFALLS_SIFTED_SANDS, DirectionType.NORTH, TransitionType.BURROW, CanBurrow())
    SANDFALLS_SPIKE_SQUARES_NORTH_TRANSITION = ('Sandfalls Spike Squares North Transition', Regions.SANDFALLS_SPIKE_SQUARES, Regions.SANDFALLS_SIFTED_SANDS_HIDDEN_LEFT_BOMB, DirectionType.NORTH, TransitionType.SCREENS, True_())

