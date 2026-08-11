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



class RegionTransitions(TransitionTypeEnum):
    BAYOU_STOP = ('Bayou Stop', Regions.OSSEX_TRAIN_INTERIOR, Regions.BACKWATERS_LOWER_SWAMP_STATION, DirectionType.OVERWORLD, TransitionType.DO_NOT_RANDOMIZE_ENTRANCE, Has(PermanentUpgrades.BAYOU_TICKET.value))
    BAYOU_STOP_2 = ('Bayou Stop 2', Regions.OSSEX_TRAIN_CAB, Regions.BACKWATERS_LOWER_SWAMP_STATION, DirectionType.OVERWORLD, TransitionType.DO_NOT_RANDOMIZE_ENTRANCE, Has(PermanentUpgrades.BAYOU_TICKET.value))
    COLTRANE_PEAK_STOP = ('Coltrane Peak Stop', Regions.OSSEX_TRAIN_INTERIOR, Regions.COLTRANE_PEAK_THORNE_ARENA, DirectionType.OVERWORLD, TransitionType.DO_NOT_RANDOMIZE_ENTRANCE, Has(PermanentUpgrades.COLTRANE_PEAK_TICKET.value) & CanClimb() & PowerLevelThreshold(power=30))
    COLTRANE_PEAK_STOP_2 = ('Coltrane Peak Stop 2', Regions.OSSEX_TRAIN_CAB, Regions.COLTRANE_PEAK_THORNE_ARENA, DirectionType.OVERWORLD, TransitionType.DO_NOT_RANDOMIZE_ENTRANCE, Has(PermanentUpgrades.COLTRANE_PEAK_TICKET.value) & CanClimb() & PowerLevelThreshold(power=30))
    KINDLEWOOD_STOP = ('Kindlewood Stop', Regions.OSSEX_TRAIN_INTERIOR, Regions.KINDLEWOOD_FARM_CROSSING, DirectionType.OVERWORLD, TransitionType.DO_NOT_RANDOMIZE_ENTRANCE, Has(PermanentUpgrades.SEPTEMBURG_TICKET.value))
    KINDLEWOOD_STOP_2 = ('Kindlewood Stop 2', Regions.OSSEX_TRAIN_CAB, Regions.KINDLEWOOD_FARM_CROSSING, DirectionType.OVERWORLD, TransitionType.DO_NOT_RANDOMIZE_ENTRANCE, Has(PermanentUpgrades.SEPTEMBURG_TICKET.value))
    OSSEX_STOP = ('Ossex Stop', Regions.OSSEX_TRAIN_INTERIOR, Regions.OSSEX_STATION, DirectionType.OVERWORLD, TransitionType.DO_NOT_RANDOMIZE_ENTRANCE, True_())
    OSSEX_STOP_2 = ('Ossex Stop 2', Regions.OSSEX_TRAIN_CAB, Regions.OSSEX_STATION, DirectionType.OVERWORLD, TransitionType.DO_NOT_RANDOMIZE_ENTRANCE, True_())
    OSSEX_TRAIN_CAB_LEFT_EXIT = ('Ossex Train Cab Left Exit', Regions.OSSEX_TRAIN_CAB, Regions.OSSEX_TRAIN_COUPLING, DirectionType.OVERWORLD, TransitionType.DO_NOT_RANDOMIZE_ENTRANCE, True_())
    OSSEX_TRAIN_CABOOSE_EAST_TRANSITION = ('Ossex Train Caboose East Transition', Regions.OSSEX_TRAIN_CABOOSE, Regions.OSSEX_TRAIN_INTERIOR, DirectionType.OVERWORLD, TransitionType.DO_NOT_RANDOMIZE_ENTRANCE, True_())
    OSSEX_TRAIN_COUPLING_EAST_EXIT = ('Ossex Train Coupling East Exit', Regions.OSSEX_TRAIN_COUPLING, Regions.OSSEX_TRAIN_CAB, DirectionType.OVERWORLD, TransitionType.DO_NOT_RANDOMIZE_ENTRANCE, True_())
    OSSEX_TRAIN_COUPLING_WEST_EXIT = ('Ossex Train Coupling West Exit', Regions.OSSEX_TRAIN_COUPLING, Regions.OSSEX_TRAIN_INTERIOR, DirectionType.OVERWORLD, TransitionType.DO_NOT_RANDOMIZE_ENTRANCE, True_())
    OSSEX_TRAIN_INTERIOR_CABIN_DOOR = ('Ossex Train Interior Cabin Door', Regions.OSSEX_TRAIN_INTERIOR, Regions.OSSEX_TRAIN_PRIVATE_CABIN_MIDDLE, DirectionType.OVERWORLD, TransitionType.DO_NOT_RANDOMIZE_ENTRANCE, True_())
    OSSEX_TRAIN_INTERIOR_EAST_EXIT = ('Ossex Train Interior East Exit', Regions.OSSEX_TRAIN_INTERIOR, Regions.OSSEX_TRAIN_COUPLING, DirectionType.OVERWORLD, TransitionType.DO_NOT_RANDOMIZE_ENTRANCE, True_())
    OSSEX_TRAIN_INTERIOR_SNEAKY_BURROW = ('Ossex Train Interior Sneaky Burrow', Regions.OSSEX_TRAIN_INTERIOR, Regions.OSSEX_TRAIN_PRIVATE_CABIN_RIGHT, DirectionType.OVERWORLD, TransitionType.DO_NOT_RANDOMIZE_ENTRANCE, CanBurrow())
    OSSEX_TRAIN_INTERIOR_WEST_TRANSITION = ('Ossex Train Interior West Transition', Regions.OSSEX_TRAIN_INTERIOR, Regions.OSSEX_TRAIN_CABOOSE, DirectionType.OVERWORLD, TransitionType.DO_NOT_RANDOMIZE_ENTRANCE, True_())
    OSSEX_TRAIN_PRIVATE_CABIN_LEFT_BURROW = ('Ossex Train Private Cabin Left Burrow', Regions.OSSEX_TRAIN_PRIVATE_CABIN_LEFT, Regions.OSSEX_TRAIN_PRIVATE_CABIN_RIGHT, DirectionType.OVERWORLD, TransitionType.DO_NOT_RANDOMIZE_ENTRANCE, CanBurrow())
    OSSEX_TRAIN_PRIVATE_CABIN_MIDDLE_EXIT = ('Ossex Train Private Cabin Middle Exit', Regions.OSSEX_TRAIN_PRIVATE_CABIN_MIDDLE, Regions.OSSEX_TRAIN_INTERIOR, DirectionType.OVERWORLD, TransitionType.DO_NOT_RANDOMIZE_ENTRANCE, True_())
    OSSEX_TRAIN_PRIVATE_CABIN_RIGHT_BURROW = ('Ossex Train Private Cabin Right Burrow', Regions.OSSEX_TRAIN_PRIVATE_CABIN_RIGHT, Regions.OSSEX_TRAIN_PRIVATE_CABIN_LEFT, DirectionType.OVERWORLD, TransitionType.DO_NOT_RANDOMIZE_ENTRANCE, CanBurrow())
    OSSEX_TRAIN_PRIVATE_CABIN_RIGHT_SNEAKY_BURROW = ('Ossex Train Private Cabin Right Sneaky Burrow', Regions.OSSEX_TRAIN_PRIVATE_CABIN_RIGHT, Regions.OSSEX_TRAIN_INTERIOR, DirectionType.OVERWORLD, TransitionType.DO_NOT_RANDOMIZE_ENTRANCE, CanBurrow())
    SANDFALLS_STOP = ('Sandfalls Stop', Regions.OSSEX_TRAIN_INTERIOR, Regions.SANDFALLS_SANDY_STATION, DirectionType.OVERWORLD, TransitionType.DO_NOT_RANDOMIZE_ENTRANCE, Has(PermanentUpgrades.BONE_BEACH_TICKET.value))
    SANDFALLS_STOP_2 = ('Sandfalls Stop 2', Regions.OSSEX_TRAIN_CAB, Regions.SANDFALLS_SANDY_STATION, DirectionType.OVERWORLD, TransitionType.DO_NOT_RANDOMIZE_ENTRANCE, Has(PermanentUpgrades.BONE_BEACH_TICKET.value))

