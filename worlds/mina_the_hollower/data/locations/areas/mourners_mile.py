from BaseClasses import LocationProgressType
from rule_builder.rules import Has, CanReachLocation
from .. import LocationData
from ... import RegionConnection, TransitionType, Transition
from ...rules.ability_rules import CanBurrow, CanJumpOneTile, CanBounce, CanJumpTiles, CanClimb, CanCarry

regions: set[str] = {
    "Mourner's Mile Knight's Rest",
    "Mourner's Mile Statue Room",
    "Mourner's Mile Shallow Tomb",
    "Mourner's Mile Ring Tomb",
    "Mourner's Mile Spike Vault",
    "Mourner's Mile Spike Vault Hidden Room",
    "Mourner's Mile Tower Tunnel",
    "Mourner's Mile Knight's Stand",
    "Mourner's Mile Mina's Grave",
    "Mourner's Mile Spike Hell",
}

transitions: dict[str, Transition] = {

}

connections: dict[str, RegionConnection] = {
}

collectable_locations: dict[str, LocationData] = {
    # Check ID - Imported and guessed
    "MM Knight's Rest Chest": LocationData(313, "Mourner's Mile Knight's Rest",
                                           CanJumpTiles(distance=3)),

    # Check ID - Imported and guessed
    "MM Statue Room Bonestone": LocationData(314, "Mourner's Mile Statue Room",
                                             CanBurrow()),

    # Check ID - Imported and guessed
    "MM Shallow Tomb Kear": LocationData(305, "Mourner's Mile Shallow Tomb",
                                         CanBurrow()),

    # Check ID - Imported and guessed
    "MM Ring Tomb Spike Spurs": LocationData(316, "Mourner's Mile Ring Tomb",
                                             CanBurrow()),

    # Check ID - Imported and guessed
    "MM Spike Vault Vial Pouch": LocationData(312, "Mourner's Mile Spike Vault",
                                              CanBurrow()),

    # Check ID - Imported and guessed
    "MM Spike Vault Hidden Room Kear": LocationData(310, "Mourner's Mile Spike Vault Hidden Room",
                                                    CanBurrow()),

    # Check ID - Imported and guessed
    "MM Tower Tunnel Chest #1": LocationData(313, "Mourner's Mile Tower Tunnel",
                                             CanBurrow()),

    # Check ID - Imported and guessed
    "MM Tower Tunnel Chest #2": LocationData(314, "Mourner's Mile Tower Tunnel",
                                             CanBurrow()),

    # Check ID - Imported and guessed
    "MM Knight's Stand Bonestone": LocationData(315, "Mourner's Mile Knight's Stand",
                                                CanBurrow() & CanCarry()),

    # Check ID - Imported and guessed
    "MM Mina's Grave Chest": LocationData(303, "Mourner's Mile Mina's Grave",
                                          Has("Sparks", 3)),

    # Check ID - Imported and guessed
    "MM Mina's Grave Starving Beastium": LocationData(308, "Mourner's Mile Mina's Grave",
                                                      Has("Sparks", count=3)),
    # Check ID - Imported and guessed
    "MM Spike Hell Chest": LocationData(355, "Mourner's Mile Spike Hell",
                                        CanJumpTiles(distance=7) | Has("Spike Spurs")),
}


