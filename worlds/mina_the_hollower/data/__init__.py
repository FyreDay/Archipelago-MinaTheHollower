from dataclasses import dataclass
from enum import Enum, IntEnum
from typing import NamedTuple, Any, Union, Optional, Callable

from BaseClasses import ItemClassification, LocationProgressType, CollectionState, CollectionRule, Item
from rule_builder.rules import Rule, True_
from ..world_base import MinaTheHollowerBase




class TransitionType(IntEnum):
    DO_NOT_RANDOMIZE_ENTRANCE = 0
    SCREENS = 1 << 3
    AREA_SCREENS = 2 << 3
    DOORS = 3 << 3
    MIRRORS = 4 << 3
    STAIRS = 5 << 3
    GEYSER_UP = 6 << 3
    GEYSER_DOWN = 7 << 3
    BURROW = 8 << 3
    TRANSITION_MASK = 1 << 3


class DirectionType(IntEnum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3
    ASTRAL = 4
    OVERWORLD = 5
    DIRECTION_MASK = (1 << 2) | (1 << 1) | 1

matching_transition_types = {
    TransitionType.SCREENS | DirectionType.NORTH: [TransitionType.SCREENS | DirectionType.SOUTH],
    TransitionType.SCREENS | DirectionType.EAST: [TransitionType.SCREENS | DirectionType.WEST],
    TransitionType.SCREENS | DirectionType.SOUTH: [TransitionType.SCREENS | DirectionType.NORTH],
    TransitionType.SCREENS | DirectionType.WEST: [TransitionType.SCREENS | DirectionType.EAST],

    TransitionType.AREA_SCREENS | DirectionType.NORTH: [TransitionType.AREA_SCREENS | DirectionType.SOUTH],
    TransitionType.AREA_SCREENS | DirectionType.EAST: [TransitionType.AREA_SCREENS | DirectionType.WEST],
    TransitionType.AREA_SCREENS | DirectionType.SOUTH: [TransitionType.AREA_SCREENS | DirectionType.NORTH],
    TransitionType.AREA_SCREENS | DirectionType.WEST: [TransitionType.AREA_SCREENS | DirectionType.EAST],

    TransitionType.DOORS | DirectionType.NORTH: [TransitionType.DOORS | DirectionType.SOUTH,
                                                 TransitionType.STAIRS | DirectionType.SOUTH,
                                                 TransitionType.STAIRS | DirectionType.NORTH],

    TransitionType.DOORS | DirectionType.EAST: [TransitionType.DOORS | DirectionType.WEST,
                                                TransitionType.STAIRS | DirectionType.WEST,
                                                TransitionType.STAIRS | DirectionType.EAST],

    TransitionType.DOORS | DirectionType.SOUTH: [TransitionType.DOORS | DirectionType.NORTH,
                                                 TransitionType.STAIRS | DirectionType.NORTH,
                                                 TransitionType.STAIRS | DirectionType.SOUTH],

    TransitionType.DOORS | DirectionType.WEST: [TransitionType.DOORS | DirectionType.EAST,
                                                TransitionType.STAIRS | DirectionType.EAST,
                                                TransitionType.STAIRS | DirectionType.WEST],

    TransitionType.MIRRORS | DirectionType.ASTRAL: [TransitionType.MIRRORS | DirectionType.OVERWORLD],
    TransitionType.MIRRORS | DirectionType.OVERWORLD: [TransitionType.MIRRORS | DirectionType.ASTRAL],

    TransitionType.STAIRS | DirectionType.NORTH: [TransitionType.DOORS | DirectionType.SOUTH,
                                                TransitionType.DOORS | DirectionType.NORTH,
                                                TransitionType.STAIRS | DirectionType.SOUTH,
                                                TransitionType.STAIRS | DirectionType.NORTH],

    TransitionType.STAIRS | DirectionType.EAST: [TransitionType.DOORS | DirectionType.WEST,
                                                TransitionType.DOORS | DirectionType.EAST,
                                                TransitionType.STAIRS | DirectionType.WEST,
                                                TransitionType.STAIRS | DirectionType.EAST],

    TransitionType.STAIRS | DirectionType.SOUTH: [TransitionType.DOORS | DirectionType.NORTH,
                                                TransitionType.DOORS | DirectionType.SOUTH,
                                                TransitionType.STAIRS | DirectionType.NORTH,
                                                TransitionType.STAIRS | DirectionType.SOUTH],

    TransitionType.STAIRS | DirectionType.WEST: [TransitionType.DOORS | DirectionType.EAST,
                                                TransitionType.DOORS | DirectionType.WEST,
                                                TransitionType.STAIRS | DirectionType.EAST,
                                                TransitionType.STAIRS | DirectionType.WEST],

}


def get_target_groups(group: int) -> list[int]:
    return matching_transition_types[group]

class ItemTypeEnum(Enum):
    def __init__(self, value: str, item_id: int, classification: ItemClassification):
        # self._value_ must be set to the first element to support lookup by value
        self._value_ = value
        self.item_id = item_id
        self.classification = classification

    @classmethod
    def from_item_id(cls, item_id: int):
        return next(item for item in cls if item.item_id == item_id)


@dataclass
class ItemData:
    type: ItemTypeEnum
    amount: int = 1

@dataclass
class ItemFiller:
    type: ItemTypeEnum
    weight: int = 1

@dataclass
class ItemMovement:
    type: ItemTypeEnum
    distance: int

@dataclass
class ItemPower:
    type: ItemTypeEnum
    power: int
    requiredType: Optional[ItemTypeEnum] = None

class ShortCutItem(NamedTuple):
    type: ItemTypeEnum
    access_rule: CollectionRule | Rule[MinaTheHollowerBase]

class RegionTypeEnum(Enum):
    def __init__(self,value: str):
        # self._value_ must be set to the first element to support lookup by value
        self._value_ = value

class ConnectionTypeEnum(Enum):
    def __init__(self, value: str, exiting_region: RegionTypeEnum, entering_region: RegionTypeEnum, rule: CollectionRule | Rule[MinaTheHollowerBase] = True_()):
        # self._value_ must be set to the first element to support lookup by value
        self._value_ = value
        self.exiting_region = exiting_region
        self.entering_region = entering_region
        self.rule = rule

class TransitionTypeEnum(Enum):
    def __init__(self, value: str, exiting_region: RegionTypeEnum, entering_region: RegionTypeEnum, direction_type: DirectionType, transition_type: TransitionType, rule: CollectionRule | Rule[MinaTheHollowerBase] = True_()):
        # self._value_ must be set to the first element to support lookup by value
        self._value_ = value
        self.exiting_screen = exiting_region
        self.entering_screen = entering_region
        self.direction = direction_type
        self.entrance_group = transition_type
        self.rule = rule

class LocationTypeEnum(Enum):
    def __init__(self, value: str, location_id: int, region: RegionTypeEnum,rule: CollectionRule | Rule[MinaTheHollowerBase] = True_(), progress_type: LocationProgressType = LocationProgressType.DEFAULT):#, item_rule: Callable[[Item], bool] =  lambda item: True_()):
        # self._value_ must be set to the first element to support lookup by value
        self._value_ = value
        self.region = region
        self.location_id = location_id
        self.rule = rule
        self.progress_type = progress_type
        # self.item_rule: Callable[[Item], bool] = item_rule

class EventTypeEnum(Enum):
    def __init__(self, value: str, region:str, event_item:str,  rule: CollectionRule | Rule[MinaTheHollowerBase] = True_()):
        # self._value_ must be set to the first element to support lookup by value
        self._value_ = value
        self.region = region
        self.event_item = event_item
        self.rule = rule

class RepairEventData(NamedTuple):
    type: EventTypeEnum
    gen_name: str
    index: int
    kear_item_type: ItemTypeEnum