from rule_builder.rules import Has
from .._generated.regions import Regions

from ... import LocationTypeEnum
from ...items import Weapons, PlayerUpgrades, Sidearms, PermanentUpgrades, BoneUps, GenericBoneUp, Trinkets, \
        SingleKears, Wallets
from ...items.abilities import ABILITY_NAMES
from ...rules.ability_rules import CanBurrow, CanBounce, HasVialsCount, CanClimb, \
        HasReachingSideArm, HasFishingRod, CanCarry, HasBeastiumTransform, HasTrinket, CanSwim, PowerLevelThreshold
from ...rules.state_rules import HasAllKears, HasTrinketCount, HasKear, RepairedGeneratorCount, ShopPrice
from ...rules.movement_rules import CanJumpTiles

class Locations(LocationTypeEnum):
    OS_FOUNTAIN_BALCONY_TRINKET = (
        "OS Fountain Balcony Trinket",162,Regions.OSSEX_HIGH_STREET_RESIDENCE_BALCONY_WEST,
    )

    OS_FISH_TRIPLE_FLAGELLUM = (
        "OS Fish Triple Flagellum",220,Regions.OSSEX_CITY_CENTER_MAIN,HasFishingRod(),
    )

    OS_BLAISE_SECOND_RACE_REWARD = (
        "OS Blaise Second Race Reward",243,Regions.OSSEX_CITY_CENTER_MAIN,CanBurrow(),
    )

    OS_BLAISE_FINAL_RACE_REWARD = (
        "OS Blaise Final Race Reward",322,Regions.OSSEX_CITY_CENTER_MAIN,CanBounce() & CanBurrow() & CanCarry() & CanClimb(),
    )

    OS_ELIZABETH_TRINKET = (
        "OS Elizabeth Trinket",161,Regions.OSSEX_COURTYARD_EAST,ShopPrice(cost=1000)
    )

    OS_COURTYARD_WEAPON_CHEST = (
        "OS Courtyard Weapon Chest",163,Regions.OSSEX_COURTYARD_WEST_CHEST,HasVialsCount(count=5),
    )

    OS_MANORS_GARDEN_TRINKET = (
        "OS Manor's Garden Trinket",171,Regions.OSSEX_COURTYARD_EAST_MANOR_SIDE,
    )

    OS_EVRA_FIGHT_REWARD = (
        "OS Evra Fight Reward",352,Regions.OSSEX_GODDREDS_GRAVE_END,PowerLevelThreshold(power=60),
    )

    OS_COUPLES_QUARTER_CHEST = (
        "OS Couple's Quarter Chest",165,Regions.OSSEX_COUPLES_QUARTER,CanBurrow() | HasReachingSideArm()
    )

    OS_HOLLOWERS_GUILD_BACK_ROOM_KEAR_CHEST = (
        "OS Hollower's Guild Back Room Kear Chest",168,Regions.OSSEX_GUILD_BACK_ROOM,
    )

    OS_HOLLOWERS_GUILD_BACK_ROOM_JOULE_ALEMBIC = (
        "OS Hollower's Guild Back Room Joule Alembic",210,Regions.OSSEX_GUILD_BACK_ROOM,HasKear(kear=SingleKears.SOUTHERN_OUTSKIRTS_ROOFTOP_KEAR.value) & ShopPrice(cost=1000),
    )

    OS_HOLLOWERS_GUILD_BACK_ROOM_ISLE_MAP = (
        "OS Hollower's Guild Back Room Isle Map",211,Regions.OSSEX_GUILD_BACK_ROOM,HasKear(kear=SingleKears.SOUTHERN_OUTSKIRTS_ROOFTOP_KEAR.value) & ShopPrice(cost=500),
    )

    OS_HOLLOWERS_GUILD_BACK_ROOM_SIDEARM_RECOVERER = (
        "OS Hollower's Guild Back Room Sidearm Recoverer",215,Regions.OSSEX_GUILD_BACK_ROOM,HasKear(kear=SingleKears.SOUTHERN_OUTSKIRTS_ROOFTOP_KEAR.value) & ShopPrice(cost=2000),
    )

    OS_HOLLOWERS_GUILD_BACK_ROOM_TRAINING_DUMMY = (
        "OS Hollower's Guild Back Room Training Dummy",218,Regions.OSSEX_GUILD_BACK_ROOM,HasKear(kear=SingleKears.SOUTHERN_OUTSKIRTS_ROOFTOP_KEAR.value) & ShopPrice(cost=500),
    )

    OS_HOLLOWERS_GUILD_BACK_ROOM_SIDEARM_DUPLICATOR = (
        "OS Hollower's Guild Back Room Sidearm Duplicator",214,Regions.OSSEX_GUILD_BACK_ROOM,HasKear(kear=SingleKears.SOUTHERN_OUTSKIRTS_ROOFTOP_KEAR.value)
        & ShopPrice(cost=2000)
        & RepairedGeneratorCount(count=2),
    )

    OS_HOLLOWERS_GUILD_BACK_ROOM_MEMORY_GOGGLES = (
        "OS Hollower's Guild Back Room Memory Goggles",217,Regions.OSSEX_GUILD_BACK_ROOM,HasKear(kear=SingleKears.SOUTHERN_OUTSKIRTS_ROOFTOP_KEAR.value)
        & ShopPrice(cost=2000)
        & RepairedGeneratorCount(count=2),
    )

    OS_HOLLOWERS_GUILD_BACK_ROOM_PHONOGRAPH = (
        "OS Hollower's Guild Back Room Phonograph",216,Regions.OSSEX_GUILD_BACK_ROOM,HasKear(kear=SingleKears.SOUTHERN_OUTSKIRTS_ROOFTOP_KEAR.value)
        & ShopPrice(cost=500)
        & RepairedGeneratorCount(count=2),
    )

    OS_HOLLOWERS_GUILD_BACK_ROOM_ENHANCED_MAP = (
        "OS Hollower's Guild Back Room Enhanced Map",212,Regions.OSSEX_GUILD_BACK_ROOM,HasKear(kear=SingleKears.SOUTHERN_OUTSKIRTS_ROOFTOP_KEAR.value)
        & ShopPrice(cost=500)
        & RepairedGeneratorCount(count=3),
    )

    OS_HOLLOWERS_GUILD_BACK_ROOM_ALL_SEEING_SKULL = (
        "OS Hollower's Guild Back Room All-Seeing Skull",213,Regions.OSSEX_GUILD_BACK_ROOM,HasKear(kear=SingleKears.SOUTHERN_OUTSKIRTS_ROOFTOP_KEAR.value)
        & ShopPrice(cost=4000)
        & RepairedGeneratorCount(count=5),
    )

    OS_HOLLOWERS_GUILD_BACK_ROOM_SMACK_MURIEL = (
        "OS Hollower's Guild Back Room Smack Muriel",146,Regions.OSSEX_GUILD_BACK_ROOM,Has(Weapons.BLASTSTRIKE_MAUL.value, count=3),
    )

    OS_KEAR_INSTITUTE_KEAR_1 = (
        "OS Kear Institute Kear #1",199,Regions.OSSEX_KEAR_INSTITUTE,ShopPrice(cost=300)
    )

    OS_KEAR_INSTITUTE_KEAR_2 = (
        "OS Kear Institute Kear #2",200,Regions.OSSEX_KEAR_INSTITUTE,ShopPrice(cost=500),
    )

    OS_KEAR_INSTITUTE_KEAR_3 = (
        "OS Kear Institute Kear #3",201,Regions.OSSEX_KEAR_INSTITUTE,ShopPrice(cost=750),
    )

    OS_KEAR_INSTITUTE_KEAR_4 = (
        "OS Kear Institute Kear #4",202,Regions.OSSEX_KEAR_INSTITUTE,ShopPrice(cost=875),
    )

    OS_KEAR_INSTITUTE_KEAR_5 = (
        "OS Kear Institute Kear #5",203,Regions.OSSEX_KEAR_INSTITUTE,ShopPrice(cost=1000),
    )

    OS_KEAR_INSTITUTE_KEAR_6 = (
        "OS Kear Institute Kear #6",204,Regions.OSSEX_KEAR_INSTITUTE,ShopPrice(cost=1175),
    )

    OS_KEAR_INSTITUTE_KEAR_7 = (
        "OS Kear Institute Kear #7",205,Regions.OSSEX_KEAR_INSTITUTE,ShopPrice(cost=1250),
    )

    OS_KEAR_INSTITUTE_KEAR_8 = (
        "OS Kear Institute Kear #8",206,Regions.OSSEX_KEAR_INSTITUTE,ShopPrice(cost=1375),
    )

    OS_KEAR_INSTITUTE_KEAR_9 = (
        "OS Kear Institute Kear #9",207,Regions.OSSEX_KEAR_INSTITUTE,ShopPrice(cost=1500),
    )

    OS_KEAR_INSTITUTE_KEAR_COMPLETION = (
        "OS Kear Institute Kear Completion",150,Regions.OSSEX_KEAR_INSTITUTE,HasAllKears(),
    )

    OS_EMPORIUM_HEALTH_ROSE_1 = (
        "OS Emporium Health Rose #1",186,Regions.OSSEX_EMPORIUM,ShopPrice(cost=500),
    )

    OS_EMPORIUM_HEALTH_ROSE_2 = (
        "OS Emporium Health Rose #2",187,Regions.OSSEX_EMPORIUM,ShopPrice(cost=1000),
    )

    OS_EMPORIUM_HEALTH_ROSE_3 = (
        "OS Emporium Health Rose #3",188,Regions.OSSEX_EMPORIUM,ShopPrice(cost=1500),
    )

    OS_EMPORIUM_JOULE_BOX_1 = (
        "OS Emporium Joule Box #1",193,Regions.OSSEX_EMPORIUM,ShopPrice(cost=500),
    )

    OS_EMPORIUM_JOULE_BOX_2 = (
        "OS Emporium Joule Box #2",194,Regions.OSSEX_EMPORIUM,ShopPrice(cost=2000),
    )

    OS_EMPORIUM_JOULE_BOX_3 = (
        "OS Emporium Joule Box #3",195,Regions.OSSEX_EMPORIUM,ShopPrice(cost=4000),
    )

    OS_EMPORIUM_TRINKET_BAG_1 = (
        "OS Emporium Trinket Bag #1",196,Regions.OSSEX_EMPORIUM,ShopPrice(cost=1500),
    )

    OS_EMPORIUM_TRINKET_BAG_2 = (
        "OS Emporium Trinket Bag #2",197,Regions.OSSEX_EMPORIUM,ShopPrice(cost=3000),
    )

    OS_EMPORIUM_TRINKET_BAG_3 = (
        "OS Emporium Trinket Bag #3",198,Regions.OSSEX_EMPORIUM,ShopPrice(cost=5000),
    )

    OS_EMPORIUM_VIAL_POUCH_1 = (
        "OS Emporium Vial Pouch #1",189,Regions.OSSEX_EMPORIUM,ShopPrice(cost=1000),
    )

    OS_EMPORIUM_VIAL_POUCH_2 = (
        "OS Emporium Vial Pouch #2",190,Regions.OSSEX_EMPORIUM,ShopPrice(cost=2500),
    )

    OS_EMPORIUM_VIAL_POUCH_3 = (
        "OS Emporium Vial Pouch #3",191,Regions.OSSEX_EMPORIUM,ShopPrice(cost=3000),
    )

    OS_EMPORIUM_SPARK_CONTAINER = (
        "OS Emporium Spark Container",192,Regions.OSSEX_EMPORIUM,ShopPrice(cost=1500),
    )

    OS_LEGOVICHS_ARMS_WHIP = (
        "OS Legovich's Arms Whip",174,Regions.OSSEX_LEGOVICHS_ARMS,ShopPrice(cost=3000) & CanBurrow(),
    )

    OS_LEGOVICHS_ARMS_HAMMER = (
        "OS Legovich's Arms Hammer",175,Regions.OSSEX_LEGOVICHS_ARMS,ShopPrice(cost=3000) & CanBurrow(),
    )

    OS_LEGOVICHS_ARMS_DAGGERS = (
        "OS Legovich's Arms Daggers",176,Regions.OSSEX_LEGOVICHS_ARMS,ShopPrice(cost=3000) & CanBurrow(),
    )

    OS_LEGOVICHS_ARMS_GUARDIAN_CASKET = (
        "OS Legovich's Arms Guardian Casket",178,Regions.OSSEX_LEGOVICHS_ARMS,ShopPrice(cost=3000) & CanBurrow(),
    )

    OS_LEGOVICHS_ARMS_BATTERY_BUSTER = (
        "OS Legovich's Arms Battery Buster",177,Regions.OSSEX_LEGOVICHS_ARMS,ShopPrice(cost=3000) & CanBurrow(),
    )

    OS_GUTTERWAYS_BONESTONE = (
        "OS Gutterways Bonestone",172,Regions.OSSEX_GUTTERWAYS,Has(Sidearms.IRON_STEED.value),
    )

    OS_FURL_NOSE_TRINKET = (
        "OS Furl Nose Trinket",154,Regions.OSSEX_HIGH_STREET_SE_GARDEN,CanCarry(),
    )

    OS_HIGH_STREET_SEWER_CHEST = (
        "OS High Street Sewer Chest",164,Regions.OSSEX_HIGH_STREET_SEWER,
    )

    OS_STRATEGY_CENTER_CHEST = (
        "OS Strategy Center Chest",167,Regions.OSSEX_STRATEGY_CENTER,HasReachingSideArm() & CanBurrow(),
    )

    OS_STRATEGY_CENTER_OPHIDIO_BONESTONE = (
        "OS Strategy Center Ophidio Bonestone",153,Regions.OSSEX_STRATEGY_CENTER,Has(Weapons.WHISPER_AND_VESPER.value, count=2) & CanBurrow(),
    )

    OS_OSSEX_TELESCOPE_METEOR = (
        "OS Ossex Telescope Meteor",155,Regions.OSSEX_BALCONY_EAST,
    )

    OS_ATTIC_CHEST = (
        "OS Attic Chest",166,Regions.OSSEX_HIGH_STREET_RESIDENCE_UPPER_PUZZLE,
    )

    OS_ATELIER_CHEST = (
        "OS Atelier Chest",169,Regions.OSSEX_ATELIER,CanJumpTiles(distance=3, has_wall=True) & CanBurrow(),
    )

    OS_ATELIER_VITALITY_VEST = (
        "OS Atelier Vitality Vest",208,Regions.OSSEX_ATELIER,ShopPrice(cost=3000),
    )

    OS_ATELIER_CUSTOM_FIT = (
        "OS Atelier Custom Fit",209,Regions.OSSEX_ATELIER,Has(PermanentUpgrades.VITALITY_VEST.value)
        & Has(PermanentUpgrades.SAFETY_SHROUD.value)
        & ShopPrice(cost=2000),
    )

    OS_BOWERY_BRANDISH_DUAL_SIDEARM_PERMIT = (
        "OS Bowery Brandish Dual Sidearm Permit",219,Regions.OSSEX_BOWERY_MAIN,Has(BoneUps.SIDEARM_BONE_UP_CAP.value, count=4)
        | Has(GenericBoneUp.ALL_BONE_UP_CAP.value, count=4),
    )

    OS_BOWERY_UPPER_CHEST = (
        "OS Bowery Upper Chest",173,Regions.OSSEX_BOWERY_UPPER,CanBurrow()
        & (
            HasReachingSideArm()
            | HasTrinket(trinket=Trinkets.SEISMIC_BELT.value)
            | HasBeastiumTransform()
        ),
    )

    OS_LINDY_THE_GIRAFFE_BONESTONE = (
        "OS Lindy The Giraffe Bonestone",159,Regions.OSSEX_BOWERY_TALL_RESIDENCE_UPPER_MAIN,CanBurrow(),
    )

    OS_GIFT_HOMELESS_REWARD = (
        "OS Gift Homeless Reward",156,Regions.OSSEX_BOWERY_BEGGER_RESIDENCE,
    )

    OS_MUSIC_HALL_CHEST = (
        "OS Music Hall Chest",170,Regions.OSSEX_MUSIC_HALL,
    )

    OS_MUSIC_HALL_WONDER_WILLIS_TRINKET = (
        "OS Music Hall Wonder Willis Trinket",148,Regions.OSSEX_MUSIC_HALL,CanCarry() & CanBurrow() & CanSwim() & CanClimb(),PowerLevelThreshold(power=30),
    )

    OS_STATION_UNDERSIDE_FRAYD_TRINKET = (
        "OS Station Underside Frayd Trinket",158,Regions.OSSEX_STATION_UNDERSIDE_MAIN,ShopPrice(cost=1000),
    )

    OS_TRINKET_BAZAAR_KEAR = (
        "OS Trinket Bazaar Kear",160,Regions.OSSEX_TRINKET_BAZAAR,CanBurrow(),
    )

    OS_TRINKET_BAZAAR_PLASMA_FUNNEL = (
        "OS Trinket Bazaar Plasma Funnel",179,Regions.OSSEX_TRINKET_BAZAAR,ShopPrice(cost=700),
    )

    OS_TRINKET_BAZAAR_SEISMIC_BELT = (
        "OS Trinket Bazaar Seismic Belt",180,Regions.OSSEX_TRINKET_BAZAAR,ShopPrice(cost=700),
    )

    OS_TRINKET_BAZAAR_BRISK_BREW = (
        "OS Trinket Bazaar Brisk Brew",181,Regions.OSSEX_TRINKET_BAZAAR,ShopPrice(cost=700),
    )

    OS_TRINKET_BAZAAR_INTREVENOUS_VIAL = (
        "OS Trinket Bazaar Intrevenous Vial",182,Regions.OSSEX_TRINKET_BAZAAR,ShopPrice(cost=1250) & HasTrinketCount(count=5),
    )

    OS_TRINKET_BAZAAR_SHOCK_FLINT = (
        "OS Trinket Bazaar Shock Flint",183,Regions.OSSEX_TRINKET_BAZAAR,ShopPrice(cost=1250) & HasTrinketCount(count=5),
    )

    OS_TRINKET_BAZAAR_URANIUM_BRACELET = (
        "OS Trinket Bazaar Uranium Bracelet",25,Regions.OSSEX_TRINKET_BAZAAR,HasTrinketCount(count=10) & ShopPrice(cost=2000),
    )

    OS_TRINKET_BAZAAR_BUBBLE_RING = (
        "OS Trinket Bazaar Bubble Ring",184,Regions.OSSEX_TRINKET_BAZAAR,HasTrinketCount(count=10) & ShopPrice(cost=1500),
    )

    OS_TRINKET_BAZAAR_COUNTER_VIAL = (
        "OS Trinket Bazaar Counter Vial",185,Regions.OSSEX_TRINKET_BAZAAR,HasTrinketCount(count=20) & ShopPrice(cost=1500),
    )

    OS_TRAIN_CHEST = (
        "OS Train Chest",360,Regions.OSSEX_TRAIN_PRIVATE_CABIN_LEFT,CanBurrow() & HasKear(kear=SingleKears.OSSEX_TRAIN_KEAR_1.value),
    )

    OS_TRAIN_SAFETY_SHROUD = (
        "OS Train Safety Shroud",357,Regions.OSSEX_TRAIN_PRIVATE_CABIN_LEFT,CanBurrow()
        & HasKear(kear=SingleKears.OSSEX_TRAIN_KEAR_1.value)
        & HasKear(kear=SingleKears.OSSEX_TRAIN_KEAR_2.value),
    )
# "OS Station Train Ticket Donation": LocationData(149, "Ossex Station", progress_type=LocationProgressType.EXCLUDED),
# "OS Forgotten Cave Disturbing Dance": LocationData(351, "Ossex City Center Main", CanBurrow() & CanBounce() & CanClimb()),
class BossLocations(LocationTypeEnum):
    OS_DEFEAT_ARMOND = ("OS Defeat Armond", 1021, Regions.OSSEX_LEGOVICHS_ARMS_BASEMENT,CanBurrow() & PowerLevelThreshold(power=20))
    OS_DEFEAT_EVRA = ("OS Defeat Evra", 1022, Regions.OSSEX_GODDREDS_GRAVE_ARENA,PowerLevelThreshold(power=60))
    OS_DEFEAT_WILLY = ("OS Defeat Willy", 1020, Regions.OSSEX_MUSIC_HALL, CanCarry() & CanBurrow() & CanSwim() & CanClimb(),PowerLevelThreshold(power=30))