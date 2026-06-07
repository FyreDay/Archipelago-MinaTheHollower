from BaseClasses import LocationProgressType
from rule_builder.rules import Has, CanReachLocation
from .. import LocationData
from ... import RegionConnection, TransitionType, Transition
from ...rules.ability_rules import CanBurrow, CanJumpOneTile, CanBounce, CanJumpTiles, CanClimb, CanCarry

collectable_locations: dict[str, LocationData] = {
    "Left Shipwreck Weapon": LocationData(17, "ShipWreck", Has("Left Shipwreck Weapon Kear")),
    "Right Shipwreck Weapon": LocationData(18, "ShipWreck", Has("Right Shipwreck Weapon Kear")),
    # "Loners Landing_o_1011": LocationData(19, "Loners Landing"), lock
    # "Loners Landing_o_1453": LocationData(20, "Loners Landing"),lock
    # "Loners Landing_o_14532": LocationData(21, "Loners Landing"),lock
    # "Loners Landing_o_14531": LocationData(22, "Loners Landing"),lock
"LL Residence Bubble": LocationData(23, "Loners Landing"),
"Shipwreck Cappy Chat": LocationData(24, "Loners Landing"),
"LL Defeat Kraken": LocationData(25, "Loners Landing", progress_type=LocationProgressType.EXCLUDED), # maybe seed a lot of Bonestone in here in defeat
"LL Knight Room Chest": LocationData(26, "LL Lower Bridge", CanClimb() & CanBurrow()),
"LL Boardwalk Fire Bounce Chest": LocationData(27, "LL Boardwalk", CanBounce()),
"LL Fences Side Cave Chest": LocationData(28, "LL Fences"),
    "LL Blighted Docks Tall Room Chest": LocationData(29, "LL Bridge"),
    "LL Boardwalk Sandfalls Ledge Chest": LocationData(30, "LL Boardwalk", CanBounce()),
"LL Bridge Cliff Chest": LocationData(31, "LL Bridge"),
    "LL Shipwreck Beach" : LocationData(32,"Loners Landing"),
"Bone Beach Outlook Chest": LocationData(324,"LL Boardwalk", CanBounce()),
}

regions: set[str] = {
"LL Shipwreck",
"LL Blighted Docks Tall Room",
"LL Blighted Docks Side Cave",
"LL Blighted Docks Bridge",
"LL Blighted Docks Residence",
"LL Blighted Docks Burrow",
"LL Boardwalk Fire Bounce",
"LL Boardwalk Sandfalls Ledge",
"LL Shipwreck Beach",
"LL Belowdecks",
"LL Boardwalk Fence Room",
}

connections: dict[str, RegionConnection] = {
    "LL Boardwalk_Southern Outskirts" : RegionConnection("LL Boardwalk", "Southern Outskirts", CanJumpTiles(distance=2)),

    "Loners Landing_Shipwreck" : RegionConnection("Loners Landing", "ShipWreck", CanReachLocation("Thorne 1", parent_region_name="mansion"), EntranceType.DOORS),
    "Shipwreck_Loners Landing" : RegionConnection("ShipWreck", "Loners Landing", entrance_group=EntranceType.DOORS),

    "LL Fences_Loners Landing" : RegionConnection("LL Fences", "Loners Landing", CanJumpOneTile() & CanBurrow()),
    "Loners Landing_LL Fences" : RegionConnection("Loners Landing", "LL Fences", CanJumpOneTile() & CanBurrow() & CanCarry()),

    "LL Bridge_LL Lower Bridge" : RegionConnection("LL Bridge", "LL Lower Bridge", CanClimb()),
    "LL Lower Bridge_LL Bridge" : RegionConnection("LL Lower Bridge", "LL Bridge", CanClimb()),

    "LL Residence Road_LL Lower Bridge" : RegionConnection("LL Residence Road", "LL Lower Bridge", CanJumpTiles(distance=1)),

    "LL Lower Bridge_LL Fences" : RegionConnection("LL Lower Bridge", "LL Fences", CanJumpOneTile() & CanBurrow()),
    "LL Fences_LL Lower Bridge" : RegionConnection("LL Fences", "LL Lower Bridge", CanJumpOneTile() & CanBurrow()),

    "LL Bridge_LL Residence Road" : RegionConnection("LL Bridge", "LL Residence Road", CanBounce() & CanClimb() & CanJumpOneTile),

    "LL Residence_LL Residence Road" : RegionConnection("LL Residence", "LL Residence Road", CanBurrow()),
    "LL Residence Road_LL Residence" : RegionConnection("LL Residence Road", "LL Residence", CanBurrow()),

    "LL Boardwalk_LL Residence Road" : RegionConnection("LL Boardwalk", "LL Residence Road", CanJumpTiles(distance=2) & Has("LL Boardwalk Kear")),
    "LL Residence Road_LL Boardwalk" : RegionConnection("LL Residence Road", "LL Boardwalk", CanJumpTiles(distance=2) & Has("LL Boardwalk Kear")),
}

transitions: dict[str, Transition] = {

}

