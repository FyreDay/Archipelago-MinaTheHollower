from BaseClasses import ItemClassification
from .. import ItemTypeEnum
from ...constants import ITEMS_OFFSET_PROGRESSIVES


class Weapons(ItemTypeEnum):
    NIGHTSTAR = ("Nightstar", ITEMS_OFFSET_PROGRESSIVES, ItemClassification.progression) #2, 3 and 4 are internal game ids
    BLASTSTRIKE_MAUL = ("Blaststrike Maul", ITEMS_OFFSET_PROGRESSIVES+1, ItemClassification.progression) #5, 6 and 7 are internal game ids
    WHISPER_AND_VESPER = ("Whisper and Vesper", ITEMS_OFFSET_PROGRESSIVES+2, ItemClassification.progression) #8, 9, and 10 are internal game ids
    BATTERY_BUSTER = ("Battery Buster", ITEMS_OFFSET_PROGRESSIVES+3, ItemClassification.progression) #11, 12 and 13 are internal game ids
    GUARDIAN_CASKET = ("Guardian Casket", ITEMS_OFFSET_PROGRESSIVES + 4, ItemClassification.progression)  #14, 15 and 16 are internal game ids



class BoneUps(ItemTypeEnum):
    ATTACK_BONE_UP_CAP = ("Progressive Attack Cap", ITEMS_OFFSET_PROGRESSIVES+5, ItemClassification.progression)
    DEFENSE_BONE_UP_CAP = ("Progressive Defense Cap", ITEMS_OFFSET_PROGRESSIVES+6, ItemClassification.progression)
    SIDEARM_BONE_UP_CAP = ("Progressive Sidearm Cap", ITEMS_OFFSET_PROGRESSIVES+7, ItemClassification.progression)

class GenericBoneUp(ItemTypeEnum):
    ALL_BONE_UP_CAP = ("Progressive Bone Up Cap", ITEMS_OFFSET_PROGRESSIVES+8, ItemClassification.progression)

class FishingUpgrades(ItemTypeEnum):
    FISHING_ROD = ("Progressive Fishing Rod", ITEMS_OFFSET_PROGRESSIVES+9, ItemClassification.progression)
    #fishing rod->raft=>gold rod

class Wallets(ItemTypeEnum):
    WALLET_SIZE = ("Progressive Bone Wallet", ITEMS_OFFSET_PROGRESSIVES+11, ItemClassification.progression)
