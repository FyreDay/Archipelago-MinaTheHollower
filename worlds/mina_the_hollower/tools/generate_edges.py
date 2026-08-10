"""CLI + library: render edges.csv into areas/_generated/<area>_edges.py.

Usage:
    python -m worlds.mina_the_hollower.tools.generate_edges path/to/edges.csv
"""
from __future__ import annotations

import argparse
import pathlib
import sys
import re

try:  # standalone-first so the tooling never needs to boot the Archipelago stack
    import edge_schema as es
except ModuleNotFoundError:  # running via `python -m worlds.mina_the_hollower.tools...`
    from worlds.mina_the_hollower.tools import edge_schema as es

BANNER = (
    "# AUTO-GENERATED -- DO NOT EDIT.\n"
    "# Regenerate from the spreadsheet export with:\n"
    "#   python -m worlds.mina_the_hollower.tools.generate_edges <edges.csv>\n"
    "# The spreadsheet is the source of truth, not this file.\n"
)

IMPORTS = (
    "from .regions import Regions\n"
    "from rule_builder.rules import Has, True_, CanReachLocation\n"
    "from ... import RegionConnection, Transition, DirectionType, TransitionType, RegionTypeEnum,ConnectionTypeEnum, TransitionTypeEnum\n"
    "from ...rules.ability_rules import (\n"
    "    CanBurrow, CanCarry, CanClimb, CanSwim, CanBounce, PowerLevelThreshold,\n"
    "    HasVialsCount, HasReachingSideArm, HasFishingRod, CanSpring, HasTrinket \n"
    ")\n"
     "from ...rules.movement_rules import (\n"
    "    CanJumpTiles, \n"
    ")\n"
    "from ...rules.state_rules import (\n"
    "   HasLadder, HasAccessToTorch, StartedInOssex, \n"
    "   AnyThreeAstralPlatforms, HasKear, HasSparks, \n"
    "   RepairedGenerator, RepairedGeneratorCount,\n"
    ")\n"
    "from ...events import (\n"
    "   QUEENSBURY_CRYPT_DATA, NOXS_BAYOU_DATA, SEPTEMBURG_DATA, \n"
    "   BONE_BEACH_DATA, COLTRANE_PEAK_DATA, ASTRAL_ORRERY_DATA, \n"
    ")\n"
    "from ...items.game_items import (\n"
    "   PermanentUpgrades, PlayerUpgrades, Trinkets, Sidearms\n"
    ")\n"
    "from ...items.kears import (\n"
    "   SingleKears,\n"
    ")\n"
    "from ...items.blockers import (\n"
    "   AstralPlatforms,\n"
    ")\n"
)

GENERATED_INIT = (
    "# AUTO-GENERATED package of edge data. DO NOT EDIT.\n"
    "# Regenerate with python -m worlds.mina_the_hollower.tools.generate_edges\n"
)


def _rule_suffix(rule: str) -> str:
    rule = rule.strip()
    return f", {rule}" if rule else ", True_()"


def _comment(notes: str) -> str:
    notes = notes.strip().replace("\n", " ")
    return f"  # {notes}" if notes else ""

def make_enum_name(value: str) -> str:
    name = re.sub(r"[^a-zA-Z0-9]+", "_", value)
    name = re.sub(r"_+", "_", name)
    return name.strip("_").upper()

def render_region_enum(edges: "list[es.Edge]"):
    regions = sorted({e.from_region for e in edges})
    out: list[str] = [BANNER, IMPORTS, ""]
    out.append("class Regions(RegionTypeEnum):")
    for r in regions:
        enum_name = make_enum_name(r)
        out.append(f"    {enum_name} = {r!r}")
    out.append("")
    return "\n".join(out) + "\n"

def render_area_module(area: str, edges: "list[es.Edge]") -> str:
    area_edges = [e for e in edges if e.area == area]
    connections = sorted((e for e in area_edges if e.is_internal),
                         key=lambda e: e.resolved_name)
    transitions = sorted((e for e in area_edges if not e.is_internal),
                         key=lambda e: e.resolved_name)

    out: list[str] = [BANNER, IMPORTS, ""]


    out.append("class RegionConnections(ConnectionTypeEnum):")
    for e in connections:
        out.append(
            f"    {make_enum_name(e.resolved_name)} = ("
            f"{e.resolved_name!r}, "
            f"Regions.{make_enum_name(e.from_region)}, "
            f"Regions.{make_enum_name(e.to_region)}"
            f"{_rule_suffix(e.rule)}"
            f"),"
            f"{_comment(e.notes)}"
        )
    out.append("")

    out.append("class RegionTransitions(TransitionTypeEnum):")
    for e in transitions:
        out.append(
            f"    {make_enum_name(e.resolved_name)} = ("
            f"{e.resolved_name!r}, "
            f"Regions.{make_enum_name(e.from_region)}, "
            f"Regions.{make_enum_name(e.to_region)}, "
            f"DirectionType.{e.direction}, TransitionType.{e.transition_type}"
            f"{_rule_suffix(e.rule)}"
            f"),"
            f"{_comment(e.notes)}"
        )
    out.append("")

    return "\n".join(out) + "\n"


def write_modules(edges: "list[es.Edge]", out_dir: pathlib.Path) -> "list[pathlib.Path]":
    out_dir.mkdir(parents=True, exist_ok=True)
    written: list[pathlib.Path] = []

    init_path = out_dir / "__init__.py"
    init_path.write_text(GENERATED_INIT, encoding="utf-8")
    written.append(init_path)
    regions_path = out_dir / f"regions.py"
    regions_path.write_text(render_region_enum(edges), encoding="utf-8")
    written.append(regions_path)

    for area in sorted({e.area for e in edges}):
        path = out_dir / f"{area}_edges.py"
        path.write_text(render_area_module(area, edges), encoding="utf-8")
        written.append(path)

    return written


def main(argv: "list[str] | None" = None) -> int:
    parser = argparse.ArgumentParser(description="Generate Mina edge modules")
    parser.add_argument("csv", type=pathlib.Path)
    args = parser.parse_args(argv)

    edges = es.read_edges_csv(args.csv)
    out_dir = (pathlib.Path(__file__).resolve().parents[1]
               / "data" / "locations" / "_generated")
    written = write_modules(edges, out_dir)
    print(f"Wrote {len(written)} files to {out_dir}:")
    for p in written:
        print(f"  - {p.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
