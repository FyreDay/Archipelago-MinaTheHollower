from BaseClasses import ItemClassification
from .. import MovementItemData

movement_trinkets: dict[str, MovementItemData] = {
    "A": MovementItemData(0x78, 3, ItemClassification.progression),
    "B": MovementItemData(0x78, 2, ItemClassification.progression),
    "C": MovementItemData(0x78, 1, ItemClassification.progression),

}
