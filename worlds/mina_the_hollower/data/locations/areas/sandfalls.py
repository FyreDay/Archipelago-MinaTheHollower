from BaseClasses import LocationProgressType
from rule_builder.rules import Has, CanReachLocation
from .. import LocationData
from ... import RegionConnection, TransitionType, Transition
from ...rules.ability_rules import CanBurrow, CanJumpOneTile, CanBounce, CanJumpTiles, CanClimb, CanCarry

regions: set[str] = {
    "Sandfalls Hobo Holdout",
    "Sandfalls Sifted Sands",
    "Sandfalls Guiding Grains",
    "Sandfalls Hidden Cave",
    "Sandfalls Ring Dive Parlor",
    "Sandfalls Shifty Seclusion",
    "Sandfalls Payload Passage",
    "Sandfalls Miner's Den",
    "Sandfalls Shoreline Generator",
    "Sandfalls Bone Junction",
    "Sandfalls Train",
}

transitions: dict[str, Transition] = {

}

connections: dict[str, RegionConnection] = {
}

collectable_locations: dict[str, LocationData] = {
    "SF Hobo Holdout Puffer Beak": LocationData(82, "Sandfalls Hobo Holdout",
                                                Has("Vials", count=2) & CanBurrow() & CanBounce() & Has("Fishing Rod")),

    # Check ID - Imported and guessed
    "SF Sifted Sands Snake Bomb Chest": LocationData(324, "Sandfalls Sifted Sands",
                                                     CanBurrow() & CanCarry()),

    # Check ID - Imported and guessed
    "SF Sifted Sands Kear": LocationData(319, "Sandfalls Sifted Sands"),

    # Check ID - Imported and guessed
    "SF Guiding Grains Niter Belt": LocationData(330, "Sandfalls Guiding Grains",
                                                 Has("SF Sifted Sands Kear")),

    # Check ID - Imported and guessed
    "SF Guiding Grains Bonestone #1": LocationData(328, "Sandfalls Guiding Grains",
                                                   Has("SF Sifted Sands Kear")),

    # Check ID - Imported and guessed
    "SF Guiding Grains Bonestone #2": LocationData(329, "Sandfalls Guiding Grains",
                                                   Has("SF Sifted Sands Kear")),

    # Check ID - Imported and guessed
    "SF Hidden Cave Vial Pouch": LocationData(323, "Sandfalls Hidden Cave",
                                              CanBurrow() & Has("SF Sifted Sands Kear")),

    "SF Ring Dive Parlor Tunneler's Codex": LocationData(317, "Sandfalls Ring Dive Parlor",
                                                         CanBurrow()),

    # Check ID - Imported and guessed
    "SF Shifty Seclusion Chest": LocationData(322, "Sandfalls Shifty Seclusion",
                                              CanBurrow() & CanCarry()),

    # Check ID - Imported and guessed
    "SF Payload Passage Chest": LocationData(328, "Sandfalls Payload Passage",
                                             CanBurrow() & CanCarry()),

    # Special rules - expression contains custom logic, double check
    "SF Miner's Den Major Miner": LocationData(0, "Sandfalls Miner's Den",
                                               Has("Vials", count=3) & CanBurrow() &
                                               (Has("Spike Spurs") | Has("Carry/Throw"))),

    # No ID available (N/A vanilla item)
    "SF Shoreline Generator Activated": LocationData(0, "Sandfalls Shoreline Generator",
                                                     CanBurrow()),

    # Check ID - Imported and guessed
    "SF Bone Junction Chest": LocationData(329, "Sandfalls Bone Junction",
                                           CanBurrow() & CanCarry()),

    # Check ID - Imported and guessed
    "SF Train Vita's Shop": LocationData(327, "Sandfalls Train",
                                         CanBurrow()),
}

bosses: dict[str, LocationData] = {
}

