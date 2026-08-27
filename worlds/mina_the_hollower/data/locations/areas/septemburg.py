from BaseClasses import LocationProgressType
from rule_builder.rules import Has, CanReachLocation
from .._generated.regions import Regions
from ... import LocationTypeEnum
from ...events import SEPTEMBURG_DATA
from ...items import SingleKears
from ...rules.ability_rules import CanBurrow, CanBounce, CanClimb, CanCarry, HasFishingRod, CanSpring, \
    PowerLevelThreshold
from ...rules.state_rules import HasKear, HasSparks, RepairedGenerator
from ...rules.movement_rules import CanJumpTiles

class Locations(LocationTypeEnum):
    SB_LAUNCH_PAD_SECRET_ROOM_CHEST = (
        "SB Launch Pad Secret Room Chest",91,Regions.SEPTEMBURG_WITHERED_FARMS_HILLS_MAZE,CanSpring(),
    )

    SB_LAUNCH_PAD_CROW_FIGHT_REWARD = (
        "SB Launch Pad Crow Fight Reward",89,Regions.SEPTEMBURG_WITHERED_FARMS_SECRET_SPRINGS,CanSpring(),
    )

    SB_WITHERED_FARMS_KID_ROOM_CHEST = (
        "SB Withered Farms Kid Room Chest",92,Regions.SEPTEMBURG_WITHERED_FARMS_KID_ROOM_1,CanBurrow(),
    )

    SB_HIDDEN_MANDRAKE_ROOM_CHEST = (
        "SB Hidden Mandrake Room Chest",93,Regions.SEPTEMBURG_HIDDEN_MANDRAKE_ROOM,CanJumpTiles(distance=2),
    )

    SB_HIDDEN_CROP_THRESHER_ROOM_CHEST = (
        "SB Hidden Crop Thresher Room Chest",90,Regions.SEPTEMBURG_TRACTOR_CHASE,CanSpring() & CanBurrow() & CanClimb(),
    )

    SB_ROTTEN_BARN_SQUEALER_CHEST = (
        "SB Rotten Barn Squealer Chest",94,Regions.SEPTEMBURG_ROTTEN_BARN_KID_ROOM,CanBurrow(),
    )

    SB_TUNNEL_LOCKED_CHEST = (
        "SB Tunnel Locked Chest",98,Regions.SEPTEMBURG_CROW_TOWN_TUNNEL_TOP,HasKear(kear=SingleKears.SEPTEMBURG_CROW_TOWN_TUNNEL_KEAR.value),
    )

    SB_CROW_TOWN_SHOP_TRINKET = (
        "SB Crow Town Shop Trinket",102,Regions.SEPTEMBURG_CROW_TOWN,
    )

    SB_CROW_TOWN_SHOP_KEAR = (
        "SB Crow Town Shop Kear",103,Regions.SEPTEMBURG_CROW_TOWN,
    )

    SB_CROW_TOWN_FARMHOUSE_ROOF_WEAPON_CHEST = (
        "SB Crow Town Farmhouse Roof Weapon Chest",99,Regions.SEPTEMBURG_FARM_HOUSE_ROOF,CanBurrow() & CanCarry(),
    )

    SB_TANGLED_WOODS_HIDDEN_GROVE_CHEST = (
        "SB Tangled Woods Hidden Grove Chest",97,Regions.SEPTEMBURG_TANGLED_WOODS_HIDDEN_GROVE,CanBurrow(),
    )

    SB_TANGLED_WOODS_GALLOWAY_ROOM_CHEST = (
        "SB Tangled Woods Galloway Room Chest",100,Regions.SEPTEMBURG_TANGLED_WOODS_KID_ROOM,CanBurrow() & CanSpring(),
    )

    SB_STORMWATCH_WAY_CHEST = (
        "SB Stormwatch Way Chest",101,Regions.SEPTEMBURG_STORMWATCH_WIND,CanBurrow(),
    )

    SB_CARVING_MAN_FIGHT_REWARD = (
        "SB The Carving Man Fight Reward",95,Regions.SEPTEMBURG_CARVING_SHACK_ARENA, PowerLevelThreshold(power=25)
    )

    SB_DARK_DELUXY_FIGHT_REWARD = (
        "SB Dark Deluxy Fight Reward",353,Regions.SEPTEMBURG_WINDY_GENERATOR,CanBurrow() & RepairedGenerator(event=SEPTEMBURG_DATA) & HasSparks(count=2) & PowerLevelThreshold(power=40),
    )

    SB_FISH_SPINCER_PINCERS = (
        "SB Fish Spincer Pincers",108,Regions.SEPTEMBURG_WASTEWATER_CANAL_WELL_ENTRANCE,HasFishingRod(),
    )

    SB_WASTEWATER_CANAL_SLIME_ROOM_CHEST = (
        "SB Wastewater Canal Slime Room Chest",106,Regions.SEPTEMBURG_WASTEWATER_CANAL_SLIME_ROOM,CanBurrow(),
    )

    SB_WASTEWATER_CANAL_BOX_ROOM_CHEST = (
        "SB Wastewater Canal Box Room Chest",105,Regions.SEPTEMBURG_WASTEWATER_CANAL_BOXES,CanBurrow(),
    )

    SB_WASTEWATER_CANAL_WELL_ENTRANCE_CHEST = (
        "SB Wastewater Canal Well Entrance Chest",107,Regions.SEPTEMBURG_WASTEWATER_CANAL_WELL_ENTRANCE,
    )

    SB_SAVE_STUDENTS_TRINKET = (
        "SB Save Students Trinket",334,Regions.OSSEX_TRINKET_BAZAAR,RepairedGenerator(event=SEPTEMBURG_DATA),
    )

class BossLocations(LocationTypeEnum):
    SB_DEFEAT_THE_CARVING_MAN = ("SB Defeat The Carving Man", 1003, Regions.SEPTEMBURG_CARVING_SHACK_ARENA, PowerLevelThreshold(power=25))
    SB_DEFEAT_DARK_DELUXY = ("SB Defeat Dark Deluxy", 1024, Regions.SEPTEMBURG_WINDY_GENERATOR, PowerLevelThreshold(power=40))
    # SB_WINDY_GENERATOR = ("SB Windy Generator Repaired", 6002, Regions.SEPTEMBURG_WINDY_GENERATOR)
