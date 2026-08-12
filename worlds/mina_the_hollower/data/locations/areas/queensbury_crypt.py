from BaseClasses import LocationProgressType
from rule_builder.rules import Has, CanReachLocation
from .._generated.regions import Regions
from ... import LocationTypeEnum
from ...events import QUEENSBURY_CRYPT_DATA
from ...items import SingleKears
from ...rules.ability_rules import CanBurrow, CanBounce, CanClimb, CanCarry, \
    HasFishingRod, HasVialsCount, PowerLevelThreshold
from ...rules.movement_rules import CanJumpTiles
from ...rules.state_rules import RepairedGenerator, HasKear

class Locations(LocationTypeEnum):
    QC_OLD_GRAVEYARD_BONESTONE = (
        "QC Old Graveyard Bonestone",51,Regions.QUEENSBURY_CRYPT_OLD_GRAVEYARD_MAIN,
    )

    QC_MRS_SODSBY_REWARD = (
        "QC Mrs. Sodsby Reward",52,Regions.QUEENSBURY_CRYPT_OLD_GRAVEYARD_SODSBY,CanBurrow(),
    )

    QC_BONNET_TOMB_TRINKET = (
        "QC Bonnet Tomb Trinket",57,Regions.QUEENSBURY_CRYPT_BONNET_TOMB_INNER,
    )

    QC_BROKEN_BRIDGE_BONESTONE = (
        "QC Broken Bridge Bonestone",54,Regions.QUEENSBURY_CRYPT_BROKEN_BRIDGE,
    )

    QC_PIPE_ROOM_BONESTONE = (
        "QC Pipe Room Bonestone",53,Regions.QUEENSBURY_CRYPT_PIPE_ROOM,
    )

    QC_CASTLE_ENTRY_WEAPON_CHEST = (
        "QC Castle Entry Weapon Chest",56,Regions.QUEENSBURY_CRYPT_CASTLE_ENTRY,
    )

    QC_MIDDEN_1_KEAR = (
        "QC Midden 1 Kear",64,Regions.QUEENSBURY_CRYPT_SMELLY_SECRET,
    )

    QC_HIDDEN_TUNNEL_BONESTONE = (
        "QC Hidden Tunnel Bonestone",61,Regions.QUEENSBURY_CRYPT_HIDDEN_TUNNEL,
    )

    QC_STATUE_HEAD_HALL_CHEST = (
        "QC Statue Head Hall Chest",63,Regions.QUEENSBURY_CRYPT_STATUE_HEAD_HALL_ENTRANCE,
    )

    QC_MIRROR_ROOM_CHEST = (
        "QC Mirror Room Chest",65,Regions.QUEENSBURY_CRYPT_MIRROR_ROOM_WEST,
    )

    QC_MIRROR_ROOM_BELVEDERE_TRINKET = (
        "QC Mirror Room Belvedere Trinket",66,Regions.QUEENSBURY_CRYPT_MIRROR_ROOM_WEST,
    )

    QC_MIRROR_ROOM_BELVEDERE_KEAR = (
        "QC Mirror Room Belvedere Kear",67,Regions.QUEENSBURY_CRYPT_MIRROR_ROOM_WEST,
    )

    QC_MIDDEN_2_BONESTONE = (
        "QC Midden 2 Bonestone",62,Regions.QUEENSBURY_CRYPT_PUTRID_PLACE,
    )

    QC_FISH_TOMBSTONE = (
        "QC Fish Tombstone",68,Regions.QUEENSBURY_CRYPT_SMELLY_SECRET,HasFishingRod(),
    )

    QC_MIDDEN_FIGHT_REWARD = (
        "QC Midden Fight Reward",59,Regions.QUEENSBURY_CRYPT_RANCID_ROOM,
    )

    QC_THE_DUCHESS_FIGHT_REWARD = (
        "QC The Duchess Fight Reward",58,Regions.QUEENSBURY_CRYPT_ANCESTRAL_CHAMBER,
    )

    QC_THE_DUKE_ESCORT_REWARD = (
        "QC The Duke Escort Reward",60,Regions.QUEENSBURY_CRYPT_ROYAL_TOMB,HasVialsCount(count=2) & CanClimb(),
    )

    EH_POST_GENERATOR_HEAD_ESCORT_CHEST = (
        "EH Post Generator Head Escort Chest",238,Regions.EASTERN_HEATH_EAST_CORNER,RepairedGenerator(event=QUEENSBURY_CRYPT_DATA)
        & HasKear(kear=SingleKears.MOURNERS_MILE_AFTER_GENERATOR_KEAR.value)
        & CanCarry()
        & CanClimb(),
    )

    MM_KNIGHTS_REST_POST_GENERATOR_BONESTONE = (
        "MM Knight's Rest Post Generator Bonestone",303,Regions.MOURNERS_MILE_KNIGHTS_GUARD_HILL,CanCarry(),
    )

class BossLocations(LocationTypeEnum):
    QB_DEFEAT_MIDDEN = ("QB Defeat Midden", 1028, Regions.QUEENSBURY_CRYPT_RANCID_ROOM, PowerLevelThreshold(power=25))
    QB_DEFEAT_THE_DUCHESS = ("QB Defeat The Duchess", 1001, Regions.QUEENSBURY_CRYPT_SOLEMN_GENERATOR, PowerLevelThreshold(power=25))
    # QB_SOLEMN_GENERATOR = ("QB Solemn Generator Repaired", 6001, Regions.QUEENSBURY_CRYPT_SOLEMN_GENERATOR)

