from BaseClasses import LocationProgressType
from rule_builder.rules import Has, CanReachLocation
from .. import LocationData
from ... import RegionConnection, TransitionType, Transition
from ...rules.ability_rules import CanBurrow, CanJumpOneTile, CanBounce, CanJumpTiles, CanClimb, CanCarry

regions: set[str] = {
    "Astral Orrery Mirror's End",
    "Astral Orrery Mirror's End Moving Platform Room",
    "Astral Orrery Stellarium",
    "Astral Orrery Gravity Zone Long Hallway",
    "Astral Orrery Gravity Zone Secret Room #1",
    "Astral Orrery Gravity Zone Secret Room #2",
    "Astral Orrery Cog Chamber Secret Room #1",
    "Astral Orrery Cog Chamber Secret Room #2",
    "Astral Orrery Mutant Lab Secret Room #1",
    "Astral Orrery Mutant Lab Secret Room #2",
    "Astral Orrery Hall of Scholars Below Boss Chamber",
    "Astral Orrery Hall of Scholars Boss Chamber",
    "Astral Orrery Hall of Scholars Exit",
    "Astral Orrery Sealed Archive Congealed Chamber",
    "Astral Orrery Starry Generator",
}

transitions: dict[str, Transition] = {

}

connections: dict[str, RegionConnection] = {
}

collectable_locations: dict[str, LocationData] = {
    # Check ID - Imported and guessed
    "AO Mirror's End Beach Room Chest": LocationData(126, "Astral Orrery Mirror's End",
                                                     CanBurrow()),

    # Special rules - 3 tiles of air movement + Carry/Throw
    "AO Mirror's End Reckless Beastium": LocationData(127, "Astral Orrery Mirror's End",
                                                      CanJumpTiles(distance=3) & CanCarry()),

    # Check ID - Imported and guessed
    "AO Mirror's End West Ledge Trinket Bag": LocationData(279, "Astral Orrery Mirror's End",
                                                           Has("Kear")),

    "AO Mirror's End Trunkstar Core": LocationData(282, "Astral Orrery Mirror's End",
                                                   Has("Fishing Rod")),

    # Special rules - (Blue Tile Switch OR 5 tiles air movement)
    "AO Mirror's End Moving Platform Room Chest": LocationData(128, "Astral Orrery Mirror's End Moving Platform Room",
                                                               Has("Blue Tile Switch") | CanJumpTiles(distance=5)),

    # Check ID - Imported and guessed
    "AO Stellarium East Chest": LocationData(129, "Astral Orrery Stellarium",
                                             Has("Kear")),

    "AO Tubert Vial Salvo": LocationData(137, "Astral Orrery Stellarium"),

    # Mirror requirement noted in sheet but not expressible in current rule set
    "AO Tubert Vial Kear": LocationData(135, "Astral Orrery Stellarium",
                                        Has("Kear")),

    # Special rules - 2 tiles air movement + Void Portal switch
    "AO Gravity Zone Long Hallway Chest": LocationData(130, "Astral Orrery Gravity Zone Long Hallway",
                                                       CanJumpTiles(distance=2) & Has("Void Portal Switch")),

    # Check ID - Imported and guessed
    "AO Gravity Zone Secret Room #1 Kear": LocationData(134, "Astral Orrery Gravity Zone Secret Room #1"),

    # Check ID - Imported and guessed
    "AO Gravity Zone Secret Room #2 Chest": LocationData(131, "Astral Orrery Gravity Zone Secret Room #2"),

    # Check ID - Imported and guessed
    "AO Cog Chamber Secret Room #1 Chest": LocationData(133, "Astral Orrery Cog Chamber Secret Room #1",
                                                        CanBurrow() & CanCarry()),

    # Check ID - Imported and guessed
    "AO Cog Chamber Secret Room #2 Kear": LocationData(132, "Astral Orrery Cog Chamber Secret Room #1",
                                                       CanBurrow() & CanCarry()),

    # Check ID - Imported and guessed
    "AO Mutant Lab Secret Room #1 Chest": LocationData(136, "Astral Orrery Mutant Lab Secret Room #1",
                                                       CanBurrow()),

    # Check ID - Imported and guessed
    "AO Mutant Lab Secret Room #2 Bridge Weaver": LocationData(132, "Astral Orrery Mutant Lab Secret Room #2",
                                                               CanBurrow()),

    # Check ID - Imported and guessed
    "AO Hall of Scholars Below Boss Chamber Bonestone": LocationData(131,
                                                                     "Astral Orrery Hall of Scholars Below Boss Chamber"),

    # No ID available (N/A vanilla item)
    "AO Defeat Lumenarks": LocationData(0, "Astral Orrery Hall of Scholars Boss Chamber"),

    # Check ID - Imported and guessed
    "AO Hall of Scholars Exit Chest": LocationData(133, "Astral Orrery Hall of Scholars Exit"),

    "AO Sealed Archive Health Rose": LocationData(125, "Astral Orrery Sealed Archive",
                                                  CanBurrow()),


}
bosses: dict[str, LocationData] = {
    # No ID available (N/A vanilla item)
    "AO Sealed Archive The Congealed": LocationData(0, "Astral Orrery Sealed Archive"),

    # No ID available (N/A vanilla item)
    "AO Starry Generator Activated": LocationData(0, "Astral Orrery Starry Generator"),
}

