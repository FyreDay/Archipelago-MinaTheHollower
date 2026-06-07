from enum import Enum, IntEnum
from typing import NamedTuple, Any, Union

from BaseClasses import ItemClassification, LocationProgressType, CollectionState, CollectionRule
from rule_builder.rules import Rule, True_
from ..world_base import MinaTheHollowerBase

class TransitionType(IntEnum):
    DO_NOT_RANDOMIZE_ENTRANCE = 0
    SCREENS = 1
    AREA_SCREENS = 2
    DOORS = 3
    MIRRORS = 4
    TREES = 5

class DirectionType(IntEnum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 2

class ItemData(NamedTuple):
    item_id: int
    classification: ItemClassification
    amount: int = 1

class MovementItemData(NamedTuple):
    item_id: int
    distance: int
    classification: ItemClassification
    amount: int = 1

class RegionConnection(NamedTuple):
    exiting_sub_region: str
    entering_region: str
    rule: CollectionRule | Rule[MinaTheHollowerBase] = True_()

class Transition(NamedTuple):
    name: str # Human-readable name
    exiting_screen: str
    entering_screen: str
    direction: int
    entrance_group: int = TransitionType.SCREENS
    rule: CollectionRule | Rule[MinaTheHollowerBase] = True_()

class LocationData(NamedTuple):
    location_id: int
    region: str
    rule: CollectionRule | Rule[MinaTheHollowerBase] = True_()
    progress_type: LocationProgressType = LocationProgressType.DEFAULT

AnyItemData: type = Union[ItemData, MovementItemData]