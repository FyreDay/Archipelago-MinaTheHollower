from .events import RepairGenerators
from .. import RepairEventData
from ..items import AreaKears
from ...constants import *

QUEENSBURY_CRYPT_DATA = RepairEventData(RepairGenerators.REPAIR_QUEENSBURY_CRYPT, QUEENSBURY_CRYPT, repair_generator_indexes[QUEENSBURY_CRYPT], AreaKears.QUEENSBURY_KEARS)
NOXS_BAYOU_DATA = RepairEventData(RepairGenerators.REPAIR_NOXS_BAYOU, NOXS_BAYOU, repair_generator_indexes[NOXS_BAYOU], AreaKears.BAYOU_KEARS)
SEPTEMBURG_DATA = RepairEventData(RepairGenerators.REPAIR_SEPTEMBURG, SEPTEMBURG, repair_generator_indexes[SEPTEMBURG], AreaKears.SEPTEMBURG_KEARS)
BONE_BEACH_DATA = RepairEventData(RepairGenerators.REPAIR_BONE_BEACH, BONE_BEACH, repair_generator_indexes[BONE_BEACH], AreaKears.BONE_BEACH_KEARS)
COLTRANE_PEAK_DATA = RepairEventData(RepairGenerators.REPAIR_COLTRANE_PEAK, COLTRANE_PEAK, repair_generator_indexes[COLTRANE_PEAK], AreaKears.COLTRANE_PEAK_KEARS)
ASTRAL_ORRERY_DATA = RepairEventData(RepairGenerators.REPAIR_ASTRAL_ORRERY, ASTRAL_ORRERY, repair_generator_indexes[ASTRAL_ORRERY], AreaKears.ASTRAL_ORRERY_KEARS)
RADIANT_MANOR_DATA = RepairEventData(RepairGenerators.REPAIR_PRIME_GENERATOR, "Randiant Manor", 10, AreaKears.RADIANT_MANOR_KEARS)

repair_generator_data: list[RepairEventData] = [
    QUEENSBURY_CRYPT_DATA,
    NOXS_BAYOU_DATA,
    SEPTEMBURG_DATA,
    BONE_BEACH_DATA,
    COLTRANE_PEAK_DATA,
    ASTRAL_ORRERY_DATA
]

all_generator_data: list[RepairEventData] = [
    QUEENSBURY_CRYPT_DATA,
    NOXS_BAYOU_DATA,
    SEPTEMBURG_DATA,
    BONE_BEACH_DATA,
    COLTRANE_PEAK_DATA,
    ASTRAL_ORRERY_DATA,
    RADIANT_MANOR_DATA
]