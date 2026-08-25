from rule_builder.rules import True_, Has
from .abilities import Abilities
from .blockers import AstralPlatforms
from .game_items import Sidearms, PermanentUpgrades, PlayerUpgrades, Trinkets, BoneFiller, JunkFiller, CosmeticUpgrades, \
    FilledJug, FillerUpgrades
from .kears import Kear, AreaKears, SingleKears
from .progressives import Weapons, BoneUps, GenericBoneUp, FishingUpgrades, Wallets
from .. import ItemData, ItemTypeEnum, ItemFiller, ItemMovement, ItemPower

all_items: list[ItemTypeEnum] = [
    *Abilities,
    *AstralPlatforms,
    *Sidearms,
    *PermanentUpgrades,
    *PlayerUpgrades,
    *Trinkets,
    *BoneFiller,
    *JunkFiller,
    *Kear,
    *AreaKears,
    *SingleKears,
    *Weapons,
    *BoneUps,
    *GenericBoneUp,
    *FishingUpgrades,
    *CosmeticUpgrades,
    *FillerUpgrades,
    *FilledJug,
    *Wallets
]

item_name_to_type = {
    item.value: item
    for item in all_items
}

all_filler_items: list[ItemFiller] = [
    # ItemFiller(BoneFiller.BONE_DUST, 64),
    # ItemFiller(BoneFiller.BONE_STONE, 32),
    ItemFiller(BoneFiller.BONE_STONE_1, 4),
    ItemFiller(BoneFiller.BONE_STONE_2, 8),
    ItemFiller(BoneFiller.BONE_STONE_3, 16),
    ItemFiller(BoneFiller.BONE_STONE_4, 12),
    ItemFiller(BoneFiller.BONE_STONE_5, 10),
    ItemFiller(BoneFiller.BONE_STONE_6, 8),
    ItemFiller(BoneFiller.BONE_STONE_7, 6),
    ItemFiller(BoneFiller.BONE_STONE_8, 4),
    ItemFiller(BoneFiller.BONE_STONE_9, 2),
    ItemFiller(BoneFiller.BONE_STONE_10, 2),

    # ItemFiller(BoneFiller.TREASURE_BOSS, 4),
    # ItemFiller(BoneFiller.TREASURE_GOLD_LARGEST, 8),
    # ItemFiller(BoneFiller.TREASURE_JEWEL_LARGE, 8),
    # ItemFiller(BoneFiller.TREASURE_JEWEL_LARGEST, 4),
    # ItemFiller(JunkFiller.HEALING_VIAL_PICKUP, 4),
    # ItemFiller(JunkFiller.HEALING_VIAL_PACK_PICKUP, 2),
    # ItemFiller(JunkFiller.RED_FLOWER, 10),
    # ItemFiller(JunkFiller.YELLOW_FLOWER, 4),
    # ItemFiller(JunkFiller.MAGIC_LARGE, 4),
    # ItemFiller(JunkFiller.MAGIC_MEDIUM, 8),
    # ItemFiller(JunkFiller.MAGIC_SMALL, 16),
]

BASE_ITEM_TOTAL = 15

base_items: list[ItemData] = [
    ItemData(PlayerUpgrades.HEALTH_ROSE, 8),
    ItemData(PlayerUpgrades.TRINKET_BAG, 1),
    ItemData(PlayerUpgrades.JOULE_BOX,2),
    ItemData(PlayerUpgrades.HEALING_VIAL, 3),
    ItemData(PlayerUpgrades.SPARK_CONTAINER, 1),
    # ItemData(Weapons.NIGHTSTAR, 1),
    # ItemData(PlayerUpgrades.HEALING_VIAL_POUCH, 1), NEED TO STOP THE GIVING OF
]

upgrade_items: list[ItemData] = [
    ItemData(PlayerUpgrades.HEALTH_ROSE, 10),
    ItemData(PlayerUpgrades.TRINKET_BAG, 5),
    ItemData(PlayerUpgrades.JOULE_BOX, 8),
    ItemData(PlayerUpgrades.HEALING_VIAL, 7),
    ItemData(PlayerUpgrades.SPARK_CONTAINER, 3),
    ItemData(FishingUpgrades.FISHING_ROD, 3),
    # ItemData(MapUpgrades.PROGRESSIVE_MAP, 2)
]

movement_sidearms: list[ItemTypeEnum] = [
    Sidearms.DEFLECTOR_PARASOL,
    Sidearms.DRIVER_DRILL,
    Sidearms.IRON_STEED,
    Sidearms.MIST_JAR,
]

movement_trinkets: list[ItemTypeEnum] = [
    Trinkets.SPRING_HEELS,
    Trinkets.BRIDGE_WEAVER,
    Trinkets.KERI_THE_WISP,
    Trinkets.PIT_PRESERVER,
    Trinkets.BELLOWS_BUSTLE,
    Trinkets.BRISK_BREW,
    Trinkets.WALLOWERS_GAUNTLETS,
    Trinkets.DUMMY_CACHE,
    Trinkets.TUNNELING_CODEX
]
#Raft?
all_movement_items: list[ItemTypeEnum] = [
    Abilities.BURROW,
    Abilities.SWIM,
    Weapons.GUARDIAN_CASKET,
    PlayerUpgrades.JOULE_BOX,
    PlayerUpgrades.TRINKET_BAG,
    *movement_trinkets,
    *movement_sidearms
]



item_powers_dependencies: list[ItemPower] = [
    ItemPower(PlayerUpgrades.TRINKET_BAG, 0),
]


trinket_powers: list[ItemPower] = [
    ItemPower(Trinkets.LACE_GLOVE, 1),
    ItemPower(Trinkets.INTRAVENOUS_VIAL, 1, PlayerUpgrades.HEALING_VIAL),
    ItemPower(Trinkets.URANIUM_BRACELET, 2),
    ItemPower(Trinkets.BUBBLE_RING, 4),
    ItemPower(Trinkets.COUNTER_VIAL, 2),
    ItemPower(Trinkets.VALOR_MEDALION, 4, PlayerUpgrades.HEALING_VIAL),
    ItemPower(Trinkets.SMELLING_SALTS, 1),
    ItemPower(Trinkets.WILLOW_THE_WISP, 2),
    ItemPower(Trinkets.HELIO_THE_WISP, 3),
    ItemPower(Trinkets.CHAIN_CAPACITOR, 2),
    ItemPower(Trinkets.PROTO_SPARK, 8),
    ItemPower(Trinkets.PRIMED_VIAL_POUCH, 6, PlayerUpgrades.HEALING_VIAL),
    ItemPower(Trinkets.NITER_BELT, 1),
    ItemPower(Trinkets.JOULE_SYRINGE, 2),
    ItemPower(Trinkets.TUNNELING_CODEX, 1),
    ItemPower(Trinkets.EVASION_POWDER, 2),
    ItemPower(FilledJug.PLASMA_JUG, 2, PlayerUpgrades.HEALING_VIAL),
    ItemPower(Trinkets.VASCULAR_SYRUP, 1),
    ItemPower(Trinkets.TWILL_WEAVE, 1),
    ItemPower(Trinkets.PNEUMATIC_ARMLET, 2),
    ItemPower(Trinkets.BLINKING_GLASS, 2),
    ItemPower(Trinkets.DODGING_PENDULUM, 4),
    ItemPower(Trinkets.RECKLESS_BEASTIUM, 2),
    ItemPower(Trinkets.VIAL_SALVO, 2, PlayerUpgrades.HEALING_VIAL),
    ItemPower(Trinkets.WARDING_BEASTIUM, 2),
]

upgrade_powers: list[ItemPower] = [
    ItemPower(PlayerUpgrades.HEALTH_ROSE, 2),
    ItemPower(PlayerUpgrades.JOULE_BOX, 1),
    ItemPower(PlayerUpgrades.HEALING_VIAL, 1),
    ItemPower(BoneUps.ATTACK_BONE_UP_CAP, 1),
    ItemPower(BoneUps.DEFENSE_BONE_UP_CAP, 1),
    ItemPower(BoneUps.SIDEARM_BONE_UP_CAP, 1),
    ItemPower(GenericBoneUp.ALL_BONE_UP_CAP, 3),
    ItemPower(PermanentUpgrades.SAFETY_SHROUD, 3),
    ItemPower(PermanentUpgrades.VITALITY_VEST, 3),
]

all_power_items: list[ItemPower] = [
    *upgrade_powers,
    *trinket_powers,
    *item_powers_dependencies
]

all_starting_upgrades: list[ItemData] = [
    ItemData(FillerUpgrades.PROGRESSIVE_MAP, 2),
    ItemData(FillerUpgrades.RADAR_MAP, 1),
    ItemData(FillerUpgrades.TRAINING_DUMMY, 1),
    ItemData(FillerUpgrades.CANDLE_VISION, 1),
]

valid_power_types = {
    power.type
    for power in trinket_powers + upgrade_powers
}