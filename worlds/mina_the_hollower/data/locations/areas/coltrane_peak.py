from BaseClasses import LocationProgressType
from rule_builder.rules import Has, CanReachLocation
from .. import LocationData
from ... import RegionConnection, TransitionType, Transition
from ...rules.ability_rules import CanBurrow, CanJumpOneTile, CanBounce, CanJumpTiles, CanClimb, CanCarry

regions: set[str] = {
    "Coltrane Peak Fateful Cliff",
    "Coltrane Peak Frigid Station",
    "Coltrane Peak Frozen Pass",
    "Coltrane Peak Dead Man's Gorge",
    "Coltrane Peak Frostbite Woods",
    "Coltrane Peak Rail Yard",
    "Coltrane Peak Icebound Cavern",
    "Coltrane Peak Spiral Summit",
    "Coltrane Peak Agnes Express",
    "Coltrane Peak Maelstrom",
    "Coltrane Peak Frozen Generator",
}

transitions: dict[str, Transition] = {

}

connections: dict[str, RegionConnection] = {
}

collectable_locations: dict[str, LocationData] = {
    # Check ID - Imported and guessed
    "CTP Fateful Cliff Thorne CTP Boss": LocationData(110, "Coltrane Peak Fateful Cliff",
                                                      CanBurrow() & CanClimb()),

    # Check ID - Imported and guessed
    "CTP Frigid Station Missed Train Chest": LocationData(113, "Coltrane Peak Frigid Station",
                                                          CanBurrow() & CanClimb()),

    # Check ID - Imported and guessed
    "CTP Frozen Pass Rope Chest": LocationData(112, "Coltrane Peak Frozen Pass",
                                               CanBurrow() & CanClimb()),

    # Check ID - Imported and guessed
    "CTP Dead Man's Gorge Passage Trinket": LocationData(110, "Coltrane Peak Dead Man's Gorge",
                                                         CanBurrow() & CanClimb()),

    # Check ID - Imported and guessed
    "CTP Dead Man's Gorge Rail Kear": LocationData(111, "Coltrane Peak Dead Man's Gorge",
                                                   CanBurrow() & CanClimb()),

    # Check ID - Imported and guessed
    "CTP Frostbite Woods Blinking Glass": LocationData(114, "Coltrane Peak Frostbite Woods",
                                                       CanBurrow() & CanClimb()),

    # No ID available (N/A vanilla item)
    "CTP Frostbite Woods Mirren": LocationData(0, "Coltrane Peak Frostbite Woods",
                                               CanBurrow() & CanClimb()),

    # Check ID - Imported and guessed
    "CTP Rail Yard Purple Structure Chest": LocationData(118, "Coltrane Peak Rail Yard",
                                                         CanBurrow() & CanClimb()),

    # Check ID - Imported and guessed
    "CTP Rail Yard Cliff Chest": LocationData(117, "Coltrane Peak Rail Yard",
                                              CanBurrow() & CanClimb()),

    # Check ID - Imported and guessed
    "CTP Rail Yard Casket Chest": LocationData(120, "Coltrane Peak Rail Yard",
                                               CanBurrow() & CanClimb()),

    # Special rules - Kear requirement (1 Kear + Fishing Rod)
    "CTP Rail Yard Kear Room Fish": LocationData(122, "Coltrane Peak Rail Yard",
                                                 CanBurrow() & CanClimb() &
                                                 Has("Coltrane Peak Rail Yard Kear") & Has("Fishing Rod")),

    # Check ID - Imported and guessed
    "CTP Rail Yard Kear Room Rupert Shop Trinket": LocationData(119, "Coltrane Peak Rail Yard",
                                                                CanBurrow() & CanClimb() &
                                                                Has("Kear")),

    # Check ID - Imported and guessed
    "CTP Rail Yard Kear Room Rupert Shop": LocationData(121, "Coltrane Peak Rail Yard",
                                                             CanBurrow() & CanClimb() &
                                                             Has("Coltrane Peak Rail Yard Kear")),
    # Check ID - Imported and guessed
    "CTP Spiral Summit Kear": LocationData(121, "Coltrane Peak Spiral Summit",
                                           CanBurrow() & CanClimb()),

    # Check ID - Imported and guessed
    "CTP Agnes Express Bone Mimic": LocationData(123, "Coltrane Peak Agnes Express",
                                                 CanBurrow() & CanClimb()),

    # Check ID - Imported and guessed
    "CTP Maelstrom Locomotress Health Rose": LocationData(124, "Coltrane Peak Maelstrom",
                                                          CanBurrow() & CanClimb()),


}


bosses: dict[str, LocationData] = {
    # No ID available (N/A vanilla item)
    "CTP Icebound Cavern Frozen Horror Boss": LocationData(0, "Coltrane Peak Icebound Cavern",
                                                           CanBurrow() & CanClimb()),
    # No ID available (N/A vanilla item)
    "CTP Maelstrom Locomotress Agnes Boss": LocationData(0, "Coltrane Peak Maelstrom",
                                                         CanBurrow() & CanClimb()),

    # No ID available (N/A vanilla item)
    "CTP Frozen Generator Activated": LocationData(0, "Coltrane Peak Frozen Generator",
                                                   CanBurrow() & CanClimb()),
}