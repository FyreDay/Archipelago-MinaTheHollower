from rule_builder.rules import Has
from .. import RegionConnectionData
from ..rules import CanJumpOneTile, CanJumpSevenTiles

connections: dict[str, RegionConnectionData] = {
    "Shipwreck_burrow" : RegionConnectionData("Shipwreck","Blighted Docks 3", Has("Burrow")),
    "Blighted Docks 3 Jump" : RegionConnectionData("Blighted Docks 3","Blighted Docks 4", CanJumpOneTile()),
    "Blighted Docks 4 Jump" : RegionConnectionData("Blighted Docks 4","Blighted Docks 6 Residence", CanJumpSevenTiles() & Has("Burrow"))
}