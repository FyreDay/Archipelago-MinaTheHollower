from BaseClasses import LocationProgressType
from rule_builder.rules import Has, CanReachLocation
from .. import LocationData
from ... import RegionConnection, TransitionType, Transition
from ...rules.ability_rules import CanBurrow, CanJumpOneTile, CanBounce, CanJumpTiles, CanClimb, CanCarry

regions: set[str] = {
    "Kindlewood Overgrowth Bonfire",
    "Kindlewood Residence Basement",
    "Kindlewood Madd House",
    "Kindlewood Behind Madd House",
    "Kindlewood Train Station",
    "Kindlewood Farm Crossing Shack",
    "Kindlewood Wallower's Room",
    "Kindlewood Rail Tunnel"
}

transitions: dict[str, Transition] = {

}

connections: dict[str, RegionConnection] = {
}

collectable_locations: dict[str, LocationData] = {
    # Check ID - Imported and guessed
    # Check ID - Imported and guessed
    "KW Overgrowth Bonfire Chest": LocationData(335, "Kindlewood Overgrowth Bonfire",
                                                CanBurrow()),
    # Check ID - Imported and guessed
    "KW Residence Basement Chest": LocationData(341, "Kindlewood Residence Basement",
                                                CanBurrow() & CanCarry()),
    # Check ID - Imported and guessed
    "KW Madd House Draining Beastium": LocationData(348, "Kindlewood Madd House"),
    "KW Madd House Oozing Organ": LocationData(347, "Kindlewood Madd House"),
    # Check ID - Imported and guessed
    "KW Madd House Voltaic Guard": LocationData(349, "Kindlewood Madd House"),
    # Check ID - Imported and guessed
    "KW Madd House Kear": LocationData(341, "Kindlewood Madd House"),
    # Check ID - Imported and guessed
    "KW Behind Madd House Chest": LocationData(339, "Kindlewood Behind Madd House",
                                               CanBurrow() & CanCarry()),
    # Check ID - Imported and guessed
    "KW Train Station Gourdan": LocationData(335, "Kindlewood Train Station",
                                             CanBurrow() & Has("Oozing Organ")),
    # Check ID - Imported and guessed
    "KW Train Station Ledge Chest": LocationData(346, "Kindlewood Train Station",
                                                 CanBurrow()),
    # Check ID - Imported and guessed
    "KW Farm Crossing Shack Chest": LocationData(341, "Kindlewood Farm Crossing Shack",
                                                 CanBurrow() & Has("Reaching Sidearm")),
    "KW Wallower's Room Wallower's Gauntlets": LocationData(344, "Kindlewood Wallower's Room",
                                                            Has("KW Wallower's Room Kear") & CanBurrow()),

    # Special rules - contains air movement requirement, double check
    # Special rules - "Wallower's Gloves" may need verification against item naming
    # Special rules - "5+ Tiles of Air Movement"
    # Check ID - Imported and guessed
    "KW Wallower's Room Chest": LocationData(346, "Kindlewood Wallower's Room",
                                             (Has("Wallower's Gloves") & CanBurrow()) |
                                             CanJumpTiles(distance=5)),
    # Check ID - Imported and guessed
    "KW Rail Tunnel Vial Pouch": LocationData(343, "Kindlewood Rail Tunnel",
                                              CanBurrow() & CanCarry() & Has("Pipes")),
}

bosses: dict[str, LocationData] = {
    "KW Madd House": LocationData(0, "Kindlewood Madd House"),
}

