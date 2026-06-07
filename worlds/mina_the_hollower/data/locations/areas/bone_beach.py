from BaseClasses import LocationProgressType
from rule_builder.rules import Has, CanReachLocation
from .. import LocationData
from ... import RegionConnection, TransitionType, Transition
from ...rules.ability_rules import CanBurrow, CanJumpOneTile, CanBounce, CanJumpTiles, CanClimb, CanCarry, CanSwim

regions: set[str] = {
}

transitions: dict[str, Transition] = {

}

connections: dict[str, RegionConnection] = {
}

collectable_locations: dict[str, LocationData] = {
    # Check ID - Imported and guessed
    "BB Sandwater Junction Goremaw Fang": LocationData(88, "Bone Beach Sandwater Junction",
                                                       CanBurrow() & CanCarry() & CanClimb() &
                                                       Has("Fishing Rod") & CanJumpTiles(distance=5)),

    # Check ID - Imported and guessed
    "BB Sandwater Junction Angler's Raft": LocationData(79, "Bone Beach Sandwater Junction",
                                                        CanBurrow() & CanCarry() & CanClimb() &
                                                        CanJumpTiles(distance=5)),

    # Check ID - Imported and guessed
    "BB Bone Rush Trail Furgus Tunnel Chest": LocationData(70, "Bone Beach Bone Rush Trail",
                                                           CanBurrow() & CanCarry() & Has("Vials", count=3)),

    # Special rules - Can leave through BB Mirror instead of vials and CanBounce()
    "BB Gold Grasp Bonestone": LocationData(71, "Bone Beach Gold Grasp",
                                            (CanBurrow() & CanCarry() & Has("Vials", count=3))),

    # Special rules - Can leave through BB Mirror instead of vials
    "BB Large Conveyor Bonestone": LocationData(72, "Bone Beach Large Conveyor",
                                                Has("Vials", count=3) &
                                                CanBounce() & CanClimb()),


    # Check ID - Imported and guessed
    "BB Split Room Chest": LocationData(73, "Bone Beach Split Room",
                                        CanJumpTiles(distance=2)),

    # Special rules - Float OR Tunneler's Codex
    # Check ID - Imported and guessed
    "BB Aquatic Conveyor Chest": LocationData(78, "Bone Beach Aquatic Conveyor",
                                              CanBurrow() & CanSwim() &
                                              (CanBounce() | Has("Tunneler's Codex"))),

    "BB Brac's Tent Polyp Lamp": LocationData(80, "Bone Beach Brac's Tent"),

    # Check ID - Imported and guessed
    "BB Brac's Tent Kear": LocationData(81, "Bone Beach Brac's Tent"),

    # Check ID - Imported and guessed
    "BB Secret Shoals Joule Syringe": LocationData(74, "Bone Beach Secret Shoals",
                                                   CanBurrow() & CanSwim()),

    # Check ID - Imported and guessed
    "BB Calcified Caverns Kear": LocationData(79, "Bone Beach Calcified Caverns",
                                              CanClimb()),

    # Check ID - Imported and guessed
    "BB Calcified Cage Bonestone": LocationData(84, "Bone Beach Calcified Cage",
                                                CanClimb() & CanBurrow()),

    # Check ID - Imported and guessed
    "BB Submerged Handles Chest": LocationData(85, "Bone Beach Submerged Handles",
                                               CanBurrow() & CanSwim() & CanBounce()),

    # Check ID - Imported and guessed
    "BB Pulsing Tract Bonestone": LocationData(76, "Bone Beach Pulsing Tract",
                                               CanBurrow() & CanBounce()),

    "BB Worm's Back Battery Buster": LocationData(75, "Bone Beach Worm's Back",
                                                  CanBounce()),

    # Check ID - Imported and guessed
    "BB Worm's Spine Bonestone": LocationData(77, "Bone Beach Worm's Spine",
                                              CanBurrow()),

    # Check ID - Imported and guessed
    "BB Stomach Mine Kear": LocationData(83, "Bone Beach Stomach Mine",
                                         CanBurrow() & CanBounce()),

    # Check ID - Imported and guessed
    "BB Moving Stairs Bonestone": LocationData(85, "Bone Beach Moving Stairs",
                                               CanBurrow() & CanBounce()),

    # Check ID - Imported and guessed
    "BB Gut Passage Chest": LocationData(86, "Bone Beach Gut Passage",
                                         CanBurrow()),

    # Check ID - Imported and guessed
    "BB Brain Alcove Health Rose": LocationData(83, "Bone Beach Brain Alcove",
                                                CanBurrow()),
}


bosses: dict[str, LocationData] = {
    "BB Brain Alcove Mined Mind": LocationData(0, "Bone Beach Brain Alcove",
                                               CanBurrow()),
}