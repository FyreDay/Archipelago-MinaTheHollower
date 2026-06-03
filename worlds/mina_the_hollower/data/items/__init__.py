from collections import ChainMap

from . import trinkets
from .. import MovementItemData, AnyItemData

all_movement_items: ChainMap[str, MovementItemData] = ChainMap(
    trinkets.movement_trinkets
)