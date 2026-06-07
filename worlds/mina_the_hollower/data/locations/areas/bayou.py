from BaseClasses import LocationProgressType
from rule_builder.options import OptionFilter
from rule_builder.rules import Has, True_
from .. import LocationData
from ... import RegionConnection, Transition
from ...rules.ability_rules import CanBurrow, CanJumpOneTile, CanJumpTiles, CanBounce, CanSwim, CanCarry, CanClimb

regions: set[str] = {
    "Nox's Bayou Boat Takeoff",
    "Nox's Bayou Guard Room",
    "Nox's Bayou First Flooder",
    "Nox's Bayou Shallow Pool",
    "Nox's Bayou Lagoon Burrow",
    "Nox's Bayou Submerged Side Room",
    "Nox's Bayou Swamp Shack",
    "Nox's Bayou Moonlit Path",
    "Nox's Bayou Moonlit Mosh",
    "Nox's Bayou Moonlit Hideaway",
    "Nox's Bayou Plant Passage",
    "Nox's Bayou Twin Thicket",
    "Nox's Bayou Hidden Cave",
    "Nox's Bayou Grate Lake",
    "Nox's Bayou Tainted Depths",
    "Nox's Bayou Swampy Generator",
    "Nox's Bayou Gutter Pipe",
}

transitions: dict[str, Transition] = {

}

connections: dict[str, RegionConnection] = {
}

collectable_locations: dict[str, LocationData] = {
    "NB Boat Takeoff Shrimpter Tail": LocationData(50, "Nox's Bayou Boat Takeoff",
                                                   Has("Fishing Rod") & CanBurrow() & CanSwim()),

    "NB Guard Room Twill Weave": LocationData(47, "Nox's Bayou Guard Room",
                                              CanBurrow() & CanSwim() & CanClimb()),

    # Check ID - Imported and guessed
    "NB First Flooder Chest": LocationData(35, "Nox's Bayou First Flooder",
                                           CanBurrow() & CanSwim()),

    # Check ID - Imported and guessed
    "NB Shallow Pool Chest": LocationData(36, "Nox's Bayou Shallow Pool",
                                          CanBurrow() & CanSwim()),

    # Check ID - Imported and guessed
    "NB Lagoon Burrow Chest": LocationData(42, "Nox's Bayou Lagoon Burrow",
                                           CanBurrow() & CanSwim()),

    "NB Submerged Side Room Vascular Syrup": LocationData(40, "Nox's Bayou Submerged Side Room",
                                                          CanBurrow() & CanSwim()),

    "NB Swamp Shack Pit Preserver": LocationData(48, "Nox's Bayou Swamp Shack",
                                                 CanBurrow() & CanSwim()),

    # Check ID - Imported and guessed
    "NB Swamp Shack Kear": LocationData(44, "Nox's Bayou Swamp Shack",
                                        CanBurrow() & CanSwim()),

    # Check ID - Imported and guessed
    "NB Swamp Shack Blastrike Maul": LocationData(45, "Nox's Bayou Swamp Shack",
                                                  CanBurrow() & CanSwim()),

    # Check ID - Imported and guessed
    "NB Moonlit Path Chest": LocationData(38, "Nox's Bayou Moonlit Path",
                                          CanBurrow() & CanSwim()),

    # No ID available (N/A vanilla item)
    "NB Moonlit Mosh Mock Moon": LocationData(0, "Nox's Bayou Moonlit Mosh",
                                              CanBurrow() & CanSwim()),

    "NB Moonlit Hideaway Iron Lung": LocationData(37, "Nox's Bayou Moonlit Hideaway",
                                                  CanBurrow() & CanSwim()),

    # Check ID - Imported and guessed
    "NB Plant Passage Chest": LocationData(39, "Nox's Bayou Plant Passage",
                                           CanBurrow() & CanSwim()),

    # Check ID - Imported and guessed
    "NB Twin Thicket Chest": LocationData(43, "Nox's Bayou Twin Thicket",
                                          CanBurrow() & CanSwim()),

    # Check ID - Imported and guessed
    "NB Hidden Cave Chest": LocationData(49, "Nox's Bayou Hidden Cave",
                                         CanBurrow() & CanSwim()),

    # Check ID - Imported and guessed
    "NB Grate Lake Chest": LocationData(41, "Nox's Bayou Grate Lake",
                                        CanBurrow() & CanSwim() & CanClimb()),

    "NB Tainted Depths Health Rose": LocationData(34, "Nox's Bayou Tainted Depths",
                                                  CanBurrow() & CanSwim() & CanClimb()),



    # Check ID - Imported and guessed
    "NB Gutter Pipe Chest": LocationData(46, "Nox's Bayou Gutter Pipe",
                                         CanBurrow() & CanBounce() & CanClimb()),
}


bosses: dict[str, LocationData] = {
    # No ID available (N/A vanilla item)
    "NB Tainted Depths Nox's Beast": LocationData(0, "Nox's Bayou Tainted Depths",
                                                  CanBurrow() & CanSwim() & CanClimb()),

    # No ID available (N/A vanilla item)
    "NB Swampy Generator Activated": LocationData(0, "Nox's Bayou Swampy Generator",
                                                  CanBurrow() & CanSwim() & CanClimb()),
}