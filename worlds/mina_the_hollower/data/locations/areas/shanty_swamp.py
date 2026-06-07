from BaseClasses import LocationProgressType
from rule_builder.options import OptionFilter
from rule_builder.rules import Has, True_
from .. import LocationData
from ... import RegionConnectionData
from ...rules.ability_rules import CanBurrow, CanJumpOneTile, CanJumpTiles, CanBounce, CanSwim, CanCarry, CanClimb

collectable_locations: dict[str, LocationData] = {
     # "Lock" : LocationData(283, ""),
    # "Lock" : LocationData(284, ""),
    # "Lock" : LocationData(285, ""),
    "BW Pinky's Parlor Joule Box" : LocationData(286, "Backwaters Pinky's Parlor", CanCarry()),
    "BW Upper Backwaters Side Room Chest" : LocationData(287, "Upper Backwaters Side Room"),
    "BW Lower Shanty Swamp Bonestone Block" : LocationData(288, "Lower Backwaters", Has("Backwaters Bonestone Block kear")),
    "BW Gain Empty Jug" : LocationData(289, "Waterfall Backwaters"),
    "BW Upper Backwaters Plasma Jug" : LocationData(290, "Upper Backwaters"),
    "BW Lower Shanty Swamp Tumbling Tutu" : LocationData(291, "Lower Backwaters", CanCarry() & CanClimb()),
    "BW Lucky's Lair Kear" : LocationData(292, "Backwaters Lucky's Lair"),
    "BW Lower Shanty Swamp Bonestone" : LocationData(293, "Lower Backwaters", Has("Backwaters Bonestone Kear")),
    "BW Lower Shanty Swamp Evasion Powder" : LocationData(294, "Lower Backwaters", CanCarry() & (CanJumpTiles(distance=4) | (CanBurrow() & CanSwim))),
    "BW Lantern Cave Vial Pouch" : LocationData(295, "Backwaters Lantern Cave"),
    "BW Lantern Cave Bonestone" : LocationData(296, "Backwaters Lantern Cave"),
    "BW Pinky's Parlor Spark Catcher" : LocationData(297, "Backwaters Pinky's Parlor"),
    "BW Pinky's Parlor Kear" : LocationData(298, "Backwaters Pinky's Parlor"),
    "BW Fishing Hole Thalessian Pearl" : LocationData(299, "Backwaters Fishing Hole"),
    "BW Fishing Hole Fishing Rod" : LocationData(300, "Backwaters Fishing Hole"),
    "BW Fishing Hole Gilded Rod" : LocationData(301, "Backwaters Fishing Hole"),
    "Trigger Fish Boss" : LocationData(302, "Waterfall Backwaters"),
}

boss_locations: dict[str, LocationData] = {
    "Defeat Fish Boss": LocationData(0, "Waterfall Backwaters"),
}


connections: dict[str, RegionConnectionData] = {
    "Waterfall Backwaters_Western Wilds Occupied Bridge" : RegionConnectionData("Waterfall Backwaters", "Western Wilds Occupied Bridge", (CanSwim() | CanJumpTiles(distance=4)) & CanBurrow()),
    "Lower Backwaters_Ossex Train Staion" : RegionConnectionData("Lower Backwaters", "Ossex Train Staion", Has("BayouTicket")),
    "Lower Backwaters_Bayou Entrance": RegionConnectionData("Lower Backwaters", "Bayou Entrance", (CanSwim() | CanJumpTiles(distance=4)) & CanBurrow()),


    "Upper Backwaters_Waterfall Backwaters" : RegionConnectionData("Upper Backwaters","Waterfall Backwaters", (CanSwim() | CanJumpTiles(distance=4))),
    "Waterfall Backwaters_Upper Backwaters" : RegionConnectionData("Waterfall Backwaters","Upper Backwaters", (CanSwim() | CanJumpTiles(distance=4))),

    "Upper Backwaters_Upper Backwaters Side Room" : RegionConnectionData("Upper Backwaters","Upper Backwaters Side Room", CanSwim()),
    "Upper Backwaters Side Room_Upper Backwaters" : RegionConnectionData("Upper Backwaters Side Room","Upper Backwaters", CanSwim()),

    "Upper Backwaters_Backwaters Lantern Cave" : RegionConnectionData("Upper Backwaters","Backwaters Lantern Cave", CanSwim() & Has("Spark", 1) & Has("Backwaters Lantern Cave Kear")),
    "Backwaters Lantern Cave_Upper Backwaters" : RegionConnectionData("Backwaters Lantern Cave","Upper Backwaters", CanSwim() & Has("Spark", 1) & Has("Backwaters Lantern Cave Kear")),

    "Upper Backwaters_Lower Backwaters" : RegionConnectionData("Upper Backwaters","Lower Backwaters", CanSwim()),
    "Lower Backwaters_Upper Backwaters" : RegionConnectionData("Lower Backwaters","Upper Backwaters", CanSwim()),

    "Lower Backwaters_Backwaters Fishing Hole" : RegionConnectionData("Lower Backwaters","Backwaters Fishing Hole"),
    "Backwaters Fishing Hole_Lower Backwaters" : RegionConnectionData("Backwaters Fishing Hole","Lower Backwaters"),

    "Lower Backwaters_Backwaters Lucky's Lair" : RegionConnectionData("Lower Backwaters","Backwaters Lucky's Lair"),
    "Backwaters Lucky's Lair_Lower Backwaters" : RegionConnectionData("Backwaters Lucky's Lair","Lower Backwaters"),

    "Backwaters Pinky's Parlor_Upper Backwaters" : RegionConnectionData("Backwaters Pinky's Parlor","Upper Backwaters", Has("Pinky Parlor Kear")),
    "Upper Backwaters_Backwaters Pinky's Parlor" : RegionConnectionData("Upper Backwaters","Backwaters Pinky's Parlor", Has("Pinky Parlor Kear")),
}