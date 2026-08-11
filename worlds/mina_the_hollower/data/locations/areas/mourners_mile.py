from BaseClasses import LocationProgressType
from rule_builder.rules import Has, CanReachLocation
from .._generated.regions import Regions
from ... import LocationTypeEnum
from ...items import PlayerUpgrades, Trinkets, Sidearms
from ...rules.ability_rules import CanBurrow, CanBounce, CanClimb, CanCarry, HasTrinket
from ...rules.movement_rules import CanJumpTiles

class Locations(LocationTypeEnum):
    MM_KNIGHT_S_REST_CHEST = (
        "MM Knight's Rest Chest", 311, Regions.MOURNERS_MILE_KNIGHTS_REST_CHEST,
    )

    MM_STATUE_ROOM_BONESTONE = (
        "MM Statue Room Bonestone", 315, Regions.MOURNERS_MILE_STATUE_ROOM_ROPE, CanBurrow(),
    )

    MM_SHALLOW_TOMB_KEAR = (
        "MM Shallow Tomb Kear", 305, Regions.MOURNERS_MILE_DARK_SHALLOW_TOMB_DARK,
    )

    MM_SPIKE_TOMB_TRINKET = (
        "MM Spike Tomb Trinket", 316, Regions.MOURNERS_MILE_SHALLOW_TOMB,
    )

    MM_SPIKE_VAULT_VIAL_POUCH = (
        "MM Spike Vault Vial Pouch", 312, Regions.MOURNERS_MILE_SPIKE_VAULT_UPPER,
    )

    MM_SPIKE_VAULT_HIDDEN_ROOM_KEAR = (
        "MM Spike Vault Hidden Room Kear", 310, Regions.MOURNERS_MILE_SPIKE_VAULT_HIDDEN_ROOM,
    )

    MM_TOWER_TUNNEL_CHEST_1 = (
        "MM Tower Tunnel Chest #1", 313, Regions.MOURNERS_MILE_TOWER_TUNNEL_DARK, CanBurrow(),
    )

    MM_TOWER_TUNNEL_CHEST_2 = (
        "MM Tower Tunnel Chest #2", 314, Regions.MOURNERS_MILE_TOWER_TUNNEL_DARK, CanBurrow(),
    )

    MM_MINA_S_GRAVE_CHEST = (
        "MM Mina's Grave Chest", 309, Regions.MOURNERS_MILE_MINAS_GRAVE,
    )

    MM_MINA_S_GRAVE_TRINKET = (
        "MM Mina's Grave Trinket", 308, Regions.MOURNERS_MILE_MINAS_GRAVE,
    )

    MM_SPIKE_HELL_CHEST = (
        "MM Spike Hell Chest", 355, Regions.MOURNERS_MILE_SPIKE_HELL_SANDFALL, (
            HasTrinket(trinket=Trinkets.SPIKE_SPURS.value)
            & Has(PlayerUpgrades.HEALTH_ROSE.value, count=6)
        )
        | (
            Has(Sidearms.MIST_JAR.value)
            & Has(PlayerUpgrades.JOULE_BOX.value, count=2)
        ),
    )


