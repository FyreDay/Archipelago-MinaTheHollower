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
    RADIANT_MANOR_BACKLIT_CORRIDOR_ROPE_RADIANT_MANOR_BACKLIT_CORRIDOR = ('Radiant Manor Backlit Corridor Rope_Radiant Manor Backlit Corridor', Regions.RADIANT_MANOR_BACKLIT_CORRIDOR_ROPE, Regions.RADIANT_MANOR_BACKLIT_CORRIDOR, CanClimb() & CanBurrow())
    RADIANT_MANOR_BACKLIT_CORRIDOR_RADIANT_MANOR_BACKLIT_CORRIDOR_ROPE = ('Radiant Manor Backlit Corridor_Radiant Manor Backlit Corridor Rope', Regions.RADIANT_MANOR_BACKLIT_CORRIDOR, Regions.RADIANT_MANOR_BACKLIT_CORRIDOR_ROPE, CanClimb() & CanBurrow())
    RADIANT_MANOR_BALLROOM_BALCONY_EAST_RADIANT_MANOR_BALLROOM = ('Radiant Manor Ballroom Balcony East_Radiant Manor Ballroom', Regions.RADIANT_MANOR_BALLROOM_BALCONY_EAST, Regions.RADIANT_MANOR_BALLROOM, True_())
    RADIANT_MANOR_BALLROOM_BALCONY_EAST_RADIANT_MANOR_BALLROOM_TOP = ('Radiant Manor Ballroom Balcony East_Radiant Manor Ballroom Top', Regions.RADIANT_MANOR_BALLROOM_BALCONY_EAST, Regions.RADIANT_MANOR_BALLROOM_TOP, True_())
    RADIANT_MANOR_BALLROOM_BALCONY_WEST_RADIANT_MANOR_BALLROOM_TOP = ('Radiant Manor Ballroom Balcony West_Radiant Manor Ballroom Top', Regions.RADIANT_MANOR_BALLROOM_BALCONY_WEST, Regions.RADIANT_MANOR_BALLROOM_TOP, True_())
    RADIANT_MANOR_BALLROOM_TOP_RADIANT_MANOR_BALLROOM_BALCONY_EAST = ('Radiant Manor Ballroom Top_Radiant Manor Ballroom Balcony East', Regions.RADIANT_MANOR_BALLROOM_TOP, Regions.RADIANT_MANOR_BALLROOM_BALCONY_EAST, CanBounce())
    RADIANT_MANOR_BALLROOM_UPPER_PILLARS_RADIANT_MANOR_BALLROOM = ('Radiant Manor Ballroom Upper Pillars_Radiant Manor Ballroom', Regions.RADIANT_MANOR_BALLROOM_UPPER_PILLARS, Regions.RADIANT_MANOR_BALLROOM, CanClimb())
    RADIANT_MANOR_GALLERY_RIGHT_RADIANT_MANOR_GALLERY = ('Radiant Manor Gallery Right_Radiant Manor Gallery', Regions.RADIANT_MANOR_GALLERY_RIGHT, Regions.RADIANT_MANOR_GALLERY, CanJumpTiles(distance=2))
    RADIANT_MANOR_GALLERY_STAIRS_RIGHT_RADIANT_MANOR_GALLERY_STAIRS = ('Radiant Manor Gallery Stairs Right_Radiant Manor Gallery Stairs', Regions.RADIANT_MANOR_GALLERY_STAIRS_RIGHT, Regions.RADIANT_MANOR_GALLERY_STAIRS, CanBurrow())
    RADIANT_MANOR_GALLERY_STAIRS_RADIANT_MANOR_GALLERY_STAIRS_RIGHT = ('Radiant Manor Gallery Stairs_Radiant Manor Gallery Stairs Right', Regions.RADIANT_MANOR_GALLERY_STAIRS, Regions.RADIANT_MANOR_GALLERY_STAIRS_RIGHT, CanBurrow())
    RADIANT_MANOR_GALLERY_RADIANT_MANOR_GALLERY_RIGHT = ('Radiant Manor Gallery_Radiant Manor Gallery Right', Regions.RADIANT_MANOR_GALLERY, Regions.RADIANT_MANOR_GALLERY_RIGHT, CanJumpTiles(distance=2))
    RADIANT_MANOR_GREENHOUSE_LEFT_RADIANT_MANOR_GREENHOUSE_RIGHT = ('Radiant Manor Greenhouse Left_Radiant Manor Greenhouse Right', Regions.RADIANT_MANOR_GREENHOUSE_LEFT, Regions.RADIANT_MANOR_GREENHOUSE_RIGHT, CanBounce() & CanBurrow())
    RADIANT_MANOR_GREENHOUSE_LIGHTNING_END_RADIANT_MANOR_GREENHOUSE_LIGHTNING = ('Radiant Manor Greenhouse Lightning End_Radiant Manor Greenhouse Lightning', Regions.RADIANT_MANOR_GREENHOUSE_LIGHTNING_END, Regions.RADIANT_MANOR_GREENHOUSE_LIGHTNING, CanBounce())
    RADIANT_MANOR_GREENHOUSE_LIGHTNING_RADIANT_MANOR_GREENHOUSE_LIGHTNING_END = ('Radiant Manor Greenhouse Lightning_Radiant Manor Greenhouse Lightning End', Regions.RADIANT_MANOR_GREENHOUSE_LIGHTNING, Regions.RADIANT_MANOR_GREENHOUSE_LIGHTNING_END, CanBounce())
    RADIANT_MANOR_GREENHOUSE_RIGHT_RADIANT_MANOR_GREENHOUSE_LEFT = ('Radiant Manor Greenhouse Right_Radiant Manor Greenhouse Left', Regions.RADIANT_MANOR_GREENHOUSE_RIGHT, Regions.RADIANT_MANOR_GREENHOUSE_LEFT, CanBounce() & CanBurrow())
    RADIANT_MANOR_GREENHOUSE_STATUES_BRIDGE_RADIANT_MANOR_GREENHOUSE_STATUES = ('Radiant Manor Greenhouse Statues Bridge_Radiant Manor Greenhouse Statues', Regions.RADIANT_MANOR_GREENHOUSE_STATUES_BRIDGE, Regions.RADIANT_MANOR_GREENHOUSE_STATUES, CanClimb())
    RADIANT_MANOR_ORPHANAGE_BEDS_RADIANT_MANOR_ORPHANAGE_PRIVATE_ROOM = ('Radiant Manor Orphanage Beds_Radiant Manor Orphanage Private Room', Regions.RADIANT_MANOR_ORPHANAGE_BEDS, Regions.RADIANT_MANOR_ORPHANAGE_PRIVATE_ROOM, CanBurrow())
    RADIANT_MANOR_ORPHANAGE_PRIVATE_ROOM_RADIANT_MANOR_ORPHANAGE_BEDS = ('Radiant Manor Orphanage Private Room_Radiant Manor Orphanage Beds', Regions.RADIANT_MANOR_ORPHANAGE_PRIVATE_ROOM, Regions.RADIANT_MANOR_ORPHANAGE_BEDS, CanBurrow())
    RADIANT_MANOR_RAFTERS_DOOR_TRAP_RADIANT_MANOR_RAFTERS_DOOR = ('Radiant Manor Rafters Door Trap_Radiant Manor Rafters Door', Regions.RADIANT_MANOR_RAFTERS_DOOR_TRAP, Regions.RADIANT_MANOR_RAFTERS_DOOR, CanBurrow())
    RADIANT_MANOR_RAFTERS_DOOR_RADIANT_MANOR_RAFTERS_DOOR_TRAP = ('Radiant Manor Rafters Door_Radiant Manor Rafters Door Trap', Regions.RADIANT_MANOR_RAFTERS_DOOR, Regions.RADIANT_MANOR_RAFTERS_DOOR_TRAP, CanBurrow())
    RADIANT_MANOR_RAFTERS_STAIR_RADIANT_MANOR_RAFTERS = ('Radiant Manor Rafters Stair_Radiant Manor Rafters', Regions.RADIANT_MANOR_RAFTERS_STAIR, Regions.RADIANT_MANOR_RAFTERS, CanBounce() & CanBurrow())
    RADIANT_MANOR_RAFTERS_RADIANT_MANOR_RAFTERS_STAIR = ('Radiant Manor Rafters_Radiant Manor Rafters Stair', Regions.RADIANT_MANOR_RAFTERS, Regions.RADIANT_MANOR_RAFTERS_STAIR, CanBounce() & CanBurrow())
    RADIANT_MANOR_ROOFTOP_EAST_GAP_RADIANT_MANOR_ROOFTOP_EAST = ('Radiant Manor Rooftop East Gap_Radiant Manor Rooftop East', Regions.RADIANT_MANOR_ROOFTOP_EAST_GAP, Regions.RADIANT_MANOR_ROOFTOP_EAST, True_())
    RADIANT_MANOR_ROOFTOP_EAST_OSSEX_COURTYARD_EAST = ('Radiant Manor Rooftop East_Ossex Courtyard East', Regions.RADIANT_MANOR_ROOFTOP_EAST, Regions.OSSEX_COURTYARD_EAST, CanClimb())
    RADIANT_MANOR_ROOFTOP_EAST_RADIANT_MANOR_ROOFTOP_EAST_GAP = ('Radiant Manor Rooftop East_Radiant Manor Rooftop East Gap', Regions.RADIANT_MANOR_ROOFTOP_EAST, Regions.RADIANT_MANOR_ROOFTOP_EAST_GAP, True_())
    RADIANT_MANOR_ROOFTOP_GREENHOUSE_RADIANT_MANOR_GREENHOUSE_STATUES_BRIDGE = ('Radiant Manor Rooftop Greenhouse_Radiant Manor Greenhouse Statues Bridge', Regions.RADIANT_MANOR_ROOFTOP_GREENHOUSE, Regions.RADIANT_MANOR_GREENHOUSE_STATUES_BRIDGE, CanClimb())
    RADIANT_MANOR_ROOFTOP_PANELS_BUSH_EAST_RADIANT_MANOR_ROOFTOP_PANELS_BUSH_WEST = ('Radiant Manor Rooftop Panels Bush East_Radiant Manor Rooftop Panels Bush West', Regions.RADIANT_MANOR_ROOFTOP_PANELS_BUSH_EAST, Regions.RADIANT_MANOR_ROOFTOP_PANELS_BUSH_WEST, CanBurrow())
    RADIANT_MANOR_ROOFTOP_PANELS_BUSH_WEST_RADIANT_MANOR_ROOFTOP_PANELS_BUSH_EAST = ('Radiant Manor Rooftop Panels Bush West_Radiant Manor Rooftop Panels Bush East', Regions.RADIANT_MANOR_ROOFTOP_PANELS_BUSH_WEST, Regions.RADIANT_MANOR_ROOFTOP_PANELS_BUSH_EAST, CanBurrow())
    RADIANT_MANOR_ROOFTOP_PANELS_EAST_RADIANT_MANOR_ROOFTOP_PANELS = ('Radiant Manor Rooftop Panels East_Radiant Manor Rooftop Panels', Regions.RADIANT_MANOR_ROOFTOP_PANELS_EAST, Regions.RADIANT_MANOR_ROOFTOP_PANELS, True_())
    RADIANT_MANOR_ROOFTOP_PANELS_WEST_RADIANT_MANOR_ROOFTOP_PANELS = ('Radiant Manor Rooftop Panels West_Radiant Manor Rooftop Panels', Regions.RADIANT_MANOR_ROOFTOP_PANELS_WEST, Regions.RADIANT_MANOR_ROOFTOP_PANELS, True_())
    RADIANT_MANOR_ROOFTOP_PANELS_RADIANT_MANOR_ROOFTOP_PANELS_EAST = ('Radiant Manor Rooftop Panels_Radiant Manor Rooftop Panels East', Regions.RADIANT_MANOR_ROOFTOP_PANELS, Regions.RADIANT_MANOR_ROOFTOP_PANELS_EAST, CanBurrow())
    RADIANT_MANOR_ROOFTOP_PANELS_RADIANT_MANOR_ROOFTOP_PANELS_WEST = ('Radiant Manor Rooftop Panels_Radiant Manor Rooftop Panels West', Regions.RADIANT_MANOR_ROOFTOP_PANELS, Regions.RADIANT_MANOR_ROOFTOP_PANELS_WEST, CanBurrow())

class RegionTransitions(TransitionTypeEnum):
    RADIANT_MANOR_BACKLIT_BALCONY_EAST_TRANSITION = ('Radiant Manor Backlit Balcony East Transition', Regions.RADIANT_MANOR_BACKLIT_BALCONY, Regions.RADIANT_MANOR_BACKLIT_CORRIDOR, DirectionType.EAST, TransitionType.SCREENS, True_())
    RADIANT_MANOR_BACKLIT_BALCONY_STAIRS = ('Radiant Manor Backlit Balcony Stairs', Regions.RADIANT_MANOR_BACKLIT_BALCONY, Regions.RADIANT_MANOR_ROOFTOP_GREENHOUSE, DirectionType.NORTH, TransitionType.STAIRS, True_())
    RADIANT_MANOR_BACKLIT_CORRIDOR_ROPE_TRANSITION = ('Radiant Manor Backlit Corridor Rope Transition', Regions.RADIANT_MANOR_BACKLIT_CORRIDOR_ROPE, Regions.RADIANT_MANOR_BALLROOM_BALCONY_WEST, DirectionType.EAST, TransitionType.SCREENS, True_())
    RADIANT_MANOR_BACKLIT_CORRIDOR_WEST_TRANSITION = ('Radiant Manor Backlit Corridor West Transition', Regions.RADIANT_MANOR_BACKLIT_CORRIDOR, Regions.RADIANT_MANOR_BACKLIT_BALCONY, DirectionType.WEST, TransitionType.SCREENS, True_())
    RADIANT_MANOR_BALCONY_EAST_CHAMBER_WEST_TRANSITION = ('Radiant Manor Balcony East Chamber West Transition', Regions.RADIANT_MANOR_BALCONY_EAST_CHAMBER, Regions.RADIANT_MANOR_BALLROOM_BALCONY_EAST, DirectionType.WEST, TransitionType.SCREENS, True_())
    RADIANT_MANOR_BALLROOM_BALCONY_EAST_EAST_TRANSITION = ('Radiant Manor Ballroom Balcony East East Transition', Regions.RADIANT_MANOR_BALLROOM_BALCONY_EAST, Regions.RADIANT_MANOR_BALCONY_EAST_CHAMBER, DirectionType.EAST, TransitionType.SCREENS, True_())
    RADIANT_MANOR_BALLROOM_BALCONY_EAST_STAIRS = ('Radiant Manor Ballroom Balcony East Stairs', Regions.RADIANT_MANOR_BALLROOM_BALCONY_EAST, Regions.RADIANT_MANOR_FINALE_DINING_ROOM, DirectionType.NORTH, TransitionType.STAIRS, True_())
    RADIANT_MANOR_BALLROOM_BALCONY_WEST_TRANSITION = ('Radiant Manor Ballroom Balcony West Transition', Regions.RADIANT_MANOR_BALLROOM_BALCONY_WEST, Regions.RADIANT_MANOR_BACKLIT_CORRIDOR_ROPE, DirectionType.WEST, TransitionType.SCREENS, True_())
    RADIANT_MANOR_BALLROOM_DINING_STAIRS = ('Radiant Manor Ballroom Dining Stairs', Regions.RADIANT_MANOR_BALLROOM, Regions.RADIANT_MANOR_DINING_ROOM, DirectionType.NORTH, TransitionType.STAIRS, True_())
    RADIANT_MANOR_BALLROOM_GREENHOUSE_DOORS = ('Radiant Manor Ballroom Greenhouse Doors', Regions.RADIANT_MANOR_BALLROOM, Regions.RADIANT_MANOR_GREENHOUSE_WING, DirectionType.NORTH, TransitionType.DOORS, RepairedGeneratorCount(count=6))
    RADIANT_MANOR_BALLROOM_MEOWSTRO_DOORS = ('Radiant Manor Ballroom Meowstro Doors', Regions.RADIANT_MANOR_BALLROOM, Regions.RADIANT_MANOR_MEOWSTROS_CHAMBER, DirectionType.NORTH, TransitionType.DOORS, RepairedGeneratorCount(count=6))
    RADIANT_MANOR_BALLROOM_MIMIC_STAIRS = ('Radiant Manor Ballroom Mimic Stairs', Regions.RADIANT_MANOR_BALLROOM, Regions.RADIANT_MANOR_MIMIC_CHAMBER, DirectionType.NORTH, TransitionType.STAIRS, True_())
    RADIANT_MANOR_BALLROOM_SOUTH_TRANSITION = ('Radiant Manor Ballroom South Transition', Regions.RADIANT_MANOR_BALLROOM, Regions.RADIANT_MANOR_ENTRY, DirectionType.SOUTH, TransitionType.SCREENS, True_())
    RADIANT_MANOR_BALLROOM_UPPER_PILLARS_BURROW_NORTH = ('Radiant Manor Ballroom Upper Pillars Burrow North', Regions.RADIANT_MANOR_BALLROOM_UPPER_PILLARS, Regions.RADIANT_MANOR_WEST_CHAMBER, DirectionType.NORTH, TransitionType.BURROW, CanBurrow())
    RADIANT_MANOR_BALLROOM_UPPER_PILLARS_EAST_TRANSITION = ('Radiant Manor Ballroom Upper Pillars East Transition', Regions.RADIANT_MANOR_BALLROOM_UPPER_PILLARS, Regions.RADIANT_MANOR_GALLERY_STAIRS, DirectionType.EAST, TransitionType.SCREENS, True_())
    RADIANT_MANOR_BALLROOM_UPPER_PILLARS_WEST_TRANSITION = ('Radiant Manor Ballroom Upper Pillars West Transition', Regions.RADIANT_MANOR_BALLROOM_UPPER_PILLARS, Regions.RADIANT_MANOR_RAFTERS_STAIR, DirectionType.WEST, TransitionType.SCREENS, True_())
    RADIANT_MANOR_BATHROOM_DOOR = ('Radiant Manor Bathroom Door', Regions.RADIANT_MANOR_BATHROOM, Regions.RADIANT_MANOR_FOYER, DirectionType.NORTH, TransitionType.DO_NOT_RANDOMIZE_ENTRANCE, True_())
    RADIANT_MANOR_BATHROOM_SUITE_PIPE = ('Radiant Manor Bathroom Suite Pipe', Regions.RADIANT_MANOR_BATHROOM_SUITE, Regions.RADIANT_MANOR_BATHROOM, DirectionType.OVERWORLD, TransitionType.DO_NOT_RANDOMIZE_ENTRANCE, True_())
    RADIANT_MANOR_BATHROOM_SUITE_WEST_TRANSITION = ('Radiant Manor Bathroom Suite West Transition', Regions.RADIANT_MANOR_BATHROOM_SUITE, Regions.RADIANT_MANOR_GENERATOR_CORE_UNDERLAB, DirectionType.EAST, TransitionType.DO_NOT_RANDOMIZE_ENTRANCE, True_())
    RADIANT_MANOR_DINING_ROOM_STAIRS = ('Radiant Manor Dining Room Stairs', Regions.RADIANT_MANOR_DINING_ROOM, Regions.RADIANT_MANOR_BALLROOM, DirectionType.NORTH, TransitionType.STAIRS, True_())
    RADIANT_MANOR_ENTRY_NORTH_TRANSITION = ('Radiant Manor Entry North Transition', Regions.RADIANT_MANOR_ENTRY, Regions.RADIANT_MANOR_BALLROOM, DirectionType.NORTH, TransitionType.SCREENS, True_())
    RADIANT_MANOR_ENTRY_SOUTH_TRANSITION = ('Radiant Manor Entry South Transition', Regions.RADIANT_MANOR_ENTRY, Regions.RADIANT_MANOR_FOYER, DirectionType.SOUTH, TransitionType.SCREENS, True_())
    RADIANT_MANOR_FINALE_DINING_ROOM_NORTH = ('Radiant Manor Finale Dining Room North', Regions.RADIANT_MANOR_FINALE_DINING_ROOM, Regions.RADIANT_MANOR_FINALE_LIONS, DirectionType.NORTH, TransitionType.DO_NOT_RANDOMIZE_ENTRANCE, True_())
    RADIANT_MANOR_FINALE_DINING_ROOM_STAIRS = ('Radiant Manor Finale Dining Room Stairs', Regions.RADIANT_MANOR_FINALE_DINING_ROOM, Regions.RADIANT_MANOR_BALLROOM_BALCONY_EAST, DirectionType.NORTH, TransitionType.STAIRS, True_())
    RADIANT_MANOR_FINALE_LIONS_NORTH = ('Radiant Manor Finale Lions North', Regions.RADIANT_MANOR_FINALE_LIONS, Regions.RADIANT_MANOR_GENERATOR_CORE, DirectionType.NORTH, TransitionType.DO_NOT_RANDOMIZE_ENTRANCE, CanBurrow())
    RADIANT_MANOR_FINALE_LIONS_SOUTH = ('Radiant Manor Finale Lions South', Regions.RADIANT_MANOR_FINALE_LIONS, Regions.RADIANT_MANOR_FINALE_DINING_ROOM, DirectionType.SOUTH, TransitionType.DO_NOT_RANDOMIZE_ENTRANCE, True_())
    RADIANT_MANOR_FOYER_BUTLERS_DOORS = ("Radiant Manor Foyer Butler's Doors", Regions.RADIANT_MANOR_FOYER, Regions.RADIANT_MANOR_FOYER_BUTLERS_OFFICE, DirectionType.NORTH, TransitionType.DOORS, True_())
    RADIANT_MANOR_FOYER_BUTLERS_OFFICE_DOORS = ('Radiant Manor Foyer Butlers Office Doors', Regions.RADIANT_MANOR_FOYER_BUTLERS_OFFICE, Regions.RADIANT_MANOR_FOYER, DirectionType.SOUTH, TransitionType.DOORS, True_())
    RADIANT_MANOR_FOYER_EXIT = ('Radiant Manor Foyer Exit', Regions.RADIANT_MANOR_FOYER, Regions.OSSEX_COURTYARD, DirectionType.SOUTH, TransitionType.DOORS, True_())
    RADIANT_MANOR_FOYER_LIBRARY_DOORS = ('Radiant Manor Foyer Library Doors', Regions.RADIANT_MANOR_FOYER, Regions.RADIANT_MANOR_FOYER_LIBRARY, DirectionType.NORTH, TransitionType.DOORS, True_())
    RADIANT_MANOR_FOYER_MIRROR = ('Radiant Manor Foyer Mirror', Regions.RADIANT_MANOR_FOYER, Regions.ASTRAL_ORRERY_MIRRORS_END, DirectionType.OVERWORLD, TransitionType.MIRRORS, True_())
    RADIANT_MANOR_FOYER_NORTH_TRANSITION = ('Radiant Manor Foyer North Transition', Regions.RADIANT_MANOR_FOYER, Regions.RADIANT_MANOR_ENTRY, DirectionType.NORTH, TransitionType.SCREENS, RepairedGeneratorCount(count=6))
    RADIANT_MANOR_FOYER_ORPHANAGE_DOORS = ('Radiant Manor Foyer Orphanage Doors', Regions.RADIANT_MANOR_FOYER, Regions.RADIANT_MANOR_ORPHANAGE, DirectionType.NORTH, TransitionType.DOORS, True_())
    RADIANT_MANOR_GALLERY_RIGHT_EAST_TRANSITION = ('Radiant Manor Gallery Right East Transition', Regions.RADIANT_MANOR_GALLERY_RIGHT, Regions.RADIANT_MANOR_SERVANTS_QUARTERS, DirectionType.EAST, TransitionType.SCREENS, True_())
    RADIANT_MANOR_GALLERY_STAIRS_RIGHT_TRANSITION = ('Radiant Manor Gallery Stairs Right Transition', Regions.RADIANT_MANOR_GALLERY_STAIRS_RIGHT, Regions.RADIANT_MANOR_GALLERY, DirectionType.EAST, TransitionType.SCREENS, True_())
    RADIANT_MANOR_GALLERY_STAIRS_WEST_TRANSITION = ('Radiant Manor Gallery Stairs West Transition', Regions.RADIANT_MANOR_GALLERY_STAIRS, Regions.RADIANT_MANOR_BALLROOM_UPPER_PILLARS, DirectionType.WEST, TransitionType.SCREENS, True_())
    RADIANT_MANOR_GALLERY_WEST_TRANSITION = ('Radiant Manor Gallery West Transition', Regions.RADIANT_MANOR_GALLERY, Regions.RADIANT_MANOR_GALLERY_STAIRS_RIGHT, DirectionType.WEST, TransitionType.SCREENS, True_())
    RADIANT_MANOR_GENERATOR_CORE_NORTH = ('Radiant Manor Generator Core North', Regions.RADIANT_MANOR_GENERATOR_CORE, Regions.RADIANT_MANOR_GENERATOR_CORE_UNDERLAB, DirectionType.NORTH, TransitionType.DO_NOT_RANDOMIZE_ENTRANCE, True_())
    RADIANT_MANOR_GENERATOR_CORE_UNDERLAB_EAST_TRANSITION = ('Radiant Manor Generator Core Underlab East Transition', Regions.RADIANT_MANOR_GENERATOR_CORE_UNDERLAB, Regions.RADIANT_MANOR_BATHROOM_SUITE, DirectionType.WEST, TransitionType.DO_NOT_RANDOMIZE_ENTRANCE, True_())
    RADIANT_MANOR_GENERATOR_CORE_UNDERLAB_NORTH = ('Radiant Manor Generator Core Underlab North', Regions.RADIANT_MANOR_GENERATOR_CORE_UNDERLAB, Regions.RADIANT_MANOR_STUDY, DirectionType.NORTH, TransitionType.DO_NOT_RANDOMIZE_ENTRANCE, True_())
    RADIANT_MANOR_GREENHOUSE_LEFT_GEYSER_UP = ('Radiant Manor Greenhouse Left Geyser_Up', Regions.RADIANT_MANOR_GREENHOUSE_LEFT, Regions.RADIANT_MANOR_GREENHOUSE_LIGHTNING, DirectionType.OVERWORLD, TransitionType.GEYSER_UP, True_())
    RADIANT_MANOR_GREENHOUSE_LIGHTNING_END_EAST_TRANSITION = ('Radiant Manor Greenhouse Lightning End East Transition', Regions.RADIANT_MANOR_GREENHOUSE_LIGHTNING_END, Regions.RADIANT_MANOR_GREENHOUSE_LIGHTNING_EXIT, DirectionType.EAST, TransitionType.SCREENS, True_())
    RADIANT_MANOR_GREENHOUSE_LIGHTNING_EXIT_ROPE = ('Radiant Manor Greenhouse Lightning Exit Rope', Regions.RADIANT_MANOR_GREENHOUSE_LIGHTNING_EXIT, Regions.RADIANT_MANOR_GREENHOUSE_LOOKOUT, DirectionType.NORTH, TransitionType.SCREENS, CanBounce() & CanClimb())
    RADIANT_MANOR_GREENHOUSE_LIGHTNING_EXIT_WEST_TRANSITION = ('Radiant Manor Greenhouse Lightning Exit West Transition', Regions.RADIANT_MANOR_GREENHOUSE_LIGHTNING_EXIT, Regions.RADIANT_MANOR_GREENHOUSE_LIGHTNING_END, DirectionType.WEST, TransitionType.SCREENS, True_())
    RADIANT_MANOR_GREENHOUSE_LOOKOUT_EAST_TRANSITION = ('Radiant Manor Greenhouse Lookout East Transition', Regions.RADIANT_MANOR_GREENHOUSE_LOOKOUT, Regions.RADIANT_MANOR_GREENHOUSE_STATUES_BRIDGE, DirectionType.EAST, TransitionType.SCREENS, True_())
    RADIANT_MANOR_GREENHOUSE_LOOKOUT_SOUTH_TRANSITION = ('Radiant Manor Greenhouse Lookout South Transition', Regions.RADIANT_MANOR_GREENHOUSE_LOOKOUT, Regions.RADIANT_MANOR_GREENHOUSE_LIGHTNING_EXIT, DirectionType.SOUTH, TransitionType.SCREENS, CanClimb())
    RADIANT_MANOR_GREENHOUSE_RIGHT_EAST_TRANSITION = ('Radiant Manor Greenhouse Right East Transition', Regions.RADIANT_MANOR_GREENHOUSE_RIGHT, Regions.RADIANT_MANOR_GREENHOUSE_STATUES, DirectionType.EAST, TransitionType.SCREENS, True_())
    RADIANT_MANOR_GREENHOUSE_STATUES_BRIDGE_DOORS = ('Radiant Manor Greenhouse Statues Bridge Doors', Regions.RADIANT_MANOR_GREENHOUSE_STATUES_BRIDGE, Regions.RADIANT_MANOR_RAFTERS_DOOR, DirectionType.NORTH, TransitionType.DOORS, True_())
    RADIANT_MANOR_GREENHOUSE_STATUES_BRIDGE_WEST_TRANSITION = ('Radiant Manor Greenhouse Statues Bridge West Transition', Regions.RADIANT_MANOR_GREENHOUSE_STATUES_BRIDGE, Regions.RADIANT_MANOR_GREENHOUSE_LOOKOUT, DirectionType.WEST, TransitionType.SCREENS, True_())
    RADIANT_MANOR_GREENHOUSE_STATUES_DOORS = ('Radiant Manor Greenhouse Statues Doors', Regions.RADIANT_MANOR_GREENHOUSE_STATUES, Regions.RADIANT_MANOR_GREENHOUSE_WING_EXIT, DirectionType.NORTH, TransitionType.DOORS, True_())
    RADIANT_MANOR_GREENHOUSE_STATUES_WEST_TRANSITION = ('Radiant Manor Greenhouse Statues West Transition', Regions.RADIANT_MANOR_GREENHOUSE_STATUES, Regions.RADIANT_MANOR_GREENHOUSE_RIGHT, DirectionType.WEST, TransitionType.SCREENS, True_())
    RADIANT_MANOR_GREENHOUSE_WING_DOORS = ('Radiant Manor Greenhouse Wing Doors', Regions.RADIANT_MANOR_GREENHOUSE_WING, Regions.RADIANT_MANOR_BALLROOM, DirectionType.NORTH, TransitionType.DOORS, RepairedGeneratorCount(count=6))
    RADIANT_MANOR_GREENHOUSE_WING_EXIT_DOORS = ('Radiant Manor Greenhouse Wing Exit Doors', Regions.RADIANT_MANOR_GREENHOUSE_WING_EXIT, Regions.RADIANT_MANOR_GREENHOUSE_STATUES, DirectionType.NORTH, TransitionType.DOORS, True_())
    RADIANT_MANOR_GREENHOUSE_WING_EXIT_EAST_TRANSITION = ('Radiant Manor Greenhouse Wing Exit East Transition', Regions.RADIANT_MANOR_GREENHOUSE_WING_EXIT, Regions.RADIANT_MANOR_GREENHOUSE_WING, DirectionType.EAST, TransitionType.SCREENS, True_())
    RADIANT_MANOR_GREENHOUSE_WING_WEST_TRANSITION = ('Radiant Manor Greenhouse Wing West Transition', Regions.RADIANT_MANOR_GREENHOUSE_WING, Regions.RADIANT_MANOR_GREENHOUSE_WING_EXIT, DirectionType.WEST, TransitionType.SCREENS, True_())
    RADIANT_MANOR_LIBRARY_DOORS = ('Radiant Manor Library Doors', Regions.RADIANT_MANOR_FOYER_LIBRARY, Regions.RADIANT_MANOR_FOYER, DirectionType.SOUTH, TransitionType.DOORS, True_())
    RADIANT_MANOR_MEOWSTROS_CHAMBER_DOORS = ("Radiant Manor Meowstro's Chamber Doors", Regions.RADIANT_MANOR_MEOWSTROS_CHAMBER, Regions.RADIANT_MANOR_BALLROOM, DirectionType.NORTH, TransitionType.DOORS, RepairedGeneratorCount(count=6))
    RADIANT_MANOR_MIMIC_CHAMBER_STAIRS = ('Radiant Manor Mimic Chamber Stairs', Regions.RADIANT_MANOR_MIMIC_CHAMBER, Regions.RADIANT_MANOR_BALLROOM, DirectionType.NORTH, TransitionType.STAIRS, True_())
    RADIANT_MANOR_ORPHANAGE_BEDS_WEST_TRANSITION = ('Radiant Manor Orphanage Beds West Transition', Regions.RADIANT_MANOR_ORPHANAGE_BEDS, Regions.RADIANT_MANOR_ORPHANAGE, DirectionType.WEST, TransitionType.SCREENS, True_())
    RADIANT_MANOR_ORPHANAGE_DOORS = ('Radiant Manor Orphanage Doors', Regions.RADIANT_MANOR_ORPHANAGE, Regions.RADIANT_MANOR_FOYER, DirectionType.SOUTH, TransitionType.DOORS, True_())
    RADIANT_MANOR_ORPHANAGE_EAST_TRANSITION = ('Radiant Manor Orphanage East Transition', Regions.RADIANT_MANOR_ORPHANAGE, Regions.RADIANT_MANOR_ORPHANAGE_BEDS, DirectionType.EAST, TransitionType.SCREENS, True_())
    RADIANT_MANOR_ORPHANAGE_PRIVATE_ROOM_WEST_TRANSITION = ('Radiant Manor Orphanage Private Room West Transition', Regions.RADIANT_MANOR_ORPHANAGE_PRIVATE_ROOM, Regions.RADIANT_MANOR_ORPHANAGE, DirectionType.WEST, TransitionType.SCREENS, True_())
    RADIANT_MANOR_PRIME_GENERATOR_SOUTH = ('Radiant Manor Prime Generator South', Regions.RADIANT_MANOR_PRIME_GENERATOR, Regions.RADIANT_MANOR_STUDY, DirectionType.SOUTH, TransitionType.DO_NOT_RANDOMIZE_ENTRANCE, True_())
    RADIANT_MANOR_RAFTERS_DOOR_DOORS = ('Radiant Manor Rafters Door Doors', Regions.RADIANT_MANOR_RAFTERS_DOOR, Regions.RADIANT_MANOR_GREENHOUSE_STATUES_BRIDGE, DirectionType.NORTH, TransitionType.DOORS, True_())
    RADIANT_MANOR_RAFTERS_DOOR_TRAP_EAST_TRANSITION = ('Radiant Manor Rafters Door Trap East Transition', Regions.RADIANT_MANOR_RAFTERS_DOOR_TRAP, Regions.RADIANT_MANOR_RAFTERS, DirectionType.EAST, TransitionType.SCREENS, True_())
    RADIANT_MANOR_RAFTERS_STAIR_EAST_TRANSITION = ('Radiant Manor Rafters Stair East Transition', Regions.RADIANT_MANOR_RAFTERS_STAIR, Regions.RADIANT_MANOR_BALLROOM_UPPER_PILLARS, DirectionType.EAST, TransitionType.SCREENS, True_())
    RADIANT_MANOR_RAFTERS_WEST_TRANSITION = ('Radiant Manor Rafters West Transition', Regions.RADIANT_MANOR_RAFTERS, Regions.RADIANT_MANOR_RAFTERS_DOOR_TRAP, DirectionType.WEST, TransitionType.SCREENS, True_())
    RADIANT_MANOR_ROOFTOP_EAST_GAP_WEST_TRANSITION = ('Radiant Manor Rooftop East Gap West Transition', Regions.RADIANT_MANOR_ROOFTOP_EAST_GAP, Regions.RADIANT_MANOR_ROOFTOP_PANELS_EAST, DirectionType.WEST, TransitionType.SCREENS, CanJumpTiles(distance=2))
    RADIANT_MANOR_ROOFTOP_EAST_RAIL = ('Radiant Manor Rooftop East Rail', Regions.RADIANT_MANOR_ROOFTOP_EAST, Regions.RADIANT_MANOR_ROOFTOP_LEDGE, DirectionType.EAST, TransitionType.DO_NOT_RANDOMIZE_ENTRANCE, True_())
    RADIANT_MANOR_ROOFTOP_GREENHOUSE_EAST_TRANSITION = ('Radiant Manor Rooftop Greenhouse East Transition', Regions.RADIANT_MANOR_ROOFTOP_GREENHOUSE, Regions.RADIANT_MANOR_ROOFTOP_PANELS_BUSH_WEST, DirectionType.EAST, TransitionType.SCREENS, True_())
    RADIANT_MANOR_ROOFTOP_GREENHOUSE_STAIRS = ('Radiant Manor Rooftop Greenhouse Stairs', Regions.RADIANT_MANOR_ROOFTOP_GREENHOUSE, Regions.RADIANT_MANOR_BACKLIT_BALCONY, DirectionType.NORTH, TransitionType.STAIRS, True_())
    RADIANT_MANOR_ROOFTOP_LEDGE_RAIL = ('Radiant Manor Rooftop Ledge Rail', Regions.RADIANT_MANOR_ROOFTOP_LEDGE, Regions.RADIANT_MANOR_ROOFTOP_EAST, DirectionType.WEST, TransitionType.DO_NOT_RANDOMIZE_ENTRANCE, True_())
    RADIANT_MANOR_ROOFTOP_LEDGE_STAIRS = ('Radiant Manor Rooftop Ledge Stairs', Regions.RADIANT_MANOR_ROOFTOP_LEDGE, Regions.RADIANT_MANOR_SERVANTS_ARENA, DirectionType.NORTH, TransitionType.STAIRS, True_())
    RADIANT_MANOR_ROOFTOP_PANELS_BUSH_EAST_EAST_TRANSITION = ('Radiant Manor Rooftop Panels Bush East East Transition', Regions.RADIANT_MANOR_ROOFTOP_PANELS_BUSH_EAST, Regions.RADIANT_MANOR_ROOFTOP_PANELS_WEST, DirectionType.EAST, TransitionType.SCREENS, True_())
    RADIANT_MANOR_ROOFTOP_PANELS_BUSH_WEST_WEST_TRANSITION = ('Radiant Manor Rooftop Panels Bush West West Transition', Regions.RADIANT_MANOR_ROOFTOP_PANELS_BUSH_WEST, Regions.RADIANT_MANOR_ROOFTOP_GREENHOUSE, DirectionType.WEST, TransitionType.SCREENS, True_())
    RADIANT_MANOR_ROOFTOP_PANELS_EAST_TRANSITION = ('Radiant Manor Rooftop Panels East Transition', Regions.RADIANT_MANOR_ROOFTOP_PANELS_EAST, Regions.RADIANT_MANOR_ROOFTOP_EAST_GAP, DirectionType.EAST, TransitionType.SCREENS, CanJumpTiles(distance=2))
    RADIANT_MANOR_ROOFTOP_PANELS_WEST_WEST_TRANSITION = ('Radiant Manor Rooftop Panels West West Transition', Regions.RADIANT_MANOR_ROOFTOP_PANELS_WEST, Regions.RADIANT_MANOR_ROOFTOP_PANELS_BUSH_EAST, DirectionType.WEST, TransitionType.SCREENS, True_())
    RADIANT_MANOR_SERVANTS_ARENA_SOUTH_TRANSITION = ("Radiant Manor Servant's Arena South Transition", Regions.RADIANT_MANOR_SERVANTS_ARENA, Regions.RADIANT_MANOR_SERVANTS_QUARTERS, DirectionType.SOUTH, TransitionType.SCREENS, PowerLevelThreshold(power=40))
    RADIANT_MANOR_SERVANTS_ARENA_STAIRS = ("Radiant Manor Servant's Arena Stairs", Regions.RADIANT_MANOR_SERVANTS_ARENA, Regions.RADIANT_MANOR_ROOFTOP_LEDGE, DirectionType.NORTH, TransitionType.STAIRS, PowerLevelThreshold(power=40))
    RADIANT_MANOR_SERVANTS_QUARTERS_NORTH_TRANSITION = ("Radiant Manor Servant's Quarters North Transition", Regions.RADIANT_MANOR_SERVANTS_QUARTERS, Regions.RADIANT_MANOR_SERVANTS_ARENA, DirectionType.NORTH, TransitionType.SCREENS, True_())
    RADIANT_MANOR_SERVANTS_QUARTERS_WEST_TRANSITION = ("Radiant Manor Servant's Quarters West Transition", Regions.RADIANT_MANOR_SERVANTS_QUARTERS, Regions.RADIANT_MANOR_GALLERY_RIGHT, DirectionType.WEST, TransitionType.SCREENS, True_())
    RADIANT_MANOR_STUDY_NORTH = ('Radiant Manor Study North', Regions.RADIANT_MANOR_STUDY, Regions.RADIANT_MANOR_PRIME_GENERATOR, DirectionType.NORTH, TransitionType.DO_NOT_RANDOMIZE_ENTRANCE, PowerLevelThreshold(power=50))
    RADIANT_MANOR_STUDY_SOUTH = ('Radiant Manor Study South', Regions.RADIANT_MANOR_STUDY, Regions.RADIANT_MANOR_GENERATOR_CORE_UNDERLAB, DirectionType.SOUTH, TransitionType.DO_NOT_RANDOMIZE_ENTRANCE, PowerLevelThreshold(power=50))
    RADIANT_MANOR_WEST_CHAMBER_BURROW_SOUTH = ('Radiant Manor West Chamber Burrow South', Regions.RADIANT_MANOR_WEST_CHAMBER, Regions.RADIANT_MANOR_BALLROOM, DirectionType.SOUTH, TransitionType.BURROW, CanBurrow())

