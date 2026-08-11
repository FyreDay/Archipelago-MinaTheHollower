from BaseClasses import LocationProgressType
from rule_builder.rules import Has, CanReachLocation, True_
from .._generated.regions import Regions
from ... import LocationTypeEnum
from ...items import SingleKears
from ...rules.ability_rules import CanBurrow, CanBounce, CanClimb, CanCarry, CanSwim
from ...rules.state_rules import HasKear
from ...rules.movement_rules import CanJumpTiles

class Locations(LocationTypeEnum):
    RM_MIMIC_CHAMBER_TRINKET = (
        "RM Mimic Chamber Trinket",140,Regions.RADIANT_MANOR_MIMIC_CHAMBER,CanBurrow(),
    )

    RM_RAFTERS_CHEST = (
        "RM Rafters Chest",143,Regions.RADIANT_MANOR_RAFTERS,CanBurrow(),
    )

    RM_SERVANT_S_QUARTERS_TRINKET = (
        "RM Servant's Quarters Trinket",145,Regions.RADIANT_MANOR_SERVANTS_QUARTERS,CanBurrow(),
    )

    RM_BALLROOM_CHEST = (
        "RM Ballroom Chest",144,Regions.RADIANT_MANOR_BALLROOM_BALCONY_EAST,
    )

    RM_BALLROOM_TILE_CHAMBER_CHEST = (
        "RM Ballroom Tile Chamber Chest",142,Regions.RADIANT_MANOR_BALCONY_EAST_CHAMBER,CanJumpTiles(distance=2),
    )

    RM_MEOWSTRO_S_CHAMBER_BONESTONE = (
        "RM Meowstro's Chamber Bonestone",139,Regions.RADIANT_MANOR_MEOWSTROS_CHAMBER,CanBurrow()
        & CanSwim()
        & CanCarry()
        & CanBounce()
        & CanClimb()
        & HasKear(kear=SingleKears.RADIANT_MANOR_MEOWSTRO_ROOM_KEAR.value),
    )



class PermanentLocations(LocationTypeEnum):
    RM_FOYER_LIBRARY_CHEST = (
        "RM Foyer Library Chest",275,Regions.RADIANT_MANOR_FOYER_LIBRARY,CanJumpTiles(distance=2) & CanClimb(),
    )

class BossLocations(LocationTypeEnum):
    RM_DEFEAT_FURGUS = ("RM Defeat Furgus", 1019, Regions.RADIANT_MANOR_SERVANTS_ARENA)
    RM_DEFEAT_LIONEL = ("RM Defeat Lionel", 1007, Regions.RADIANT_MANOR_STUDY, True_(), LocationProgressType.EXCLUDED)
    RM_DEFEAT_GIGA_LIONEL = ("RM Defeat Giga Lionel", 1008, Regions.RADIANT_MANOR_PRIME_GENERATOR, True_(), LocationProgressType.EXCLUDED)

