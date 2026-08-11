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
    ASTRAL_ORRERY_BAYOU_MIRROR_ASTRAL_ORRERY_MIRRORS_END = ("Astral Orrery Bayou Mirror_Astral Orrery Mirror's End", Regions.ASTRAL_ORRERY_BAYOU_MIRROR, Regions.ASTRAL_ORRERY_MIRRORS_END, Has(AstralPlatforms.GREEN_ASTRAL_PLATFORMS.value))
    ASTRAL_ORRERY_BONE_BEACH_MIRROR_ASTRAL_ORRERY_MIRRORS_END = ("Astral Orrery Bone Beach Mirror_Astral Orrery Mirror's End", Regions.ASTRAL_ORRERY_BONE_BEACH_MIRROR, Regions.ASTRAL_ORRERY_MIRRORS_END, Has(AstralPlatforms.RED_ASTRAL_PLATFORMS.value))
    ASTRAL_ORRERY_COLTRANE_PEAK_MIRROR_ASTRAL_ORRERY_MIRRORS_END = ("Astral Orrery Coltrane Peak Mirror_Astral Orrery Mirror's End", Regions.ASTRAL_ORRERY_COLTRANE_PEAK_MIRROR, Regions.ASTRAL_ORRERY_MIRRORS_END, Has(AstralPlatforms.PURPLE_ASTRAL_PLATFORMS.value))
    ASTRAL_ORRERY_MIRRORS_END_BLUE_STAIRS_ASTRAL_ORRERY_MIRRORS_END = ("Astral Orrery Mirror's End Blue Stairs_Astral Orrery Mirror's End", Regions.ASTRAL_ORRERY_MIRRORS_END_BLUE_STAIRS, Regions.ASTRAL_ORRERY_MIRRORS_END, Has(AstralPlatforms.BLUE_ASTRAL_PLATFORMS.value) | CanJumpTiles(distance=5, has_wall=True))
    ASTRAL_ORRERY_MIRRORS_END_MOVING_PLATFORMS_ASTRAL_ORRERY_MIRRORS_END_MOVING_STAIRS = ("Astral Orrery Mirror's End Moving Platforms_Astral Orrery Mirror's End Moving Stairs", Regions.ASTRAL_ORRERY_MIRRORS_END_MOVING_PLATFORMS, Regions.ASTRAL_ORRERY_MIRRORS_END_MOVING_STAIRS, CanBurrow() | CanJumpTiles(distance=2))
    ASTRAL_ORRERY_MIRRORS_END_MOVING_STAIRS_ASTRAL_ORRERY_MIRRORS_END_MOVING_PLATFORMS = ("Astral Orrery Mirror's End Moving Stairs_Astral Orrery Mirror's End Moving Platforms", Regions.ASTRAL_ORRERY_MIRRORS_END_MOVING_STAIRS, Regions.ASTRAL_ORRERY_MIRRORS_END_MOVING_PLATFORMS, CanClimb() | CanBurrow() | CanJumpTiles(distance=2))
    ASTRAL_ORRERY_MIRRORS_END_TOP_ASTRAL_ORRERY_MIRRORS_END = ("Astral Orrery Mirror's End Top_Astral Orrery Mirror's End", Regions.ASTRAL_ORRERY_MIRRORS_END_TOP, Regions.ASTRAL_ORRERY_MIRRORS_END, CanBurrow() & AnyThreeAstralPlatforms())
    ASTRAL_ORRERY_MIRRORS_END_ASTRAL_ORRERY_MIRRORS_END_BLUE_STAIRS = ("Astral Orrery Mirror's End_Astral Orrery Mirror's End Blue Stairs", Regions.ASTRAL_ORRERY_MIRRORS_END, Regions.ASTRAL_ORRERY_MIRRORS_END_BLUE_STAIRS, Has(AstralPlatforms.BLUE_ASTRAL_PLATFORMS.value) | CanJumpTiles(distance=5, has_wall=True))
    ASTRAL_ORRERY_MIRRORS_END_ASTRAL_ORRERY_MIRRORS_END_TOP = ("Astral Orrery Mirror's End_Astral Orrery Mirror's End Top", Regions.ASTRAL_ORRERY_MIRRORS_END, Regions.ASTRAL_ORRERY_MIRRORS_END_TOP, CanBurrow() & AnyThreeAstralPlatforms())
    ASTRAL_ORRERY_QUEENSBURY_MIRROR_ASTRAL_ORRERY_MIRRORS_END = ("Astral Orrery Queensbury Mirror_Astral Orrery Mirror's End", Regions.ASTRAL_ORRERY_QUEENSBURY_MIRROR, Regions.ASTRAL_ORRERY_MIRRORS_END, Has(AstralPlatforms.BLUE_ASTRAL_PLATFORMS.value))
    ASTRAL_ORRERY_SEPTEMBURG_MIRROR_ASTRAL_ORRERY_MIRRORS_END = ("Astral Orrery Septemburg Mirror_Astral Orrery Mirror's End", Regions.ASTRAL_ORRERY_SEPTEMBURG_MIRROR, Regions.ASTRAL_ORRERY_MIRRORS_END, Has(AstralPlatforms.YELLOW_ASTRAL_PLATFORMS.value))
    ASTRAL_ORRERY_STELLARIUM_COG_SWITCH_ASTRAL_ORRERY_STELLARIUM = ('Astral Orrery Stellarium Cog Switch_Astral Orrery Stellarium', Regions.ASTRAL_ORRERY_STELLARIUM_COG_SWITCH, Regions.ASTRAL_ORRERY_STELLARIUM, True_())
    ASTRAL_ORRERY_STELLARIUM_GRAVITY_SWITCH_ASTRAL_ORRERY_STELLARIUM = ('Astral Orrery Stellarium Gravity Switch_Astral Orrery Stellarium', Regions.ASTRAL_ORRERY_STELLARIUM_GRAVITY_SWITCH, Regions.ASTRAL_ORRERY_STELLARIUM, True_())
    ASTRAL_ORRERY_STELLARIUM_MUTANT_SWITCH_ASTRAL_ORRERY_STELLARIUM = ('Astral Orrery Stellarium Mutant Switch_Astral Orrery Stellarium', Regions.ASTRAL_ORRERY_STELLARIUM_MUTANT_SWITCH, Regions.ASTRAL_ORRERY_STELLARIUM, CanClimb())
    ASTRAL_ORRERY_STELLARIUM_MUTANT_SWITCH_ASTRAL_ORRERY_STELLARIUM_SCHOLARS_PIPE = ('Astral Orrery Stellarium Mutant Switch_Astral Orrery Stellarium Scholars Pipe', Regions.ASTRAL_ORRERY_STELLARIUM_MUTANT_SWITCH, Regions.ASTRAL_ORRERY_STELLARIUM_SCHOLARS_PIPE, CanClimb())
    ASTRAL_ORRERY_STELLARIUM_SCHOLARS_PIPE_ASTRAL_ORRERY_STELLARIUM_MUTANT_SWITCH = ('Astral Orrery Stellarium Scholars Pipe_Astral Orrery Stellarium Mutant Switch', Regions.ASTRAL_ORRERY_STELLARIUM_SCHOLARS_PIPE, Regions.ASTRAL_ORRERY_STELLARIUM_MUTANT_SWITCH, CanClimb())
    ASTRAL_ORRERY_STELLARIUM_SCHOLARS_SWITCH_ASTRAL_ORRERY_STELLARIUM_MUTANT_SWITCH = ('Astral Orrery Stellarium Scholars Switch_Astral Orrery Stellarium Mutant Switch', Regions.ASTRAL_ORRERY_STELLARIUM_SCHOLARS_SWITCH, Regions.ASTRAL_ORRERY_STELLARIUM_MUTANT_SWITCH, True_())
    ASTRAL_ORRERY_STELLARIUM_ASTRAL_ORRERY_STELLARIUM_COMPLETE = ('Astral Orrery Stellarium_Astral Orrery Stellarium Complete', Regions.ASTRAL_ORRERY_STELLARIUM, Regions.ASTRAL_ORRERY_STELLARIUM_COMPLETE, CanCarry() & CanBurrow() & CanClimb())

class RegionTransitions(TransitionTypeEnum):
    ASTRAL_ORRERY_BAYOU_MIRROR = ('Astral Orrery Bayou Mirror', Regions.ASTRAL_ORRERY_BAYOU_MIRROR, Regions.NOXS_BAYOU_MOONLIT_MIRROR, DirectionType.ASTRAL, TransitionType.MIRRORS, True_())
    ASTRAL_ORRERY_BONE_BEACH_MIRROR = ('Astral Orrery Bone Beach Mirror', Regions.ASTRAL_ORRERY_BONE_BEACH_MIRROR, Regions.BONE_BEACH_WORMS_BACK_HIDE_TENT, DirectionType.ASTRAL, TransitionType.MIRRORS, True_())
    ASTRAL_ORRERY_COG_CHAMBER_DUNGEON = ('Astral Orrery Cog Chamber Dungeon', Regions.ASTRAL_ORRERY_COG_CHAMBER, Regions.ASTRAL_ORRERY_COG_CHAMBER_END, DirectionType.ASTRAL, TransitionType.DO_NOT_RANDOMIZE_ENTRANCE, CanCarry() & CanBurrow())
    ASTRAL_ORRERY_COG_CHAMBER_END_MIRROR = ('Astral Orrery Cog Chamber End Mirror', Regions.ASTRAL_ORRERY_COG_CHAMBER_END, Regions.ASTRAL_ORRERY_STELLARIUM_COG_SWITCH, DirectionType.ASTRAL, TransitionType.MIRRORS, True_())
    ASTRAL_ORRERY_COG_CHAMBER_PIPE = ('Astral Orrery Cog Chamber Pipe', Regions.ASTRAL_ORRERY_COG_CHAMBER, Regions.ASTRAL_ORRERY_STELLARIUM, DirectionType.ASTRAL, TransitionType.DO_NOT_RANDOMIZE_ENTRANCE, True_())
    ASTRAL_ORRERY_COLTRANE_PEAK_MIRROR = ('Astral Orrery Coltrane Peak Mirror', Regions.ASTRAL_ORRERY_COLTRANE_PEAK_MIRROR, Regions.COLTRANE_PEAK_FROZEN_MIRROR_ROOM, DirectionType.ASTRAL, TransitionType.MIRRORS, True_())
    ASTRAL_ORRERY_GRAVITY_ZONE_END_MIRROR = ('Astral Orrery Gravity Zone End Mirror', Regions.ASTRAL_ORRERY_GRAVITY_ZONE_END, Regions.ASTRAL_ORRERY_STELLARIUM_GRAVITY_SWITCH, DirectionType.ASTRAL, TransitionType.MIRRORS, True_())
    ASTRAL_ORRERY_GRAVITY_ZONE_PIPE = ('Astral Orrery Gravity Zone Pipe', Regions.ASTRAL_ORRERY_GRAVITY_ZONE, Regions.ASTRAL_ORRERY_STELLARIUM, DirectionType.ASTRAL, TransitionType.DO_NOT_RANDOMIZE_ENTRANCE, True_())
    ASTRAL_ORRERY_GRAVITY_ZONE_ASTRAL_ORRERY_GRAVITY_ZONE_END = ('Astral Orrery Gravity Zone_Astral Orrery Gravity Zone End', Regions.ASTRAL_ORRERY_GRAVITY_ZONE, Regions.ASTRAL_ORRERY_GRAVITY_ZONE_END, DirectionType.ASTRAL, TransitionType.DO_NOT_RANDOMIZE_ENTRANCE, True_())
    ASTRAL_ORRERY_HALL_OF_SCHOLARS_END_MIRROR = ('Astral Orrery Hall Of Scholars End Mirror', Regions.ASTRAL_ORRERY_HALL_OF_SCHOLARS_END, Regions.ASTRAL_ORRERY_STELLARIUM_SCHOLARS_SWITCH, DirectionType.ASTRAL, TransitionType.MIRRORS, True_())
    ASTRAL_ORRERY_HALL_OF_SCHOLARS_FIGHT = ('Astral Orrery Hall Of Scholars Fight', Regions.ASTRAL_ORRERY_HALL_OF_SCHOLARS, Regions.ASTRAL_ORRERY_HALL_OF_SCHOLARS_END, DirectionType.ASTRAL, TransitionType.DO_NOT_RANDOMIZE_ENTRANCE, CanBurrow())
    ASTRAL_ORRERY_MIRRORS_END_BLUE_CHEST_SOUTH_TRANSITION = ("Astral Orrery Mirror's End Blue Chest South Transition", Regions.ASTRAL_ORRERY_MIRRORS_END_BLUE_CHEST, Regions.ASTRAL_ORRERY_MIRRORS_END_BLUE_STAIRS, DirectionType.SOUTH, TransitionType.SCREENS, True_())
    ASTRAL_ORRERY_MIRRORS_END_BLUE_STAIRS_NORTH_TRANSITION = ("Astral Orrery Mirror's End Blue Stairs North Transition", Regions.ASTRAL_ORRERY_MIRRORS_END_BLUE_STAIRS, Regions.ASTRAL_ORRERY_MIRRORS_END_BLUE_CHEST, DirectionType.NORTH, TransitionType.SCREENS, True_())
    ASTRAL_ORRERY_MIRRORS_END_EAST_PURPLE_BURROW = ("Astral Orrery Mirror's End East Purple Burrow", Regions.ASTRAL_ORRERY_COLTRANE_PEAK_MIRROR, Regions.ASTRAL_ORRERY_UNDER_COLTRANE_PEAK_MIRROR, DirectionType.EAST, TransitionType.BURROW, (Has(AstralPlatforms.PURPLE_ASTRAL_PLATFORMS.value) | CanJumpTiles(distance=5, has_wall=True)) & CanBurrow())
    ASTRAL_ORRERY_MIRRORS_END_EAST_RED_BURROW = ("Astral Orrery Mirror's End East Red Burrow", Regions.ASTRAL_ORRERY_MIRRORS_END, Regions.ASTRAL_ORRERY_MIRRORS_END_UNDER_RED_SWITCH, DirectionType.EAST, TransitionType.BURROW, Has(AstralPlatforms.RED_ASTRAL_PLATFORMS.value) & CanBurrow())
    ASTRAL_ORRERY_MIRRORS_END_LARGE_MIRROR = ("Astral Orrery Mirror's End Large Mirror", Regions.ASTRAL_ORRERY_MIRRORS_END, Regions.RADIANT_MANOR_FOYER, DirectionType.ASTRAL, TransitionType.MIRRORS, True_())
    ASTRAL_ORRERY_MIRRORS_END_MOVING_PLATFORMS_SOUTH_BURROW = ("Astral Orrery Mirror's End Moving Platforms South Burrow", Regions.ASTRAL_ORRERY_MIRRORS_END_MOVING_PLATFORMS, Regions.ASTRAL_ORRERY_MIRRORS_END_TOP, DirectionType.SOUTH, TransitionType.BURROW, True_())
    ASTRAL_ORRERY_MIRRORS_END_MOVING_STAIRS_STAIRS = ("Astral Orrery Mirror's End Moving Stairs Stairs", Regions.ASTRAL_ORRERY_MIRRORS_END_MOVING_STAIRS, Regions.ASTRAL_ORRERY_STELLARIUM, DirectionType.NORTH, TransitionType.STAIRS, True_())
    ASTRAL_ORRERY_MIRRORS_END_RED_CHEST_WEST_BURROW = ("Astral Orrery Mirror's End Red Chest West Burrow", Regions.ASTRAL_ORRERY_MIRRORS_END_RED_CHEST, Regions.ASTRAL_ORRERY_MIRRORS_END_UNDER_RED_SWITCH, DirectionType.WEST, TransitionType.BURROW, Has(AstralPlatforms.RED_ASTRAL_PLATFORMS.value) & CanBurrow())
    ASTRAL_ORRERY_MIRRORS_END_TOP_NORTH_BURROW = ("Astral Orrery Mirror's End Top North Burrow", Regions.ASTRAL_ORRERY_MIRRORS_END_TOP, Regions.ASTRAL_ORRERY_MIRRORS_END_MOVING_PLATFORMS, DirectionType.NORTH, TransitionType.BURROW, True_())
    ASTRAL_ORRERY_MIRRORS_END_UNDER_RED_SWITCH_BURROW_WEST = ("Astral Orrery Mirror's End Under Red Switch Burrow West", Regions.ASTRAL_ORRERY_MIRRORS_END_UNDER_RED_SWITCH, Regions.ASTRAL_ORRERY_MIRRORS_END, DirectionType.WEST, TransitionType.BURROW, Has(AstralPlatforms.RED_ASTRAL_PLATFORMS.value) & CanBurrow())
    ASTRAL_ORRERY_MIRRORS_END_UNDER_RED_SWITCH_EAST_BURROW = ("Astral Orrery Mirror's End Under Red Switch East Burrow", Regions.ASTRAL_ORRERY_MIRRORS_END_UNDER_RED_SWITCH, Regions.ASTRAL_ORRERY_MIRRORS_END_RED_CHEST, DirectionType.EAST, TransitionType.BURROW, Has(AstralPlatforms.RED_ASTRAL_PLATFORMS.value) & CanBurrow())
    ASTRAL_ORRERY_MUTANT_LAB_DUNGEON = ('Astral Orrery Mutant Lab Dungeon', Regions.ASTRAL_ORRERY_MUTANT_LAB, Regions.ASTRAL_ORRERY_MUTANT_LAB_END, DirectionType.ASTRAL, TransitionType.DO_NOT_RANDOMIZE_ENTRANCE, CanCarry() & CanBurrow())
    ASTRAL_ORRERY_MUTANT_LAB_END_MIRROR = ('Astral Orrery Mutant Lab End Mirror', Regions.ASTRAL_ORRERY_MUTANT_LAB_END, Regions.ASTRAL_ORRERY_STELLARIUM_MUTANT_SWITCH, DirectionType.ASTRAL, TransitionType.MIRRORS, True_())
    ASTRAL_ORRERY_MUTANT_LAB_PIPE = ('Astral Orrery Mutant Lab Pipe', Regions.ASTRAL_ORRERY_MUTANT_LAB, Regions.ASTRAL_ORRERY_STELLARIUM, DirectionType.ASTRAL, TransitionType.DO_NOT_RANDOMIZE_ENTRANCE, True_())
    ASTRAL_ORRERY_QUEENSBURY_MIRROR = ('Astral Orrery Queensbury Mirror', Regions.ASTRAL_ORRERY_QUEENSBURY_MIRROR, Regions.QUEENSBURY_CRYPT_MIRROR_ROOM_EAST, DirectionType.ASTRAL, TransitionType.MIRRORS, True_())
    ASTRAL_ORRERY_SCHOLARS_PIPE = ('Astral Orrery Scholars  Pipe', Regions.ASTRAL_ORRERY_HALL_OF_SCHOLARS, Regions.ASTRAL_ORRERY_STELLARIUM_SCHOLARS_PIPE, DirectionType.ASTRAL, TransitionType.DO_NOT_RANDOMIZE_ENTRANCE, True_())
    ASTRAL_ORRERY_SEALED_ARCHIVE_BOXES_NORTH_TRANSITION = ('Astral Orrery Sealed Archive Boxes North Transition', Regions.ASTRAL_ORRERY_SEALED_ARCHIVE_BOXES, Regions.ASTRAL_ORRERY_SEALED_ARCHIVE_HALL, DirectionType.NORTH, TransitionType.DO_NOT_RANDOMIZE_ENTRANCE, True_())
    ASTRAL_ORRERY_SEALED_ARCHIVE_BOXES_SOUTH_TRANSITION = ('Astral Orrery Sealed Archive Boxes South Transition', Regions.ASTRAL_ORRERY_SEALED_ARCHIVE_BOXES, Regions.ASTRAL_ORRERY_SEALED_ARCHIVE_GLASS, DirectionType.SOUTH, TransitionType.DO_NOT_RANDOMIZE_ENTRANCE, True_())
    ASTRAL_ORRERY_SEALED_ARCHIVE_CONGEALED_CHAMBER_NORTH_TRANSITION = ('Astral Orrery Sealed Archive Congealed Chamber North Transition', Regions.ASTRAL_ORRERY_SEALED_ARCHIVE_CONGEALED_CHAMBER, Regions.ASTRAL_ORRERY_STARRY_GENERATOR_STAIRS, DirectionType.NORTH, TransitionType.DO_NOT_RANDOMIZE_ENTRANCE, True_())
    ASTRAL_ORRERY_SEALED_ARCHIVE_CONGEALED_CHAMBER_SOUTH_TRANSITION = ('Astral Orrery Sealed Archive Congealed Chamber South Transition', Regions.ASTRAL_ORRERY_SEALED_ARCHIVE_CONGEALED_CHAMBER, Regions.ASTRAL_ORRERY_SEALED_ARCHIVE_HALL, DirectionType.SOUTH, TransitionType.DO_NOT_RANDOMIZE_ENTRANCE, True_())
    ASTRAL_ORRERY_SEALED_ARCHIVE_GLASS_NORTH_TRANSITION = ('Astral Orrery Sealed Archive Glass North Transition', Regions.ASTRAL_ORRERY_SEALED_ARCHIVE_GLASS, Regions.ASTRAL_ORRERY_SEALED_ARCHIVE_BOXES, DirectionType.NORTH, TransitionType.DO_NOT_RANDOMIZE_ENTRANCE, True_())
    ASTRAL_ORRERY_SEALED_ARCHIVE_GLASS_SOUTH_TRANSITION = ('Astral Orrery Sealed Archive Glass South Transition', Regions.ASTRAL_ORRERY_SEALED_ARCHIVE_GLASS, Regions.ASTRAL_ORRERY_SEALED_ARCHIVE, DirectionType.SOUTH, TransitionType.DO_NOT_RANDOMIZE_ENTRANCE, True_())
    ASTRAL_ORRERY_SEALED_ARCHIVE_HALL_NORTH_TRANSITION = ('Astral Orrery Sealed Archive Hall North Transition', Regions.ASTRAL_ORRERY_SEALED_ARCHIVE_HALL, Regions.ASTRAL_ORRERY_SEALED_ARCHIVE_CONGEALED_CHAMBER, DirectionType.NORTH, TransitionType.DO_NOT_RANDOMIZE_ENTRANCE, True_())
    ASTRAL_ORRERY_SEALED_ARCHIVE_HALL_SOUTH_TRANSITION = ('Astral Orrery Sealed Archive Hall South Transition', Regions.ASTRAL_ORRERY_SEALED_ARCHIVE_HALL, Regions.ASTRAL_ORRERY_SEALED_ARCHIVE_BOXES, DirectionType.SOUTH, TransitionType.DO_NOT_RANDOMIZE_ENTRANCE, True_())
    ASTRAL_ORRERY_SEALED_ARCHIVE_MIRROR = ('Astral Orrery Sealed Archive Mirror', Regions.ASTRAL_ORRERY_SEALED_ARCHIVE, Regions.ASTRAL_ORRERY_STELLARIUM_COMPLETE, DirectionType.ASTRAL, TransitionType.MIRRORS, True_())
    ASTRAL_ORRERY_SEALED_ARCHIVE_NORTH_TRANSITION = ('Astral Orrery Sealed Archive North Transition', Regions.ASTRAL_ORRERY_SEALED_ARCHIVE, Regions.ASTRAL_ORRERY_SEALED_ARCHIVE_GLASS, DirectionType.NORTH, TransitionType.DO_NOT_RANDOMIZE_ENTRANCE, True_())
    ASTRAL_ORRERY_SEPTEMBURG_MIRROR = ('Astral Orrery Septemburg Mirror', Regions.ASTRAL_ORRERY_SEPTEMBURG_MIRROR, Regions.SEPTEMBURG_FARM_HOUSE, DirectionType.ASTRAL, TransitionType.MIRRORS, True_())
    ASTRAL_ORRERY_STARRY_GENERATOR_SOUTH_TRANSITION = ('Astral Orrery Starry Generator South Transition', Regions.ASTRAL_ORRERY_STARRY_GENERATOR, Regions.ASTRAL_ORRERY_STARRY_GENERATOR_STAIRS, DirectionType.SOUTH, TransitionType.BURROW, CanBurrow())
    ASTRAL_ORRERY_STARRY_GENERATOR_STAIRS_NORTH_TRANSITION = ('Astral Orrery Starry Generator Stairs North Transition', Regions.ASTRAL_ORRERY_STARRY_GENERATOR_STAIRS, Regions.ASTRAL_ORRERY_STARRY_GENERATOR, DirectionType.NORTH, TransitionType.BURROW, CanBurrow())
    ASTRAL_ORRERY_STARRY_GENERATOR_STAIRS_SOUTH_TRANSITION = ('Astral Orrery Starry Generator Stairs South Transition', Regions.ASTRAL_ORRERY_STARRY_GENERATOR_STAIRS, Regions.ASTRAL_ORRERY_SEALED_ARCHIVE_CONGEALED_CHAMBER, DirectionType.SOUTH, TransitionType.DO_NOT_RANDOMIZE_ENTRANCE, True_())
    ASTRAL_ORRERY_STARRY_GENERATOR_STAIRS_STAIRS = ('Astral Orrery Starry Generator Stairs Stairs', Regions.ASTRAL_ORRERY_STARRY_GENERATOR_STAIRS, Regions.ASTRAL_ORRERY_STARRY_MIRROR_ROOM, DirectionType.NORTH, TransitionType.STAIRS, True_())
    ASTRAL_ORRERY_STARRY_MIRROR_ROOM_MIRROR = ('Astral Orrery Starry Mirror Room Mirror', Regions.ASTRAL_ORRERY_STARRY_MIRROR_ROOM, Regions.OSSEX_HIGH_STREET_RESIDENCE_MIRROR, DirectionType.ASTRAL, TransitionType.MIRRORS, True_())
    ASTRAL_ORRERY_STARRY_MIRROR_ROOM_STAIRS = ('Astral Orrery Starry Mirror Room Stairs', Regions.ASTRAL_ORRERY_STARRY_MIRROR_ROOM, Regions.ASTRAL_ORRERY_STARRY_GENERATOR_STAIRS, DirectionType.NORTH, TransitionType.STAIRS, True_())
    ASTRAL_ORRERY_STELLARIUM_COG_CHAMBER_PIPE = ('Astral Orrery Stellarium Cog Chamber Pipe', Regions.ASTRAL_ORRERY_STELLARIUM, Regions.ASTRAL_ORRERY_COG_CHAMBER, DirectionType.ASTRAL, TransitionType.DO_NOT_RANDOMIZE_ENTRANCE, True_())
    ASTRAL_ORRERY_STELLARIUM_COG_SWITCH_MIRROR = ('Astral Orrery Stellarium Cog Switch Mirror', Regions.ASTRAL_ORRERY_STELLARIUM_COG_SWITCH, Regions.ASTRAL_ORRERY_COG_CHAMBER_END, DirectionType.ASTRAL, TransitionType.MIRRORS, True_())
    ASTRAL_ORRERY_STELLARIUM_COMPLETE_MIRROR = ('Astral Orrery Stellarium Complete Mirror', Regions.ASTRAL_ORRERY_STELLARIUM_COMPLETE, Regions.ASTRAL_ORRERY_SEALED_ARCHIVE, DirectionType.ASTRAL, TransitionType.MIRRORS, True_())
    ASTRAL_ORRERY_STELLARIUM_GRAVITY_SWITCH_MIRROR = ('Astral Orrery Stellarium Gravity Switch Mirror', Regions.ASTRAL_ORRERY_STELLARIUM_GRAVITY_SWITCH, Regions.ASTRAL_ORRERY_GRAVITY_ZONE_END, DirectionType.ASTRAL, TransitionType.MIRRORS, True_())
    ASTRAL_ORRERY_STELLARIUM_GRAVITY_ZONE_PIPE = ('Astral Orrery Stellarium Gravity Zone Pipe', Regions.ASTRAL_ORRERY_STELLARIUM, Regions.ASTRAL_ORRERY_GRAVITY_ZONE, DirectionType.ASTRAL, TransitionType.DO_NOT_RANDOMIZE_ENTRANCE, True_())
    ASTRAL_ORRERY_STELLARIUM_MUTANT_LAB_PIPE = ('Astral Orrery Stellarium Mutant Lab Pipe', Regions.ASTRAL_ORRERY_STELLARIUM, Regions.ASTRAL_ORRERY_MUTANT_LAB, DirectionType.ASTRAL, TransitionType.DO_NOT_RANDOMIZE_ENTRANCE, True_())
    ASTRAL_ORRERY_STELLARIUM_MUTANT_SWITCH_MIRROR = ('Astral Orrery Stellarium Mutant Switch Mirror', Regions.ASTRAL_ORRERY_STELLARIUM_MUTANT_SWITCH, Regions.ASTRAL_ORRERY_MUTANT_LAB_END, DirectionType.ASTRAL, TransitionType.MIRRORS, True_())
    ASTRAL_ORRERY_STELLARIUM_SCHOLARS_PIPE = ('Astral Orrery Stellarium Scholars Pipe', Regions.ASTRAL_ORRERY_STELLARIUM_SCHOLARS_PIPE, Regions.ASTRAL_ORRERY_HALL_OF_SCHOLARS, DirectionType.ASTRAL, TransitionType.DO_NOT_RANDOMIZE_ENTRANCE, True_())
    ASTRAL_ORRERY_STELLARIUM_SCHOLARS_SWITCH_MIRROR = ('Astral Orrery Stellarium Scholars Switch Mirror', Regions.ASTRAL_ORRERY_STELLARIUM_SCHOLARS_SWITCH, Regions.ASTRAL_ORRERY_HALL_OF_SCHOLARS_END, DirectionType.ASTRAL, TransitionType.MIRRORS, True_())
    ASTRAL_ORRERY_STELLARIUM_STAIRS = ('Astral Orrery Stellarium Stairs', Regions.ASTRAL_ORRERY_STELLARIUM, Regions.ASTRAL_ORRERY_MIRRORS_END_MOVING_STAIRS, DirectionType.NORTH, TransitionType.STAIRS, True_())
    ASTRAL_ORRERY_UNDER_COLTRANE_PEAK_MIRROR_WEST_BURROW = ('Astral Orrery Under Coltrane Peak Mirror West Burrow', Regions.ASTRAL_ORRERY_UNDER_COLTRANE_PEAK_MIRROR, Regions.ASTRAL_ORRERY_COLTRANE_PEAK_MIRROR, DirectionType.WEST, TransitionType.BURROW, (Has(AstralPlatforms.PURPLE_ASTRAL_PLATFORMS.value) | CanJumpTiles(distance=5, has_wall=True)) & CanBurrow())

