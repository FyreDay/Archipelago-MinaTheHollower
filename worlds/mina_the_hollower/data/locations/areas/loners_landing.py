from .._generated.regions import Regions
from ... import LocationTypeEnum
from ...items import SingleKears, Wallets
from ...rules.ability_rules import CanBurrow, CanBounce, CanClimb, CanCarry, HasFishingRod, CanSwim
from ...rules.state_rules import HasKear, HasLadder
from ...rules.movement_rules import CanJumpTiles

class Locations(LocationTypeEnum):
    LL_BLIGHTED_DOCKS_FENCE_CHEST = (
        "LL Blighted Docks Fence Chest", 29, Regions.LONERS_LANDING_BLIGHTED_DOCKS_FENCES_BOTTOM,
    )

    LL_BLIGHTED_DOCKS_SIDE_ROOM_CHEST = (
        "LL Blighted Docks Side Room Chest", 28, Regions.LONERS_LANDING_BLIGHTED_DOCKS_SIDE_CAVE,
    )

    LL_BLIGHTED_DOCKS_BRIDGE_CHEST = (
        "LL Blighted Docks Bridge Chest", 31, Regions.LONERS_LANDING_BLIGHTED_DOCKS_BRIDGE_CLIFF, (CanBounce() | CanJumpTiles(distance=3)) & CanClimb(),
    )

    LL_BLIGHTED_DOCKS_GUARD_ROOM_CHEST = (
        "LL Blighted Docks Guard Room Chest", 26, Regions.LONERS_LANDING_BLIGHTED_DOCKS_RESIDENCE, CanBurrow(),
    )

    LL_BLIGHTED_DOCKS_ROOM_BUBBLE = (
        "LL Blighted Docks Room Bubble", 23, Regions.LONERS_LANDING_BLIGHTED_DOCKS_BURROW, CanJumpTiles(distance=2),
    )

    LL_BOARDWALK_FIRE_BOUNCE_CHEST = (
        "LL Boardwalk Fire Bounce Chest", 27, Regions.LONERS_LANDING_BOARDWALK_FIRE_BOUNCE, CanBounce(),
    )

    LL_BOARDWALK_SANDWATER_LEDGE_CHEST = (
        "LL Boardwalk Sandwater Ledge Chest", 324, Regions.LONERS_LANDING_BOARDWALK_SANDFALLS_LEDGE,
    )

    LL_FISH_TRIGGER_ANTENNAE = (
        "LL Fish Trigger Antennae", 32, Regions.LONERS_LANDING_BOAT_SIDE, HasFishingRod() & CanBurrow(),
    )

    LL_BELOWDECKS_LEFT_UNCHOSEN_WEAPON = (
        "LL Belowdecks Left Unchosen Weapon", 17, Regions.LONERS_LANDING_BELOWDECKS_CHESTS, HasKear(kear=SingleKears.LONERS_LANDING_BELOWDECKS_LEFT_WEAPON_KEAR.value),
    )

    LL_BELOWDECKS_RIGHT_UNCHOSEN_WEAPON = (
        "LL Belowdecks Right Unchosen Weapon", 18, Regions.LONERS_LANDING_BELOWDECKS_CHESTS, HasKear(kear=SingleKears.LONERS_LANDING_BELOWDECKS_RIGHT_WEAPON_KEAR.value),
    )

    LL_BELOWDECKS_CHEST = (
        "LL Belowdecks Chest", 30, Regions.LONERS_LANDING_BELOWDECKS, CanJumpTiles(distance=2),
    )

class OptionalLocations(LocationTypeEnum):
    LL_CAPTAINS_GIFT = ("LL Captain's Gift", 24, Regions.LONERS_LANDING_SHIPWRECK)
    LL_HULK_TROOPER = ("LL Defeat Hulk Trooper", 1024, Regions.SOUTHERN_OUTSKIRTS_COMMONS_OSSEX_ENTRY)
    LL_THORNE_1 = ("LL Defeat Thorne 1", 1024, Regions.OSSEX_COURTYARD)



