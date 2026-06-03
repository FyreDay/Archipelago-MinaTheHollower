from enum import Enum, IntEnum
from typing import NamedTuple, Any, Union

from BaseClasses import ItemClassification, LocationProgressType, CollectionState, CollectionRule
from rule_builder.rules import Rule, True_
from ..world_base import MinaTheHollowerBase

class EntranceType(IntEnum):
    DO_NOT_RANDOMIZE_ENTRANCE = 0
    DOORS = 1


class ItemData(NamedTuple):
    item_id: int
    classification: ItemClassification

class MovementItemData(NamedTuple):
    item_id: int
    distance: int
    classification: ItemClassification

class RegionConnectionData(NamedTuple):
    exiting_region: str
    entering_region: str
    rule: CollectionRule | Rule[MinaTheHollowerBase]
    entrance_group: int = EntranceType.DO_NOT_RANDOMIZE_ENTRANCE

class LocationData(NamedTuple):
    progress_type: LocationProgressType
    region: str
    rule: CollectionRule | Rule[MinaTheHollowerBase] = True_[MinaTheHollowerBase]()

AnyItemData: type = Union[ItemData, MovementItemData]