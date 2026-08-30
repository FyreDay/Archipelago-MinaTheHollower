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
    MOURNERS_MILE_KNIGHTS_GUARD_GENERATOR_MOURNERS_MILE_KNIGHTS_GUARD_HILL = ("Mourner's Mile Knight's Guard Generator_Mourner's Mile Knight's Guard Hill", Regions.MOURNERS_MILE_KNIGHTS_GUARD_GENERATOR, Regions.MOURNERS_MILE_KNIGHTS_GUARD_HILL, CanBurrow())
    MOURNERS_MILE_KNIGHTS_GUARD_GENERATOR_MOURNERS_MILE_KNIGHTS_GUARD_MAIN = ("Mourner's Mile Knight's Guard Generator_Mourner's Mile Knight's Guard Main", Regions.MOURNERS_MILE_KNIGHTS_GUARD_GENERATOR, Regions.MOURNERS_MILE_KNIGHTS_GUARD_MAIN, True_())
    MOURNERS_MILE_KNIGHTS_GUARD_HILL_MOURNERS_MILE_KNIGHTS_GUARD_GENERATOR = ("Mourner's Mile Knight's Guard Hill_Mourner's Mile Knight's Guard Generator", Regions.MOURNERS_MILE_KNIGHTS_GUARD_HILL, Regions.MOURNERS_MILE_KNIGHTS_GUARD_GENERATOR, CanBurrow())
    MOURNERS_MILE_KNIGHTS_GUARD_LEDGE_MOURNERS_MILE_KNIGHTS_GUARD_MAIN = ("Mourner's Mile Knight's Guard Ledge_Mourner's Mile Knight's Guard Main", Regions.MOURNERS_MILE_KNIGHTS_GUARD_LEDGE, Regions.MOURNERS_MILE_KNIGHTS_GUARD_MAIN, HasKear(kear=SingleKears.MOURNERS_MILES_BIKE_KEAR.value))
    MOURNERS_MILE_KNIGHTS_GUARD_MAIN_MOURNERS_MILE_KNIGHTS_GUARD_BIKE = ("Mourner's Mile Knight's Guard Main_Mourner's Mile Knight's Guard Bike", Regions.MOURNERS_MILE_KNIGHTS_GUARD_MAIN, Regions.MOURNERS_MILE_KNIGHTS_GUARD_BIKE, HasKear(kear=SingleKears.MOURNERS_MILES_BIKE_KEAR.value))
    MOURNERS_MILE_KNIGHTS_REST_CHEST_MOURNERS_MILE_KNIGHTS_REST_MAIN = ("Mourner's Mile Knight's Rest Chest_Mourner's Mile Knight's Rest Main", Regions.MOURNERS_MILE_KNIGHTS_REST_CHEST, Regions.MOURNERS_MILE_KNIGHTS_REST_MAIN, CanClimb())
    MOURNERS_MILE_KNIGHTS_REST_MAIN_MOURNERS_MILE_KNIGHTS_REST_CHEST = ("Mourner's Mile Knight's Rest Main_Mourner's Mile Knight's Rest Chest", Regions.MOURNERS_MILE_KNIGHTS_REST_MAIN, Regions.MOURNERS_MILE_KNIGHTS_REST_CHEST, CanJumpTiles(distance=3, has_wall=True))
    MOURNERS_MILE_SPIKE_HELL_MOURNER_MOURNERS_MILE_SPIKE_HELL_SANDFALL = ("Mourner's Mile Spike Hell Mourner_Mourner's Mile Spike Hell Sandfall", Regions.MOURNERS_MILE_SPIKE_HELL_MOURNER, Regions.MOURNERS_MILE_SPIKE_HELL_SANDFALL, (HasTrinket(trinket=Trinkets.SPIKE_SPURS.value) & Has(PlayerUpgrades.HEALTH_ROSE.value, count=6)) | (Has(Sidearms.MIST_JAR.value) & Has(PlayerUpgrades.JOULE_BOX.value, count=2)))
    MOURNERS_MILE_SPIKE_HELL_SANDFALL_MOURNERS_MILE_SPIKE_HELL_MOURNER = ("Mourner's Mile Spike Hell Sandfall_Mourner's Mile Spike Hell Mourner", Regions.MOURNERS_MILE_SPIKE_HELL_SANDFALL, Regions.MOURNERS_MILE_SPIKE_HELL_MOURNER, True_())
    MOURNERS_MILE_SPIKE_VAULT_HIDDEN_MOURNERS_MILE_SPIKE_VAULT_MAIN = ("Mourner's Mile Spike Vault Hidden_Mourner's Mile Spike Vault Main", Regions.MOURNERS_MILE_SPIKE_VAULT_HIDDEN, Regions.MOURNERS_MILE_SPIKE_VAULT_MAIN, True_())
    MOURNERS_MILE_SPIKE_VAULT_UPPER_MOURNERS_MILE_SPIKE_VAULT_HIDDEN = ("Mourner's Mile Spike Vault Upper_Mourner's Mile Spike Vault Hidden", Regions.MOURNERS_MILE_SPIKE_VAULT_UPPER, Regions.MOURNERS_MILE_SPIKE_VAULT_HIDDEN, True_())
    MOURNERS_MILE_SPIKE_VAULT_UPPER_MOURNERS_MILE_SPIKE_VAULT_MAIN = ("Mourner's Mile Spike Vault Upper_Mourner's Mile Spike Vault Main", Regions.MOURNERS_MILE_SPIKE_VAULT_UPPER, Regions.MOURNERS_MILE_SPIKE_VAULT_MAIN, True_())
    MOURNERS_MILE_STATUE_ROOM_ROPE_MOURNERS_MILE_STATUE_ROOM_MAIN = ("Mourner's Mile Statue Room Rope_Mourner's Mile Statue Room Main", Regions.MOURNERS_MILE_STATUE_ROOM_ROPE, Regions.MOURNERS_MILE_STATUE_ROOM_MAIN, CanClimb())

class RegionTransitions(TransitionTypeEnum):
    MOURNERS_MILE_DARK_SHALLOW_TOMB_DARK_GEYSER_UP = ("Mourner's Mile Dark Shallow Tomb Dark Geyser Up", Regions.MOURNERS_MILE_DARK_SHALLOW_TOMB_DARK, Regions.MOURNERS_MILE_HIDDEN_GRAVES, DirectionType.OVERWORLD, TransitionType.GEYSER_UP, True_())
    MOURNERS_MILE_DARK_SHALLOW_TOMB_PEEKHOLE_GEYSER_UP = ("Mourner's Mile Dark Shallow Tomb Peekhole Geyser Up", Regions.MOURNERS_MILE_DARK_SHALLOW_TOMB_PEEKHOLE, Regions.MOURNERS_MILE_HIDDEN_GRAVES, DirectionType.OVERWORLD, TransitionType.GEYSER_UP, True_())
    MOURNERS_MILE_GRAVEYARD_HIDDEN_GEYSER = ("Mourner's Mile Graveyard Hidden Geyser", Regions.MOURNERS_MILE_GRAVEYARD, Regions.MOURNERS_MILE_SPIKE_VAULT_HIDDEN, DirectionType.OVERWORLD, TransitionType.GEYSER_DOWN, True_())
    MOURNERS_MILE_GRAVEYARD_MAIN_GEYSER = ("Mourner's Mile Graveyard Main Geyser", Regions.MOURNERS_MILE_GRAVEYARD, Regions.MOURNERS_MILE_SPIKE_VAULT_MAIN, DirectionType.OVERWORLD, TransitionType.GEYSER_DOWN, True_())
    MOURNERS_MILE_GRAVEYARD_UPPER_DOOR_GEYSER = ("Mourner's Mile Graveyard Upper Door Geyser", Regions.MOURNERS_MILE_GRAVEYARD, Regions.MOURNERS_MILE_SPIKE_VAULT_UPPER, DirectionType.OVERWORLD, TransitionType.GEYSER_DOWN, True_())
    MOURNERS_MILE_GRAVEYARD_UPPER_GEYSER = ("Mourner's Mile Graveyard Upper Geyser", Regions.MOURNERS_MILE_GRAVEYARD, Regions.MOURNERS_MILE_SPIKE_VAULT_UPPER, DirectionType.OVERWORLD, TransitionType.GEYSER_DOWN, True_())
    MOURNERS_MILE_GRAVEYARD_WEST_TRANSITION = ("Mourner's Mile Graveyard West Transition", Regions.MOURNERS_MILE_GRAVEYARD, Regions.MOURNERS_MILE_KNIGHTS_GUARD_MAIN, DirectionType.WEST, TransitionType.SCREENS, True_())
    MOURNERS_MILE_GRAVEYARD_LEDGE_WEST_TRANSITION_NORTH = ("Mourner's Mile Graveyard ledge West Transition North", Regions.MOURNERS_MILE_GRAVEYARD_LEDGE, Regions.MOURNERS_MILE_KNIGHTS_GUARD_LEDGE, DirectionType.WEST, TransitionType.SCREENS, True_())
    MOURNERS_MILE_GRAVEYARD_LEDGE_WEST_TRANSITION_SOUTH = ("Mourner's Mile Graveyard ledge West Transition South", Regions.MOURNERS_MILE_GRAVEYARD_LEDGE, Regions.MOURNERS_MILE_KNIGHTS_GUARD_MAIN, DirectionType.WEST, TransitionType.SCREENS, True_())
    MOURNERS_MILE_HIDDEN_GRAVES_LEFT_GEYSER_DROP = ("Mourner's Mile Hidden Graves Left Geyser Drop", Regions.MOURNERS_MILE_HIDDEN_GRAVES, Regions.MOURNERS_MILE_DARK_SHALLOW_TOMB_DARK, DirectionType.OVERWORLD, TransitionType.GEYSER_DOWN, True_())
    MOURNERS_MILE_HIDDEN_GRAVES_NORTH_BURROW = ("Mourner's Mile Hidden Graves North Burrow", Regions.MOURNERS_MILE_HIDDEN_GRAVES, Regions.MOURNERS_MILE_KNIGHTS_REST_MAIN, DirectionType.NORTH, TransitionType.SCREENS, CanBurrow())
    MOURNERS_MILE_HIDDEN_GRAVES_RIGHT_GEYSER_DROP = ("Mourner's Mile Hidden Graves Right Geyser Drop", Regions.MOURNERS_MILE_HIDDEN_GRAVES, Regions.MOURNERS_MILE_DARK_SHALLOW_TOMB_PEEKHOLE, DirectionType.OVERWORLD, TransitionType.GEYSER_DOWN, True_())
    MOURNERS_MILE_HIDDEN_GRAVES_WEST_TRANSITION = ("Mourner's Mile Hidden Graves West Transition", Regions.MOURNERS_MILE_HIDDEN_GRAVES, Regions.MOURNERS_MILE_STATUE_ROOM_ROPE, DirectionType.WEST, TransitionType.SCREENS, True_())
    MOURNERS_MILE_KNIGHTS_GATE_BUTTON_DOOR = ("Mourner's Mile Knight's Gate Button Door", Regions.MOURNERS_MILE_KNIGHTS_GATE_BUTTON, Regions.MOURNERS_MILE_SPIKE_VAULT_UPPER, DirectionType.NORTH, TransitionType.DOORS, True_())
    MOURNERS_MILE_KNIGHTS_GATE_MAIN_DOOR = ("Mourner's Mile Knight's Gate Main Door", Regions.MOURNERS_MILE_KNIGHTS_GATE_MAIN, Regions.MOURNERS_MILE_SPIKE_VAULT_MAIN, DirectionType.NORTH, TransitionType.DOORS, True_())
    MOURNERS_MILE_KNIGHTS_GATE_MAIN_EAST_TRANSITION = ("Mourner's Mile Knight's Gate Main East Transition", Regions.MOURNERS_MILE_KNIGHTS_GATE_MAIN, Regions.MOURNERS_MILE_STAIRS, DirectionType.EAST, TransitionType.SCREENS, True_())
    MOURNERS_MILE_KNIGHTS_GATE_MAIN_GEYSER_DROP = ("Mourner's Mile Knight's Gate Main Geyser Drop", Regions.MOURNERS_MILE_KNIGHTS_GATE_MAIN, Regions.MOURNERS_MILE_SHALLOW_TOMB, DirectionType.SOUTH, TransitionType.GEYSER_DOWN, True_())
    MOURNERS_MILE_KNIGHTS_GATE_MAIN_NORTH_TRANSITION = ("Mourner's Mile Knight's Gate Main North Transition", Regions.MOURNERS_MILE_KNIGHTS_GATE_MAIN, Regions.MOURNERS_MILE_KNIGHTS_GUARD_MAIN, DirectionType.NORTH, TransitionType.SCREENS, True_())
    MOURNERS_MILE_KNIGHTS_GATE_MAIN_SOUTH_BURROW_TRANSITION = ("Mourner's Mile Knight's Gate Main South Burrow Transition", Regions.MOURNERS_MILE_KNIGHTS_GATE_MAIN, Regions.MOURNERS_MILE_KNIGHTS_REST_CHEST, DirectionType.SOUTH, TransitionType.BURROW, CanBurrow())
    MOURNERS_MILE_KNIGHTS_GATE_MAIN_SOUTH_TRANSITION = ("Mourner's Mile Knight's Gate Main South Transition", Regions.MOURNERS_MILE_KNIGHTS_GATE_MAIN, Regions.MOURNERS_MILE_KNIGHTS_REST_MAIN, DirectionType.SOUTH, TransitionType.SCREENS, True_())
    MOURNERS_MILE_KNIGHTS_GUARD_BIKE_MINAS_GRAVE_DOOR = ("Mourner's Mile Knight's Guard Bike Mina's Grave Door", Regions.MOURNERS_MILE_KNIGHTS_GUARD_BIKE, Regions.MOURNERS_MILE_MINAS_GRAVE, DirectionType.NORTH, TransitionType.DOORS, CanJumpTiles(distance=2, has_wall=True) & HasSparks(count=3))
    MOURNERS_MILE_KNIGHTS_GUARD_GENERATOR_OUTSIDE_DOOR = ("Mourner's Mile Knight's Guard Generator Outside Door", Regions.MOURNERS_MILE_KNIGHTS_GUARD_GENERATOR, Regions.MOURNERS_MILE_TOWER_TUNNEL_MAIN, DirectionType.NORTH, TransitionType.STAIRS, True_())
    MOURNERS_MILE_KNIGHTS_GUARD_LEDGE_EAST_TRANSITION = ("Mourner's Mile Knight's Guard Ledge East Transition", Regions.MOURNERS_MILE_KNIGHTS_GUARD_LEDGE, Regions.MOURNERS_MILE_GRAVEYARD_LEDGE, DirectionType.EAST, TransitionType.SCREENS, True_())
    MOURNERS_MILE_KNIGHTS_GUARD_LEDGE_WEST_BURROW = ("Mourner's Mile Knight's Guard Ledge West Burrow", Regions.MOURNERS_MILE_KNIGHTS_GUARD_LEDGE, Regions.MOURNERS_MILE_TOWER_TUNNEL_DARK, DirectionType.WEST, TransitionType.BURROW, CanBurrow())
    MOURNERS_MILE_KNIGHTS_GUARD_MAIN_EAST_TRANSITION_NORTH = ("Mourner's Mile Knight's Guard Main East Transition North", Regions.MOURNERS_MILE_KNIGHTS_GUARD_MAIN, Regions.MOURNERS_MILE_GRAVEYARD_LEDGE, DirectionType.EAST, TransitionType.SCREENS, True_())
    MOURNERS_MILE_KNIGHTS_GUARD_MAIN_EAST_TRANSITION_SOUTH = ("Mourner's Mile Knight's Guard Main East Transition South", Regions.MOURNERS_MILE_KNIGHTS_GUARD_MAIN, Regions.MOURNERS_MILE_GRAVEYARD, DirectionType.EAST, TransitionType.SCREENS, True_())
    MOURNERS_MILE_KNIGHTS_GUARD_MAIN_SOUTH_TRANSITION = ("Mourner's Mile Knight's Guard Main South Transition", Regions.MOURNERS_MILE_KNIGHTS_GUARD_MAIN, Regions.MOURNERS_MILE_KNIGHTS_GATE_MAIN, DirectionType.SOUTH, TransitionType.SCREENS, True_())
    MOURNERS_MILE_KNIGHTS_REST_CHEST_NORTH_BURROW = ("Mourner's Mile Knight's Rest Chest North Burrow", Regions.MOURNERS_MILE_KNIGHTS_REST_CHEST, Regions.MOURNERS_MILE_KNIGHTS_GATE_MAIN, DirectionType.NORTH, TransitionType.BURROW, CanBurrow())
    MOURNERS_MILE_KNIGHTS_REST_MAIN_NORTH_TRANSITION = ("Mourner's Mile Knight's Rest Main North Transition", Regions.MOURNERS_MILE_KNIGHTS_REST_MAIN, Regions.MOURNERS_MILE_KNIGHTS_GATE_MAIN, DirectionType.NORTH, TransitionType.SCREENS, True_())
    MOURNERS_MILE_KNIGHTS_REST_MAIN_SOUTH_BURROW = ("Mourner's Mile Knight's Rest Main South Burrow", Regions.MOURNERS_MILE_KNIGHTS_REST_MAIN, Regions.MOURNERS_MILE_HIDDEN_GRAVES, DirectionType.SOUTH, TransitionType.BURROW, CanBurrow())
    MOURNERS_MILE_KNIGHTS_REST_MAIN_SOUTH_TRANSITION = ("Mourner's Mile Knight's Rest Main South Transition", Regions.MOURNERS_MILE_KNIGHTS_REST_MAIN, Regions.MOURNERS_MILE_STATUE_ROOM_MAIN, DirectionType.SOUTH, TransitionType.SCREENS, True_())
    MOURNERS_MILE_KNIGHTS_REST_MAIN_WEST_AREA_TRANSITION = ("Mourner's Mile Knight's Rest Main West Area Transition", Regions.MOURNERS_MILE_KNIGHTS_REST_MAIN, Regions.EASTERN_HEATH_MOURNERS_GATE, DirectionType.WEST, TransitionType.SCREENS, True_())
    MOURNERS_MILE_MINAS_GRAVE_EXIT = ("Mourner's Mile Mina's Grave Exit", Regions.MOURNERS_MILE_MINAS_GRAVE, Regions.MOURNERS_MILE_KNIGHTS_GUARD_BIKE, DirectionType.SOUTH, TransitionType.DOORS, True_())
    MOURNERS_MILE_SHALLOW_TOMB_GEYSER_UP = ("Mourner's Mile Shallow Tomb Geyser Up", Regions.MOURNERS_MILE_SHALLOW_TOMB, Regions.MOURNERS_MILE_KNIGHTS_GATE_MAIN, DirectionType.OVERWORLD, TransitionType.GEYSER_UP, True_())
    MOURNERS_MILE_SPIKE_HELL_MOURNER_NORTH_BURROW = ("Mourner's Mile Spike Hell Mourner North Burrow", Regions.MOURNERS_MILE_SPIKE_HELL_MOURNER, Regions.MOURNERS_MILE_STAIRS, DirectionType.NORTH, TransitionType.SCREENS, CanBurrow())
    MOURNERS_MILE_SPIKE_HELL_SANDFALL_EAST_AREA_TRANSITION = ("Mourner's Mile Spike Hell Sandfall East Area Transition", Regions.MOURNERS_MILE_SPIKE_HELL_SANDFALL, Regions.SANDFALLS_BONE_JUNCTION_PLANK, DirectionType.EAST, TransitionType.SCREENS, True_())
    MOURNERS_MILE_SPIKE_VAULT_HIDDEN_ROOM_EAST_TRANSITION = ("Mourner's Mile Spike Vault Hidden Room East Transition", Regions.MOURNERS_MILE_SPIKE_VAULT_HIDDEN_ROOM, Regions.MOURNERS_MILE_SPIKE_VAULT_HIDDEN, DirectionType.EAST, TransitionType.SCREENS, True_())
    MOURNERS_MILE_SPIKE_VAULT_HIDDEN_WEST_TRANSITION = ("Mourner's Mile Spike Vault Hidden West Transition", Regions.MOURNERS_MILE_SPIKE_VAULT_HIDDEN, Regions.MOURNERS_MILE_SPIKE_VAULT_HIDDEN_ROOM, DirectionType.WEST, TransitionType.SCREENS, True_())
    MOURNERS_MILE_SPIKE_VAULT_MAIN_EXIT = ("Mourner's Mile Spike Vault Main Exit", Regions.MOURNERS_MILE_SPIKE_VAULT_MAIN, Regions.MOURNERS_MILE_KNIGHTS_GATE_MAIN, DirectionType.SOUTH, TransitionType.DOORS, True_())
    MOURNERS_MILE_SPIKE_VAULT_UPPER_EXIT = ("Mourner's Mile Spike Vault Upper Exit", Regions.MOURNERS_MILE_SPIKE_VAULT_UPPER, Regions.MOURNERS_MILE_KNIGHTS_GATE_BUTTON, DirectionType.SOUTH, TransitionType.DOORS, True_())
    MOURNERS_MILE_STAIRS_EAST_AREA_TRANSITION = ("Mourner's Mile Stairs East Area Transition", Regions.MOURNERS_MILE_STAIRS, Regions.QUEENSBURY_CRYPT_OLD_ENTRANCE, DirectionType.EAST, TransitionType.AREA_SCREENS, True_())
    MOURNERS_MILE_STAIRS_SOUTH_BURROW = ("Mourner's Mile Stairs South Burrow", Regions.MOURNERS_MILE_STAIRS, Regions.MOURNERS_MILE_SPIKE_HELL_MOURNER, DirectionType.SOUTH, TransitionType.SCREENS, CanBurrow())
    MOURNERS_MILE_STAIRS_WEST_TRANSITION = ("Mourner's Mile Stairs West Transition", Regions.MOURNERS_MILE_STAIRS, Regions.MOURNERS_MILE_KNIGHTS_GATE_MAIN, DirectionType.WEST, TransitionType.SCREENS, True_())
    MOURNERS_MILE_STATUE_ROOM_MAIN_NORTH_TRANSITION = ("Mourner's Mile Statue Room Main North Transition", Regions.MOURNERS_MILE_STATUE_ROOM_MAIN, Regions.MOURNERS_MILE_KNIGHTS_REST_MAIN, DirectionType.NORTH, TransitionType.SCREENS, True_())
    MOURNERS_MILE_STATUE_ROOM_MAIN_WEST_TRANSITION = ("Mourner's Mile Statue Room Main West Transition", Regions.MOURNERS_MILE_STATUE_ROOM_MAIN, Regions.EASTERN_HEATH_EAST_CORNER_CLIFF, DirectionType.WEST, TransitionType.SCREENS, True_())
    MOURNERS_MILE_STATUE_ROOM_ROPE_EAST_TRANSITION = ("Mourner's Mile Statue Room Rope East Transition", Regions.MOURNERS_MILE_STATUE_ROOM_ROPE, Regions.MOURNERS_MILE_HIDDEN_GRAVES, DirectionType.EAST, TransitionType.SCREENS, True_())
    MOURNERS_MILE_TOWER_TUNNEL_DARK_EAST_BURROW = ("Mourner's Mile Tower Tunnel Dark East Burrow", Regions.MOURNERS_MILE_TOWER_TUNNEL_DARK, Regions.MOURNERS_MILE_KNIGHTS_GUARD_LEDGE, DirectionType.EAST, TransitionType.BURROW, CanBurrow())
    MOURNERS_MILE_TOWER_TUNNEL_MAIN_NORTH_DOOR = ("Mourner's Mile Tower Tunnel Main North Door", Regions.MOURNERS_MILE_TOWER_TUNNEL_MAIN, Regions.QUEENSBURY_CRYPT_SOLEMN_GENERATOR, DirectionType.NORTH, TransitionType.STAIRS, True_())
    MOURNERS_MILE_TOWER_TUNNEL_MAIN_STAIRS = ("Mourner's Mile Tower Tunnel Main Stairs", Regions.MOURNERS_MILE_TOWER_TUNNEL_MAIN, Regions.MOURNERS_MILE_KNIGHTS_GUARD_GENERATOR, DirectionType.NORTH, TransitionType.STAIRS, True_())

