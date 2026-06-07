from BaseClasses import LocationProgressType
from rule_builder.rules import Has, CanReachLocation
from .. import LocationData
from ... import RegionConnection, TransitionType, Transition
from ...rules.ability_rules import CanBurrow, CanJumpOneTile, CanBounce, CanJumpTiles, CanClimb, CanCarry

regions: set[str] = {
    "Septemburg Withered Farm Secret Room #1",
    "Septemburg Withered Farm Secret Room #2",
    "Septemburg Kid Room",
    "Septemburg Hidden Mandrake Room",
    "Septemburg Hidden Crop Thresher Room",
    "Septemburg Rotten Barn",
    "Septemburg Below Crow Town Bridge",
    "Septemburg Crow Town",
    "Septemburg Tangled Woods Hidden Grove",
    "Septemburg Galloway Room",
    "Septemburg Stormwatch Way Chest",
    "Septemburg Carving Shack",
    "Septemburg Windy Generator",
    "Septemburg Wastewater Canal",
    "Septemburg Wastewater Canal Slime Room",
    "Septemburg Wastewater Canal Pipe Room",
    "Septemburg Wastewater Canal Well Entrance",
}

transitions: dict[str, Transition] = {

}

connections: dict[str, RegionConnection] = {
}

collectable_locations: dict[str, LocationData] = {
    # Check ID - Imported and guessed
    "SB Launch Pad Secret Room #1 Chest": LocationData(91, "Septemburg Withered Farm Secret Room #1",
                                                       CanBounce()),

    # Check ID - Imported and guessed
    "SB Launch Pad Secret Room #2 Kear": LocationData(97, "Septemburg Withered Farm Secret Room #2",
                                                      CanBounce()),

    # Check ID - Imported and guessed
    "SB Kid Room Chest": LocationData(92, "Septemburg Kid Room",
                                      CanBurrow()),

    # Check ID - Imported and guessed
    "SB Hidden Mandrake Room Chest": LocationData(93, "Septemburg Hidden Mandrake Room",
                                                  CanBurrow()),

    # Check ID - Imported and guessed
    "SB Hidden Crop Thresher Room Chest": LocationData(90, "Septemburg Hidden Crop Thresher Room",
                                                       CanBurrow()),

    # Check ID - Imported and guessed
    "SB Rotten Barn Chest": LocationData(94, "Septemburg Rotten Barn",
                                         CanBurrow()),

    # Check ID - Imported and guessed
    "SB Below Crow Town Bridge Chest": LocationData(98, "Septemburg Below Crow Town Bridge",
                                                    CanBurrow()),

    "SB Below Crow Town Gazeworm Eye": LocationData(104, "Septemburg Below Crow Town",
                                                    Has("Fishing Rod")),

    "SB Crow Town Shop Repulsing Root": LocationData(102, "Septemburg Crow Town"),

    # Check ID - Imported and guessed
    "SB Crow Town Shop Kear": LocationData(103, "Septemburg Crow Town"),

    # Check ID - Imported and guessed
    "SB Crow Town Farmhouse Roof Chest": LocationData(99, "Septemburg Crow Town",
                                                      CanBurrow() & CanCarry()),

    # Check ID - Imported and guessed
    "SB Tangled Woods Hidden Grove Chest": LocationData(100, "Septemburg Tangled Woods Hidden Grove",
                                                        CanBurrow()),

    # Check ID - Imported and guessed
    "SB Galloway Room Chest": LocationData(101, "Septemburg Galloway Room",
                                           CanBurrow() & CanBounce()),

    # Check ID - Imported and guessed
    "SB Stormwatch Way Chest": LocationData(96, "Septemburg Stormwatch Way Chest",
                                            CanBurrow()),

    # Check ID - Imported and guessed
    "SB Carving Shack Health Rose": LocationData(95, "Septemburg Carving Shack"),

    # No ID available (N/A vanilla item)
    "SB The Carving Man": LocationData(0, "Septemburg Carving Shack"),

    # No ID available (N/A vanilla item)
    "SB Windy Generator Activated": LocationData(0, "Septemburg Windy Generator",
                                                 CanBounce() & CanBurrow()),

    # Check ID - Imported and guessed
    "SB Dark Deluxy Spark Container": LocationData(353, "Septemburg Windy Generator",
                                                   CanBurrow() & Has("Pipes")),

    # Check ID - Imported and guessed
    "SB Wastewater Canal Spincer": LocationData(108, "Septemburg Wastewater Canal",
                                                Has("Fishing Rod")),

    # Check ID - Imported and guessed
    "SB Wastewater Canal Slime Room Chest": LocationData(106, "Septemburg Wastewater Canal Slime Room",
                                                         CanBurrow()),

    # Check ID - Imported and guessed
    "SB Wastewater Canal Pipe Room Chest": LocationData(105, "Septemburg Wastewater Canal Pipe Room",
                                                        CanBurrow()),

    # Check ID - Imported and guessed
    "SB Wastewater Canal Well Entrance Chest": LocationData(107, "Septemburg Wastewater Canal Well Entrance",
                                                            CanBurrow()),
}


bosses: dict[str, LocationData] = {
    # No ID available (N/A vanilla item)
    "SB Dark Deluxy": LocationData(0, "Septemburg Windy Generator",
                                   CanBurrow() & Has("Pipes")),
}