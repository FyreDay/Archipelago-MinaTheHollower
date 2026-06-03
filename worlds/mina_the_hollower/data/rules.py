import dataclasses
from typing import override, ChainMap

from BaseClasses import CollectionState
from NetUtils import JSONMessagePart
from rule_builder.options import OptionFilter
from rule_builder.rules import Rule, Has

from . import MovementItemData
from ..constants import MINA_THE_HOLLOWER
from .items import all_movement_items
from ..options import AbilityRando
from ..world_base import MinaTheHollowerBase


@dataclasses.dataclass(kw_only=True)
class CanJumpOneTile(Rule[MinaTheHollowerBase], game=MINA_THE_HOLLOWER):

    @override
    def _instantiate(self, world: MinaTheHollowerBase) -> Rule.Resolved:
        # caching_enabled only needs to be passed in when your world inherits from CachedRuleBuilderWorld
        return Has("Jump", options=[OptionFilter(AbilityRando, AbilityRando.option_false, operator="ne") ]).resolve(world)

@dataclasses.dataclass(kw_only=True)
class CanJumpSevenTiles(Rule[MinaTheHollowerBase], game=MINA_THE_HOLLOWER):

    @override
    def _instantiate(self, world: MinaTheHollowerBase) -> Rule.Resolved:
        # caching_enabled only needs to be passed in when your world inherits from CachedRuleBuilderWorld
        return self.Resolved(all_movement_items, player=world.player, caching_enabled=True)

    class Resolved(Rule.Resolved):
        all_movement_items: ChainMap[str, MovementItemData]

        @override
        def _evaluate(self, state: CollectionState) -> bool:
            found_items : list[MovementItemData] = [value for key,value in self.all_movement_items if state.has(key, self.player)]
            tiles = sum([item.distance for item in found_items])

            return tiles > 7

        @override
        def item_dependencies(self) -> dict[str, set[int]]:
            return  {key : {id(self)} for key in all_movement_items.keys()}

        @override
        def explain_json(self, state: CollectionState | None = None) -> list[JSONMessagePart]:
            # this method can be overridden to display custom explanations
            return [
                {"type": "color", "color": "green" if state and self(state) else "salmon", "text": str(self)},
            ]
        @override
        def __str__(self) -> str:
            return "Jump Seven tiles"