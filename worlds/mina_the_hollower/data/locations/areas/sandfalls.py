from BaseClasses import LocationProgressType
from rule_builder.rules import Has, CanReachLocation
from .._generated.regions import Regions
from ... import LocationTypeEnum
from ...events import BONE_BEACH_DATA
from ...items import SingleKears, PermanentUpgrades
from ...rules.ability_rules import CanBurrow, CanBounce, CanClimb, CanCarry, \
    HasFishingRod, CanSwim, PowerLevelThreshold
from ...rules.state_rules import HasKear, RepairedGenerator
from ...rules.movement_rules import CanJumpTiles

class Locations(LocationTypeEnum):
    SF_FISH_PUFFER_BEAK = (
        "SF Fish Puffer Beak",82,Regions.SANDFALLS_MINING_OUTLOOK,HasFishingRod(),
    )

    SF_SIFTED_SANDS_SNAKE_BOMB_CHEST = (
        "SF Sifted Sands Snake Bomb Chest",326,Regions.SANDFALLS_SIFTED_SANDS,CanBurrow() & CanCarry(),
    )

    SF_GUIDING_GRAINS_TRINKET = (
        "SF Guiding Grains Trinket",330,Regions.SANDFALLS_PACHINKO,
    )

    SF_GUIDING_GRAINS_BONESTONE_LEFT = (
        "SF Guiding Grains Bonestone Left",329,Regions.SANDFALLS_PACHINKO,
    )

    SF_GUIDING_GRAINS_BONESTONE_RIGHT = (
        "SF Guiding Grains Bonestone Right",328,Regions.SANDFALLS_PACHINKO,
    )

    SF_HIDDEN_CAVE_VIAL_POUCH = (
        "SF Hidden Cave Vial Pouch",323,Regions.SANDFALLS_SIFTED_SANDS_HIDDEN_CAVE,CanBurrow() & HasKear(kear=SingleKears.SANDFALLS_HIDDEN_CAVE_KEAR.value),
    )

    SF_RING_DIVE_PARLOR_TRINKET = (
        "SF Ring Dive Parlor Trinket",317,Regions.SANDFALLS_RING_DIVE_PARLOR,CanBurrow(),
    )

    SF_SHIFTY_SECLUSION_MIMIC_CHEST = (
        "SF Shifty Seclusion Mimic Chest",327,Regions.SANDFALLS_SHIFTY_SECLUSION,
    )

    SF_PAYLOAD_PASSAGE_CHEST = (
        "SF Payload Passage Chest",332,Regions.SANDFALLS_PAYLOAD_PASSAGE_CHEST,CanBurrow() & CanCarry(),
    )

    SF_BONE_JUNCTION_CHEST = (
        "SF Bone Junction Chest",356,Regions.SANDFALLS_BONE_JUNCTION,
    )

    SF_TRAIN_VITA_S_SHOP = (
        "SF Train Vita's Shop",333,Regions.SANDFALLS_SANDY_STATION,Has(PermanentUpgrades.TRAIN_PASS.value) & Has(PermanentUpgrades.BAYOU_TICKET.value),
    )

    BB_SANDWATER_JUNCTION_ANGLER_S_RAFT = (
        "BB Sandwater Junction Angler's Raft",325,Regions.SANDFALLS_SANDWATER_JUNCTION,CanJumpTiles(distance=2) | CanSwim(),
    )
class BossLocations(LocationTypeEnum):
    SF_DEFEAT_MAJOR_MINER = ("SF Defeat Major Miner", 1013, Regions.SANDFALLS_MINERS_DEN, PowerLevelThreshold(power=20))

