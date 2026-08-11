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
    LONERS_LANDING_BAY_CLIFF_LONERS_LANDING_BAY = ("Loner's Landing Bay Cliff_Loner's Landing Bay", Regions.LONERS_LANDING_BAY_CLIFF, Regions.LONERS_LANDING_BAY, True_())
    LONERS_LANDING_BAY_LONERS_LANDING_BAY_CLIFF = ("Loner's Landing Bay_Loner's Landing Bay Cliff", Regions.LONERS_LANDING_BAY, Regions.LONERS_LANDING_BAY_CLIFF, HasLadder())
    LONERS_LANDING_BELOWDECKS_CHESTS_LONERS_LANDING_BELOWDECKS = ("Loner's Landing Belowdecks Chests_Loner's Landing Belowdecks", Regions.LONERS_LANDING_BELOWDECKS_CHESTS, Regions.LONERS_LANDING_BELOWDECKS, HasKear(kear=SingleKears.LONERS_LANDING_BELOWDECKS_BACK_KEAR.value) & CanJumpTiles(distance=2, over_water=True))
    LONERS_LANDING_BELOWDECKS_CHESTS_LONERS_LANDING_BELOWDECKS_FRONT = ("Loner's Landing Belowdecks Chests_Loner's Landing Belowdecks Front", Regions.LONERS_LANDING_BELOWDECKS_CHESTS, Regions.LONERS_LANDING_BELOWDECKS_FRONT, CanJumpTiles(distance=2, over_water=True))
    LONERS_LANDING_BELOWDECKS_FRONT_LONERS_LANDING_BELOWDECKS_CHESTS = ("Loner's Landing Belowdecks Front_Loner's Landing Belowdecks Chests", Regions.LONERS_LANDING_BELOWDECKS_FRONT, Regions.LONERS_LANDING_BELOWDECKS_CHESTS, CanJumpTiles(distance=2, over_water=True))
    LONERS_LANDING_BELOWDECKS_LONERS_LANDING_BELOWDECKS_CHESTS = ("Loner's Landing Belowdecks_Loner's Landing Belowdecks Chests", Regions.LONERS_LANDING_BELOWDECKS, Regions.LONERS_LANDING_BELOWDECKS_CHESTS, HasKear(kear=SingleKears.LONERS_LANDING_BELOWDECKS_BACK_KEAR.value) & CanJumpTiles(distance=2, over_water=True))
    LONERS_LANDING_BLIGHTED_DOCKS_BRIDGE_CLIFF_LONERS_LANDING_BLIGHTED_DOCKS_BRIDGE = ("Loner's Landing Blighted Docks Bridge Cliff_Loner's Landing Blighted Docks Bridge", Regions.LONERS_LANDING_BLIGHTED_DOCKS_BRIDGE_CLIFF, Regions.LONERS_LANDING_BLIGHTED_DOCKS_BRIDGE, CanClimb() & CanBounce())
    LONERS_LANDING_BLIGHTED_DOCKS_BRIDGE_CLIFF_LONERS_LANDING_BLIGHTED_DOCKS_LOWER_BRIDGE = ("Loner's Landing Blighted Docks Bridge Cliff_Loner's Landing Blighted Docks Lower Bridge", Regions.LONERS_LANDING_BLIGHTED_DOCKS_BRIDGE_CLIFF, Regions.LONERS_LANDING_BLIGHTED_DOCKS_LOWER_BRIDGE, CanClimb())
    LONERS_LANDING_BLIGHTED_DOCKS_BRIDGE_LONERS_LANDING_BLIGHTED_DOCKS_LOWER_BRIDGE = ("Loner's Landing Blighted Docks Bridge_Loner's Landing Blighted Docks Lower Bridge", Regions.LONERS_LANDING_BLIGHTED_DOCKS_BRIDGE, Regions.LONERS_LANDING_BLIGHTED_DOCKS_LOWER_BRIDGE, True_())
    LONERS_LANDING_BLIGHTED_DOCKS_FENCES_BOTTOM_LONERS_LANDING_BLIGHTED_DOCKS_FENCES_TOP = ("Loner's Landing Blighted Docks Fences Bottom_Loner's Landing Blighted Docks Fences Top", Regions.LONERS_LANDING_BLIGHTED_DOCKS_FENCES_BOTTOM, Regions.LONERS_LANDING_BLIGHTED_DOCKS_FENCES_TOP, CanBurrow())
    LONERS_LANDING_BLIGHTED_DOCKS_FIRST_BURROW_TOP_LONERS_LANDING_BLIGHTED_DOCKS_FIRST_BURROW = ("Loner's Landing Blighted Docks First Burrow Top_Loner's Landing Blighted Docks First Burrow", Regions.LONERS_LANDING_BLIGHTED_DOCKS_FIRST_BURROW_TOP, Regions.LONERS_LANDING_BLIGHTED_DOCKS_FIRST_BURROW, CanBurrow())
    LONERS_LANDING_BLIGHTED_DOCKS_FIRST_BURROW_LONERS_LANDING_BLIGHTED_DOCKS_FIRST_BURROW_TOP = ("Loner's Landing Blighted Docks First Burrow_Loner's Landing Blighted Docks First Burrow Top", Regions.LONERS_LANDING_BLIGHTED_DOCKS_FIRST_BURROW, Regions.LONERS_LANDING_BLIGHTED_DOCKS_FIRST_BURROW_TOP, CanBurrow())
    LONERS_LANDING_BLIGHTED_DOCKS_FIRST_BURROW_LONERS_LANDING_BLIGHTED_DOCKS_FIRST_CARRY = ("Loner's Landing Blighted Docks First Burrow_Loner's Landing Blighted Docks First Carry", Regions.LONERS_LANDING_BLIGHTED_DOCKS_FIRST_BURROW, Regions.LONERS_LANDING_BLIGHTED_DOCKS_FIRST_CARRY, CanBurrow())
    LONERS_LANDING_BLIGHTED_DOCKS_FIRST_CARRY_LONERS_LANDING_BLIGHTED_DOCKS_FIRST_BURROW = ("Loner's Landing Blighted Docks First Carry_Loner's Landing Blighted Docks First Burrow", Regions.LONERS_LANDING_BLIGHTED_DOCKS_FIRST_CARRY, Regions.LONERS_LANDING_BLIGHTED_DOCKS_FIRST_BURROW, CanCarry() | (HasReachingSideArm() & CanBurrow()))
    LONERS_LANDING_BLIGHTED_DOCKS_LOWER_BRIDGE_LONERS_LANDING_BLIGHTED_DOCKS_BRIDGE_CLIFF = ("Loner's Landing Blighted Docks Lower Bridge_Loner's Landing Blighted Docks Bridge Cliff", Regions.LONERS_LANDING_BLIGHTED_DOCKS_LOWER_BRIDGE, Regions.LONERS_LANDING_BLIGHTED_DOCKS_BRIDGE_CLIFF, CanClimb())
    LONERS_LANDING_BLIGHTED_DOCKS_ROAD_UPPER_LONERS_LANDING_BLIGHTED_DOCKS_ROAD = ("Loner's Landing Blighted Docks Road Upper_Loner's Landing Blighted Docks Road", Regions.LONERS_LANDING_BLIGHTED_DOCKS_ROAD_UPPER, Regions.LONERS_LANDING_BLIGHTED_DOCKS_ROAD, True_())
    LONERS_LANDING_BLIGHTED_DOCKS_ROAD_LONERS_LANDING_BLIGHTED_DOCKS_ROAD_LOWER = ("Loner's Landing Blighted Docks Road_Loner's Landing Blighted Docks Road Lower", Regions.LONERS_LANDING_BLIGHTED_DOCKS_ROAD, Regions.LONERS_LANDING_BLIGHTED_DOCKS_ROAD_LOWER, True_())
    LONERS_LANDING_BOARDWALK_ROAD_LONERS_LANDING_BOARDWALK_FIREWALK = ("Loner's Landing Boardwalk Road_Loner's Landing Boardwalk Firewalk", Regions.LONERS_LANDING_BOARDWALK_ROAD, Regions.LONERS_LANDING_BOARDWALK_FIREWALK, CanJumpTiles(distance=2))
    LONERS_LANDING_BOARDWALK_SPIKE_PATH_UPPER_LONERS_LANDING_BOARDWALK_SPIKE_PATH = ("Loner's Landing Boardwalk Spike Path Upper_Loner's Landing Boardwalk Spike Path", Regions.LONERS_LANDING_BOARDWALK_SPIKE_PATH_UPPER, Regions.LONERS_LANDING_BOARDWALK_SPIKE_PATH, True_())
    LONERS_LANDING_BOARDWALK_SPIKE_PATH_LONERS_LANDING_BOARDWALK_SPIKE_GATE = ("Loner's Landing Boardwalk Spike Path_Loner's Landing Boardwalk Spike Gate", Regions.LONERS_LANDING_BOARDWALK_SPIKE_PATH, Regions.LONERS_LANDING_BOARDWALK_SPIKE_GATE, CanBurrow())
    LONERS_LANDING_CLIFF_LONERS_LANDING_WATERFALL = ("Loner's Landing Cliff_Loner's Landing Waterfall", Regions.LONERS_LANDING_CLIFF, Regions.LONERS_LANDING_WATERFALL, CanClimb())
    LONERS_LANDING_SHIPWRECK_BLOCKED_LONERS_LANDING_SHIPWRECK = ("Loner's Landing Shipwreck Blocked_Loner's Landing Shipwreck", Regions.LONERS_LANDING_SHIPWRECK_BLOCKED, Regions.LONERS_LANDING_SHIPWRECK, True_())
    LONERS_LANDING_SHIPWRECK_LONERS_LANDING_DOCK = ("Loner's Landing Shipwreck_Loner's Landing Dock", Regions.LONERS_LANDING_SHIPWRECK, Regions.LONERS_LANDING_DOCK, True_())

class RegionTransitions(TransitionTypeEnum):
    LONERS_LANDING_BAY_CLIFF_EAST_TRANSITION = ("Loner's Landing Bay Cliff East Transition", Regions.LONERS_LANDING_BAY_CLIFF, Regions.LONERS_LANDING_CLIFF, DirectionType.EAST, TransitionType.SCREENS, True_())
    LONERS_LANDING_BAY_EAST_TRANSITION = ("Loner's Landing Bay East Transition", Regions.LONERS_LANDING_BAY, Regions.LONERS_LANDING_BOAT_SIDE, DirectionType.EAST, TransitionType.SCREENS, True_())
    LONERS_LANDING_BAY_NORTH_AREA_TRANSITION = ("Loner's Landing Bay North Area Transition", Regions.LONERS_LANDING_BAY, Regions.BACKWATERS_LOWER_SWAMP_STATION, DirectionType.NORTH, TransitionType.AREA_SCREENS, True_())
    LONERS_LANDING_BELOWDECKS_EAST_BURROW = ("Loner's Landing Belowdecks East Burrow", Regions.LONERS_LANDING_BELOWDECKS, Regions.LONERS_LANDING_WATERFALL, DirectionType.EAST, TransitionType.BURROW, CanBurrow())
    LONERS_LANDING_BELOWDECKS_FRONT_STAIRS = ("Loner's Landing Belowdecks Front Stairs", Regions.LONERS_LANDING_BELOWDECKS_FRONT, Regions.LONERS_LANDING_SHIPWRECK_BLOCKED, DirectionType.NORTH, TransitionType.STAIRS, True_())
    LONERS_LANDING_BLIGHTED_DOCKS_BRIDGE_CLIFF_DOOR = ("Loner's Landing Blighted Docks Bridge Cliff Door", Regions.LONERS_LANDING_BLIGHTED_DOCKS_BRIDGE_CLIFF, Regions.LONERS_LANDING_BLIGHTED_DOCKS_RESIDENCE, DirectionType.NORTH, TransitionType.DOORS, True_())
    LONERS_LANDING_BLIGHTED_DOCKS_BRIDGE_EAST_TRANSITION = ("Loner's Landing Blighted Docks Bridge East Transition", Regions.LONERS_LANDING_BLIGHTED_DOCKS_BRIDGE, Regions.LONERS_LANDING_BLIGHTED_DOCKS_ROAD_UPPER, DirectionType.EAST, TransitionType.SCREENS, True_())
    LONERS_LANDING_BLIGHTED_DOCKS_BRIDGE_GATE_NORTH_TRANSITION = ("Loner's Landing Blighted Docks Bridge Gate North Transition", Regions.LONERS_LANDING_BLIGHTED_DOCKS_BRIDGE_GATE, Regions.LONERS_LANDING_BLIGHTED_DOCKS_LOWER_BRIDGE, DirectionType.NORTH, TransitionType.SCREENS, True_())
    LONERS_LANDING_BLIGHTED_DOCKS_BRIDGE_GATE_SOUTH_TRANSITION = ("Loner's Landing Blighted Docks Bridge Gate South Transition", Regions.LONERS_LANDING_BLIGHTED_DOCKS_BRIDGE_GATE, Regions.LONERS_LANDING_BLIGHTED_DOCKS_FENCES_TOP, DirectionType.SOUTH, TransitionType.SCREENS, True_())
    LONERS_LANDING_BLIGHTED_DOCKS_BURROW_GEYSER_UP = ("Loner's Landing Blighted Docks Burrow Geyser Up", Regions.LONERS_LANDING_BLIGHTED_DOCKS_BURROW, Regions.LONERS_LANDING_BLIGHTED_DOCKS_ROAD, DirectionType.OVERWORLD, TransitionType.GEYSER_UP, True_())
    LONERS_LANDING_BLIGHTED_DOCKS_FENCES_BOTTOM_SOUTH_TRANSITION = ("Loner's Landing Blighted Docks Fences Bottom South Transition", Regions.LONERS_LANDING_BLIGHTED_DOCKS_FENCES_BOTTOM, Regions.LONERS_LANDING_BLIGHTED_DOCKS_FIRST_BURROW_TOP, DirectionType.SOUTH, TransitionType.SCREENS, True_())
    LONERS_LANDING_BLIGHTED_DOCKS_FENCES_TOP_NORTH_TRANSITION = ("Loner's Landing Blighted Docks Fences Top North Transition", Regions.LONERS_LANDING_BLIGHTED_DOCKS_FENCES_TOP, Regions.LONERS_LANDING_BLIGHTED_DOCKS_BRIDGE_GATE, DirectionType.NORTH, TransitionType.SCREENS, True_())
    LONERS_LANDING_BLIGHTED_DOCKS_FENCES_TOP_WEST_TRANSITION = ("Loner's Landing Blighted Docks Fences Top West Transition", Regions.LONERS_LANDING_BLIGHTED_DOCKS_FENCES_TOP, Regions.LONERS_LANDING_BLIGHTED_DOCKS_SIDE_CAVE, DirectionType.WEST, TransitionType.BURROW, CanBurrow())
    LONERS_LANDING_BLIGHTED_DOCKS_FIRST_BURROW_TOP_NORTH_TRANSITION = ("Loner's Landing Blighted Docks First Burrow Top North Transition", Regions.LONERS_LANDING_BLIGHTED_DOCKS_FIRST_BURROW_TOP, Regions.LONERS_LANDING_BLIGHTED_DOCKS_FENCES_BOTTOM, DirectionType.NORTH, TransitionType.SCREENS, True_())
    LONERS_LANDING_BLIGHTED_DOCKS_FIRST_CARRY_WEST_TRANSTITION = ("Loner's Landing Blighted Docks First Carry West Transtition", Regions.LONERS_LANDING_BLIGHTED_DOCKS_FIRST_CARRY, Regions.LONERS_LANDING_BLIGHTED_DOCKS_GANGPLANK, DirectionType.WEST, TransitionType.SCREENS, True_())
    LONERS_LANDING_BLIGHTED_DOCKS_GANGPLANK_EAST_TRANSITION = ("Loner's Landing Blighted Docks Gangplank East Transition", Regions.LONERS_LANDING_BLIGHTED_DOCKS_GANGPLANK, Regions.LONERS_LANDING_BLIGHTED_DOCKS_FIRST_CARRY, DirectionType.EAST, TransitionType.SCREENS, True_())
    LONERS_LANDING_BLIGHTED_DOCKS_GANGPLANK_WEST_TRANSITION = ("Loner's Landing Blighted Docks Gangplank West Transition", Regions.LONERS_LANDING_BLIGHTED_DOCKS_GANGPLANK, Regions.LONERS_LANDING_DOCK, DirectionType.WEST, TransitionType.SCREENS, True_())
    LONERS_LANDING_BLIGHTED_DOCKS_LOWER_BRIDGE_EAST_TRANSITION = ("Loner's Landing Blighted Docks Lower Bridge East Transition", Regions.LONERS_LANDING_BLIGHTED_DOCKS_LOWER_BRIDGE, Regions.LONERS_LANDING_BLIGHTED_DOCKS_ROAD_LOWER, DirectionType.EAST, TransitionType.SCREENS, True_())
    LONERS_LANDING_BLIGHTED_DOCKS_LOWER_BRIDGE_SOUTH_TRANSITION = ("Loner's Landing Blighted Docks Lower Bridge South Transition", Regions.LONERS_LANDING_BLIGHTED_DOCKS_LOWER_BRIDGE, Regions.LONERS_LANDING_BLIGHTED_DOCKS_BRIDGE_GATE, DirectionType.SOUTH, TransitionType.SCREENS, True_())
    LONERS_LANDING_BLIGHTED_DOCKS_RESIDENCE_EXIT = ("Loner's Landing Blighted Docks Residence Exit", Regions.LONERS_LANDING_BLIGHTED_DOCKS_RESIDENCE, Regions.LONERS_LANDING_BLIGHTED_DOCKS_BRIDGE_CLIFF, DirectionType.SOUTH, TransitionType.DOORS, True_())
    LONERS_LANDING_BLIGHTED_DOCKS_ROAD_EAST_TRANSITION = ("Loner's Landing Blighted Docks Road East Transition", Regions.LONERS_LANDING_BLIGHTED_DOCKS_ROAD, Regions.LONERS_LANDING_BOARDWALK_ROAD, DirectionType.EAST, TransitionType.SCREENS, HasKear(kear=SingleKears.LONERS_LANDING_BOARDWALK_KEAR.value))
    LONERS_LANDING_BLIGHTED_DOCKS_ROAD_GEYSER_DOWN = ("Loner's Landing Blighted Docks Road Geyser Down", Regions.LONERS_LANDING_BLIGHTED_DOCKS_ROAD, Regions.LONERS_LANDING_BLIGHTED_DOCKS_BURROW, DirectionType.OVERWORLD, TransitionType.GEYSER_DOWN, True_())
    LONERS_LANDING_BLIGHTED_DOCKS_ROAD_LOWER_WEST_TRANSITION = ("Loner's Landing Blighted Docks Road Lower West Transition", Regions.LONERS_LANDING_BLIGHTED_DOCKS_ROAD_LOWER, Regions.LONERS_LANDING_BLIGHTED_DOCKS_LOWER_BRIDGE, DirectionType.WEST, TransitionType.SCREENS, True_())
    LONERS_LANDING_BLIGHTED_DOCKS_ROAD_UPPER_WEST_TRANSITION = ("Loner's Landing Blighted Docks Road Upper West Transition", Regions.LONERS_LANDING_BLIGHTED_DOCKS_ROAD_UPPER, Regions.LONERS_LANDING_BLIGHTED_DOCKS_BRIDGE, DirectionType.WEST, TransitionType.SCREENS, True_())
    LONERS_LANDING_BLIGHTED_DOCKS_SIDE_CAVE_EAST_BURROW = ("Loner's Landing Blighted Docks Side Cave East Burrow", Regions.LONERS_LANDING_BLIGHTED_DOCKS_SIDE_CAVE, Regions.LONERS_LANDING_BLIGHTED_DOCKS_FENCES_TOP, DirectionType.EAST, TransitionType.BURROW, CanBurrow())
    LONERS_LANDING_BOARDWALK_FIRE_BOUNCE_EAST_TRANSITION = ("Loner's Landing Boardwalk Fire Bounce East Transition", Regions.LONERS_LANDING_BOARDWALK_FIRE_BOUNCE, Regions.LONERS_LANDING_BOARDWALK_SANDFALLS_LEDGE, DirectionType.EAST, TransitionType.SCREENS, CanBounce())
    LONERS_LANDING_BOARDWALK_FIRE_BOUNCE_NORTH_TRANSITION = ("Loner's Landing Boardwalk Fire Bounce North Transition", Regions.LONERS_LANDING_BOARDWALK_FIRE_BOUNCE, Regions.LONERS_LANDING_BOARDWALK_FIREWALK, DirectionType.NORTH, TransitionType.SCREENS, CanBounce())
    LONERS_LANDING_BOARDWALK_FIREWALK_NORTH_TRANSITION = ("Loner's Landing Boardwalk Firewalk North Transition", Regions.LONERS_LANDING_BOARDWALK_FIREWALK, Regions.LONERS_LANDING_BOARDWALK_SPIKE_PATH, DirectionType.NORTH, TransitionType.SCREENS, True_())
    LONERS_LANDING_BOARDWALK_FIREWALK_SOUTH_TRANSITION = ("Loner's Landing Boardwalk Firewalk South Transition", Regions.LONERS_LANDING_BOARDWALK_FIREWALK, Regions.LONERS_LANDING_BOARDWALK_FIRE_BOUNCE, DirectionType.SOUTH, TransitionType.SCREENS, CanBounce())
    LONERS_LANDING_BOARDWALK_PIPE_LANDING_NORTH_DROP = ("Loner's Landing Boardwalk Pipe Landing North Drop", Regions.LONERS_LANDING_BOARDWALK_PIPE_LANDING, Regions.LONERS_LANDING_BOARDWALK_SANDFALLS_LEDGE, DirectionType.NORTH, TransitionType.SCREENS, True_())
    LONERS_LANDING_BOARDWALK_PIPE_LANDING_PIPE = ("Loner's Landing Boardwalk Pipe Landing Pipe", Regions.LONERS_LANDING_BOARDWALK_PIPE_LANDING, Regions.LONERS_LANDING_DOCK, DirectionType.OVERWORLD, TransitionType.DO_NOT_RANDOMIZE_ENTRANCE, True_())
    LONERS_LANDING_BOARDWALK_ROAD_WEST_TRANSITION = ("Loner's Landing Boardwalk Road West Transition", Regions.LONERS_LANDING_BOARDWALK_ROAD, Regions.LONERS_LANDING_BLIGHTED_DOCKS_ROAD, DirectionType.WEST, TransitionType.SCREENS, HasKear(kear=SingleKears.LONERS_LANDING_BOARDWALK_KEAR.value))
    LONERS_LANDING_BOARDWALK_SANDFALLS_LAKE_NORTH_TRANSITION = ("Loner's Landing Boardwalk Sandfalls Lake North Transition", Regions.LONERS_LANDING_BOARDWALK_SANDFALLS_LAKE, Regions.SANDFALLS_SANDWATER_JUNCTION, DirectionType.NORTH, TransitionType.SCREENS, True_())
    LONERS_LANDING_BOARDWALK_SANDFALLS_LAKE_SOUTH_TRANSITION = ("Loner's Landing Boardwalk Sandfalls Lake South Transition", Regions.LONERS_LANDING_BOARDWALK_SANDFALLS_LAKE, Regions.LONERS_LANDING_BOARDWALK_SANDFALLS_PIPE_LAKE, DirectionType.SOUTH, TransitionType.SCREENS, CanJumpTiles(distance=2))
    LONERS_LANDING_BOARDWALK_SANDFALLS_LEDGE_WEST_TRANSITION = ("Loner's Landing Boardwalk Sandfalls Ledge West Transition", Regions.LONERS_LANDING_BOARDWALK_SANDFALLS_LEDGE, Regions.LONERS_LANDING_BOARDWALK_FIRE_BOUNCE, DirectionType.WEST, TransitionType.SCREENS, CanBounce())
    LONERS_LANDING_BOARDWALK_SANDFALLS_PIPE_LAKE_NORTH_TRANSITION = ("Loner's Landing Boardwalk Sandfalls Pipe Lake North Transition", Regions.LONERS_LANDING_BOARDWALK_SANDFALLS_PIPE_LAKE, Regions.LONERS_LANDING_BOARDWALK_SANDFALLS_LAKE, DirectionType.NORTH, TransitionType.SCREENS, True_())
    LONERS_LANDING_BOARDWALK_SPIKE_CAVE_EAST_BURROW = ("Loner's Landing Boardwalk Spike Cave East Burrow", Regions.LONERS_LANDING_BOARDWALK_SPIKE_CAVE, Regions.LONERS_LANDING_BOARDWALK_SPIKE_PATH, DirectionType.EAST, TransitionType.BURROW, CanBurrow())
    LONERS_LANDING_BOARDWALK_SPIKE_CAVE_SOUTH_BURROW_EAST = ("Loner's Landing Boardwalk Spike Cave South Burrow East", Regions.LONERS_LANDING_BOARDWALK_SPIKE_CAVE, Regions.LONERS_LANDING_BOARDWALK_SPIKE_PATH_UPPER, DirectionType.SOUTH, TransitionType.BURROW, CanBurrow())
    LONERS_LANDING_BOARDWALK_SPIKE_CAVE_SOUTH_BURROW_WEST = ("Loner's Landing Boardwalk Spike Cave South Burrow West", Regions.LONERS_LANDING_BOARDWALK_SPIKE_CAVE, Regions.LONERS_LANDING_BOARDWALK_SPIKE_PATH_UPPER, DirectionType.SOUTH, TransitionType.BURROW, CanBurrow())
    LONERS_LANDING_BOARDWALK_SPIKE_GATE_NORTH_AREA_TRANSITION = ("Loner's Landing Boardwalk Spike Gate North Area Transition", Regions.LONERS_LANDING_BOARDWALK_SPIKE_GATE, Regions.SOUTHERN_OUTSKIRTS_COMMONS_MAIN, DirectionType.NORTH, TransitionType.AREA_SCREENS, True_())
    LONERS_LANDING_BOARDWALK_SPIKE_PATH_SOUTH_TRANSITION = ("Loner's Landing Boardwalk Spike Path South Transition", Regions.LONERS_LANDING_BOARDWALK_SPIKE_PATH, Regions.LONERS_LANDING_BOARDWALK_FIREWALK, DirectionType.SOUTH, TransitionType.SCREENS, True_())
    LONERS_LANDING_BOARDWALK_SPIKE_PATH_UPPER_NORTH_BURROW_EAST = ("Loner's Landing Boardwalk Spike Path Upper North Burrow East", Regions.LONERS_LANDING_BOARDWALK_SPIKE_PATH_UPPER, Regions.LONERS_LANDING_BOARDWALK_SPIKE_CAVE, DirectionType.NORTH, TransitionType.BURROW, CanBurrow())
    LONERS_LANDING_BOARDWALK_SPIKE_PATH_UPPER_NORTH_BURROW_WEST = ("Loner's Landing Boardwalk Spike Path Upper North Burrow West", Regions.LONERS_LANDING_BOARDWALK_SPIKE_PATH_UPPER, Regions.LONERS_LANDING_BOARDWALK_SPIKE_CAVE, DirectionType.NORTH, TransitionType.BURROW, CanBurrow())
    LONERS_LANDING_BOARDWALK_SPIKE_PATH_WEST_BURROW = ("Loner's Landing Boardwalk Spike Path West Burrow", Regions.LONERS_LANDING_BOARDWALK_SPIKE_PATH, Regions.LONERS_LANDING_BOARDWALK_SPIKE_CAVE, DirectionType.WEST, TransitionType.BURROW, CanBurrow())
    LONERS_LANDING_BOAT_SIDE_WEST_TRANSITION = ("Loner's Landing Boat Side West Transition", Regions.LONERS_LANDING_BOAT_SIDE, Regions.LONERS_LANDING_BAY, DirectionType.WEST, TransitionType.SCREENS, True_())
    LONERS_LANDING_CLIFF_WEST_TRANSITION = ("Loner's Landing Cliff West Transition", Regions.LONERS_LANDING_CLIFF, Regions.LONERS_LANDING_BAY_CLIFF, DirectionType.WEST, TransitionType.SCREENS, True_())
    LONERS_LANDING_DOCK_EAST_TRANSITION = ("Loner's Landing Dock East Transition", Regions.LONERS_LANDING_DOCK, Regions.LONERS_LANDING_BLIGHTED_DOCKS_GANGPLANK, DirectionType.EAST, TransitionType.SCREENS, True_())
    LONERS_LANDING_DOCK_PIPE = ("Loner's Landing Dock Pipe", Regions.LONERS_LANDING_DOCK, Regions.LONERS_LANDING_BOARDWALK_PIPE_LANDING, DirectionType.OVERWORLD, TransitionType.DO_NOT_RANDOMIZE_ENTRANCE, (HasKear(kear=SingleKears.LONERS_LANDING_BOARDWALK_KEAR.value) | StartedInOssex()))
    LONERS_LANDING_SHIPWRECK_STAIRS = ("Loner's Landing Shipwreck Stairs", Regions.LONERS_LANDING_SHIPWRECK_BLOCKED, Regions.LONERS_LANDING_BELOWDECKS_FRONT, DirectionType.NORTH, TransitionType.STAIRS, True_())
    LONERS_LANDING_WATERFALL_WEST_BURROW = ("Loner's Landing Waterfall West Burrow", Regions.LONERS_LANDING_WATERFALL, Regions.LONERS_LANDING_BELOWDECKS, DirectionType.WEST, TransitionType.BURROW, CanSwim())

