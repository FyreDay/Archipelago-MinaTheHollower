from BaseClasses import ItemClassification
from ...constants import ITEMS_OFFSET_TRAPS
from .. import ItemTypeEnum


class Traps(ItemTypeEnum):
    FLIP_CONTROLS_TRAP = ("Flip Controls Trap", ITEMS_OFFSET_TRAPS + 15, ItemClassification.trap)
    FLOOR_IS_LAVA_TRAP = ("Floor Is Lava Trap", ITEMS_OFFSET_TRAPS + 174, ItemClassification.trap)
    GIANT_TRAP = ("Giant Trap", ITEMS_OFFSET_TRAPS + 190, ItemClassification.trap)
    X2_GIANT_TRAP = ("2x Giant Trap", ITEMS_OFFSET_TRAPS + 191, ItemClassification.trap)
    GIANT_ENEMIES_TRAP = ("Giant Enemies Trap", ITEMS_OFFSET_TRAPS + 192, ItemClassification.trap)
    X2_GIANT_ENEMIES_TRAP = ("2x Giant Enemies Trap", ITEMS_OFFSET_TRAPS + 193, ItemClassification.trap)
    INVISIBLE_TRAP = ("Invisible Trap", ITEMS_OFFSET_TRAPS + 195, ItemClassification.trap)
    NO_HUD_TRAP = ("No HUD Trap", ITEMS_OFFSET_TRAPS + 197, ItemClassification.trap)
    ROTATE_CAMERA_TRAP = ("Rotate Camera Trap", ITEMS_OFFSET_TRAPS + 202, ItemClassification.trap)
    ROTATE_CAMERA_INPUT_TRAP = ("Rotate Camera Input Trap", ITEMS_OFFSET_TRAPS + 203, ItemClassification.trap)
    MIRROR_SCREEN_TRAP = ("Mirror Screen Trap", ITEMS_OFFSET_TRAPS + 204, ItemClassification.trap)
    UPSIDEDOWN_SCREEN_TRAP = ("Upsidedown Screen Trap", ITEMS_OFFSET_TRAPS + 205, ItemClassification.trap)


def get_default_dict():
    return {
        trap.value: 50
        for trap in Traps
    }