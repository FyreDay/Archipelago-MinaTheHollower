from BaseClasses import LocationProgressType
from rule_builder.rules import Has, CanReachLocation
from .. import LocationData
from ... import RegionConnection, TransitionType, Transition
from ...rules.ability_rules import CanBurrow, CanJumpOneTile, CanBounce, CanJumpTiles, CanClimb, CanCarry

regions: set[str] = {
    "Queensbury Crypt Old Graveyard",
    "Queensbury Crypt Bonnet Tomb",
    "Queensbury Crypt Broken Bridge",
    "Queensbury Crypt Pipe Room",
    "Queensbury Crypt Castle Entry",
    "Queensbury Crypt Smelly Secret",
    "Queensbury Crypt Hidden Tunnel",
    "Queensbury Crypt Statue Head Hall",
    "Queensbury Crypt Mirror Room",
    "Queensbury Crypt Putrid Place",
    "Queensbury Crypt Rancid Room",
    "Queensbury Crypt Ancestral Chamber",
    "Queensbury Crypt Royal Tomb",
    "Queensbury Crypt Solemn Generator",
}

transitions: dict[str, Transition] = {

}

connections: dict[str, RegionConnection] = {
}

collectable_locations: dict[str, LocationData] = {
    # Check ID - Imported and guessed
    "QC Old Graveyard Bonestone": LocationData(51, "Queensbury Crypt Old Graveyard"),

    # Check ID - Imported and guessed
    "QC Old Graveyard Kear": LocationData(52, "Queensbury Crypt Old Graveyard",
                                          CanBurrow()),

    "QC Bonnet Tomb Desperation Bonnet": LocationData(57, "Queensbury Crypt Bonnet Tomb",
                                                      CanBurrow() & Has("QC Old Graveyard Kear")),

    # Check ID - Imported and guessed
    "QC Broken Bridge Bonestone": LocationData(53, "Queensbury Crypt Broken Bridge"),

    # Check ID - Imported and guessed
    "QC Pipe Room Bonestone": LocationData(54, "Queensbury Crypt Pipe Room"),

    # Check ID - Imported and guessed
    "QC Castle Entry Weapon Chest": LocationData(56, "Queensbury Crypt Castle Entry"),

    # Check ID - Imported and guessed
    "QC Smelly Secret Kear": LocationData(64, "Queensbury Crypt Smelly Secret"),

    # Check ID - Imported and guessed
    "QC Hidden Tunnel Bonestone": LocationData(61, "Queensbury Crypt Hidden Tunnel",
                                               CanBurrow()),

    # Check ID - Imported and guessed
    "QC Statue Head Hall Chest": LocationData(62, "Queensbury Crypt Statue Head Hall",
                                              CanBurrow() & CanCarry()),

    # Check ID - Imported and guessed
    "QC Mirror Room Chest": LocationData(63, "Queensbury Crypt Mirror Room",
                                         CanBurrow() & CanCarry()),

    "QC Mirror Room Stolenoid": LocationData(66, "Queensbury Crypt Mirror Room",
                                             CanBurrow() & CanCarry()),

    # Check ID - Imported and guessed
    "QC Mirror Room Kear": LocationData(67, "Queensbury Crypt Mirror Room",
                                        CanBurrow() & CanCarry()),

    # Check ID - Imported and guessed
    "QC Putrid Place Bonestone": LocationData(65, "Queensbury Crypt Putrid Place",
                                              CanBurrow() & CanCarry()),

    "QC Putrid Place Tombstone": LocationData(68, "Queensbury Crypt Putrid Place",
                                              CanBurrow() & CanCarry() & Has("Fishing Rod")),

    "QC Rancid Room Fly Bait": LocationData(59, "Queensbury Crypt Rancid Room",
                                            CanBurrow() & CanCarry() & Has("Vials", count=2)),



    "QC Ancestral Chamber Health Rose": LocationData(58, "Queensbury Crypt Ancestral Chamber",
                                                     CanBurrow() & CanCarry()),



    "QC Royal Tomb Proto Spark": LocationData(60, "Queensbury Crypt Royal Tomb",
                                              CanBurrow() & CanCarry() & CanClimb() &
                                              Has("Vials", count=2)),


}
bosses: dict[str, LocationData] = {
# No ID available (N/A vanilla item)
"QC Rancid Room Midden": LocationData(0, "Queensbury Crypt Rancid Room",
                                      CanBurrow() & CanCarry() & Has("Vials", count=2)),
    # No ID available (N/A vanilla item)
    "QC Ancestral Chamber The Duchess": LocationData(0, "Queensbury Crypt Ancestral Chamber",
                                                     CanBurrow() & CanCarry()),
    # No ID available (N/A vanilla item)
    "QC Solemn Generator Activated": LocationData(0, "Queensbury Crypt Solemn Generator",
                                                  CanBurrow() & CanCarry()),
}