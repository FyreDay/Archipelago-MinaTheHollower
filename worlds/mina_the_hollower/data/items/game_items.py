from BaseClasses import ItemClassification
from .. import ItemTypeEnum
from ...constants import ITEMS_OFFSET_PROGRESSIVES


class Sidearms(ItemTypeEnum):
    HOLLOWERS_ROCKS = ("Hollowers Rocks", 28, ItemClassification.progression)
    GYRO_DAGGER = ("Gyro Dagger", 22, ItemClassification.progression)
    VOLT_HATCHET = ("Volt Hatchet", 21, ItemClassification.progression)

    FOG_THROWER = ("Fog Thrower", 29, ItemClassification.progression)  # burrow
    DEFLECTOR_PARASOL = ("Deflector Parasol", 33, ItemClassification.progression)  # burrow
    MIST_JAR = ("Mist Jar", 31, ItemClassification.progression)  # burrow
    DRIVER_DRILL = ("Driver Drill", 25, ItemClassification.progression)  # burrow

    RECALL_DISC = ("Recall Disc", 23, ItemClassification.progression)
    DYNAMO_LANTURN = ("Dynamo Lanturn", 24, ItemClassification.progression)

    BOUNDING_BOMBS = ("Bounding Bombs", 26, ItemClassification.progression)
    IRON_STEED = ("Iron Steed", 27, ItemClassification.progression)  # 2 sparks or train ticket and septemburg ticket

    BECKONING_COLLAR = ("Beckoning Collar", 30, ItemClassification.progression)

    GNAWING_GHOSTS = ("Gnawing Ghosts", 32, ItemClassification.progression)

    FISHING_ROD = ("Fishing Rod",34, ItemClassification.progression) #103 is gold
    # ANGLERS_RAFT = ("Angler's Raft", 102, ItemClassification.progression)
    # "FishingGoldPickup": ItemData(103, ItemClassification.progression),



class PermanentUpgrades(ItemTypeEnum):
    # HEALING_VIAL_POUCH = ("Healing Vial Pouch", 18, ItemClassification.progression)
    # CANDLE_VISION = ("Memory Goggles", 74, ItemClassification.useful)
    # WORLD_MAP = ("World Map", 75, ItemClassification.useful)
    # ENHANCED_MAP = ("Enhanced Map", 76, ItemClassification.useful)
    # RADAR_MAP = ("All-Seeing Skull", 77, ItemClassification.useful)
    DOUBLE_SIDEARM_PERMIT = ("Dual Sidearm Permit", 78, ItemClassification.progression)
    VITALITY_VEST = ("Vitality Vest", 79, ItemClassification.progression)
    SAFETY_SHROUD = ("Safety Shroud", 80, ItemClassification.progression)
    ARMOR_CUSTOM = ("Custom Fitting", 81, ItemClassification.filler)
    # "ArmorDefault" : ItemData(92, ItemClassification.progression),
    # "ArmorUpgradeAll" : ItemData(93, ItemClassification.progression),
    JOULE_ALMEMBIC = ("Joule Alembic", 82, ItemClassification.progression)
    SIDEARM_SAVER = ("Sidearm Recoverer", 83, ItemClassification.progression)
    SIDEARM_KEEPER = ("Sidearm Duplicator", 84, ItemClassification.progression)
    PHONOGRAPH = ("Phonograph", 86, ItemClassification.filler)
    TRAIN_PASS = ("Train Pass",94, ItemClassification.progression)
    # OSSEX_TICKET = ("Ossex Ticket", 95, ItemClassification.progression)
    BAYOU_TICKET = ("Bayou Ticket",96, ItemClassification.progression)
    SEPTEMBURG_TICKET = ("Septemburg Ticket",97, ItemClassification.progression)
    BONE_BEACH_TICKET = ("Bone Beach Ticket",98, ItemClassification.progression)
    COLTRANE_PEAK_TICKET = ("Coltrane Peak Ticket",99, ItemClassification.progression)

class FillerUpgrades(ItemTypeEnum):
    TRAINING_DUMMY = ("Training Dummy", 85, ItemClassification.useful)
    PROGRESSIVE_MAP = ("Progressive World Map", ITEMS_OFFSET_PROGRESSIVES + 10, ItemClassification.useful)
    RADAR_MAP = ("All-Seeing Skull", 77, ItemClassification.useful)
    CANDLE_VISION = ("Memory Goggles", 74, ItemClassification.useful)

class CosmeticUpgrades(ItemTypeEnum):
    UNDERLAB_DEFAULT =("Underlab Default" ,120, ItemClassification.filler)
    UNDERLAB_CRYPT = ("Underlab Crypt", 121, ItemClassification.filler)
    UNDERLAB_BAYOU = ("Underlab Bayou", 122, ItemClassification.filler)
    UNDERLAB_SEPTEMBURG = ("Underlab Septemburg", 123, ItemClassification.filler)
    UNDERLAB_TRAINYARD = ("Underlab Trainyard", 124, ItemClassification.filler)
    UNDERLAB_BONE_BEACH = ("Underlab BoneBeach", 125, ItemClassification.filler)
    UNDERLAB_ASTRAL = ("Underlab Astral", 126, ItemClassification.filler)
    UNDERLAB_MANSION = ("Underlab Mansion", 127, ItemClassification.filler)
    UNDERLAB_HUB = ("Underlab HUB", 128, ItemClassification.filler)
    UNDERLAB_EAST = ("Underlab East", 129, ItemClassification.filler)
    UNDERLAB_WEST = ("Underlab West", 130, ItemClassification.filler)
    UNDERLAB_SOUTH = ("Underlab South", 131, ItemClassification.filler)
    UNDERLAB_SEWER = ("Underlab Sewer", 132, ItemClassification.filler)
    UNDERLAB_GUILD = ("Underlab Guild", 133, ItemClassification.filler)
    WIERD_DANCE = ("Weird Dance", 90, ItemClassification.useful)

 # "Lock" : ItemData(64, ItemClassification.progression),
    # "EarlyBuy" : ItemData(65, ItemClassification.progression),
    # "Note" : ItemData(66, ItemClassification.progression),
    # "Trinket" : ItemData(67, ItemClassification.progression),

# "Upgrade_FishingRod" : ItemData(87, ItemClassification.progression),
    # "FishingUpgrade1" : ItemData(88, ItemClassification.progression),
    # "FishingRodGold" : ItemData(89, ItemClassification.progression),

    # "TwoSidearmHUD" : ItemData(91, ItemClassification.progression),


    # "ExitTicket" : ItemData(100, ItemClassification.progression),
    # "UnavailableTicket" : ItemData(101, ItemClassification.progression),

    # "FishGhost" : ItemData(104, ItemClassification.progression),
    # "FishPuffer" : ItemData(105, ItemClassification.progression),
    # "FishFlag" : ItemData(106, ItemClassification.progression),
    # "FishCrumble" : ItemData(107, ItemClassification.progression),
    # "FishSpincer" : ItemData(108, ItemClassification.progression),
    # "FishIce" : ItemData(109, ItemClassification.progression),
    # "FishTrigger" : ItemData(110, ItemClassification.progression),
    # "FishGlomp" : ItemData(111, ItemClassification.progression),
    # "FishGoremaw" : ItemData(112, ItemClassification.progression),
    # "FishDork" : ItemData(113, ItemClassification.progression),
    # "FishEel" : ItemData(114, ItemClassification.progression),
    # "FishGazeworm" : ItemData(115, ItemClassification.progression),
    # "FishCuddlepus" : ItemData(116, ItemClassification.progression),
    # "FishTrunkstar" : ItemData(117, ItemClassification.progression),
    # "FishShrimpster" : ItemData(118, ItemClassification.progression),
    # "FishBoss" : ItemData(119, ItemClassification.progression),

class PlayerUpgrades(ItemTypeEnum):
    JOULE_BOX = ("Joule Box",68, ItemClassification.progression) #magic_upgrade
    HEALTH_ROSE = ("Health Rose",69, ItemClassification.progression) #health_upgrade
    SPARK_CONTAINER = ("Spark Container",70, ItemClassification.progression) #spark_upgrade
    HEALING_VIAL = ("Healing Vial",71, ItemClassification.progression) #vial_upgrade
    TRINKET_BAG = ("Trinket Bag",72, ItemClassification.progression) #trinket_upgrade

class Trinkets(ItemTypeEnum):
    LACE_GLOVE = ("Lace Glove", 134, ItemClassification.progression)
    TWILL_WEAVE = ("Twill Weave", 135, ItemClassification.progression)
    SMELLING_SALTS = ("Smelling Salts", 136, ItemClassification.progression)
    BRISK_BREW = ("Brisk Brew", 137, ItemClassification.progression)
    SEISMIC_BELT = ("Seismic Belt", 138, ItemClassification.progression)
    PLASMA_FUNNEL = ("Plasma Funnel", 139, ItemClassification.progression)
    DEBONING_WAND = ("Deboning Wand", 140, ItemClassification.progression)
    STEADY_SOLES = ("Steady Soles", 141, ItemClassification.progression)
    VALOR_MEDALION = ("Valor Medallion", 142, ItemClassification.progression)
    BELL_OF_GRACE = ("Bell Of Grace", 143, ItemClassification.progression)
    WILLOW_THE_WISP = ("Willow The Wisp", 144, ItemClassification.progression)
    HELIO_THE_WISP = ("Helio The Wisp", 145, ItemClassification.progression)
    KERI_THE_WISP = ("Keri The Wisp", 146, ItemClassification.progression)
    WINDFALL_CHARM = ("Windfall Charm", 147, ItemClassification.progression)
    CHAIN_CAPACITOR = ("Chain Capacitor", 148, ItemClassification.progression)
    SPIKE_SPURS = ("Spike Spurs", 149, ItemClassification.progression)
    DESPERATION_BONNET = ("Desperation Bonnet", 150, ItemClassification.progression)
    STOLENOID = ("Stolenoid", 151, ItemClassification.progression)
    FLY_BAIT = ("Fly Bait", 152, ItemClassification.progression)
    PROTO_SPARK = ("Proto Spark", 153, ItemClassification.progression)
    PRIMED_VIAL_POUCH = ("Primed Vial Pouch", 154, ItemClassification.progression)
    FLAME_GUARD = ("Flame Guard", 155, ItemClassification.progression)
    SPARK_CATCHER = ("Spark Catcher", 156, ItemClassification.progression)
    EVASION_POWDER = ("Evasion Powder", 157, ItemClassification.progression)
    VASCULAR_SYRUP = ("Vascular Syrup", 158, ItemClassification.progression)
    PIT_PRESERVER = ("Pit Preserver", 159, ItemClassification.progression)
    IRON_LUNG = ("Iron Lung", 160, ItemClassification.progression)
    TUMBLING_TUTU = ("Tumbling Tutu", 161, ItemClassification.progression)
    EMPTY_JUG = ("Empty Plasma Jug", 162, ItemClassification.progression)
    URANIUM_BRACELET = ("Uranium Bracelet", 163, ItemClassification.progression)
    BUBBLE_RING = ("Bubble Ring", 164, ItemClassification.progression)
    SHOCK_FLINT = ("Shock Flint", 165, ItemClassification.progression)
    INTRAVENOUS_VIAL = ("Intravenous Vial", 166, ItemClassification.progression)
    PNEUMATIC_ARMLET = ("Pneumatic Armlet", 167, ItemClassification.progression)
    STARVING_BEASTIUM = ("Starving Beastium", 168, ItemClassification.progression)
    DRAINING_BEASTIUM = ("Draining Beastium", 169, ItemClassification.progression)
    RECKLESS_BEASTIUM = ("Reckless Beastium", 170, ItemClassification.progression)
    VOLATILE_BEASTIUM = ("Volatile Beastium", 171, ItemClassification.progression)
    BURNING_BEASTIUM = ("Burning Beastium", 172, ItemClassification.progression)
    WARDING_BEASTIUM = ("Warding Beastium", 173, ItemClassification.progression)
    DUMMY_CACHE = ("Dummy Cache", 174, ItemClassification.progression)
    BLINKING_GLASS = ("Blinking Glass", 175, ItemClassification.progression)
    WATCHFUL_EYE = ("Watchful Eye", 176, ItemClassification.progression)
    BRIDGE_WEAVER = ("Bridge Weaver", 177, ItemClassification.progression)
    VIAL_SALVO = ("Vial Salvo", 178, ItemClassification.progression)
    DODGING_PENDULUM = ("Dodging Pendulum", 179, ItemClassification.progression)
    SPRING_HEELS = ("Spring Heels", 180, ItemClassification.progression)
    WALLOWERS_GAUNTLETS = ("Wallowers Gauntlets", 181, ItemClassification.progression)
    OOZING_ORGAN = ("Oozing Organ", 182, ItemClassification.progression)
    VOLTAIC_GUARD = ("Voltaic Guard", 183, ItemClassification.progression)
    REPULSING_ROOT = ("Repulsing Root", 184, ItemClassification.progression)
    LIGHTNING_GRIP = ("Lightning Grip", 185, ItemClassification.progression)
    DEAD_LEAF = ("Dead Leaf", 186, ItemClassification.progression)
    NITER_BELT = ("Niter Belt", 187, ItemClassification.progression)
    BELLOWS_BUSTLE = ("Bellows Bustle", 188, ItemClassification.progression)
    TUNNELING_CODEX = ("Tunneling Codex", 189, ItemClassification.progression)
    JOULE_SYRINGE = ("Joule Syringe", 190, ItemClassification.progression)
    POLYP_LAMP = ("Polyp Lamp", 191, ItemClassification.progression)
    THERMAL_PACK = ("Thermal Pack", 192, ItemClassification.progression)
    COUNTER_VIAL = ("Counter Vial", 193, ItemClassification.progression)

class FilledJug(ItemTypeEnum):
    PLASMA_JUG = ("Plasma Jug", 194, ItemClassification.progression)


class BoneFiller(ItemTypeEnum):
    # BONE_DUST = ("BoneDust",50, ItemClassification.filler)
    # BONE_STONE = ("Bonestone",51, ItemClassification.filler)
    BONE_STONE_1 = ("100 Bonestone", 52, ItemClassification.filler) #100
    BONE_STONE_2 = ("200 Bonestone",53, ItemClassification.filler) #200
    BONE_STONE_3 = ("500 Bonestone",54, ItemClassification.filler) #500
    BONE_STONE_4 = ("800 Bonestone",55, ItemClassification.filler) #800
    BONE_STONE_5 = ("1000 Bonestone",56, ItemClassification.filler) #1000
    BONE_STONE_6 = ("2000 Bonestone",57, ItemClassification.filler) #2000
    BONE_STONE_7 = ("3000 Bonestone",58, ItemClassification.filler) #3000
    BONE_STONE_8 = ("4000 Bonestone",59, ItemClassification.filler) #4000
    BONE_STONE_9 = ("5000 Bonestone",60, ItemClassification.filler) #5000
    BONE_STONE_10 = ("6000 Bonestone",61, ItemClassification.filler) #6000
    TREASURE_SMALLEST = ("TreasureSmallest (1)", 40, ItemClassification.filler) #1
    TREASURE_SMALL = ("TreasureSmall (5)", 41, ItemClassification.filler) #5
    TREASURE_MEDIUM = ("TreasureMedium (20)", 42, ItemClassification.filler) #20
    TREASURE_LARGE = ("TreasureLarge (50)", 43, ItemClassification.filler) #50
    TREASURE_LARGEST = ("TreasureLargest (100)", 44, ItemClassification.filler) #100
    TREASURE_BOSS = ("TreasureBoss (200)", 45, ItemClassification.filler) #200
    TREASURE_GOLD_LARGE = ("TreasureGoldLarge (200)", 46, ItemClassification.filler) #200
    TREASURE_GOLD_LARGEST = ("TreasureGoldLargest (500)", 47, ItemClassification.filler) #500
    TREASURE_JEWEL_LARGE = ("TreasureJewelLarge (1000)", 48, ItemClassification.filler) #1000
    TREASURE_JEWEL_LARGEST = ("TreasureJewelLargest (2000)", 49, ItemClassification.filler) #2000
    # "BonestoneTower" : ItemData(62, ItemClassification.progression),

class JunkFiller(ItemTypeEnum):
    # "HealingVial" : 17
    SPARK = ("Spark",73, ItemClassification.filler)
    HEALING_VIAL_PICKUP = ("Healing Vial Pickup",19, ItemClassification.filler)
    # HEALING_VIAL_PACK_PICKUP = ("HealingVialPackPickup",20, ItemClassification.filler)
    YELLOW_FLOWER = ("Yellow Flower Heal",35, ItemClassification.filler)
    RED_FLOWER = ("Red Flower Heal",36, ItemClassification.filler)
    MAGIC_SMALL = ("MagicSmall",37, ItemClassification.filler)
    MAGIC_MEDIUM = ("MagicMedium", 38, ItemClassification.filler)
    MAGIC_LARGE = ("MagicLarge", 39, ItemClassification.filler)
