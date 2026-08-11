from collections import ChainMap

from ._generated import eastern_heath_edges, mourners_mile_edges, ossex_edges, queensbury_crypt_edges, \
    southern_outskirts_edges, western_wilds_edges, ossex_train_edges, sandfalls_edges, loners_landing_edges, \
    backwaters_edges, bayou_edges, septemburg_edges, bone_beach_edges, kindlewood_edges, coltrane_peak_edges, \
    radiant_manor_edges, astral_orrery_edges
from ._generated.regions import Regions
from .areas import astral_orrery, bayou, bone_beach, coltrane_peak, eastern_heath, kindlewood, loners_landing, \
    mourners_mile, ossex, queensbury_crypt, radiant_manor, sandfalls, septemburg, southern_outskirts, backwaters, \
    western_wilds, mirrors_end
from .. import LocationTypeEnum, RegionTypeEnum, ConnectionTypeEnum, \
    TransitionTypeEnum
from ..events import QUEENSBURY_CRYPT_DATA, ASTRAL_ORRERY_DATA, COLTRANE_PEAK_DATA, BONE_BEACH_DATA, SEPTEMBURG_DATA, \
    NOXS_BAYOU_DATA, RADIANT_MANOR_DATA

all_collectables: list[LocationTypeEnum] = [
    *astral_orrery.Locations,
    *mirrors_end.Locations,
    *bayou.Locations,
    *bone_beach.Locations,
    *coltrane_peak.Locations,
    *eastern_heath.Locations,
    *kindlewood.Locations,
    *loners_landing.Locations,
    *mourners_mile.Locations,
    *ossex.Locations,
    *queensbury_crypt.Locations,
    *radiant_manor.Locations,
    *sandfalls.Locations,
    *septemburg.Locations,
    *southern_outskirts.Locations,
    *backwaters.Locations,
    *western_wilds.Locations
]

all_optional_locations: list[LocationTypeEnum] =[
    *loners_landing.OptionalLocations
]

all_bosses: list[LocationTypeEnum] =[
    *astral_orrery.BossLocations,
    *bayou.BossLocations,
    *bone_beach.BossLocations,
    *coltrane_peak.BossLocations,
    *eastern_heath.BossLocations,
    *kindlewood.BossLocations,
    # *loners_landing.BossLocations,
    # *mourners_mile.BossLocations,
    *ossex.BossLocations,
    *queensbury_crypt.BossLocations,
    *radiant_manor.BossLocations,
    *sandfalls.BossLocations,
    *septemburg.BossLocations,
    *southern_outskirts.BossLocations,
    *backwaters.BossLocations,
    # western_wilds.BossLocations,
]

all_locations: list[LocationTypeEnum] = [
    *all_collectables,
    *all_bosses
]

dungeon_locations: dict[int, list[LocationTypeEnum]]= {
    QUEENSBURY_CRYPT_DATA.index: [*queensbury_crypt.Locations, *queensbury_crypt.BossLocations],
    NOXS_BAYOU_DATA.index: [*bayou.Locations, *bayou.BossLocations],
    SEPTEMBURG_DATA.index: [*septemburg.Locations, *septemburg.BossLocations],
    BONE_BEACH_DATA.index: [*bone_beach.Locations, *bone_beach.BossLocations],
    COLTRANE_PEAK_DATA.index: [*coltrane_peak.Locations, *coltrane_peak.BossLocations],
    ASTRAL_ORRERY_DATA.index: [*astral_orrery.Locations, *astral_orrery.BossLocations],
    RADIANT_MANOR_DATA.index: [*radiant_manor.Locations, *radiant_manor.BossLocations],
}

all_permanent_locations: list[LocationTypeEnum] = [
    *mirrors_end.Locations,
    *eastern_heath.Locations,
    *eastern_heath.BossLocations,
    *kindlewood.Locations,
    *kindlewood.BossLocations,
    *loners_landing.Locations,
    *mourners_mile.Locations,
    *ossex.Locations,
    *ossex.BossLocations,
    *sandfalls.Locations,
    *sandfalls.BossLocations,
    *southern_outskirts.Locations,
    *southern_outskirts.BossLocations,
    *backwaters.Locations,
    *backwaters.BossLocations,
    *western_wilds.Locations,
    *radiant_manor.Locations,
    *radiant_manor.BossLocations,
]

all_regions: list[RegionTypeEnum] = [*Regions]

all_internal_region_connections: list[ConnectionTypeEnum] = [
    *astral_orrery_edges.RegionConnections,
    *bayou_edges.RegionConnections,
    *bone_beach_edges.RegionConnections,
    *coltrane_peak_edges.RegionConnections,
    *eastern_heath_edges.RegionConnections,
    *kindlewood_edges.RegionConnections,
    *loners_landing_edges.RegionConnections,
    *mourners_mile_edges.RegionConnections,
    *ossex_edges.RegionConnections,
    *queensbury_crypt_edges.RegionConnections,
    *radiant_manor_edges.RegionConnections,
    *sandfalls_edges.RegionConnections,
    *septemburg_edges.RegionConnections,
    *southern_outskirts_edges.RegionConnections,
    *backwaters_edges.RegionConnections,
    *western_wilds_edges.RegionConnections,
]

all_region_transitions: list[TransitionTypeEnum] = [
    *astral_orrery_edges.RegionTransitions,
    *bayou_edges.RegionTransitions,
    *bone_beach_edges.RegionTransitions,
    *coltrane_peak_edges.RegionTransitions,
    *eastern_heath_edges.RegionTransitions,
    *kindlewood_edges.RegionTransitions,
    *loners_landing_edges.RegionTransitions,
    *mourners_mile_edges.RegionTransitions,
    *ossex_edges.RegionTransitions,
    *ossex_train_edges.RegionTransitions,
    *queensbury_crypt_edges.RegionTransitions,
    *radiant_manor_edges.RegionTransitions,
    *sandfalls_edges.RegionTransitions,
    *septemburg_edges.RegionTransitions,
    *southern_outskirts_edges.RegionTransitions,
    *backwaters_edges.RegionTransitions,
    *western_wilds_edges.RegionTransitions,
]


