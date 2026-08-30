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
    OSSEX_BALCONY_WEST_OSSEX_CITY_CENTER_MAIN = ('Ossex Balcony West_Ossex City Center Main', Regions.OSSEX_BALCONY_WEST, Regions.OSSEX_CITY_CENTER_MAIN, CanBurrow())
    OSSEX_BOWERY_TALL_RESIDENCE_UPPER_TOP_ENTRANCE_OSSEX_BOWERY_TALL_RESIDENCE_UPPER_MAIN = ('Ossex Bowery Tall Residence Upper Top Entrance_Ossex Bowery Tall Residence Upper Main', Regions.OSSEX_BOWERY_TALL_RESIDENCE_UPPER_TOP_ENTRANCE, Regions.OSSEX_BOWERY_TALL_RESIDENCE_UPPER_MAIN, True_())
    OSSEX_BOWERY_UPPER_OSSEX_BOWERY_MAIN = ('Ossex Bowery Upper_Ossex Bowery Main', Regions.OSSEX_BOWERY_UPPER, Regions.OSSEX_BOWERY_MAIN, True_())
    OSSEX_CITY_CENTER_BIKE_OSSEX_CITY_CENTER_MAIN = ('Ossex City Center Bike_Ossex City Center Main', Regions.OSSEX_CITY_CENTER_BIKE, Regions.OSSEX_CITY_CENTER_MAIN, True_())
    OSSEX_CITY_CENTER_EXCHANGE_OSSEX_CITY_CENTER_MAIN = ('Ossex City Center Exchange_Ossex City Center Main', Regions.OSSEX_CITY_CENTER_EXCHANGE, Regions.OSSEX_CITY_CENTER_MAIN, True_())
    OSSEX_CITY_CENTER_UPPER_OSSEX_CITY_CENTER_MAIN = ('Ossex City Center Upper_Ossex City Center Main', Regions.OSSEX_CITY_CENTER_UPPER, Regions.OSSEX_CITY_CENTER_MAIN, True_())
    OSSEX_COURTYARD_EAST_GAP_OSSEX_COURTYARD_EAST = ('Ossex Courtyard East Gap_Ossex Courtyard East', Regions.OSSEX_COURTYARD_EAST_GAP, Regions.OSSEX_COURTYARD_EAST, CanJumpTiles(distance=8, has_wall=True) | CanBurrow())
    OSSEX_COURTYARD_EAST_MANOR_SIDE_GARDEN_OSSEX_COURTYARD_EAST_MANOR_SIDE = ('Ossex Courtyard East Manor Side Garden_Ossex Courtyard East Manor Side', Regions.OSSEX_COURTYARD_EAST_MANOR_SIDE_GARDEN, Regions.OSSEX_COURTYARD_EAST_MANOR_SIDE, HasVialsCount(count=3) & HasKear(kear=SingleKears.OSSEX_EAST_GARDEN_KEAR.value))
    OSSEX_COURTYARD_EAST_MANOR_SIDE_OSSEX_COURTYARD_EAST_MANOR_SIDE_GARDEN = ('Ossex Courtyard East Manor Side_Ossex Courtyard East Manor Side Garden', Regions.OSSEX_COURTYARD_EAST_MANOR_SIDE, Regions.OSSEX_COURTYARD_EAST_MANOR_SIDE_GARDEN, HasVialsCount(count=3) & HasKear(kear=SingleKears.OSSEX_EAST_GARDEN_KEAR.value))
    OSSEX_COURTYARD_EAST_OSSEX_COURTYARD_EAST_GAP = ('Ossex Courtyard East_Ossex Courtyard East Gap', Regions.OSSEX_COURTYARD_EAST, Regions.OSSEX_COURTYARD_EAST_GAP, CanJumpTiles(distance=8, has_wall=True))
    OSSEX_COURTYARD_WEST_CHEST_BREAKABLE = ('Ossex Courtyard West Chest Breakable', Regions.OSSEX_COURTYARD_WEST_CHEST, Regions.OSSEX_COURTYARD_WEST, True_())
    OSSEX_HIGH_STREET_BALCONY_OSSEX_HIGH_STREET_MAIN = ('Ossex High Street Balcony_Ossex High Street Main', Regions.OSSEX_HIGH_STREET_BALCONY, Regions.OSSEX_HIGH_STREET_MAIN, HasKear(kear=SingleKears.OSSEX_HIGHSTREET_BALCONY_KEAR.value))
    OSSEX_HIGH_STREET_MAIN_OSSEX_HIGH_STREET_BALCONY = ('Ossex High Street Main_Ossex High Street Balcony', Regions.OSSEX_HIGH_STREET_MAIN, Regions.OSSEX_HIGH_STREET_BALCONY, HasKear(kear=SingleKears.OSSEX_HIGHSTREET_BALCONY_KEAR.value))
    OSSEX_HIGH_STREET_MAIN_OSSEX_HIGH_STREET_SE_GARDEN = ('Ossex High Street Main_Ossex High Street SE Garden', Regions.OSSEX_HIGH_STREET_MAIN, Regions.OSSEX_HIGH_STREET_SE_GARDEN, HasKear(kear=SingleKears.OSSEX_HIGH_STREET_SE_GARDEN_KEAR.value))
    OSSEX_HIGH_STREET_RESIDENCE_MIRROR_OSSEX_HIGH_STREET_RESIDENCE = ('Ossex High Street Residence Mirror_Ossex High Street Residence', Regions.OSSEX_HIGH_STREET_RESIDENCE_MIRROR, Regions.OSSEX_HIGH_STREET_RESIDENCE, CanClimb())
    OSSEX_HIGH_STREET_SE_GARDEN_OSSEX_HIGH_STREET_MAIN = ('Ossex High Street SE Garden_Ossex High Street Main', Regions.OSSEX_HIGH_STREET_SE_GARDEN, Regions.OSSEX_HIGH_STREET_MAIN, HasKear(kear=SingleKears.OSSEX_HIGH_STREET_SE_GARDEN_KEAR.value))
    OSSEX_HIGH_STREET_SE_GARDEN_OSSEX_HIGH_STREET_SE_GARDEN_SEWER = ('Ossex High Street SE Garden_Ossex High Street SE Garden Sewer', Regions.OSSEX_HIGH_STREET_SE_GARDEN, Regions.OSSEX_HIGH_STREET_SE_GARDEN_SEWER, CanSwim())
    OSSEX_STATION_UNDERSIDE_BURROW_OSSEX_STATION_UNDERSIDE_MAIN = ('Ossex Station Underside Burrow_Ossex Station Underside Main', Regions.OSSEX_STATION_UNDERSIDE_BURROW, Regions.OSSEX_STATION_UNDERSIDE_MAIN, CanClimb())
    OSSEX_STATION_UNDERSIDE_BURROW_OSSEX_STATION_UNDERSIDE_UPPER = ('Ossex Station Underside Burrow_Ossex Station Underside Upper', Regions.OSSEX_STATION_UNDERSIDE_BURROW, Regions.OSSEX_STATION_UNDERSIDE_UPPER, CanClimb() & HasVialsCount(count=4))
    OSSEX_STATION_UNDERSIDE_MAIN_OSSEX_STATION_UNDERSIDE_UPPER = ('Ossex Station Underside Main_Ossex Station Underside Upper', Regions.OSSEX_STATION_UNDERSIDE_MAIN, Regions.OSSEX_STATION_UNDERSIDE_UPPER, (CanJumpTiles(distance=4, has_wall=True) | CanBurrow()) & HasVialsCount(count=4) & CanClimb())
    OSSEX_STATION_UNDERSIDE_UPPER_OSSEX_STATION_UNDERSIDE_MAIN = ('Ossex Station Underside Upper_Ossex Station Underside Main', Regions.OSSEX_STATION_UNDERSIDE_UPPER, Regions.OSSEX_STATION_UNDERSIDE_MAIN, True_())

class RegionTransitions(TransitionTypeEnum):
    OSSEX_ATELIER_EXIT = ('Ossex Atelier Exit', Regions.OSSEX_ATELIER, Regions.OSSEX_HIGH_STREET_MAIN, DirectionType.SOUTH, TransitionType.DOORS, True_())
    OSSEX_BALCONY_EAST_SOUTH_OSSEX_HIGH_STEET_BALCONY = ('Ossex Balcony East South Ossex High Steet Balcony', Regions.OSSEX_BALCONY_EAST, Regions.OSSEX_HIGH_STREET_BALCONY, DirectionType.SOUTH, TransitionType.SCREENS, True_())
    OSSEX_BALCONY_EAST_WEST_OSSEX_BALCONY_WEST = ('Ossex Balcony East West Ossex Balcony West', Regions.OSSEX_BALCONY_EAST, Regions.OSSEX_BALCONY_WEST, DirectionType.WEST, TransitionType.SCREENS, True_())
    OSSEX_BALCONY_WEST_EAST_OSSEX_BALCONY_EAST = ('Ossex Balcony West East Ossex Balcony East', Regions.OSSEX_BALCONY_WEST, Regions.OSSEX_BALCONY_EAST, DirectionType.EAST, TransitionType.SCREENS, True_())
    OSSEX_BALCONY_WEST_OVERWORLD_OSSEX_HIGH_STREET_RESIDENCE_UPPER = ('Ossex Balcony West Overworld Ossex High Street Residence Upper', Regions.OSSEX_BALCONY_WEST, Regions.OSSEX_HIGH_STREET_RESIDENCE_UPPER_PUZZLE, DirectionType.OVERWORLD, TransitionType.DO_NOT_RANDOMIZE_ENTRANCE, CanBurrow())
    OSSEX_BIKE_RESIDENCE_DOOR = ('Ossex Bike Residence Door', Regions.OSSEX_BIKE_RESIDENCE, Regions.OSSEX_CITY_CENTER_MAIN, DirectionType.SOUTH, TransitionType.DOORS, True_())
    OSSEX_BIKE_RESIDENCE_NORTH_BURROW = ('Ossex Bike Residence North Burrow', Regions.OSSEX_BIKE_RESIDENCE, Regions.OSSEX_CITY_CENTER_BIKE, DirectionType.NORTH, TransitionType.SCREENS, CanBurrow())
    OSSEX_BOWERY_BEGGER_RESIDENCE_BACK_CORNER_EAST_TRANSITION = ('Ossex Bowery Begger Residence Back Corner East Transition', Regions.OSSEX_BOWERY_BEGGER_RESIDENCE_BACK_CORNER, Regions.OSSEX_BOWERY_BEGGER_RESIDENCE_BACK, DirectionType.EAST, TransitionType.SCREENS, True_())
    OSSEX_BOWERY_BEGGER_RESIDENCE_BACK_CORNER_SOUTH_BURROW = ('Ossex Bowery Begger Residence Back Corner South Burrow', Regions.OSSEX_BOWERY_BEGGER_RESIDENCE_BACK_CORNER, Regions.OSSEX_WESTERN_WALL, DirectionType.SOUTH, TransitionType.BURROW, CanBurrow())
    OSSEX_BOWERY_BEGGER_RESIDENCE_BACK_SOUTH_BURROW = ('Ossex Bowery Begger Residence Back South Burrow', Regions.OSSEX_BOWERY_BEGGER_RESIDENCE_BACK, Regions.OSSEX_BOWERY_BEGGER_RESIDENCE, DirectionType.SOUTH, TransitionType.BURROW, CanBurrow())
    OSSEX_BOWERY_BEGGER_RESIDENCE_BACK_WEST_TRANSITION = ('Ossex Bowery Begger Residence Back West Transition', Regions.OSSEX_BOWERY_BEGGER_RESIDENCE_BACK, Regions.OSSEX_BOWERY_BEGGER_RESIDENCE_BACK_CORNER, DirectionType.WEST, TransitionType.SCREENS, True_())
    OSSEX_BOWERY_BEGGER_RESIDENCE_EXIT = ('Ossex Bowery Begger Residence Exit', Regions.OSSEX_BOWERY_BEGGER_RESIDENCE, Regions.OSSEX_BOWERY_UPPER, DirectionType.SOUTH, TransitionType.DOORS, True_())
    OSSEX_BOWERY_BEGGER_RESIDENCE_NORTH_BURROW = ('Ossex Bowery Begger Residence North Burrow', Regions.OSSEX_BOWERY_BEGGER_RESIDENCE, Regions.OSSEX_BOWERY_BEGGER_RESIDENCE_BACK, DirectionType.NORTH, TransitionType.BURROW, CanBurrow())
    OSSEX_BOWERY_MAIN_EAST_TRANSITION = ('Ossex Bowery Main East Transition', Regions.OSSEX_BOWERY_MAIN, Regions.OSSEX_CITY_CENTER_MAIN, DirectionType.OVERWORLD, TransitionType.DO_NOT_RANDOMIZE_ENTRANCE, True_())
    OSSEX_BOWERY_MAIN_MUSIC_HALL_DOOR = ('Ossex Bowery Main Music Hall Door', Regions.OSSEX_BOWERY_MAIN, Regions.OSSEX_MUSIC_HALL, DirectionType.NORTH, TransitionType.DOORS, CanBurrow())
    OSSEX_BOWERY_MAIN_STATION_UNDERSIDE_DOOR = ('Ossex Bowery Main Station Underside Door', Regions.OSSEX_BOWERY_MAIN, Regions.OSSEX_STATION_UNDERSIDE_MAIN, DirectionType.NORTH, TransitionType.DOORS, True_())
    OSSEX_BOWERY_MAIN_TALL_RESIDENCE_DOOR = ('Ossex Bowery Main Tall Residence Door', Regions.OSSEX_BOWERY_MAIN, Regions.OSSEX_BOWERY_TALL_RESIDENCE, DirectionType.NORTH, TransitionType.DOORS, True_())
    OSSEX_BOWERY_TALL_RESIDENCE_EXIT = ('Ossex Bowery Tall Residence Exit', Regions.OSSEX_BOWERY_TALL_RESIDENCE, Regions.OSSEX_BOWERY_MAIN, DirectionType.SOUTH, TransitionType.DOORS, True_())
    OSSEX_BOWERY_TALL_RESIDENCE_NORTH_TRANSITION = ('Ossex Bowery Tall Residence North Transition', Regions.OSSEX_BOWERY_TALL_RESIDENCE, Regions.OSSEX_BOWERY_TALL_RESIDENCE_UPPER_MAIN, DirectionType.NORTH, TransitionType.SCREENS, True_())
    OSSEX_BOWERY_TALL_RESIDENCE_STORAGE_SOUTH_BURROW_LEFT = ('Ossex Bowery Tall Residence Storage South Burrow Left', Regions.OSSEX_BOWERY_TALL_RESIDENCE_STORAGE, Regions.OSSEX_BOWERY_TALL_RESIDENCE_UPPER_MAIN, DirectionType.SOUTH, TransitionType.BURROW, CanBurrow())
    OSSEX_BOWERY_TALL_RESIDENCE_STORAGE_SOUTH_BURROW_RIGHT = ('Ossex Bowery Tall Residence Storage South Burrow Right', Regions.OSSEX_BOWERY_TALL_RESIDENCE_STORAGE, Regions.OSSEX_BOWERY_TALL_RESIDENCE_UPPER_MAIN, DirectionType.SOUTH, TransitionType.BURROW, CanBurrow())
    OSSEX_BOWERY_TALL_RESIDENCE_UPPER_MAIN_NORTH_BURROW_LEFT = ('Ossex Bowery Tall Residence Upper Main North Burrow Left', Regions.OSSEX_BOWERY_TALL_RESIDENCE_UPPER_MAIN, Regions.OSSEX_BOWERY_TALL_RESIDENCE_STORAGE, DirectionType.NORTH, TransitionType.BURROW, CanBurrow())
    OSSEX_BOWERY_TALL_RESIDENCE_UPPER_MAIN_NORTH_BURROW_RIGHT = ('Ossex Bowery Tall Residence Upper Main North Burrow Right', Regions.OSSEX_BOWERY_TALL_RESIDENCE_UPPER_MAIN, Regions.OSSEX_BOWERY_TALL_RESIDENCE_STORAGE, DirectionType.NORTH, TransitionType.BURROW, CanBurrow())
    OSSEX_BOWERY_TALL_RESIDENCE_UPPER_MAIN_SOUTH_TRANSITION = ('Ossex Bowery Tall Residence Upper Main South Transition', Regions.OSSEX_BOWERY_TALL_RESIDENCE_UPPER_MAIN, Regions.OSSEX_BOWERY_TALL_RESIDENCE, DirectionType.SOUTH, TransitionType.SCREENS, True_())
    OSSEX_BOWERY_TALL_RESIDENCE_UPPER_TOP_ENTRANCE_STAIR_EXIT = ('Ossex Bowery Tall Residence Upper Top Entrance Stair Exit', Regions.OSSEX_BOWERY_TALL_RESIDENCE_UPPER_TOP_ENTRANCE, Regions.OSSEX_BOWERY_UPPER, DirectionType.NORTH, TransitionType.STAIRS, True_())
    OSSEX_BOWERY_UPPER_BEGGER_RESIDENCE_DOOR = ('Ossex Bowery Upper Begger Residence Door', Regions.OSSEX_BOWERY_UPPER, Regions.OSSEX_BOWERY_BEGGER_RESIDENCE, DirectionType.NORTH, TransitionType.DOORS, True_())
    OSSEX_BOWERY_UPPER_EAST_AREA_TRANSITION = ('Ossex Bowery Upper East Area Transition', Regions.OSSEX_BOWERY_UPPER, Regions.WESTERN_WILDS_OSSEX_BRIDGE, DirectionType.EAST, TransitionType.AREA_SCREENS, True_())
    OSSEX_BOWERY_UPPER_EAST_TRANSITION = ('Ossex Bowery Upper East Transition', Regions.OSSEX_BOWERY_UPPER, Regions.OSSEX_CITY_CENTER_UPPER, DirectionType.EAST, TransitionType.SCREENS, True_())
    OSSEX_BOWERY_UPPER_EXCHANGE_PIPE = ('Ossex Bowery Upper Exchange Pipe', Regions.OSSEX_BOWERY_UPPER, Regions.OSSEX_CITY_CENTER_EXCHANGE, DirectionType.OVERWORLD, TransitionType.DO_NOT_RANDOMIZE_ENTRANCE, True_())
    OSSEX_BOWERY_UPPER_STATION_DOOR = ('Ossex Bowery Upper Station Door', Regions.OSSEX_BOWERY_UPPER, Regions.OSSEX_STATION, DirectionType.NORTH, TransitionType.DOORS, True_())
    OSSEX_BOWERY_UPPER_TALL_RESIDENCE_UPPER_STAIRS = ('Ossex Bowery Upper Tall Residence Upper Stairs', Regions.OSSEX_BOWERY_UPPER, Regions.OSSEX_BOWERY_TALL_RESIDENCE_UPPER_TOP_ENTRANCE, DirectionType.NORTH, TransitionType.STAIRS, True_())
    OSSEX_CITY_CENTER_BIKE_GEYSER_DROP = ('Ossex City Center Bike Geyser Drop', Regions.OSSEX_CITY_CENTER_BIKE, Regions.OSSEX_GUTTERWAYS, DirectionType.OVERWORLD, TransitionType.GEYSER_DOWN, True_())
    OSSEX_CITY_CENTER_BIKE_RESIDENCE_BURROW = ('Ossex City Center Bike Residence Burrow', Regions.OSSEX_CITY_CENTER_BIKE, Regions.OSSEX_BIKE_RESIDENCE, DirectionType.SOUTH, TransitionType.BURROW, CanBurrow())
    OSSEX_CITY_CENTER_MAIN_BIKE_RESIDENCE_DOOR = ('Ossex City Center Main Bike Residence Door', Regions.OSSEX_CITY_CENTER_MAIN, Regions.OSSEX_BIKE_RESIDENCE, DirectionType.NORTH, TransitionType.DOORS, HasSparks( count=2))
    OSSEX_CITY_CENTER_MAIN_COUPLES_QUARTER_DOOR = ("Ossex City Center Main Couple's Quarter Door", Regions.OSSEX_CITY_CENTER_MAIN, Regions.OSSEX_COUPLES_QUARTER, DirectionType.NORTH, TransitionType.DOORS, True_())
    OSSEX_CITY_CENTER_MAIN_EMPORIUM_DOOR = ('Ossex City Center Main Emporium Door', Regions.OSSEX_CITY_CENTER_MAIN, Regions.OSSEX_EMPORIUM, DirectionType.NORTH, TransitionType.DOORS, True_())
    OSSEX_CITY_CENTER_MAIN_GUILD_HALL_DOOR = ('Ossex City Center Main Guild Hall Door', Regions.OSSEX_CITY_CENTER_MAIN, Regions.OSSEX_GUILD_HALL, DirectionType.NORTH, TransitionType.DOORS, True_())
    OSSEX_CITY_CENTER_MAIN_KEAR_INSTITUTE_DOOR = ('Ossex City Center Main Kear Institute Door', Regions.OSSEX_CITY_CENTER_MAIN, Regions.OSSEX_KEAR_INSTITUTE, DirectionType.NORTH, TransitionType.DOORS, True_())
    OSSEX_CITY_CENTER_MAIN_LEFT_TRANSITION = ('Ossex City Center Main Left Transition', Regions.OSSEX_CITY_CENTER_MAIN, Regions.OSSEX_BOWERY_MAIN, DirectionType.OVERWORLD, TransitionType.DO_NOT_RANDOMIZE_ENTRANCE, True_())
    OSSEX_CITY_CENTER_MAIN_LEGOVICHS_ARMS_DOOR = ("Ossex City Center Main Legovich's Arms Door", Regions.OSSEX_CITY_CENTER_MAIN, Regions.OSSEX_LEGOVICHS_ARMS, DirectionType.NORTH, TransitionType.DOORS, True_())
    OSSEX_CITY_CENTER_MAIN_NORTH_GATE = ('Ossex City Center Main North Gate', Regions.OSSEX_CITY_CENTER_MAIN, Regions.OSSEX_COURTYARD, DirectionType.NORTH, TransitionType.SCREENS, True_())
    OSSEX_CITY_CENTER_MAIN_PAWNTYS_EXCHANGE_DOOR = ("Ossex City Center Main Pawnty's Exchange Door", Regions.OSSEX_CITY_CENTER_MAIN, Regions.OSSEX_PAWNTY_EXCHANGE, DirectionType.NORTH, TransitionType.DOORS, True_())
    OSSEX_CITY_CENTER_MAIN_RIGHT_TRANSITION = ('Ossex City Center Main Right Transition', Regions.OSSEX_CITY_CENTER_MAIN, Regions.OSSEX_HIGH_STREET_MAIN, DirectionType.OVERWORLD, TransitionType.DO_NOT_RANDOMIZE_ENTRANCE, True_())
    OSSEX_CITY_CENTER_MAIN_SOUTH_GATE = ('Ossex City Center Main South Gate', Regions.OSSEX_CITY_CENTER_MAIN, Regions.SOUTHERN_OUTSKIRTS_COMMONS_OSSEX_ENTRY, DirectionType.SOUTH, TransitionType.AREA_SCREENS, True_())
    OSSEX_CITY_CENTER_UPPER_LEFT_TRANSITION = ('Ossex City Center Upper Left Transition', Regions.OSSEX_CITY_CENTER_UPPER, Regions.OSSEX_BOWERY_UPPER, DirectionType.WEST, TransitionType.SCREENS, True_())
    OSSEX_CITY_CENTER_UPPER_TRINKET_BAZAAR_DOOR = ('Ossex City Center Upper Trinket Bazaar Door', Regions.OSSEX_CITY_CENTER_UPPER, Regions.OSSEX_TRINKET_BAZAAR, DirectionType.NORTH, TransitionType.DOORS, True_())
    OSSEX_COUPLES_QUARTER_EXIT = ("Ossex Couple's Quarter Exit", Regions.OSSEX_COUPLES_QUARTER, Regions.OSSEX_CITY_CENTER_MAIN, DirectionType.SOUTH, TransitionType.DOORS, True_())
    OSSEX_COURTYARD_EAST_GAP_EAST_TRANSITION = ('Ossex Courtyard East Gap East Transition', Regions.OSSEX_COURTYARD_EAST_GAP, Regions.OSSEX_COURTYARD_EAST_MANOR_SIDE, DirectionType.EAST, TransitionType.SCREENS, True_())
    OSSEX_COURTYARD_EAST_MANOR_SIDE_GARDEN_GEYSER_DROP = ('Ossex Courtyard East Manor Side Garden Geyser Drop', Regions.OSSEX_COURTYARD_EAST_MANOR_SIDE_GARDEN, Regions.OSSEX_GODDREDS_GRAVE, DirectionType.OVERWORLD, TransitionType.GEYSER_DOWN, True_())
    OSSEX_COURTYARD_EAST_TRANSITION = ('Ossex Courtyard East Transition', Regions.OSSEX_COURTYARD, Regions.OSSEX_COURTYARD_EAST, DirectionType.EAST, TransitionType.SCREENS, True_())
    OSSEX_COURTYARD_EAST_WEST_TRANSITION = ('Ossex Courtyard East West Transition', Regions.OSSEX_COURTYARD_EAST, Regions.OSSEX_COURTYARD, DirectionType.WEST, TransitionType.SCREENS, True_())
    OSSEX_COURTYARD_MANSION_DOOR = ('Ossex Courtyard Mansion Door', Regions.OSSEX_COURTYARD, Regions.RADIANT_MANOR_FOYER, DirectionType.NORTH, TransitionType.DOORS, True_())
    OSSEX_COURTYARD_WEST_EAST_TRANSITION = ('Ossex Courtyard West East Transition', Regions.OSSEX_COURTYARD_WEST, Regions.OSSEX_COURTYARD, DirectionType.EAST, TransitionType.SCREENS, True_())
    OSSEX_COURTYARD_WEST_TRANSITION = ('Ossex Courtyard West Transition', Regions.OSSEX_COURTYARD, Regions.OSSEX_COURTYARD_WEST, DirectionType.WEST, TransitionType.SCREENS, True_())
    OSSEX_EMPORIUM_EXIT = ('Ossex Emporium Exit', Regions.OSSEX_EMPORIUM, Regions.OSSEX_CITY_CENTER_MAIN, DirectionType.SOUTH, TransitionType.DOORS, True_())
    OSSEX_GODDREDS_GRAVE_ARENA_NORTH_TRANSITION = ("Ossex Goddred's Grave Arena North Transition", Regions.OSSEX_GODDREDS_GRAVE_ARENA, Regions.OSSEX_GODDREDS_GRAVE_END, DirectionType.NORTH, TransitionType.SCREENS, PowerLevelThreshold(power=40))
    OSSEX_GODDREDS_GRAVE_ARENA_SOUTH_TRANSITION = ("Ossex Goddred's Grave Arena South Transition", Regions.OSSEX_GODDREDS_GRAVE_ARENA, Regions.OSSEX_GODDREDS_GRAVE_HALL, DirectionType.SOUTH, TransitionType.SCREENS, PowerLevelThreshold(power=40))
    OSSEX_GODDREDS_GRAVE_EAST_TRANSITION = ("Ossex Goddred's Grave East Transition", Regions.OSSEX_GODDREDS_GRAVE, Regions.OSSEX_GODDREDS_GRAVE_HALL, DirectionType.EAST, TransitionType.SCREENS, True_())
    OSSEX_GODDREDS_GRAVE_END_SOUTH_TRANSITION = ("Ossex Goddred's Grave End South Transition", Regions.OSSEX_GODDREDS_GRAVE_END, Regions.OSSEX_GODDREDS_GRAVE_ARENA, DirectionType.SOUTH, TransitionType.SCREENS, True_())
    OSSEX_GODDREDS_GRAVE_END_TUBE = ("Ossex Goddred's Grave End Tube", Regions.OSSEX_GODDREDS_GRAVE_END, Regions.OSSEX_GODDREDS_GRAVE_HALL, DirectionType.OVERWORLD, TransitionType.DO_NOT_RANDOMIZE_ENTRANCE, CanBurrow())
    OSSEX_GODDREDS_GRAVE_GEYSER_EXIT = ("Ossex Goddred's Grave Geyser Exit", Regions.OSSEX_GODDREDS_GRAVE, Regions.OSSEX_COURTYARD_EAST_MANOR_SIDE_GARDEN, DirectionType.OVERWORLD, TransitionType.GEYSER_UP, True_())
    OSSEX_GODDREDS_GRAVE_HALL_NORTH_TRANSITION = ("Ossex Goddred's Grave Hall North Transition", Regions.OSSEX_GODDREDS_GRAVE_HALL, Regions.OSSEX_GODDREDS_GRAVE_ARENA, DirectionType.NORTH, TransitionType.SCREENS, PowerLevelThreshold(power=40))
    OSSEX_GODDREDS_GRAVE_HALL_WEST_TRANSITION = ("Ossex Goddred's Grave Hall West Transition", Regions.OSSEX_GODDREDS_GRAVE_HALL, Regions.OSSEX_GODDREDS_GRAVE, DirectionType.WEST, TransitionType.SCREENS, True_())
    OSSEX_GUILD_BACK_ROOM_NORTH_BURROW = ('Ossex Guild Back Room North Burrow', Regions.OSSEX_GUILD_BACK_ROOM, Regions.OSSEX_CITY_CENTER_MAIN, DirectionType.NORTH, TransitionType.BURROW, CanBurrow())
    OSSEX_GUILD_BACK_ROOM_SOUTH_BURROW = ('Ossex Guild Back Room South Burrow', Regions.OSSEX_GUILD_BACK_ROOM, Regions.OSSEX_GUILD_HALL, DirectionType.SOUTH, TransitionType.BURROW, CanBurrow())
    OSSEX_GUILD_HALL_EXIT = ('Ossex Guild Hall Exit', Regions.OSSEX_GUILD_HALL, Regions.OSSEX_CITY_CENTER_MAIN, DirectionType.SOUTH, TransitionType.DOORS, True_())
    OSSEX_GUILD_HALL_NORTH_BURROW = ('Ossex Guild Hall North Burrow', Regions.OSSEX_GUILD_HALL, Regions.OSSEX_GUILD_BACK_ROOM, DirectionType.NORTH, TransitionType.BURROW, CanBurrow())
    OSSEX_GUTTERWAYS_GEYSER_UP = ('Ossex Gutterways Geyser Up', Regions.OSSEX_GUTTERWAYS, Regions.OSSEX_CITY_CENTER_BIKE, DirectionType.NORTH, TransitionType.GEYSER_UP, True_())
    OSSEX_HIGH_STREET_BALCONY_NORTH_OSSEX_BALCONY_EAST = ('Ossex High Street Balcony North Ossex Balcony East', Regions.OSSEX_HIGH_STREET_BALCONY, Regions.OSSEX_BALCONY_EAST, DirectionType.NORTH, TransitionType.SCREENS, True_())
    OSSEX_HIGH_STREET_MAIN_RESIDENCE_DOOR = ('Ossex High Street Main  Residence Door', Regions.OSSEX_HIGH_STREET_MAIN, Regions.OSSEX_HIGH_STREET_RESIDENCE, DirectionType.NORTH, TransitionType.DOORS, True_())
    OSSEX_HIGH_STREET_MAIN_ATELIER_DOOR = ('Ossex High Street Main Atelier Door', Regions.OSSEX_HIGH_STREET_MAIN, Regions.OSSEX_ATELIER, DirectionType.NORTH, TransitionType.DOORS, HasSparks( count=2))
    OSSEX_HIGH_STREET_MAIN_EAST_AREA_TRANSITION = ('Ossex High Street Main East Area Transition', Regions.OSSEX_HIGH_STREET_MAIN, Regions.EASTERN_HEATH_GRASSLAND, DirectionType.EAST, TransitionType.AREA_SCREENS, True_())
    OSSEX_HIGH_STREET_MAIN_STRATEGY_CENTER_DOOR = ('Ossex High Street Main Strategy Center Door', Regions.OSSEX_HIGH_STREET_MAIN, Regions.OSSEX_STRATEGY_CENTER, DirectionType.NORTH, TransitionType.DOORS, HasSparks(count=1))
    OSSEX_HIGH_STREET_RESIDENCE_BALCONY_EAST_STAIRS = ('Ossex High Street Residence Balcony East Stairs', Regions.OSSEX_HIGH_STREET_RESIDENCE_BALCONY_EAST, Regions.OSSEX_HIGH_STREET_RESIDENCE_UPPER_PUZZLE, DirectionType.NORTH, TransitionType.STAIRS, True_())
    OSSEX_HIGH_STREET_RESIDENCE_BALCONY_EAST_WEST_TRANSITION = ('Ossex High Street Residence Balcony East West Transition', Regions.OSSEX_HIGH_STREET_RESIDENCE_BALCONY_EAST, Regions.OSSEX_HIGH_STREET_RESIDENCE_BALCONY_WEST, DirectionType.WEST, TransitionType.SCREENS, True_())
    OSSEX_HIGH_STREET_RESIDENCE_BALCONY_WEST_DROP = ('Ossex High Street Residence Balcony West Drop', Regions.OSSEX_HIGH_STREET_RESIDENCE_BALCONY_WEST, Regions.OSSEX_CITY_CENTER_MAIN, DirectionType.OVERWORLD, TransitionType.DO_NOT_RANDOMIZE_ENTRANCE, CanBurrow())
    OSSEX_HIGH_STREET_RESIDENCE_BALCONY_WEST_EAST_TRANSITION = ('Ossex High Street Residence Balcony West East Transition', Regions.OSSEX_HIGH_STREET_RESIDENCE_BALCONY_WEST, Regions.OSSEX_HIGH_STREET_RESIDENCE_BALCONY_EAST, DirectionType.EAST, TransitionType.SCREENS, True_())
    OSSEX_HIGH_STREET_RESIDENCE_EXIT = ('Ossex High Street Residence Exit', Regions.OSSEX_HIGH_STREET_RESIDENCE, Regions.OSSEX_HIGH_STREET_MAIN, DirectionType.SOUTH, TransitionType.DOORS, True_())
    OSSEX_HIGH_STREET_RESIDENCE_MIRROR_MIRROR = ('Ossex High Street Residence Mirror Mirror', Regions.OSSEX_HIGH_STREET_RESIDENCE_MIRROR, Regions.ASTRAL_ORRERY_STARRY_MIRROR_ROOM, DirectionType.OVERWORLD, TransitionType.MIRRORS, True_())
    OSSEX_HIGH_STREET_RESIDENCE_NORTH_TRANSITION = ('Ossex High Street Residence North Transition', Regions.OSSEX_HIGH_STREET_RESIDENCE, Regions.OSSEX_HIGH_STREET_RESIDENCE_UPPER_MAIN, DirectionType.NORTH, TransitionType.SCREENS, True_())
    OSSEX_HIGH_STREET_RESIDENCE_UPPER_MAIN_SOUTH_TRANSITION = ('Ossex High Street Residence Upper Main South Transition', Regions.OSSEX_HIGH_STREET_RESIDENCE_UPPER_MAIN, Regions.OSSEX_HIGH_STREET_RESIDENCE, DirectionType.SOUTH, TransitionType.SCREENS, True_())
    OSSEX_HIGH_STREET_RESIDENCE_UPPER_PUZZLE_SOUTH_DROP = ('Ossex High Street Residence Upper Puzzle South Drop', Regions.OSSEX_HIGH_STREET_RESIDENCE_UPPER_PUZZLE, Regions.OSSEX_HIGH_STREET_RESIDENCE, DirectionType.OVERWORLD, TransitionType.DO_NOT_RANDOMIZE_ENTRANCE, True_())
    OSSEX_HIGH_STREET_RESIDENCE_UPPER_PUZZLE_STAIRS = ('Ossex High Street Residence Upper Puzzle Stairs', Regions.OSSEX_HIGH_STREET_RESIDENCE_UPPER_PUZZLE, Regions.OSSEX_HIGH_STREET_RESIDENCE_BALCONY_EAST, DirectionType.NORTH, TransitionType.STAIRS, True_())
    OSSEX_HIGH_STREET_SE_GARDEN_NOSE_BRIDGE = ('Ossex High Street SE Garden Nose Bridge', Regions.OSSEX_HIGH_STREET_SE_GARDEN, Regions.OSSEX_EASTERN_WALL, DirectionType.OVERWORLD, TransitionType.DO_NOT_RANDOMIZE_ENTRANCE, True_())
    OSSEX_HIGH_STREET_SE_GARDEN_SEWER_NORTH_BURROW = ('Ossex High Street SE Garden Sewer North Burrow', Regions.OSSEX_HIGH_STREET_SE_GARDEN_SEWER, Regions.OSSEX_HIGH_STREET_SEWER, DirectionType.NORTH, TransitionType.BURROW, CanSwim())
    OSSEX_HIGH_STREET_SEWER_GEYSER_UP = ('Ossex High Street Sewer Geyser Up', Regions.OSSEX_HIGH_STREET_SEWER, Regions.OSSEX_HIGH_STREET_MAIN, DirectionType.NORTH, TransitionType.GEYSER_UP, True_())
    OSSEX_HIGH_STREET_SEWER_SOUTH_BURROW = ('Ossex High Street Sewer South Burrow', Regions.OSSEX_HIGH_STREET_SEWER, Regions.OSSEX_HIGH_STREET_SE_GARDEN_SEWER, DirectionType.SOUTH, TransitionType.BURROW, CanSwim())
    OSSEX_KEAR_INSTITUTE_EXIT = ('Ossex Kear Institute Exit', Regions.OSSEX_KEAR_INSTITUTE, Regions.OSSEX_CITY_CENTER_MAIN, DirectionType.SOUTH, TransitionType.DOORS, True_())
    OSSEX_LEGOVICHS_ARMS_BASEMENT_GEYSER_UP = ("Ossex Legovich's Arms Basement Geyser Up", Regions.OSSEX_LEGOVICHS_ARMS_BASEMENT, Regions.OSSEX_LEGOVICHS_ARMS, DirectionType.NORTH, TransitionType.GEYSER_UP, True_())
    OSSEX_LEGOVICHS_ARMS_EXIT = ("Ossex Legovich's Arms Exit", Regions.OSSEX_LEGOVICHS_ARMS, Regions.OSSEX_CITY_CENTER_MAIN, DirectionType.SOUTH, TransitionType.DOORS, True_())
    OSSEX_LEGOVICHS_ARMS_GEYSER_DROP = ("Ossex Legovich's Arms Geyser Drop", Regions.OSSEX_LEGOVICHS_ARMS, Regions.OSSEX_LEGOVICHS_ARMS_BASEMENT, DirectionType.SOUTH, TransitionType.GEYSER_DOWN, True_())
    OSSEX_MUSIC_HALL_EXIT = ('Ossex Music Hall Exit', Regions.OSSEX_MUSIC_HALL, Regions.OSSEX_BOWERY_MAIN, DirectionType.SOUTH, TransitionType.DOORS, True_())
    OSSEX_PAWNTY_EXCHANGE_EXIT = ('Ossex Pawnty Exchange Exit', Regions.OSSEX_PAWNTY_EXCHANGE, Regions.OSSEX_CITY_CENTER_MAIN, DirectionType.SOUTH, TransitionType.DOORS, True_())
    OSSEX_STATION_EXIT = ('Ossex Station Exit', Regions.OSSEX_STATION, Regions.OSSEX_BOWERY_UPPER, DirectionType.SOUTH, TransitionType.DOORS, True_())
    OSSEX_STATION_SOUTH_BURROW = ('Ossex Station South Burrow', Regions.OSSEX_STATION, Regions.OSSEX_STATION_UNDERSIDE_BURROW, DirectionType.SOUTH, TransitionType.BURROW, CanBurrow())
    OSSEX_STATION_UNDERSIDE_EXIT = ('Ossex Station Underside Exit', Regions.OSSEX_STATION_UNDERSIDE_MAIN, Regions.OSSEX_BOWERY_MAIN, DirectionType.SOUTH, TransitionType.DOORS, True_())
    OSSEX_STATION_UNDERSIDE_UPPER_NORTH_BURROW = ('Ossex Station Underside Upper North Burrow', Regions.OSSEX_STATION_UNDERSIDE_UPPER, Regions.OSSEX_COURTYARD_WEST_CHEST, DirectionType.NORTH, TransitionType.BURROW, CanBurrow())
    OSSEX_STATION_OSSEX_TRAIN_CABOOSE = ('Ossex Station_Ossex Train Caboose', Regions.OSSEX_STATION, Regions.OSSEX_TRAIN_CABOOSE, DirectionType.OVERWORLD, TransitionType.DO_NOT_RANDOMIZE_ENTRANCE, Has(PermanentUpgrades.TRAIN_PASS.value))
    OSSEX_STRATEGY_CENTER_EXIT = ('Ossex Strategy Center Exit', Regions.OSSEX_STRATEGY_CENTER, Regions.OSSEX_HIGH_STREET_MAIN, DirectionType.SOUTH, TransitionType.DOORS, True_())
    OSSEX_TRINKET_BAZAAR_DOOR = ('Ossex Trinket Bazaar Door', Regions.OSSEX_TRINKET_BAZAAR, Regions.OSSEX_CITY_CENTER_UPPER, DirectionType.SOUTH, TransitionType.DOORS, True_())

