from rule_builder.rules import Has, True_

from ... import RegionConnection, Transition, DirectionType, TransitionType, LocationData
from ...rules.ability_rules import CanBurrow, CanJumpOneTile, CanJumpTiles, CanBounce, HasVialsCount, CanClimb, \
    ReachingSideArm

regions: set[str] = {
    "Ossex City Center Main",
    "Ossex City Center Upper",
    "Ossex City Center Bike",
    "Ossex Courtyard",
    "Ossex Courtyard West",
    "Ossex Courtyard East",
    "Ossex Couple's Quarter",
    "Ossex Legovich's Arms",
    "Ossex Emporium",
    "Ossex Kear Institute",
    "Ossex Guild Hall",
    "Ossex Guild Back Room",
    "Ossex Guild Secret Room",
    "Ossex Residence",
    "Ossex Gutterways",
    "Ossex Trinket Bazaar",
    "Ossex Bowery Main",
    "Ossex Bowery Upper",
    "Ossex Bowery Begger Residence",
    "Ossex Bowery Begger Residence Back",
    "Ossex Western Wall",
    "Ossex South Western Wall",
    "Ossex Entry Western Wall Left",
    "Ossex Entry Western Wall Right",
    "Ossex Station",
    "Ossex Station Underside Main",
    "Ossex Station Underside Upper",
    "Ossex Music Hall",
    "Ossex Bowery Residence",
    "Ossex Bowery Residence Upper Main",
    "Ossex Bowery Residence Upper Top Entrance",
    "Ossex Bowery Residence Storage",
    "Ossex High Street Main",
    "Ossex High Street Balcony",
    "Ossex High Street SE Garden",
    "Ossex High Street Residence",
    "Ossex High Street Residence Upper Main",
    "Ossex High Street Residence Upper Puzzle",
    "Ossex High Street Sewer",
    "Ossex Balcony East",
    "Ossex Balcony West",
    "Ossex High Street Residence Balcony East",
    "Ossex High Street Residence Balcony West",
    "Ossex Strategy Center",
    "Ossex Atelier",
}

transitions: dict[str, Transition] = {
    # --- Ossex City Center Main ---
    "Ossex City Center Main North": Transition("Ossex City Center Main North", "Ossex City Center Main",
                                               "Ossex Courtyard", DirectionType.NORTH, TransitionType.SCREENS),
    "Ossex City Center Main Door North Couples": Transition("Ossex City Center Main Door North Couples",
                                                            "Ossex City Center Main", "Ossex Couple's Quarter",
                                                            DirectionType.NORTH, TransitionType.DOORS),
    "Ossex City Center Main Door North Legovich": Transition("Ossex City Center Main Door North Legovich",
                                                             "Ossex City Center Main", "Ossex Legovich's Arms",
                                                             DirectionType.NORTH, TransitionType.DOORS),
    "Ossex City Center Main Door North Emporium": Transition("Ossex City Center Main Door North Emporium",
                                                             "Ossex City Center Main", "Ossex Emporium",
                                                             DirectionType.NORTH, TransitionType.DOORS),
    "Ossex City Center Main Door North Kear": Transition("Ossex City Center Main Door North Kear",
                                                         "Ossex City Center Main", "Ossex Kear Institute",
                                                         DirectionType.NORTH, TransitionType.DOORS),
    "Ossex Guild Hall Door": Transition("Ossex Guild Hall Door",
                                                             "Ossex City Center Main", "Ossex Guild Hall",
                                                             DirectionType.NORTH, TransitionType.DOORS),
    "Ossex City Center Main To Bowery": Transition("Ossex City Center Main To Bowery", "Ossex City Center Main",
                                                   "Ossex Bowery Main", DirectionType.NORTH,
                                                   TransitionType.DO_NOT_RANDOMIZE_ENTRANCE),  # NOT RANDOMIZED
    "Ossex City Center Main Door North Residence": Transition("Ossex City Center Main Door North Residence",
                                                              "Ossex City Center Main", "Ossex Residence",
                                                              DirectionType.NORTH, TransitionType.DOORS,
                                                              Has("SparkUpgrade", count=2)),

    "Ossex City Center Main To High Street": Transition("Ossex City Center Main To High Street",
                                                        "Ossex City Center Main", "Ossex High Street Main",
                                                        DirectionType.NORTH, TransitionType.DO_NOT_RANDOMIZE_ENTRANCE),
    # NOT RANDOMIZED
    "Ossex City Center Main Area South": Transition("Ossex City Center Main Area South", "Ossex City Center Main",
                                                    "Southern Outskirts Commons Ossex Entry", DirectionType.SOUTH,
                                                    TransitionType.AREA_SCREENS),

    # --- Ossex City Center Upper ---
    "Ossex City Center Upper To Main": Transition("Ossex City Center Upper To Main", "Ossex City Center Upper",
                                                  "Ossex City Center Main", DirectionType.SOUTH, TransitionType.SCREENS,
                                                  CanBurrow()),  # Upper->Main requires Burrow per sheet
    "Ossex City Center Upper West Bowery": Transition("Ossex City Center Upper West Bowery", "Ossex City Center Upper",
                                                      "Ossex Bowery Upper", DirectionType.WEST, TransitionType.SCREENS),
    "Ossex City Center Upper Door North Trinket": Transition("Ossex City Center Upper Door North Trinket",
                                                             "Ossex City Center Upper", "Ossex Trinket Bazaar",
                                                             DirectionType.NORTH, TransitionType.DOORS),

    # --- Ossex City Center Bike ---
    "Ossex City Center Bike Geyser Drop": Transition("Ossex City Center Bike Geyser Drop", "Ossex City Center Bike",
                                                     "Ossex Gutterways", DirectionType.SOUTH, TransitionType.GEYSER_DOWN,
                                                     CanBurrow()),
    "Ossex City Center Bike To Main": Transition("Ossex City Center Bike To Main", "Ossex City Center Bike",
                                                 "Ossex City Center Main", DirectionType.SOUTH, TransitionType.SCREENS),
    "Ossex City Center Bike South Residence": Transition("Ossex City Center Bike South Residence",
                                                         "Ossex City Center Bike", "Ossex Residence",
                                                         DirectionType.SOUTH, TransitionType.SCREENS, CanBurrow()),

    # --- Ossex Courtyard ---
    "Ossex Courtyard Upper West": Transition("Ossex Courtyard Upper West", "Ossex Courtyard", "Ossex Courtyard West",
                                             DirectionType.WEST, TransitionType.SCREENS),

    "Ossex Courtyard Upper East": Transition("Ossex Courtyard Upper East", "Ossex Courtyard", "Ossex Courtyard East",
                                             DirectionType.EAST, TransitionType.SCREENS),

    # --- Ossex Courtyard West ---
    "Ossex Courtyard West Upper East": Transition("Ossex Courtyard West Upper East", "Ossex Courtyard West",
                                                  "Ossex Courtyard", DirectionType.EAST, TransitionType.SCREENS),

    # --- Ossex Courtyard East ---
    "Ossex Courtyard East Upper West": Transition("Ossex Courtyard East Upper West", "Ossex Courtyard East",
                                                  "Ossex Courtyard", DirectionType.WEST, TransitionType.SCREENS),

    # --- Ossex Couple's Quarter ---
    "Ossex Couples Quarter Door South": Transition("Ossex Couples Quarter Door South", "Ossex Couple's Quarter",
                                                   "Ossex City Center Main", DirectionType.SOUTH, TransitionType.DOORS),

    # --- Ossex Legovich's Arms ---
    "Ossex Legovichs Arms Door South": Transition("Ossex Legovichs Arms Door South", "Ossex Legovich's Arms",
                                                  "Ossex City Center Main", DirectionType.SOUTH, TransitionType.DOORS),

    # --- Ossex Emporium ---
    "Ossex Emporium Door South": Transition("Ossex Emporium Door South", "Ossex Emporium", "Ossex City Center Main",
                                            DirectionType.SOUTH, TransitionType.DOORS),

    # --- Ossex Kear Institute ---
    "Ossex Kear Institute Door South": Transition("Ossex Kear Institute Door South", "Ossex Kear Institute",
                                                  "Ossex City Center Main", DirectionType.SOUTH, TransitionType.DOORS),

    # --- Ossex Guild Hall ---
    "Ossex Guild Hall Door South": Transition("Ossex Guild Hall Door South", "Ossex Guild Hall",
                                              "Ossex City Center Main", DirectionType.SOUTH, TransitionType.DOORS),
    "Ossex Guild Hall North": Transition("Ossex Guild Hall North", "Ossex Guild Hall", "Ossex Guild Back Room",
                                         DirectionType.NORTH, TransitionType.BURROW),

    # --- Ossex Guild Back Room ---
    "Ossex Guild Back Room South To Back": Transition("Ossex Guild Back Room North To Secret", "Ossex Guild Back Room",
                                                      "Ossex Guild Secret Room", DirectionType.NORTH,
                                                      TransitionType.SCREENS, HasVialsCount(count=1) & Has("Ossex Guild Secret Kear")),

    "Ossex Guild Back Room South To Hall": Transition("Ossex Guild Back Room South To Hall", "Ossex Guild Back Room",
                                                      "Ossex Guild Hall", DirectionType.SOUTH, TransitionType.BURROW,
                                                      CanBurrow()),
    # --- Ossex Guild Secret Room ---
    "Ossex Guild Secret Room South To Back": Transition("Ossex Guild Back Secret South To Back", "Ossex Guild Secret Room",
                                                      "Ossex Guild Back Room", DirectionType.SOUTH,
                                                      TransitionType.SCREENS, HasVialsCount(count=1) & Has("Ossex Guild Secret Kear")),

    # --- Ossex Residence ---
    "Ossex Residence Door South": Transition("Ossex Residence Door South", "Ossex Residence", "Ossex City Center Main",
                                             DirectionType.SOUTH, TransitionType.DOORS),
    "Ossex Residence North Bike": Transition("Ossex Residence North Bike", "Ossex Residence", "Ossex City Center Bike",
                                             DirectionType.NORTH, TransitionType.SCREENS, CanBurrow()),

    # --- Ossex Gutterways ---
    "Ossex Gutterways Geyser Bike": Transition("Ossex Gutterways Geyser Bike", "Ossex Gutterways",
                                               "Ossex City Center Bike", DirectionType.NORTH, TransitionType.GEYSER_UP,
                                               CanBurrow()),  # GEYSER not in enum # noqa: custom type GEYSER

    # --- Ossex Trinket Bazaar ---
    "Ossex Trinket Bazaar Door South": Transition("Ossex Trinket Bazaar Door South", "Ossex Trinket Bazaar",
                                                  "Ossex City Center Upper", DirectionType.SOUTH, TransitionType.DOORS),

    # --- Ossex Bowery Main ---
    "Ossex Bowery Main NR City Center": Transition("Ossex Bowery Main NR City Center", "Ossex Bowery Main",
                                                   "Ossex City Center Main", DirectionType.SOUTH,
                                                   TransitionType.DO_NOT_RANDOMIZE_ENTRANCE),  # NOT RANDOMIZED
    "Ossex Bowery Main Door North Station Underside": Transition("Ossex Bowery Main Door North Station Underside",
                                                                 "Ossex Bowery Main", "Ossex Station Underside Main",
                                                                 DirectionType.NORTH, TransitionType.DOORS),
    "Ossex Bowery Main Door North Residence": Transition("Ossex Bowery Main Door North Residence", "Ossex Bowery Main",
                                                         "Ossex Bowery Residence", DirectionType.NORTH,
                                                         TransitionType.DOORS),
    "Ossex Bowery Main Door North Music Hall": Transition("Ossex Bowery Main Door North Music Hall",
                                                          "Ossex Bowery Main", "Ossex Music Hall", DirectionType.NORTH,
                                                          TransitionType.DOORS),

    # --- Ossex Bowery Upper ---
    "Ossex Bowery Upper Stair North Residence Top": Transition("Ossex Bowery Upper Stair North Residence Top",
                                                               "Ossex Bowery Upper",
                                                               "Ossex Bowery Residence Upper Top Entrance",
                                                               DirectionType.NORTH, TransitionType.STAIRS),
    "Ossex Bowery Upper East City Center": Transition("Ossex Bowery Upper East City Center", "Ossex Bowery Upper",
                                                      "Ossex City Center Upper", DirectionType.EAST,
                                                      TransitionType.SCREENS),
    "Ossex Bowery Upper Door North Begger": Transition("Ossex Bowery Upper Door North Begger", "Ossex Bowery Upper",
                                                       "Ossex Bowery Begger Residence", DirectionType.NORTH,
                                                       TransitionType.DOORS),
    "Ossex Bowery Upper Door North Station": Transition("Ossex Bowery Upper Door North Station", "Ossex Bowery Upper",
                                                        "Ossex Station", DirectionType.NORTH, TransitionType.DOORS),

    # --- Ossex Bowery Begger Residence ---
    "Ossex Bowery Begger Residence Door South": Transition("Ossex Bowery Begger Residence Door South",
                                                           "Ossex Bowery Begger Residence", "Ossex Bowery Upper",
                                                           DirectionType.SOUTH, TransitionType.DOORS),
    "Ossex Bowery Begger Residence Burrow North": Transition("Ossex Bowery Begger Residence Burrow North",
                                                             "Ossex Bowery Begger Residence",
                                                             "Ossex Bowery Begger Residence Back", DirectionType.NORTH,
                                                             TransitionType.BURROW),

    # --- Ossex Bowery Begger Residence Back ---
    "Ossex Bowery Begger Residence Back Burrow South Residence": Transition(
        "Ossex Bowery Begger Residence Back Burrow South Residence", "Ossex Bowery Begger Residence Back",
        "Ossex Bowery Begger Residence", DirectionType.SOUTH, TransitionType.BURROW),  # noqa: custom type BURROW
    "Ossex Bowery Begger Residence Back Burrow South West Wall": Transition(
        "Ossex Bowery Begger Residence Back Burrow South West Wall", "Ossex Bowery Begger Residence Back",
        "Ossex Western Wall", DirectionType.SOUTH, TransitionType.BURROW),  # noqa: custom type BURROW

    # --- Ossex Western Wall ---
    "Ossex Western Wall Burrow North": Transition("Ossex Western Wall Burrow North", "Ossex Western Wall",
                                                  "Ossex Bowery Begger Residence Back", DirectionType.NORTH,
                                                  TransitionType.BURROW),  # noqa: custom type BURROW
    "Ossex Western Wall Burrow South": Transition("Ossex Western Wall Burrow South", "Ossex Western Wall",
                                                  "Ossex South Western Wall", DirectionType.SOUTH,
                                                  TransitionType.BURROW),  # noqa: custom type BURROW

    # --- Ossex South Western Wall ---
    "Ossex South Western Wall Burrow North": Transition("Ossex South Western Wall Burrow North",
                                                        "Ossex South Western Wall", "Ossex Western Wall",
                                                        DirectionType.NORTH, TransitionType.BURROW),
    # noqa: custom type BURROW
    "Ossex South Western Wall East": Transition("Ossex South Western Wall East", "Ossex South Western Wall",
                                                "Ossex Entry Western Wall Left", DirectionType.EAST,
                                                TransitionType.SCREENS),

    # --- Ossex Entry Western Wall Left ---
    "Ossex Entry Western Wall Left West": Transition("Ossex Entry Western Wall Left West",
                                                     "Ossex Entry Western Wall Left", "Ossex South Western Wall",
                                                     DirectionType.WEST, TransitionType.SCREENS),

    # --- Ossex Entry Western Wall Right ---
    "Ossex Entry Western Wall Right Left": Transition("Ossex Entry Western Wall Right Left",
                                                      "Ossex Entry Western Wall Right", "Ossex Entry Western Wall Left",
                                                      DirectionType.WEST, TransitionType.SCREENS,
                                                      CanBurrow() & CanBounce()),

    # --- Ossex Station ---
    "Ossex Station Burrow South Underside": Transition("Ossex Station Burrow South Underside", "Ossex Station",
                                                       "Ossex Station Underside Main", DirectionType.SOUTH,
                                                       TransitionType.BURROW, CanBurrow() & CanClimb()),

    "Ossex Station Door South Bowery Upper": Transition("Ossex Station Door South Bowery Upper", "Ossex Station",
                                                        "Ossex Bowery Upper", DirectionType.SOUTH,
                                                        TransitionType.DOORS),

    # --- Ossex Station Underside Main ---
    "Ossex Station Underside Main Door South": Transition("Ossex Station Underside Main Door South",
                                                          "Ossex Station Underside Main", "Ossex Bowery Main",
                                                          DirectionType.SOUTH, TransitionType.DOORS),

    # --- Ossex Station Underside Upper ---
    "Ossex Station Underside Upper To Main": Transition("Ossex Station Underside Upper To Main",
                                                        "Ossex Station Underside Upper", "Ossex Station Underside Main",
                                                        DirectionType.SOUTH, TransitionType.SCREENS),

    # --- Ossex Music Hall ---
    "Ossex Music Hall Door South": Transition("Ossex Music Hall Door South", "Ossex Music Hall", "Ossex Bowery Main",
                                              DirectionType.SOUTH, TransitionType.DOORS),

    # --- Ossex Bowery Residence ---
    "Ossex Bowery Residence Door South": Transition("Ossex Bowery Residence Door South", "Ossex Bowery Residence",
                                                    "Ossex Bowery Main", DirectionType.SOUTH, TransitionType.DOORS),
    "Ossex Bowery Residence North Upper": Transition("Ossex Bowery Residence North Upper", "Ossex Bowery Residence",
                                                     "Ossex Bowery Residence Upper Main", DirectionType.NORTH,
                                                     TransitionType.SCREENS),

    # --- Ossex Bowery Residence Upper Main ---
    "Ossex Bowery Residence Upper Main South": Transition("Ossex Bowery Residence Upper Main South",
                                                          "Ossex Bowery Residence Upper Main", "Ossex Bowery Residence",
                                                          DirectionType.SOUTH, TransitionType.SCREENS),

    # --- Ossex Bowery Residence Upper Top Entrance ---
    "Ossex Bowery Residence Upper Top Stair North": Transition("Ossex Bowery Residence Upper Top Stair North",
                                                               "Ossex Bowery Residence Upper Top Entrance",
                                                               "Ossex Bowery Upper", DirectionType.NORTH,
                                                               TransitionType.STAIRS),
    # "Stair North - Ossex Bowery (Upper)" - direction NORTH guessed; stair back down to Bowery Upper
    "Ossex Bowery Residence Upper Top Burrow North": Transition("Ossex Bowery Residence Upper Top Burrow North",
                                                                "Ossex Bowery Residence Upper Top Entrance",
                                                                "Ossex Bowery Residence Storage", DirectionType.NORTH,
                                                                TransitionType.BURROW),  # noqa: custom type BURROW

    # --- Ossex Bowery Residence Storage ---
    "Ossex Bowery Residence Storage Burrow South": Transition("Ossex Bowery Residence Storage Burrow South",
                                                              "Ossex Bowery Residence Storage",
                                                              "Ossex Bowery Residence Upper Main", DirectionType.SOUTH,
                                                              TransitionType.BURROW),  # noqa: custom type BURROW

    # --- Ossex High Street Main ---
    "Ossex High Street Main Door North Residence": Transition("Ossex High Street Main Door North Residence",
                                                              "Ossex High Street Main", "Ossex High Street Residence",
                                                              DirectionType.NORTH, TransitionType.DOORS),
    "Ossex High Street Main Door North Strategy": Transition("Ossex High Street Main Door North Strategy",
                                                             "Ossex High Street Main", "Ossex Strategy Center",
                                                             DirectionType.NORTH, TransitionType.DOORS,
                                                             Has("SparkUpgrade", count=1)),
    "Ossex High Street Main Door North Atelier": Transition("Ossex High Street Main Door North Atelier",
                                                            "Ossex High Street Main", "Ossex Atelier",
                                                            DirectionType.NORTH, TransitionType.DOORS,
                                                            Has("SparkUpgrade", count=2)),
    "Ossex High Street Main Area East": Transition("Ossex High Street Main Area East", "Ossex High Street Main",
                                                   "Eastern Hearth Grassland", DirectionType.EAST,
                                                   TransitionType.AREA_SCREENS),

    # --- Ossex High Street Balcony ---
    "Ossex High Street Balcony North East": Transition("Ossex High Street Balcony North East",
                                                       "Ossex High Street Balcony", "Ossex Balcony East",
                                                       DirectionType.NORTH, TransitionType.SCREENS),  # guessed NORTH

    # --- Ossex High Street Residence ---
    "Ossex High Street Residence Door South": Transition("Ossex High Street Residence Door South",
                                                         "Ossex High Street Residence", "Ossex High Street Main",
                                                         DirectionType.SOUTH, TransitionType.DOORS),
    "Ossex High Street Residence North Upper": Transition("Ossex High Street Residence North Upper",
                                                          "Ossex High Street Residence",
                                                          "Ossex High Street Residence Upper Main", DirectionType.NORTH,
                                                          TransitionType.SCREENS),

    # --- Ossex High Street Residence Upper Main ---
    "Ossex High Street Residence Upper Main South": Transition("Ossex High Street Residence Upper Main South",
                                                               "Ossex High Street Residence Upper Main",
                                                               "Ossex High Street Residence", DirectionType.SOUTH,
                                                               TransitionType.SCREENS),

    # --- Ossex High Street Residence Upper Puzzle ---
    "Ossex High Street Residence Upper Puzzle NR": Transition("Ossex High Street Residence Upper Puzzle NR",
                                                              "Ossex High Street Residence Upper Puzzle",
                                                              "Ossex High Street Residence", DirectionType.SOUTH,
                                                              TransitionType.DO_NOT_RANDOMIZE_ENTRANCE),
    "Ossex High Street River Swim" : Transition("Ossex High Street River Swim", "Ossex High Street SE Garden", "Ossex High Street Sewer", DirectionType.NORTH, TransitionType.BURROW),
    "Ossex High Street Sewer Swim Exit" : Transition("Ossex High Street Sewer Swim Exit", "Ossex High Street Sewer", "Ossex High Street SE Garden", DirectionType.SOUTH, TransitionType.BURROW),
    "Ossex High Street Sewer Geyser Exit" : Transition("Ossex High Street River Swim", "Ossex High Street SE Garden", "Ossex High Street Sewer", DirectionType.OVERWORLD, TransitionType.GEYSER_UP),
    # NOT RANDOMIZED
    "Ossex High Street Residence Upper Puzzle Stair North Balcony East": Transition(
        "Ossex High Street Residence Upper Puzzle Stair North Balcony East", "Ossex High Street Residence Upper Puzzle",
        "Ossex High Street Residence Balcony East", DirectionType.NORTH, TransitionType.STAIRS),

    # --- Ossex Balcony East ---
    "Ossex Balcony East South High Street": Transition("Ossex Balcony East South High Street", "Ossex Balcony East",
                                                       "Ossex High Street Balcony", DirectionType.SOUTH,
                                                       TransitionType.SCREENS),
    "Ossex Balcony East West Balcony West": Transition("Ossex Balcony East West Balcony West", "Ossex Balcony East",
                                                       "Ossex Balcony West", DirectionType.WEST,
                                                       TransitionType.SCREENS),

    # --- Ossex Balcony West ---
    "Ossex Balcony West East Balcony East": Transition("Ossex Balcony West East Balcony East", "Ossex Balcony West",
                                                       "Ossex Balcony East", DirectionType.EAST,
                                                       TransitionType.SCREENS),
    "Ossex Balcony West NR High Street Residence Upper": Transition("Ossex Balcony West NR High Street Residence Upper",
                                                                    "Ossex Balcony West",
                                                                    "Ossex High Street Residence Upper Puzzle",
                                                                    DirectionType.SOUTH,
                                                                    TransitionType.DO_NOT_RANDOMIZE_ENTRANCE,
                                                                    CanBurrow()),
    "Ossex Balcony West NR City Center": Transition("Ossex Balcony West NR City Center", "Ossex Balcony West",
                                                    "Ossex City Center Main", DirectionType.SOUTH,
                                                    TransitionType.DO_NOT_RANDOMIZE_ENTRANCE, CanBurrow()),


    # --- Ossex High Street Residence Balcony East ---
    "Ossex High Street Residence Balcony East Stair North Puzzle": Transition(
        "Ossex High Street Residence Balcony East Stair North Puzzle", "Ossex High Street Residence Balcony East",
        "Ossex High Street Residence Upper Puzzle", DirectionType.NORTH, TransitionType.STAIRS),

    "Ossex High Street Residence Balcony East West Puzzle": Transition(
        "Ossex High Street Residence Balcony East West Puzzle", "Ossex High Street Residence Balcony East",
        "Ossex High Street Residence Balcony West", DirectionType.WEST, TransitionType.SCREENS),

    # --- Ossex High Street Residence Balcony West ---
    "Ossex High Street Residence Balcony West East": Transition("Ossex High Street Residence Balcony West East",
                                                                "Ossex High Street Residence Balcony West",
                                                                "Ossex High Street Residence Balcony East",
                                                                DirectionType.EAST, TransitionType.SCREENS),

    "Ossex High Street Residence Balcony West NR City Center": Transition(
        "Ossex High Street Residence Balcony West NR City Center", "Ossex High Street Residence Balcony West",
        "Ossex City Center Main", DirectionType.SOUTH, TransitionType.DO_NOT_RANDOMIZE_ENTRANCE, CanBurrow()),


    # --- Ossex Strategy Center ---
    "Ossex Strategy Center Door South": Transition("Ossex Strategy Center Door South", "Ossex Strategy Center",
                                                   "Ossex High Street Main", DirectionType.SOUTH, TransitionType.DOORS),

    # --- Ossex Atelier ---
    "Ossex Atelier Door South": Transition("Ossex Atelier Door South", "Ossex Atelier", "Ossex High Street Main",
                                           DirectionType.SOUTH, TransitionType.DOORS),
}

collectable_locations: dict[str, LocationData] = {
"OS Couple's Quarter Chest" : LocationData(165, "Ossex Couple's Quarter"),
"OS Couple's Quarter Thermal Pack" : LocationData(147, "Ossex Couple's Quarter"),
    "Trinket_PocketTrebuchet" : LocationData(148, "Ossex City Center Main"),
"Ticket_Pass" : LocationData(149, "Ossex Station"),
    "OS Kear Institute Kear Completion" : LocationData(150, "Ossex Kear Institute"),
    # "Lock" : LocationData(151, "Ossex"),
    # "Lock" : LocationData(152, "Ossex"),
"OS Music Hall Chest" : LocationData(153, "Ossex Music Hall"),
"Trinket_PlasmaSaver" : LocationData(154, "Ossex High Street Main"),
"OS Ossex Telescope Kear" : LocationData(155, "Ossex Balcony East"),
"OS Trinket Bazaar Kear" : LocationData(156,"Ossex Trinket Bazaar"),
    # "Lock" : LocationData(157, "Ossex"),
"Trinket_BoneSaver" : LocationData(158, "Ossex Courtyard East"),
"OS Bowery Upper Chest" : LocationData(159, "Ossex Bowery Upper"),
"OS City Center 2nd Race Kear" : LocationData(160, "Ossex City Center", CanBurrow()),
"OS Courtyard East Deboning Wand" : LocationData(161, "Ossex Courtyard East"),
"OS City Center Steady Soles": LocationData(162, "Ossex High Street Residence Balcony West"),
"Whip_Level_2" : LocationData(163, "Ossex Legovich's Arms"),
    "OS Gutterways Bonestone" : LocationData(146, "Ossex Residence"),
"OS High Street Sewer Chest" : LocationData(164, "Ossex Residence"),
"OS Strategy Center Chest" : LocationData(166, "Ossex Strategy Center"),
"OS Strategy Center Ophidio Bonestone" : LocationData(167, "Ossex Strategy Center", ReachingSideArm()),
"OS Hollower's Guild Back Room Kear Chest" : LocationData(168, "Ossex Guild Back Room"),
"OS Attic Chest" : LocationData(169, "Ossex High Street Residence Upper Puzzle"),
    "OS Atelier Chest" : LocationData(170, "Ossex Atelier"),
    "OS High Street Valor Medallion" : LocationData(171, "Ossex Residence"),
    "OS Bowery Residence Bonestone" : LocationData(173, "Ossex Residence"),
    "OS Legovich's Arms Whip" : LocationData(174, "Ossex Legovich's Arms"),
    "OS Legovich's Arms Hammer" : LocationData(175, "Ossex Legovich's Arms"),
    "OS Legovich's Arms Daggers" : LocationData(176, "Ossex Legovich's Arms"),
    "OS Legovich's Arms Battery Buster" : LocationData(177, "Ossex Legovich's Arms"),
    "OS Legovich's Arms Guardian Casket" : LocationData(178, "Ossex Legovich's Arms"),
    "Trinket_PlasmaFunnel" : LocationData(179, "Ossex Trinket Bazaar"),
    "Trinket_BurrowPulse" : LocationData(180, "Ossex Trinket Bazaar"),
    "Trinket_BriskBrew" : LocationData(181, "Ossex Trinket Bazaar"),
    "Trinket_AutoVial" : LocationData(182, "Ossex Trinket Bazaar"),
    "Trinket_ShockFlint" : LocationData(183, "Ossex Trinket Bazaar"),
    "Trinket_Shield" : LocationData(184, "Ossex Trinket Bazaar"),
    "Trinket_VialParry" : LocationData(185, "Ossex Trinket Bazaar"),
    "OS Emporium Health Rose #1" : LocationData(186, "Ossex Emporium"),
    "OS Emporium Health Rose #2" : LocationData(187, "Ossex Emporium"),
    "OS Emporium Health Rose #3" : LocationData(188, "Ossex Emporium"),
    "OS Emporium Vial Pouch #1" : LocationData(189, "Ossex Emporium"),
    "OS Emporium Vial Pouch #2" : LocationData(190, "Ossex Emporium"),
    "OS Emporium Vial Pouch #3" : LocationData(191, "Ossex Emporium"),
    "OS Emporium Spark Container" : LocationData(192, "Ossex Emporium"),
    "OS Emporium Joule Box #1" : LocationData(193, "Ossex Emporium"),
    "OS Emporium Joule Box #2" : LocationData(194, "Ossex Emporium"),
    "OS Emporium Joule Box #3" : LocationData(195, "Ossex Emporium"),
    "OS Emporium Trinket Bag #1" : LocationData(196, "Ossex Emporium"),
    "OS Emporium Trinket Bag #2" : LocationData(197, "Ossex Emporium"),
    "OS Emporium Trinket Bag #3" : LocationData(198, "Ossex Emporium"),
    "OS Kear Institute Kear #1" : LocationData(199, "Ossex Kear Institute"),
    "OS Kear Institute Kear #2" : LocationData(200, "Ossex Kear Institute"),
    "OS Kear Institute Kear #3" : LocationData(201, "Ossex Kear Institute"),
    "OS Kear Institute Kear #4" : LocationData(202, "Ossex Kear Institute"),
    "OS Kear Institute Kear #5" : LocationData(203, "Ossex Kear Institute"),
    "OS Kear Institute Kear #6" : LocationData(204, "Ossex Kear Institute"),
    "OS Kear Institute Kear #7" : LocationData(205, "Ossex Kear Institute"),
    "OS Kear Institute Kear #8" : LocationData(206, "Ossex Kear Institute"),
    "OS Kear Institute Kear #9" : LocationData(207, "Ossex Kear Institute"),
    "ArmorUpgrade_Health" : LocationData(208, "Ossex Atelier"),
    "ArmorUpgrade_Custom" : LocationData(209, "Ossex Atelier"),
    "Upgrade_JouleAlembic" : LocationData(210, "Ossex Guild Back Room", ),
    "Upgrade_WorldMap" : LocationData(211, "Ossex Guild Back Room"),
    "Upgrade_EnhancedMap" : LocationData(212, "Ossex Guild Back Room"),
    "Upgrade_RadarMap" : LocationData(213, "Ossex Guild Back Room"),
    "Upgrade_SidearmKeeper" : LocationData(214, "Ossex Guild Back Room"),
    "Upgrade_SidearmSaver" : LocationData(215, "Ossex Guild Back Room"),
    "Upgrade_Phonograph" : LocationData(216, "Ossex Guild Back Room"),
    "Upgrade_CandleVision" : LocationData(217, "Ossex Guild Back Room"),
    "Upgrade_TrainingDummy" : LocationData(218, "Ossex Guild Back Room"),
    "Upgrade_TwoSidearmsHUD" : LocationData(219, "Ossex Guild Back Room"),
    "OS City Center Triple Flagellum" : LocationData(220, "Ossex Main Street", Has("Fishing Rod")),
}

connections: dict[str, RegionConnection] = {
    # --- Ossex City Center Upper ---
    "Ossex City Center Upper_Ossex City Center Main": RegionConnection("Ossex City Center Upper",
                                                                       "Ossex City Center Main", CanBurrow()),

    # --- Ossex Entry Western Wall ---
    "Ossex Entry Western Wall Left_Ossex Entry Western Wall Right": RegionConnection("Ossex Entry Western Wall Left",
                                                                                     "Ossex Entry Western Wall Right",
                                                                                     CanBurrow() & CanBounce()),
    "Ossex Entry Western Wall Right_Ossex Entry Western Wall Left": RegionConnection("Ossex Entry Western Wall Right",
                                                                                     "Ossex Entry Western Wall Left",
                                                                                     CanBurrow() & CanBounce()),

    # --- Ossex Western Wall ---
    "Ossex Western Wall_Western Wilds Overgrown Path": RegionConnection("Ossex Western Wall",
                                                                        "Western Wilds Overgrown Path"),

    # --- Ossex South Western Wall ---
    "Ossex South Western Wall_Southern Outskirts Commons Western Pit Room": RegionConnection("Ossex South Western Wall",
                                                                                             "Southern Outskirts Commons Western Pit Room",
                                                                                             CanClimb()),

    # --- Ossex Bowery Main ---
    "Ossex Bowery Main_Ossex Bowery Upper": RegionConnection("Ossex Bowery Main", "Ossex Bowery Upper", CanClimb()),

    # --- Ossex High Street Main ---
    "Ossex High Street Main_Ossex High Street Balcony": RegionConnection("Ossex High Street Main",
                                                                         "Ossex High Street Balcony",
                                                                         Has("Ossex Highstreet Balcony Kear")),
    "Ossex High Street Main_Ossex High Street SE Garden": RegionConnection("Ossex High Street Main",
                                                                           "Ossex High Street SE Garden"),
    "Ossex High Street Balcony_Ossex High Street Main": RegionConnection("Ossex High Street Balcony",
                                                                         "Ossex High Street Main"),

    # --- Ossex High Street SE Garden ---
    "Ossex High Street SE Garden_Ossex High Street Main": RegionConnection("Ossex High Street SE Garden",
                                                                           "Ossex High Street Main",
                                                                           Has("Ossex High Street SE Garden Kear")),

    # --- Ossex Station Underside ---
    "Ossex Station Underside Main_Ossex Station Underside Upper": RegionConnection("Ossex Station Underside Main",
                                                                                   "Ossex Station Underside Upper"),
    "Ossex Station Underside Upper_Ossex Station Underside Main": RegionConnection("Ossex Station Underside Upper",
                                                                                   "Ossex Station Underside Main"),

    # --- Ossex Bowery Residence Upper ---
    "Ossex Bowery Residence Upper Top Entrance_Ossex Bowery Residence Upper Main": RegionConnection(
        "Ossex Bowery Residence Upper Top Entrance", "Ossex Bowery Residence Upper Main"),
    "Ossex Bowery Residence Upper Main_Ossex Bowery Residence Upper Top Entrance": RegionConnection(
        "Ossex Bowery Residence Upper Main", "Ossex Bowery Residence Upper Top Entrance"),
}
bosses: dict[str, LocationData] = {}

