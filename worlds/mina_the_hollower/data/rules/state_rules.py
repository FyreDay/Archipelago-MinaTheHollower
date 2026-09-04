import dataclasses
import math
from operator import truediv
from typing import override

from BaseClasses import CollectionState
from NetUtils import JSONMessagePart
from rule_builder.options import OptionFilter
from rule_builder.rules import Rule, Has, True_, False_
from .ability_rules import CanSwim, CanCarry, CanBurrow, CanClimb
from .movement_rules import CanJumpTiles
from .. import ShortCutItem, RepairEventData
from ..events import repair_generator_data
from ..items import Kear, SingleKears, AreaKears, Trinkets, AstralPlatforms, Sidearms, PlayerUpgrades, \
    PermanentUpgrades, Wallets
from ..items.blockers import GeneratorsComplete
from ..items.kears import kear_area_lookup
from ...constants import MINA_THE_HOLLOWER
from ...world_base import MinaTheHollowerBase

repair_generator_lookup = {data.index: data for data in repair_generator_data}

@dataclasses.dataclass(kw_only=True)
class HasKear(Rule[MinaTheHollowerBase], game=MINA_THE_HOLLOWER):
    kear: str
    @override
    def _instantiate(self, world: MinaTheHollowerBase) -> Rule.Resolved:
        if world.options.kear_rando.value == world.options.kear_rando.option_vanilla:
            if self.kear == SingleKears.LONERS_LANDING_BOARDWALK_KEAR.value and not world.ossex_start:
                return Has(Kear.UNIVERSAL_KEAR.value, 1).resolve(world)
            return Has(Kear.UNIVERSAL_KEAR.value, 40).resolve(world)
        elif world.options.kear_rando.value == world.options.kear_rando.option_apItems:
            return Has(self.kear).resolve(world)
        else:
            area_kear = kear_area_lookup.get(self.kear)
            if area_kear is not None:
                return Has(area_kear.value).resolve(world)
            else:
                return False_().resolve(world)

@dataclasses.dataclass(kw_only=True)
class HasSparks(Rule[MinaTheHollowerBase], game=MINA_THE_HOLLOWER):
    count: int
    @override
    def _instantiate(self, world: MinaTheHollowerBase) -> Rule.Resolved:
        # caching_enabled only needs to be passed in when your world inherits from CachedRuleBuilderWorld
        return self.Resolved(count=self.count, player=world.player, caching_enabled=False)

    class Resolved(Rule.Resolved):
        count:int
        @override
        def _evaluate(self, state: CollectionState) -> bool:
            sparks = 1 if state.has(Trinkets.SPARK_CATCHER.value, self.player) and state.has(PlayerUpgrades.TRINKET_BAG.value, self.player) else 0
            sparks += state.count(PlayerUpgrades.SPARK_CONTAINER.value, self.player)
            return sparks >= self.count

        @override
        def item_dependencies(self) -> dict[str, set[int]]:
            return {
                Trinkets.SPARK_CATCHER.value: {id(self)},
                PlayerUpgrades.SPARK_CONTAINER.value: {id(self)},
                PlayerUpgrades.TRINKET_BAG.value: {id(self)},
            }

        @override
        def explain_json(self, state: CollectionState | None = None) -> list[JSONMessagePart]:
            # this method can be overridden to display custom explanations
            return [
                {"type": "color", "color": "green" if state and self(state) else "salmon", "text": str(self)},
            ]
        @override
        def __str__(self) -> str:
            return f"Has Spark Count"


@dataclasses.dataclass(kw_only=True)
class HasAllKears(Rule[MinaTheHollowerBase], game=MINA_THE_HOLLOWER):
    @override
    def _instantiate(self, world: MinaTheHollowerBase) -> Rule.Resolved:
        # caching_enabled only needs to be passed in when your world inherits from CachedRuleBuilderWorld
        return self.Resolved(kear_rando=world.options.kear_rando.value, player=world.player, caching_enabled=False)

    class Resolved(Rule.Resolved):
        kear_rando:int
        @override
        def _evaluate(self, state: CollectionState) -> bool:
            if self.kear_rando == 0:
                return state.has(Kear.UNIVERSAL_KEAR.value, self.player,40)
            elif self.kear_rando == 1:
                count = 0
                for item in SingleKears:
                    if state.has(item.value, self.player):
                        count+=1
                return count >= 30
            else:
                for item in AreaKears:
                    if not state.has(item.value, self.player):
                        return False
            return True

        @override
        def item_dependencies(self) -> dict[str, set[int]]:
            return {item.value: {id(self)} for item in [*Kear, *AreaKears, *SingleKears]}

        @override
        def explain_json(self, state: CollectionState | None = None) -> list[JSONMessagePart]:
            # this method can be overridden to display custom explanations
            return [
                {"type": "color", "color": "green" if state and self(state) else "salmon", "text": str(self)},
            ]
        @override
        def __str__(self) -> str:
            return f"Has All Kears"


@dataclasses.dataclass(kw_only=True)
class HasTrinketCount(Rule[MinaTheHollowerBase], game=MINA_THE_HOLLOWER):
    count: int

    @override
    def _instantiate(self, world: MinaTheHollowerBase) -> Rule.Resolved:
        # caching_enabled only needs to be passed in when your world inherits from CachedRuleBuilderWorld
        return self.Resolved(count=self.count, player=world.player, caching_enabled=False)

    class Resolved(Rule.Resolved):
        count: int
        ability_rando = False

        @override
        def _evaluate(self, state: CollectionState) -> bool:
            trinket_count = 0
            for trinket in Trinkets:
                if state.has(trinket.value, self.player):
                    trinket_count += 1

            return trinket_count >= self.count

        @override
        def item_dependencies(self) -> dict[str, set[int]]:
            return {item.value: {id(self)} for item in Trinkets}

        @override
        def explain_json(self, state: CollectionState | None = None) -> list[JSONMessagePart]:
            # this method can be overridden to display custom explanations
            return [
                {"type": "color", "color": "green" if state and self(state) else "salmon", "text": str(self)},
            ]
        @override
        def __str__(self) -> str:
            return f"Has {self.count} Trinkets"


@dataclasses.dataclass(kw_only=True)
class StartedInOssex(Rule[MinaTheHollowerBase], game=MINA_THE_HOLLOWER):
    @override
    def _instantiate(self, world: MinaTheHollowerBase) -> Rule.Resolved:
        if world.ossex_start:
            return True_().resolve(world)
        return False_().resolve(world)

def AnyThreeAstralPlatforms():
    green = Has(AstralPlatforms.GREEN_ASTRAL_PLATFORMS.value)
    red = Has(AstralPlatforms.RED_ASTRAL_PLATFORMS.value)
    blue = Has(AstralPlatforms.BLUE_ASTRAL_PLATFORMS.value)
    yellow = Has(AstralPlatforms.YELLOW_ASTRAL_PLATFORMS.value)

    return (
        (green & red & blue) |
        (green & red & yellow) |
        (green & blue & yellow) |
        (red & blue & yellow)
    )


@dataclasses.dataclass(kw_only=True)
class RepairedGeneratorCount(Rule[MinaTheHollowerBase], game=MINA_THE_HOLLOWER):
    count: int

    @override
    def _instantiate(self, world: MinaTheHollowerBase) -> Rule.Resolved:
        return self.Resolved(
            count=self.count,
            player=world.player,
            broken_generators=tuple(world.broken_generators),
            caching_enabled=False,
        )

    class Resolved(Rule.Resolved):
        count: int
        broken_generators: tuple[int, ...]

        @override
        def _evaluate(self, state: CollectionState) -> bool:
            repaired = sum(
                state.has(repair_generator_lookup[i].type.event_item, self.player)
                for i in self.broken_generators
            )

            if self.count >= len(self.broken_generators):
                return repaired == len(self.broken_generators)

            return repaired >= self.count

        @override
        def item_dependencies(self) -> dict[str, set[int]]:
            return {item: {id(self)} for item in [item.value for item in GeneratorsComplete]}

        @override
        def explain_json(self, state: CollectionState | None = None) -> list[JSONMessagePart]:
            # this method can be overridden to display custom explanations
            return [
                {"type": "color", "color": "green" if state and self(state) else "salmon", "text": str(self)},
            ]
        @override
        def __str__(self) -> str:
            return f"Completed {self.count} Generators"



@dataclasses.dataclass(kw_only=True)
class RepairedGenerator(Rule[MinaTheHollowerBase], game=MINA_THE_HOLLOWER):
    event: RepairEventData
    @override
    def _instantiate(self, world: MinaTheHollowerBase) -> Rule.Resolved:
        if self.event.index in world.lit_generators:
            return (RepairedGeneratorCount(count=world.options.goal_generators.value) &
                Has(self.event.type.event_item)).resolve(world)

        return Has(self.event.type.event_item).resolve(world)

#figure out when screen rando exists
def HasAccessToTorch():
    return CanCarry()

#figure out when screen rando exists
def HasLadder():
    return HasKear(kear=SingleKears.PINKY_KEAR.value) & HasKear(kear=SingleKears.PINKY_BACK_KEAR.value) & (CanBurrow() | CanJumpTiles(distance=3)) & CanCarry() & CanClimb()

sidearm_rules: list[ShortCutItem] = [
    ShortCutItem(Sidearms.HOLLOWERS_ROCKS, True_()),
    ShortCutItem(Sidearms.GYRO_DAGGER, True_()),
    ShortCutItem(Sidearms.VOLT_HATCHET, True_()),
    ShortCutItem(Sidearms.IRON_STEED, CanBurrow() & Has(PlayerUpgrades.SPARK_CONTAINER.value, 2) | ((Has(PermanentUpgrades.SEPTEMBURG_TICKET.value) & Has(PermanentUpgrades.TRAIN_PASS.value)) & CanBurrow())),
    ShortCutItem(Sidearms.FOG_THROWER, CanBurrow()),
    ShortCutItem(Sidearms.DEFLECTOR_PARASOL, True_()),
    ShortCutItem(Sidearms.MIST_JAR, CanBurrow()),
    ShortCutItem(Sidearms.DRIVER_DRILL, CanBurrow()),
    ShortCutItem(Sidearms.RECALL_DISC, True_()),
    ShortCutItem(Sidearms.BOUNDING_BOMBS, True_()),
    ShortCutItem(Sidearms.BECKONING_COLLAR, True_()),
    ShortCutItem(Sidearms.GNAWING_GHOSTS, True_()),
]

def CanFishAllFish():
    return RepairedGeneratorCount(count=6)


@dataclasses.dataclass(kw_only=True)
class ShopPrice(Rule[MinaTheHollowerBase], game=MINA_THE_HOLLOWER):
    cost: int

    @override
    def _instantiate(self, world: MinaTheHollowerBase) -> Rule.Resolved:

        amount = 0
        if self.cost >= 3000:
            amount = 3
        elif self.cost >= 2000:
            amount = 2
        elif self.cost >= 3000:
            amount = 1
        if amount <= 0:
            return True_().resolve(world)

        return RepairedGeneratorCount(count=amount).resolve(world)


@dataclasses.dataclass(kw_only=True)
class IsGeneratorRequired(Rule[MinaTheHollowerBase], game=MINA_THE_HOLLOWER):
    generator: str
    @override
    def _instantiate(self, world: MinaTheHollowerBase) -> Rule.Resolved:

        names = [
            data.gen_name
            for data in repair_generator_data
            if data.index in world.broken_generators
        ]
        if self.generator in names:
            return True_().resolve(world)
        return False_().resolve(world)

@dataclasses.dataclass(kw_only=True)
class CanReachRegionWithLadder(Rule[MinaTheHollowerBase], game=MINA_THE_HOLLOWER):
    """A rule that checks if the given region is reachable by the current player"""

    region_name: str
    """The name of the region to test access to"""

    @override
    def _instantiate(self, world: MinaTheHollowerBase) -> Rule.Resolved:
        return self.Resolved(
            self.region_name,
            player=world.player,
            caching_enabled=getattr(world, "rule_caching_enabled", False),
        )

    @override
    def __str__(self) -> str:
        options = f", options={self.options}" if self.options else ""
        return f"{self.__class__.__name__}({self.region_name}{options})"

    class Resolved(Rule.Resolved):
        region_name: str

        @override
        def _evaluate(self, state: CollectionState) -> bool:
            return state.can_reach_region(self.region_name, self.player)

        @override
        def region_dependencies(self) -> dict[str, set[int]]:
            return {self.region_name: {id(self)}}

        @override
        def explain_json(self, state: CollectionState | None = None) -> list[JSONMessagePart]:
            if state is None:
                verb = "Can reach"
            elif self(state):
                verb = "Reached"
            else:
                verb = "Cannot reach"
            return [
                {"type": "text", "text": f"{verb} region "},
                {"type": "color", "color": "yellow", "text": self.region_name},
            ]

        @override
        def explain_str(self, state: CollectionState | None = None) -> str:
            if state is None:
                return str(self)
            prefix = "Reached" if self(state) else "Cannot reach"
            return f"{prefix} region {self.region_name}"

        @override
        def __str__(self) -> str:
            return f"Can reach region {self.region_name}"

