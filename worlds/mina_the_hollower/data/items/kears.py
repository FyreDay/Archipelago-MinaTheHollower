from BaseClasses import ItemClassification
from .. import ItemTypeEnum
from ...constants import ITEMS_OFFSET_KEARS

class Kear(ItemTypeEnum):
    UNIVERSAL_KEAR = ("Kear", 63, ItemClassification.progression)

class AreaKears(ItemTypeEnum):
    ASTRAL_ORRERY_KEARS = ("Astral Orrery Locks", ITEMS_OFFSET_KEARS + 500, ItemClassification.progression)
    BACKWATER_KEARS = ("Backwater Locks", ITEMS_OFFSET_KEARS + 501, ItemClassification.progression)
    BAYOU_KEARS = ("Bayou Locks", ITEMS_OFFSET_KEARS + 502, ItemClassification.progression)
    BONE_BEACH_KEARS = ("Bone Beach Locks", ITEMS_OFFSET_KEARS + 503, ItemClassification.progression)
    COLTRANE_PEAK_KEARS = ("Coltrane Peak Locks", ITEMS_OFFSET_KEARS + 504, ItemClassification.progression)
    EASTERN_HEATH_KEARS = ("Eastern Heath Locks", ITEMS_OFFSET_KEARS + 505, ItemClassification.progression)
    KINDLEWOOD_KEARS = ("Kindle Wood Locks", ITEMS_OFFSET_KEARS + 506, ItemClassification.progression)
    LONERS_LANDING_KEARS = ("Loner's Landing Locks", ITEMS_OFFSET_KEARS + 507, ItemClassification.progression)
    MOURNERS_MILE_KEARS = ("Mourner's Mile Locks", ITEMS_OFFSET_KEARS + 508, ItemClassification.progression)
    OSSEX_KEARS = ("Ossex Locks", ITEMS_OFFSET_KEARS + 509, ItemClassification.progression)
    TRAIN_KEARS = ("Train Locks", ITEMS_OFFSET_KEARS + 510, ItemClassification.progression)
    QUEENSBURY_KEARS = ("Queensbury Locks", ITEMS_OFFSET_KEARS + 511, ItemClassification.progression)
    RADIANT_MANOR_KEARS = ("Radiant Manor Locks", ITEMS_OFFSET_KEARS + 512, ItemClassification.progression)
    SANDFALLS_KEARS = ("Sandfalls Locks", ITEMS_OFFSET_KEARS + 513, ItemClassification.progression)
    SEPTEMBURG_KEARS = ("Septemburg Locks", ITEMS_OFFSET_KEARS + 514, ItemClassification.progression)
    SOUTHERN_OUTSKIRTS_KEARS = ("Southern Outskirts Locks", ITEMS_OFFSET_KEARS + 515, ItemClassification.progression)
    WESTERN_WILDS_KEARS = ("Western Wilds Locks", ITEMS_OFFSET_KEARS + 516, ItemClassification.progression)

class SingleKears(ItemTypeEnum):
    OSSEX_HIGHSTREET_BALCONY_KEAR = ("Ossex High Street Balcony Lock", ITEMS_OFFSET_KEARS + 151, ItemClassification.progression)
    OSSEX_HIGH_STREET_SE_GARDEN_KEAR = ("Ossex High Street SE Garden Lock", ITEMS_OFFSET_KEARS + 152, ItemClassification.progression)
    SOUTHERN_OUTSKIRTS_ROOFTOP_KEAR = ("Southern Outskirts Rooftop Lock", ITEMS_OFFSET_KEARS + 260, ItemClassification.progression)
    SOUTHERN_OUTSKIRTS_CAVE_NETWORK_KEAR = ( "Southern Outskirts Cave Network Lock", ITEMS_OFFSET_KEARS + 262, ItemClassification.progression)
    WESTERN_WILDS_BALCONY_KEAR = ("Western Wilds Balcony Lock", ITEMS_OFFSET_KEARS + 246, ItemClassification.progression)
    WESTERN_WILDS_FOUNDRY_KEAR = ("Western Wilds Foundry Lock", ITEMS_OFFSET_KEARS + 247, ItemClassification.progression)
    ASTRAL_ORREY_MIRROR_ROOM_RIGHT_SIDE_KEAR = ("Astral Orrery Mirror Room Right Side Lock", ITEMS_OFFSET_KEARS + 277, ItemClassification.progression)
    ASTRAL_ORREY_MIRROR_ROOM_LEFT_SIDE_KEAR = ("Astral Orrery Mirror Room Left Side Lock", ITEMS_OFFSET_KEARS + 278, ItemClassification.progression)
    CHOPPE_SHOPPE_KEAR = ("Choppe Shoppe Lock", ITEMS_OFFSET_KEARS + 225, ItemClassification.progression)
    EASTERN_HEATH_WATERFALL_KEAR = ("Eastern Heath Waterfall Lock", ITEMS_OFFSET_KEARS + 222, ItemClassification.progression) #missing kear
    EASTERN_HEATH_BUCKLERS_BLUFF_KEAR = ("Eastern Heath Bucklers Bluff Lock", ITEMS_OFFSET_KEARS + 224, ItemClassification.progression)
    MOURNERS_MILES_BIKE_KEAR = ("Mourner's Mile Bike Lock", ITEMS_OFFSET_KEARS + 307, ItemClassification.progression)
    EASTERN_HEATH_GRASSLAND_BUSHROOM_KEAR = ("Eastern Heath Grassland Bushroom Lock", ITEMS_OFFSET_KEARS + 227, ItemClassification.progression)
    MOURNERS_MILE_AFTER_GENERATOR_KEAR = ("Mourner's Mile After Generator Lock", ITEMS_OFFSET_KEARS + 304, ItemClassification.progression)
    QUEENSBURY_CRYPT_BONNET_TOMB_KEAR = ("Queensbury Crypt Bonnet Tomb Lock", ITEMS_OFFSET_KEARS + 55, ItemClassification.progression)
    FROZEN_PASS_KEAR = ("Frozen Pass Lock", ITEMS_OFFSET_KEARS + 109, ItemClassification.progression)
    OSSEX_TRAIN_KEAR_1 = ("Ossex Train Lock 1", ITEMS_OFFSET_KEARS + 358, ItemClassification.progression)
    OSSEX_TRAIN_KEAR_2 = ("Ossex Train Lock 2", ITEMS_OFFSET_KEARS + 359, ItemClassification.progression)
    OSSEX_EAST_GARDEN_KEAR = ("Ossex East Garden Lock", ITEMS_OFFSET_KEARS + 157, ItemClassification.progression)
    PINKY_KEAR = ("Backwaters Pinky's Parlor Lock", ITEMS_OFFSET_KEARS + 284, ItemClassification.progression)
    PINKY_BACK_KEAR = ("Backwaters Pinky's Parlor Back Lock", ITEMS_OFFSET_KEARS + 283, ItemClassification.progression)
    LONERS_LANDING_BELOWDECKS_RIGHT_WEAPON_KEAR = ("Loner's Landing Below Decks Right Weapon Lock", ITEMS_OFFSET_KEARS + 20, ItemClassification.progression)
    LONERS_LANDING_BELOWDECKS_LEFT_WEAPON_KEAR = ("Loner's Landing Below Decks Left Weapon Lock", ITEMS_OFFSET_KEARS + 21, ItemClassification.progression)
    LONERS_LANDING_BELOWDECKS_BACK_KEAR = ("Loner's Landing Below Decks Path Lock", ITEMS_OFFSET_KEARS + 22, ItemClassification.progression)
    NOXS_BAYOU_SWAMP_SHACK_KEAR = ("Nox's Bayou Swamp Shack Lock", ITEMS_OFFSET_KEARS + 33, ItemClassification.progression) #find leading spac
    SANDFALL_CAVE_KEAR = ("Sandfalls Cave Lock", ITEMS_OFFSET_KEARS + 320, ItemClassification.progression)
    SANDFALLS_PAYLOAD_PASSAGE_BOTTOM_KEAR = ("Sandfalls Payload Passage Bottom Lock", ITEMS_OFFSET_KEARS + 318, ItemClassification.progression) #lower case kea
    BONE_BEACH_MINING_CAMP_CAVE_KEAR = ("Bone Beach Mining Camp Cave Lock", ITEMS_OFFSET_KEARS + 69, ItemClassification.progression)
    KINDLEWOOD_WALLOWERS_PATH_TRINKET_KEAR = ("Kindlewood Wallower's Path Trinket Lock", ITEMS_OFFSET_KEARS + 336, ItemClassification.progression)
    SEPTEMBURG_CROW_TOWN_TUNNEL_KEAR = ("Septemburg Crow Town Tunnel Lock", ITEMS_OFFSET_KEARS + 96, ItemClassification.progression)
    KINDLEWOOD_TOMATO_PATCH_KEAR = ("Kindlewood Tomato Patch Lock", ITEMS_OFFSET_KEARS + 338, ItemClassification.progression)
    KINDLEWOOD_TRAIN_TUNNEL_KEAR = ( "Kindlewood Train Tunnel Lock", ITEMS_OFFSET_KEARS + 337, ItemClassification.progression)
    COLTRANE_RAIL_YARD_KEAR = ("Coltrane Rail Yard Lock", ITEMS_OFFSET_KEARS + 115, ItemClassification.progression)
    ASTRAL_ORRERY_STELLARIUM_KEAR = ("Astral Orrery Stellarium Lock", ITEMS_OFFSET_KEARS + 127, ItemClassification.progression)
    BACKWATERS_FISHING_KEAR = ("Backwaters Fishing Lock", ITEMS_OFFSET_KEARS + 285, ItemClassification.progression)
    LONERS_LANDING_BOARDWALK_KEAR = ("Loner's Landing Boardwalk Lock", ITEMS_OFFSET_KEARS + 19, ItemClassification.progression)
    WESTERN_WILDS_SECRET_PASSAGE_KEAR = ("Western Wilds Secret Passage Lock", ITEMS_OFFSET_KEARS + 244, ItemClassification.progression)
    SANDFALLS_HIDDEN_CAVE_KEAR = ("Sandfalls Hidden Cave Lock", ITEMS_OFFSET_KEARS + 321, ItemClassification.progression)
    RADIANT_MANOR_MEOWSTRO_ROOM_KEAR = ("Radiant Manor Meowstro Room Lock", ITEMS_OFFSET_KEARS + 141, ItemClassification.progression)


kear_area_lookup = {
    SingleKears.OSSEX_HIGHSTREET_BALCONY_KEAR.value : AreaKears.OSSEX_KEARS,
    SingleKears.OSSEX_HIGH_STREET_SE_GARDEN_KEAR.value : AreaKears.OSSEX_KEARS,
    SingleKears.OSSEX_EAST_GARDEN_KEAR.value : AreaKears.OSSEX_KEARS,
    SingleKears.OSSEX_TRAIN_KEAR_1.value : AreaKears.TRAIN_KEARS,
    SingleKears.OSSEX_TRAIN_KEAR_2.value : AreaKears.TRAIN_KEARS,
    SingleKears.LONERS_LANDING_BOARDWALK_KEAR.value : AreaKears.LONERS_LANDING_KEARS,
    SingleKears.LONERS_LANDING_BELOWDECKS_RIGHT_WEAPON_KEAR.value : AreaKears.LONERS_LANDING_KEARS,
    SingleKears.LONERS_LANDING_BELOWDECKS_LEFT_WEAPON_KEAR.value : AreaKears.LONERS_LANDING_KEARS,
    SingleKears.LONERS_LANDING_BELOWDECKS_BACK_KEAR.value : AreaKears.LONERS_LANDING_KEARS,
    SingleKears.SOUTHERN_OUTSKIRTS_ROOFTOP_KEAR.value : AreaKears.SOUTHERN_OUTSKIRTS_KEARS,
    SingleKears.SOUTHERN_OUTSKIRTS_CAVE_NETWORK_KEAR.value : AreaKears.SOUTHERN_OUTSKIRTS_KEARS,
    SingleKears.CHOPPE_SHOPPE_KEAR.value : AreaKears.EASTERN_HEATH_KEARS,
    SingleKears.EASTERN_HEATH_WATERFALL_KEAR.value : AreaKears.EASTERN_HEATH_KEARS,
    SingleKears.EASTERN_HEATH_BUCKLERS_BLUFF_KEAR.value : AreaKears.EASTERN_HEATH_KEARS,
    SingleKears.EASTERN_HEATH_GRASSLAND_BUSHROOM_KEAR.value : AreaKears.EASTERN_HEATH_KEARS,
    SingleKears.WESTERN_WILDS_BALCONY_KEAR.value : AreaKears.WESTERN_WILDS_KEARS,
    SingleKears.WESTERN_WILDS_FOUNDRY_KEAR.value : AreaKears.WESTERN_WILDS_KEARS,
    SingleKears.WESTERN_WILDS_SECRET_PASSAGE_KEAR.value : AreaKears.WESTERN_WILDS_KEARS,
    SingleKears.MOURNERS_MILES_BIKE_KEAR.value : AreaKears.MOURNERS_MILE_KEARS,
    SingleKears.MOURNERS_MILE_AFTER_GENERATOR_KEAR.value : AreaKears.QUEENSBURY_KEARS,
    SingleKears.QUEENSBURY_CRYPT_BONNET_TOMB_KEAR.value : AreaKears.QUEENSBURY_KEARS,
    SingleKears.PINKY_KEAR.value : AreaKears.BACKWATER_KEARS,
    SingleKears.PINKY_BACK_KEAR.value : AreaKears.BACKWATER_KEARS,
    SingleKears.BACKWATERS_FISHING_KEAR.value : AreaKears.BACKWATER_KEARS,
    SingleKears.NOXS_BAYOU_SWAMP_SHACK_KEAR.value : AreaKears.BAYOU_KEARS,
    SingleKears.KINDLEWOOD_WALLOWERS_PATH_TRINKET_KEAR.value : AreaKears.KINDLEWOOD_KEARS,
    SingleKears.KINDLEWOOD_TOMATO_PATCH_KEAR.value : AreaKears.KINDLEWOOD_KEARS,
    SingleKears.KINDLEWOOD_TRAIN_TUNNEL_KEAR.value : AreaKears.KINDLEWOOD_KEARS,
    SingleKears.SEPTEMBURG_CROW_TOWN_TUNNEL_KEAR.value : AreaKears.SEPTEMBURG_KEARS,
    SingleKears.SANDFALL_CAVE_KEAR.value : AreaKears.SANDFALLS_KEARS,
    SingleKears.SANDFALLS_HIDDEN_CAVE_KEAR.value : AreaKears.SANDFALLS_KEARS,
    SingleKears.SANDFALLS_PAYLOAD_PASSAGE_BOTTOM_KEAR.value : AreaKears.SANDFALLS_KEARS,
    SingleKears.BONE_BEACH_MINING_CAMP_CAVE_KEAR.value : AreaKears.BONE_BEACH_KEARS,
    SingleKears.COLTRANE_RAIL_YARD_KEAR.value : AreaKears.COLTRANE_PEAK_KEARS,
    SingleKears.FROZEN_PASS_KEAR.value : AreaKears.COLTRANE_PEAK_KEARS,
    SingleKears.ASTRAL_ORREY_MIRROR_ROOM_RIGHT_SIDE_KEAR.value : AreaKears.ASTRAL_ORRERY_KEARS,
    SingleKears.ASTRAL_ORREY_MIRROR_ROOM_LEFT_SIDE_KEAR.value : AreaKears.ASTRAL_ORRERY_KEARS,
    SingleKears.ASTRAL_ORRERY_STELLARIUM_KEAR.value : AreaKears.ASTRAL_ORRERY_KEARS,
    SingleKears.RADIANT_MANOR_MEOWSTRO_ROOM_KEAR.value : AreaKears.RADIANT_MANOR_KEARS,
}
