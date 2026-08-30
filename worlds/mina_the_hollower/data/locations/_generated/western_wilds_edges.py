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
    OSSEX_WESTERN_WALL_WESTERN_WILDS_OVERGROWN_PATH = ('Ossex Western Wall_Western Wilds Overgrown Path', Regions.OSSEX_WESTERN_WALL, Regions.WESTERN_WILDS_OVERGROWN_PATH, True_())
    WESTERN_WILDS_BALCONY_PATH_WESTERN_WILDS_MAIN = ('Western Wilds Balcony Path_Western Wilds Main', Regions.WESTERN_WILDS_BALCONY_PATH, Regions.WESTERN_WILDS_MAIN, CanBurrow())
    WESTERN_WILDS_BRUTES_WESTERN_WILDS_LAVA = ('Western Wilds Brutes_Western Wilds Lava', Regions.WESTERN_WILDS_BRUTES, Regions.WESTERN_WILDS_LAVA, True_())
    WESTERN_WILDS_END_WESTERN_WILDS_LAVA = ('Western Wilds End_Western Wilds Lava', Regions.WESTERN_WILDS_END, Regions.WESTERN_WILDS_LAVA, CanBurrow())
    WESTERN_WILDS_FOUNDRY_PATH_WESTERN_WILDS_FOUNDRY_PATH_DOOR = ('Western Wilds Foundry Path_Western Wilds Foundry Path Door', Regions.WESTERN_WILDS_FOUNDRY_PATH, Regions.WESTERN_WILDS_FOUNDRY_PATH_DOOR, CanJumpTiles(distance=2, has_wall=True))
    WESTERN_WILDS_FOUNDRY_PATH_WESTERN_WILDS_MAIN = ('Western Wilds Foundry Path_Western Wilds Main', Regions.WESTERN_WILDS_FOUNDRY_PATH, Regions.WESTERN_WILDS_MAIN, CanBurrow())
    WESTERN_WILDS_LAVA_WESTERN_WILDS_END = ('Western Wilds Lava_Western Wilds End', Regions.WESTERN_WILDS_LAVA, Regions.WESTERN_WILDS_END, CanBurrow())
    WESTERN_WILDS_LAVA_WESTERN_WILDS_MAIN = ('Western Wilds Lava_Western Wilds Main', Regions.WESTERN_WILDS_LAVA, Regions.WESTERN_WILDS_MAIN, CanBurrow())
    WESTERN_WILDS_MAIN_WESTERN_WILDS_BALCONY_PATH = ('Western Wilds Main_Western Wilds Balcony Path', Regions.WESTERN_WILDS_MAIN, Regions.WESTERN_WILDS_BALCONY_PATH, CanBurrow())
    WESTERN_WILDS_MAIN_WESTERN_WILDS_FOUNDRY_PATH = ('Western Wilds Main_Western Wilds Foundry Path', Regions.WESTERN_WILDS_MAIN, Regions.WESTERN_WILDS_FOUNDRY_PATH, CanBurrow())
    WESTERN_WILDS_MAIN_WESTERN_WILDS_LAVA = ('Western Wilds Main_Western Wilds Lava', Regions.WESTERN_WILDS_MAIN, Regions.WESTERN_WILDS_LAVA, CanBurrow())
    WESTERN_WILDS_MOLTEN_DUNGEON_END_WESTERN_WILDS_MOLTEN_DUNGEON_ENTRANCE = ('Western Wilds Molten Dungeon End_Western Wilds Molten Dungeon Entrance', Regions.WESTERN_WILDS_MOLTEN_DUNGEON_END, Regions.WESTERN_WILDS_MOLTEN_DUNGEON_ENTRANCE, True_())
    WESTERN_WILDS_MOLTEN_DUNGEON_FENCES_WESTERN_WILDS_MOLTEN_DUNGEON_MIDDLE = ('Western Wilds Molten Dungeon Fences_Western Wilds Molten Dungeon Middle', Regions.WESTERN_WILDS_MOLTEN_DUNGEON_FENCES, Regions.WESTERN_WILDS_MOLTEN_DUNGEON_MIDDLE, CanBurrow())
    WESTERN_WILDS_MOLTEN_DUNGEON_MIDDLE_WESTERN_WILDS_MOLTEN_DUNGEON_FENCES = ('Western Wilds Molten Dungeon Middle_Western Wilds Molten Dungeon Fences', Regions.WESTERN_WILDS_MOLTEN_DUNGEON_MIDDLE, Regions.WESTERN_WILDS_MOLTEN_DUNGEON_FENCES, CanBurrow())
    WESTERN_WILDS_MOLTEN_FOUNDRY_DARK_POPPIT_WESTERN_WILDS_MOLTEN_FOUNDRY_DARK = ('Western Wilds Molten Foundry Dark Poppit_Western Wilds Molten Foundry Dark', Regions.WESTERN_WILDS_MOLTEN_FOUNDRY_DARK_POPPIT, Regions.WESTERN_WILDS_MOLTEN_FOUNDRY_DARK, True_())
    WESTERN_WILDS_MOLTEN_FOUNDRY_DARK_WESTERN_WILDS_MOLTEN_FOUNDRY_DARK_POPPIT = ('Western Wilds Molten Foundry Dark_Western Wilds Molten Foundry Dark Poppit', Regions.WESTERN_WILDS_MOLTEN_FOUNDRY_DARK, Regions.WESTERN_WILDS_MOLTEN_FOUNDRY_DARK_POPPIT, CanBurrow())
    WESTERN_WILDS_MOLTEN_FOUNDRY_MAIN_WESTERN_WILDS_MOLTEN_FOUNDRY_SECRET = ('Western Wilds Molten Foundry Main_Western Wilds Molten Foundry Secret', Regions.WESTERN_WILDS_MOLTEN_FOUNDRY_MAIN, Regions.WESTERN_WILDS_MOLTEN_FOUNDRY_SECRET, CanBurrow())
    WESTERN_WILDS_MOLTEN_FOUNDRY_SECRET_WESTERN_WILDS_MOLTEN_FOUNDRY_MAIN = ('Western Wilds Molten Foundry Secret_Western Wilds Molten Foundry Main', Regions.WESTERN_WILDS_MOLTEN_FOUNDRY_SECRET, Regions.WESTERN_WILDS_MOLTEN_FOUNDRY_MAIN, CanBurrow())
    WESTERN_WILDS_OCCUPIED_BRIDGE_WESTERN_WILDS_BRUTES = ('Western Wilds Occupied Bridge_Western Wilds Brutes', Regions.WESTERN_WILDS_OCCUPIED_BRIDGE, Regions.WESTERN_WILDS_BRUTES, True_())
    WESTERN_WILDS_OCCUPIED_BRIDGE_WESTERN_WILDS_OSSEX_BRIDGE = ('Western Wilds Occupied Bridge_Western Wilds Ossex Bridge', Regions.WESTERN_WILDS_OCCUPIED_BRIDGE, Regions.WESTERN_WILDS_OSSEX_BRIDGE, CanBurrow())
    WESTERN_WILDS_OSSEX_BRIDGE_WESTERN_WILDS_MAIN = ('Western Wilds Ossex Bridge_Western Wilds Main', Regions.WESTERN_WILDS_OSSEX_BRIDGE, Regions.WESTERN_WILDS_MAIN, True_())
    WESTERN_WILDS_OSSEX_BRIDGE_WESTERN_WILDS_OCCUPIED_BRIDGE = ('Western Wilds Ossex Bridge_Western Wilds Occupied Bridge', Regions.WESTERN_WILDS_OSSEX_BRIDGE, Regions.WESTERN_WILDS_OCCUPIED_BRIDGE, CanBurrow())
    WESTERN_WILDS_SECRET_PASSAGEWAY_EAST_WESTERN_WILDS_SECRET_PASSAGEWAY_WEST = ('Western Wilds Secret Passageway East_Western Wilds Secret Passageway West', Regions.WESTERN_WILDS_SECRET_PASSAGEWAY_EAST, Regions.WESTERN_WILDS_SECRET_PASSAGEWAY_WEST, CanJumpTiles(distance=3, has_wall=True))
    WESTERN_WILDS_SECRET_PASSAGEWAY_WEST_WESTERN_WILDS_SECRET_PASSAGEWAY_EAST = ('Western Wilds Secret Passageway West_Western Wilds Secret Passageway East', Regions.WESTERN_WILDS_SECRET_PASSAGEWAY_WEST, Regions.WESTERN_WILDS_SECRET_PASSAGEWAY_EAST, CanJumpTiles(distance=3, has_wall=True))
    WESTERN_WILDS_WESTERN_POND_WESTERN_WILDS_END = ('Western Wilds Western Pond_Western Wilds End', Regions.WESTERN_WILDS_WESTERN_POND, Regions.WESTERN_WILDS_END, True_())

class RegionTransitions(TransitionTypeEnum):
    OSSEX_WESTERN_WALL_NORTH_BURROW = ('Ossex Western Wall North Burrow', Regions.OSSEX_WESTERN_WALL, Regions.OSSEX_BOWERY_BEGGER_RESIDENCE_BACK_CORNER, DirectionType.NORTH, TransitionType.BURROW, CanBurrow())
    OSSEX_WESTERN_WALL_SOUTH_BURROW = ('Ossex Western Wall South Burrow', Regions.OSSEX_WESTERN_WALL, Regions.OSSEX_SOUTH_WESTERN_WALL, DirectionType.SOUTH, TransitionType.BURROW, CanBurrow())
    WESTERN_WILDS_BALCONY_PATH_NORTH_TRANSITION = ('Western Wilds Balcony Path North Transition', Regions.WESTERN_WILDS_BALCONY_PATH, Regions.WESTERN_WILDS_BALCONY, DirectionType.NORTH, TransitionType.SCREENS, True_())
    WESTERN_WILDS_BALCONY_SOUTH_TRANSITION = ('Western Wilds Balcony South Transition', Regions.WESTERN_WILDS_BALCONY, Regions.WESTERN_WILDS_BALCONY_PATH, DirectionType.SOUTH, TransitionType.SCREENS, True_())
    WESTERN_WILDS_BRUTES_EAST_AREA_TRANSITION = ('Western Wilds Brutes East Area Transition', Regions.WESTERN_WILDS_BRUTES, Regions.KINDLEWOOD_OVERGROWTH_ENTRY_MAIN, DirectionType.WEST, TransitionType.AREA_SCREENS, True_())
    WESTERN_WILDS_END_SOUTH_TRANSITION = ('Western Wilds End South Transition', Regions.WESTERN_WILDS_END, Regions.WESTERN_WILDS_WESTERN_POND, DirectionType.SOUTH, TransitionType.SCREENS, True_())
    WESTERN_WILDS_FOUNDRY_PATH_NORTH_DOOR = ('Western Wilds Foundry Path North Door', Regions.WESTERN_WILDS_FOUNDRY_PATH_DOOR, Regions.WESTERN_WILDS_MOLTEN_FOUNDRY_MAIN, DirectionType.NORTH, TransitionType.DOORS, True_())
    WESTERN_WILDS_MAIN_SOUTH_TRANSITION = ('Western Wilds Main South Transition', Regions.WESTERN_WILDS_MAIN, Regions.WESTERN_WILDS_OVERGROWN_PATH, DirectionType.SOUTH, TransitionType.SCREENS, True_())
    WESTERN_WILDS_MOLTEN_DUNGEON_END_WEST_TRANSITION = ('Western Wilds Molten Dungeon End West Transition', Regions.WESTERN_WILDS_MOLTEN_DUNGEON_END, Regions.WESTERN_WILDS_MOLTEN_DUNGEON_MOVING, DirectionType.WEST, TransitionType.SCREENS, True_())
    WESTERN_WILDS_MOLTEN_DUNGEON_ENTRANCE_SOUTH_TRANSITION = ('Western Wilds Molten Dungeon Entrance South Transition', Regions.WESTERN_WILDS_MOLTEN_DUNGEON_ENTRANCE, Regions.WESTERN_WILDS_MOLTEN_DUNGEON_FENCES, DirectionType.SOUTH, TransitionType.SCREENS, True_())
    WESTERN_WILDS_MOLTEN_DUNGEON_ENTRANCE_STAIRS = ('Western Wilds Molten Dungeon Entrance Stairs', Regions.WESTERN_WILDS_MOLTEN_DUNGEON_ENTRANCE, Regions.WESTERN_WILDS_MOLTEN_FOUNDRY_DARK, DirectionType.NORTH, TransitionType.STAIRS, HasKear(kear=SingleKears.WESTERN_WILDS_FOUNDRY_KEAR.value))
    WESTERN_WILDS_MOLTEN_DUNGEON_FENCES_NORTH_TRANSITION = ('Western Wilds Molten Dungeon Fences North Transition', Regions.WESTERN_WILDS_MOLTEN_DUNGEON_FENCES, Regions.WESTERN_WILDS_MOLTEN_DUNGEON_ENTRANCE, DirectionType.NORTH, TransitionType.SCREENS, True_())
    WESTERN_WILDS_MOLTEN_DUNGEON_MIDDLE_NORTH_TRANSITION = ('Western Wilds Molten Dungeon Middle North Transition', Regions.WESTERN_WILDS_MOLTEN_DUNGEON_MIDDLE, Regions.WESTERN_WILDS_MOLTEN_DUNGEON_MOVING, DirectionType.NORTH, TransitionType.SCREENS, True_())
    WESTERN_WILDS_MOLTEN_DUNGEON_MOVING_EAST_TRANSITION = ('Western Wilds Molten Dungeon Moving East Transition', Regions.WESTERN_WILDS_MOLTEN_DUNGEON_MOVING, Regions.WESTERN_WILDS_MOLTEN_DUNGEON_END, DirectionType.EAST, TransitionType.SCREENS, True_())
    WESTERN_WILDS_MOLTEN_DUNGEON_MOVING_SOUTH_TRANSITION = ('Western Wilds Molten Dungeon Moving South Transition', Regions.WESTERN_WILDS_MOLTEN_DUNGEON_MOVING, Regions.WESTERN_WILDS_MOLTEN_DUNGEON_MIDDLE, DirectionType.SOUTH, TransitionType.SCREENS, True_())
    WESTERN_WILDS_MOLTEN_FOUNDRY_DARK_SOUTH_TRANSITION = ('Western Wilds Molten Foundry Dark South Transition', Regions.WESTERN_WILDS_MOLTEN_FOUNDRY_DARK, Regions.WESTERN_WILDS_MOLTEN_FOUNDRY_SECRET, DirectionType.SOUTH, TransitionType.SCREENS, True_())
    WESTERN_WILDS_MOLTEN_FOUNDRY_DARK_STAIRS = ('Western Wilds Molten Foundry Dark Stairs', Regions.WESTERN_WILDS_MOLTEN_FOUNDRY_DARK, Regions.WESTERN_WILDS_MOLTEN_DUNGEON_ENTRANCE, DirectionType.NORTH, TransitionType.STAIRS, HasKear(kear=SingleKears.WESTERN_WILDS_FOUNDRY_KEAR.value))
    WESTERN_WILDS_MOLTEN_FOUNDRY_MAIN_SOUTH_TRANSITION_EAST = ('Western Wilds Molten Foundry Main South Transition East', Regions.WESTERN_WILDS_MOLTEN_FOUNDRY_MAIN, Regions.WESTERN_WILDS_OSSEX_BRIDGE, DirectionType.SOUTH, TransitionType.DOORS, True_())
    WESTERN_WILDS_MOLTEN_FOUNDRY_MAIN_SOUTH_TRANSITION_WEST = ('Western Wilds Molten Foundry Main South Transition West', Regions.WESTERN_WILDS_MOLTEN_FOUNDRY_MAIN, Regions.WESTERN_WILDS_FOUNDRY_PATH, DirectionType.SOUTH, TransitionType.DOORS, True_())
    WESTERN_WILDS_MOLTEN_FOUNDRY_SECRET_NORTH_TRANSITION = ('Western Wilds Molten Foundry Secret North Transition', Regions.WESTERN_WILDS_MOLTEN_FOUNDRY_SECRET, Regions.WESTERN_WILDS_MOLTEN_FOUNDRY_DARK, DirectionType.NORTH, TransitionType.SCREENS, True_())
    WESTERN_WILDS_OSSEX_BRIDGE_DOOR = ('Western Wilds Ossex Bridge Door', Regions.WESTERN_WILDS_OSSEX_BRIDGE, Regions.WESTERN_WILDS_MOLTEN_FOUNDRY_MAIN, DirectionType.NORTH, TransitionType.DOORS, True_())
    WESTERN_WILDS_OSSEX_BRIDGE_EAST_TRANSITION = ('Western Wilds Ossex Bridge East Transition', Regions.WESTERN_WILDS_OSSEX_BRIDGE, Regions.OSSEX_BOWERY_UPPER, DirectionType.EAST, TransitionType.AREA_SCREENS, True_())
    WESTERN_WILDS_OVERGROWN_PATH_NORTH_TRANSITION = ('Western Wilds Overgrown Path North Transition', Regions.WESTERN_WILDS_OVERGROWN_PATH, Regions.WESTERN_WILDS_MAIN, DirectionType.NORTH, TransitionType.SCREENS, True_())
    WESTERN_WILDS_OVERGROWN_PATH_SECRET_POOL_GEYSER = ('Western Wilds Overgrown Path Secret Pool Geyser', Regions.WESTERN_WILDS_OVERGROWN_PATH, Regions.WESTERN_WILDS_SECRET_PASSAGEWAY_EAST, DirectionType.OVERWORLD, TransitionType.GEYSER_DOWN, True_())
    WESTERN_WILDS_OVERGROWN_PATH_SOUTH_TRANSITION = ('Western Wilds Overgrown Path South Transition', Regions.WESTERN_WILDS_OVERGROWN_PATH, Regions.SOUTHERN_OUTSKIRTS_COMMONS_WESTERN_PIT_ROOM_MAIN, DirectionType.SOUTH, TransitionType.AREA_SCREENS, True_())
    WESTERN_WILDS_SECRET_PASSAGE_EAST_GEYSER_UP = ('Western Wilds Secret Passage East Geyser Up', Regions.WESTERN_WILDS_SECRET_PASSAGEWAY_EAST, Regions.WESTERN_WILDS_OVERGROWN_PATH, DirectionType.OVERWORLD, TransitionType.GEYSER_UP, True_())
    WESTERN_WILDS_SECRET_PASSAGE_WEST_GEYSER_UP = ('Western Wilds Secret Passage West Geyser Up', Regions.WESTERN_WILDS_SECRET_PASSAGEWAY_WEST, Regions.WESTERN_WILDS_WESTERN_POND, DirectionType.OVERWORLD, TransitionType.GEYSER_UP, True_())
    WESTERN_WILDS_WESTERN_POND_SECRET_POOL_GEYSER = ('Western Wilds Western Pond Secret Pool Geyser', Regions.WESTERN_WILDS_WESTERN_POND, Regions.WESTERN_WILDS_SECRET_PASSAGEWAY_WEST, DirectionType.OVERWORLD, TransitionType.GEYSER_DOWN, True_())
    WESTERN_WILDS_WESTERN_POND_SOUTH_AREA_TRANSITION = ('Western Wilds Western Pond South Area Transition', Regions.WESTERN_WILDS_WESTERN_POND, Regions.BACKWATERS_UPPER_SWAMP_ENTRANCE, DirectionType.SOUTH, TransitionType.AREA_SCREENS, True_())

