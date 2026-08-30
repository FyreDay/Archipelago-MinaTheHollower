from BaseClasses import ItemClassification
from .. import ItemTypeEnum
from ...constants import ITEMS_OFFSET_BLOCKERS

class AstralPlatforms(ItemTypeEnum):
    GREEN_ASTRAL_PLATFORMS = ("Green Astral Switch",ITEMS_OFFSET_BLOCKERS, ItemClassification.progression)
    RED_ASTRAL_PLATFORMS = ("Red Astral Switch",ITEMS_OFFSET_BLOCKERS+1, ItemClassification.progression)
    BLUE_ASTRAL_PLATFORMS = ("Blue Astral Switch",ITEMS_OFFSET_BLOCKERS+2, ItemClassification.progression)
    YELLOW_ASTRAL_PLATFORMS = ("Yellow Astral Switch",ITEMS_OFFSET_BLOCKERS+3, ItemClassification.progression)
    PURPLE_ASTRAL_PLATFORMS = ("Purple Astral Switch",ITEMS_OFFSET_BLOCKERS+4, ItemClassification.progression)

# region_gen = {
#         "Astral Orrery": "Starry",
#         "Queensbury Crypt": "Solemn",
#         "Coltrane Peak": "Frozen",
#         "Septemburg": "Windy",
#         "Bone Beach": "Shoreline",
#         "Nox's Bayou": "Swampy"

class GeneratorsComplete(ItemTypeEnum):
    REPAIR_SOLEMN_GENERATOR = ("Repair Solemn Generator", None, ItemClassification.progression)
    REPAIR_SWAMPY_GENERATOR = ("Repair Swampy Generator", None, ItemClassification.progression)
    REPAIR_WINDY_GENERATOR = ("Repair Windy Generator", None, ItemClassification.progression)
    REPAIR_SHORELINE_GENERATOR = ("Repair Shoreline Generator", None, ItemClassification.progression)
    REPAIR_FROZEN_GENERATOR = ("Repair Frozen Generator", None, ItemClassification.progression)
    REPAIR_STARRY_GENERATOR = ("Repair Starry Generator", None, ItemClassification.progression)
    REPAIR_PRIME_GENERATOR = ("Repair Prime Generator", None, ItemClassification.progression)