"""
Market Entry Sizing Model Builder
==================================
Performs bottoms-up and top-down market sizing calculations,
reconciliation between methods, sensitivity analysis, and
produces slide-ready formatted exhibits with source-cited assumptions.

Usage:
    python market_sizer.py --input market_inputs.json
    python market_sizer.py --input market_inputs.json --sensitivity win_rate
    python market_sizer.py --help

Input JSON format (market_inputs.json):
    {
        "market_name": "US Mid-Market ITSM Software",
        "bottoms_up": {
            "icp_count": 42000,
            "avg_deal_size": 28000,
            "win_rate": 0.10,
            "segments": [
                {
                    "name": "Mid-Market IT",
                    "icp_count": 28000,
                    "avg_deal_size": 25000,
                    "win_rate": 0.10
                },
                {
                    "name": "SMB IT",
                    "icp_count": 14000,
                    "avg_deal_size": 12000,
                    "win_rate": 0.12
                }
            ]
        },
        "top_down": {
            "total_market_size": 4500000000,
            "addressable_pct": 0.35,
            "capturable_pct": 0.025
        },
        "sources": {
            "icp_count": "US Census CBP NAICS 518210, 2022",
            "avg_deal_size": "Consultant estimate based on ITSM vendor public pricing, 2024",
            "win_rate": "Gartner ITSM Market Guide 2024, comparable vendor win rates",
            "total_market_size": "IDC Software Tracker 2024, ITSM category",
            "addressable_pct": "IDC 2024: mid-market addressable segment 35% of total ITSM",
            "capturable_pct": "Consultant estimate: Year 3 realistic share target"
        }
    }
"""

from __future__ import annotations

import argparse
import json
import sys
from typing import Optional


# ---------------------------------------------------------------------------
# Bottoms-Up Model
# ---------------------------------------------------------------------------

def bottoms_up(
    icp_count: int,
    avg_deal_size: float,
    win_rate: float,
    segments: Optional[list[dict]] = None,
) -> dict:
    """
    Build a bottoms-up market sizing model.

    The TAM is the theoretical maximum revenue if every ICP purchased at the
    average deal size. SAM applies an addressability factor (default: assumes
    the full ICP count is addressable). SOM applies the win rate to the SAM.

    If segments are provided, calculates TAM/SAM/SOM per segment and aggregates.
    Segment-level win rates override the top-level win_rate for that segment.
    Segment-level avg_deal_size overrides the top-level avg_deal_size for that segment.

    Args:
        icp_count: Total number of qualifying ICP accounts. Used only if segments
                   is None or empty. Must be a positive integer.
        avg_deal_size: Average annual contract value (ACV) or transaction size in USD.
                       Used as the default if segment-level values are not provided.
                       Must be positive.
        win_rate: Realistic conversion rate (fraction, e.g., 0.12 for 12%).
                  Represents the fraction of addressable ICPs that become customers
                  in the planning horizon. Must be between 0 and 1 (exclusive).
        segments: Optional list of segment dicts. Each dict may contain:
                  - "name" (str, required): segment label
                  - "icp_count" (int, required): number of qualifying ICPs in this segment
                  - "avg_deal_size" (float, optional): overrides top-level avg_deal_size
                  - "win_rate" (float, optional): overrides top-level win_rate

    Returns:
        dict with keys:
            - "tam" (float): Total Addressable Market in USD (all ICPs × avg deal size)
            - "sam" (float): Serviceable Addressable Market in USD (equal to TAM when
                             all ICP counts represent addressable accounts; segments
                             with explicit addressability adjustments will reflect lower SAM)
            - "som" (float): Serviceable Obtainable Market in USD (SAM × aggregate win rate)
            - "segment_breakdown" (list[dict]): per-segment tam/sam/som/win_rate/avg_deal_size
            - "aggregate_win_rate" (float): weighted average win rate across segments

    Raises:
        ValueError: For invalid icp_count, avg_deal_size, win_rate, or segment data.
    """
    if avg_deal_size <= 0:
        raise ValueError(
            f"avg_deal_size must be positive; received {avg_deal_size}."
        )
    if not (0 < win_rate < 1):
        raise ValueError(
            f"win_rate must be between 0 and 1 (exclusive); received {win_rate}. "
            "Express as a decimal: 12% = 0.12."
        )

    segment_breakdown = []

    if segments:
        total_tam = 0.0
        total_sam = 0.0
        total_som = 0.0
        total_icp = 0

        for seg in segments:
            seg_name = seg.get("name", "Unnamed segment")
            seg_icp = seg.get("icp_count")
            if seg_icp is None or seg_icp <= 0:
                raise ValueError(
                    f"Segment '{seg_name}' has invalid or missing icp_count: {seg_icp}. "
                    "Each segment must have a positive icp_count."
                )
            seg_deal_size = seg.get("avg_deal_size", avg_deal_size)
            seg_win_rate = seg.get("win_rate", win_rate)

            if seg_deal_size <= 0:
                raise ValueError(
                    f"Segment '{seg_name}' avg_deal_size must be positive; received {seg_deal_size}."
                )
            if not (0 < seg_win_rate < 1):
                raise ValueError(
                    f"Segment '{seg_name}' win_rate must be between 0 and 1; received {seg_win_rate}."
                )

            seg_tam = seg_icp * seg_deal_size
            seg_sam = seg_tam  # SAM equals TAM when segment ICP counts represent addressable accounts
            seg_som = seg_sam * seg_win_rate

            segment_breakdown.append({
                "name": seg_name,
                "icp_count": seg_icp,
                "avg_deal_size": seg_deal_size,
                "win_rate": seg_win_rate,
                "tam": round(seg_tam, 2),
                "sam": round(seg_sam, 2),
                "som": round(seg_som, 2),
            })

            total_tam += seg_tam
            total_sam += seg_sam
            total_som += seg_som
            total_icp += seg_icp

        aggregate_win_rate = round(total_som / total_sam, 4) if total_sam > 0 else win_rate

        return {
            "tam": round(total_tam, 2),
            "sam": round(total_sam, 2),
            "som": round(total_som, 2),
            "segment_breakdown": segment_breakdown,
            "aggregate_win_rate": aggregate_win_rate,
        }

    else:
        # Single-segment model
        if icp_count <= 0:
            raise ValueError(
                f"icp_count must be a positive integer; received {icp_count}."
            )
        tam = icp_count * avg_deal_size
        sam = tam
        som = sam * win_rate

        segment_breakdown.append({
            "name": "All ICPs",
            "icp_count": icp_count,
            "avg_deal_size": avg_deal_size,
            "win_rate": win_rate,
            "tam": round(tam, 2),
            "sam": round(sam, 2),
            "som": round(som, 2),
        })

        return {
            "tam": round(tam, 2),
            "sam": round(sam, 2),
            "som": round(som, 2),
            "segment_breakdown": segment_breakdown,
            "aggregate_win_rate": win_rate,
        }


# ---------------------------------------------------------------------------
# Top-Down Model
# ---------------------------------------------------------------------------

def top_down(
    total_market_size: float,
    addressable_pct: float,
    capturable_pct: float,
) -> dict:
    """
    Build a top-down market sizing model using penetration rates.

    Applies a two-step penetration cascade:
      TAM = total_market_size (from cited benchmark source)
      SAM = TAM × addressable_pct  (fraction of industry TAM addressable by client's offer)
      SOM = SAM × capturable_pct   (fraction of SAM realistically capturable)

    Args:
        total_market_size: Total industry TAM in USD, from a named benchmark source.
                           Must be positive.
        addressable_pct: Fraction of the total market that matches the client's offer
                         characteristics (target geography, segments, use cases).
                         Must be between 0 and 1 (exclusive). Example: 0.35 = 35% of TAM.
        capturable_pct: Realistic fraction of the SAM the client can capture in the
                        planning horizon given their resources, GTM, and competitive position.
                        Must be between 0 and 1 (exclusive). Example: 0.025 = 2.5% of SAM.

    Returns:
        dict with keys:
            - "tam" (float): Total Addressable Market — the full industry market size
            - "sam" (float): Serviceable Addressable Market — TAM × addressable_pct
            - "som" (float): Serviceable Obtainable Market — SAM × capturable_pct
            - "addressable_pct" (float): passed-through for exhibit formatting
            - "capturable_pct" (float): passed-through for exhibit formatting

    Raises:
        ValueError: For invalid inputs.
    """
    if total_market_size <= 0:
        raise ValueError(
            f"total_market_size must be positive; received {total_market_size}."
        )
    if not (0 < addressable_pct < 1):
        raise ValueError(
            f"addressable_pct must be between 0 and 1 (exclusive); received {addressable_pct}. "
            "Express as a decimal: 35% = 0.35."
        )
    if not (0 < capturable_pct < 1):
        raise ValueError(
            f"capturable_pct must be between 0 and 1 (exclusive); received {capturable_pct}. "
            "Express as a decimal: 2.5% = 0.025."
        )

    tam = total_market_size
    sam = tam * addressable_pct
    som = sam * capturable_pct

    return {
        "tam": round(tam, 2),
        "sam": round(sam, 2),
        "som": round(som, 2),
        "addressable_pct": addressable_pct,
        "capturable_pct": capturable_pct,
    }


# ---------------------------------------------------------------------------
# Reconciliation
# ---------------------------------------------------------------------------

def reconcile(bottoms_up_tam: float, top_down_tam: float) -> dict:
    """
    Compute the reconciliation gap between bottoms-up and top-down TAM estimates.

    Args:
        bottoms_up_tam: TAM from the bottoms-up model in USD.
        top_down_tam: TAM from the top-down model in USD.

    Returns:
        dict with keys:
            - "bottoms_up_tam" (float): input value
            - "top_down_tam" (float): input value
            - "gap_absolute" (float): abs(bottoms_up_tam - top_down_tam) in USD
            - "gap_pct" (float): gap as a percentage of top_down_tam (the reference base)
            - "gap_direction" (str): "BOTTOMS_UP_HIGHER", "TOP_DOWN_HIGHER", or "ALIGNED"
            - "gap_severity" (str): "ALIGNED" (<20%), "MATERIAL_DIVERGENCE" (20-50%), "INCONSISTENT" (>50%)
            - "likely_explanation" (str): preliminary explanation of the gap direction
            - "recommended_primary" (str): which estimate to use as the planning figure base
    """
    if bottoms_up_tam <= 0 or top_down_tam <= 0:
        raise ValueError(
            "Both TAM values must be positive. "
            f"Received bottoms_up_tam={bottoms_up_tam}, top_down_tam={top_down_tam}."
        )

    gap_absolute = abs(bottoms_up_tam - top_down_tam)
    # Gap is expressed relative to top-down TAM (the benchmark-anchored reference)
    gap_pct = round((gap_absolute / top_down_tam) * 100, 1)

    if bottoms_up_tam > top_down_tam * 1.001:
        gap_direction = "BOTTOMS_UP_HIGHER"
        likely_explanation = (
            "The bottoms-up estimate exceeds the top-down benchmark. Most likely causes: "
            "(1) ICP count is overstated — the source definition may be broader than the true "
            "serviceable universe; (2) win rate assumption may be too optimistic compared to "
            "comparable market analogs; (3) average deal size may include expansion revenue "
            "beyond first-year ACV; or (4) the top-down benchmark source uses a narrower market "
            "definition than the client's intended addressable scope."
        )
        recommended_primary = "top_down"
    elif top_down_tam > bottoms_up_tam * 1.001:
        gap_direction = "TOP_DOWN_HIGHER"
        likely_explanation = (
            "The top-down benchmark exceeds the bottoms-up estimate. Most likely causes: "
            "(1) The bottoms-up ICP list is incomplete — the segment model may miss addressable "
            "geographies or customer types; (2) the addressable_pct applied in the top-down model "
            "may be too generous — the client's offer does not serve all of the SAM; (3) the "
            "bottoms-up model excludes channel or indirect revenue that is captured in the "
            "industry TAM; or (4) the industry TAM includes revenue categories adjacent to "
            "the client's specific offering."
        )
        recommended_primary = "bottoms_up"
    else:
        gap_direction = "ALIGNED"
        likely_explanation = (
            "The two methods are substantially aligned (within 0.1%), indicating the ICP-based "
            "estimate and the benchmark-anchored estimate are consistent. Use the bottoms-up "
            "as the planning figure and the top-down as the sanity check."
        )
        recommended_primary = "bottoms_up"

    if gap_pct < 20:
        gap_severity = "ALIGNED"
        recommended_primary = "bottoms_up"  # Both aligned; use bottoms-up as planning figure
    elif gap_pct <= 50:
        gap_severity = "MATERIAL_DIVERGENCE"
    else:
        gap_severity = "INCONSISTENT"
        # When inconsistent, top-down is the anchor; investigate bottoms-up assumptions
        recommended_primary = "top_down" if gap_direction == "BOTTOMS_UP_HIGHER" else "bottoms_up"

    return {
        "bottoms_up_tam": round(bottoms_up_tam, 2),
        "top_down_tam": round(top_down_tam, 2),
        "gap_absolute": round(gap_absolute, 2),
        "gap_pct": gap_pct,
        "gap_direction": gap_direction,
        "gap_severity": gap_severity,
        "likely_explanation": likely_explanation,
        "recommended_primary": recommended_primary,
    }


# ---------------------------------------------------------------------------
# Sensitivity Analysis
# ---------------------------------------------------------------------------

def sensitivity_table(
    base_inputs: dict,
    variable_name: str,
    range_pct: float = 0.20,
) -> list[dict]:
    """
    Generate a sensitivity table showing TAM/SAM/SOM impact of varying one input.

    Builds a 5-row scenario table: -range_pct, -range_pct/2, base, +range_pct/2, +range_pct.
    For each scenario, recalculates the full bottoms-up and top-down models and returns
    the resulting TAM/SAM/SOM values alongside the input change.

    Supports sensitivity on any of these named inputs:
        Bottoms-up inputs:  "icp_count", "avg_deal_size", "win_rate"
        Top-down inputs:    "total_market_size", "addressable_pct", "capturable_pct"

    Args:
        base_inputs: dict containing the full model inputs. Must have structure:
            {
                "bottoms_up": {
                    "icp_count": int,
                    "avg_deal_size": float,
                    "win_rate": float,
                    "segments": [...]  # optional
                },
                "top_down": {
                    "total_market_size": float,
                    "addressable_pct": float,
                    "capturable_pct": float
                }
            }
        variable_name: Name of the input to vary. Must be one of the supported names above.
        range_pct: Sensitivity range as a decimal. Default 0.20 = ±20%.
                   The function builds scenarios at -range_pct, -(range_pct/2),
                   base (0%), +(range_pct/2), +range_pct.

    Returns:
        list of 5 dicts, one per scenario, each with keys:
            - "scenario_label": human-readable label ("-40%", "-20%", "Base", "+20%", "+40%")
            - "variable_name": the input being varied
            - "input_value": the value of the varied input in this scenario
            - "pct_change_from_base": percentage change from base value
            - "bottoms_up_tam": float
            - "bottoms_up_sam": float
            - "bottoms_up_som": float
            - "top_down_tam": float
            - "top_down_sam": float
            - "top_down_som": float
            - "tam_pct_change": float — TAM change vs. base scenario (uses bottoms-up or top-down
                                depending on which model the variable belongs to)

    Raises:
        ValueError: For unsupported variable_name or invalid inputs.
    """
    valid_variables = {
        "icp_count", "avg_deal_size", "win_rate",
        "total_market_size", "addressable_pct", "capturable_pct",
    }
    if variable_name not in valid_variables:
        raise ValueError(
            f"variable_name '{variable_name}' is not supported. "
            f"Must be one of: {sorted(valid_variables)}."
        )

    if range_pct <= 0 or range_pct >= 1:
        raise ValueError(
            f"range_pct must be between 0 and 1 (exclusive); received {range_pct}."
        )

    bu_inputs = base_inputs.get("bottoms_up", {})
    td_inputs = base_inputs.get("top_down", {})

    # Determine which model owns this variable
    bu_variables = {"icp_count", "avg_deal_size", "win_rate"}
    td_variables = {"total_market_size", "addressable_pct", "capturable_pct"}

    # Get base value of the variable
    if variable_name in bu_variables:
        base_value = bu_inputs.get(variable_name)
    else:
        base_value = td_inputs.get(variable_name)

    if base_value is None:
        raise ValueError(
            f"variable_name '{variable_name}' not found in base_inputs. "
            f"Check that base_inputs has the correct structure."
        )

    # Build scenario multipliers: -range, -range/2, base, +range/2, +range
    multipliers = [
        (-(range_pct), f"-{int(range_pct * 100)}%"),
        (-(range_pct / 2), f"-{int(range_pct / 2 * 100)}%"),
        (0.0, "Base"),
        (range_pct / 2, f"+{int(range_pct / 2 * 100)}%"),
        (range_pct, f"+{int(range_pct * 100)}%"),
    ]

    # Compute base TAM for pct_change reference
    base_bu = bottoms_up(
        icp_count=bu_inputs.get("icp_count", 1),
        avg_deal_size=bu_inputs.get("avg_deal_size", 1.0),
        win_rate=bu_inputs.get("win_rate", 0.1),
        segments=bu_inputs.get("segments"),
    )
    base_td = top_down(
        total_market_size=td_inputs.get("total_market_size", 1.0),
        addressable_pct=td_inputs.get("addressable_pct", 0.5),
        capturable_pct=td_inputs.get("capturable_pct", 0.1),
    )

    # Reference TAM for pct_change calculation
    if variable_name in bu_variables:
        reference_base_tam = base_bu["tam"]
    else:
        reference_base_tam = base_td["tam"]

    results = []

    for delta_pct, label in multipliers:
        scenario_value = base_value * (1 + delta_pct)

        # Enforce valid ranges for rate inputs
        if variable_name in {"win_rate", "addressable_pct", "capturable_pct"}:
            scenario_value = max(0.001, min(0.999, scenario_value))

        if variable_name == "icp_count":
            scenario_value = max(1, int(round(scenario_value)))

        # Build modified inputs for this scenario
        scenario_bu_inputs = dict(bu_inputs)
        scenario_td_inputs = dict(td_inputs)

        if variable_name in bu_variables:
            # For segments with icp_count: scale all segment counts proportionally
            if variable_name == "icp_count" and bu_inputs.get("segments"):
                scale_factor = scenario_value / base_value
                new_segments = []
                for seg in bu_inputs["segments"]:
                    new_seg = dict(seg)
                    new_seg["icp_count"] = max(1, int(round(seg["icp_count"] * scale_factor)))
                    new_segments.append(new_seg)
                scenario_bu_inputs["segments"] = new_segments
            else:
                scenario_bu_inputs[variable_name] = scenario_value
                # For segment-level overrides of avg_deal_size or win_rate,
                # update all segments proportionally
                if variable_name in {"avg_deal_size", "win_rate"} and bu_inputs.get("segments"):
                    scale_factor = scenario_value / base_value
                    new_segments = []
                    for seg in bu_inputs["segments"]:
                        new_seg = dict(seg)
                        seg_val = seg.get(variable_name, base_value)
                        new_val = seg_val * scale_factor
                        if variable_name == "win_rate":
                            new_val = max(0.001, min(0.999, new_val))
                        new_seg[variable_name] = new_val
                        new_segments.append(new_seg)
                    scenario_bu_inputs["segments"] = new_segments
        else:
            scenario_td_inputs[variable_name] = scenario_value

        # Calculate models for this scenario
        try:
            scenario_bu = bottoms_up(
                icp_count=scenario_bu_inputs.get("icp_count", 1),
                avg_deal_size=scenario_bu_inputs.get("avg_deal_size", 1.0),
                win_rate=scenario_bu_inputs.get("win_rate", 0.1),
                segments=scenario_bu_inputs.get("segments"),
            )
        except ValueError:
            scenario_bu = {"tam": 0.0, "sam": 0.0, "som": 0.0}

        try:
            scenario_td = top_down(
                total_market_size=scenario_td_inputs.get("total_market_size", 1.0),
                addressable_pct=scenario_td_inputs.get("addressable_pct", 0.5),
                capturable_pct=scenario_td_inputs.get("capturable_pct", 0.1),
            )
        except ValueError:
            scenario_td = {"tam": 0.0, "sam": 0.0, "som": 0.0}

        if variable_name in bu_variables:
            scenario_tam = scenario_bu["tam"]
        else:
            scenario_tam = scenario_td["tam"]

        tam_pct_change = round(
            ((scenario_tam - reference_base_tam) / reference_base_tam) * 100, 1
        ) if reference_base_tam != 0 else 0.0

        results.append({
            "scenario_label": label,
            "variable_name": variable_name,
            "input_value": scenario_value,
            "pct_change_from_base": round(delta_pct * 100, 1),
            "bottoms_up_tam": scenario_bu["tam"],
            "bottoms_up_sam": scenario_bu["sam"],
            "bottoms_up_som": scenario_bu["som"],
            "top_down_tam": scenario_td["tam"],
            "top_down_sam": scenario_td["sam"],
            "top_down_som": scenario_td["som"],
            "tam_pct_change": tam_pct_change,
        })

    return results


# ---------------------------------------------------------------------------
# Exhibit Formatting
# ---------------------------------------------------------------------------

def _fmt_currency(value: float) -> str:
    """Format a USD value with appropriate scale suffix (M or B)."""
    if value >= 1_000_000_000:
        return f"${value / 1_000_000_000:.1f}B"
    elif value >= 1_000_000:
        return f"${value / 1_000_000:.1f}M"
    elif value >= 1_000:
        return f"${value / 1_000:.1f}K"
    else:
        return f"${value:,.0f}"


def format_exhibit(
    bottoms_up_result: dict,
    top_down_result: dict,
    reconciliation: dict,
    market_name: str = "Target Market",
) -> str:
    """
    Generate a slide-ready formatted market sizing exhibit.

    Produces a text-formatted table showing TAM/SAM/SOM from both methods
    side-by-side, with the reconciliation summary and recommended planning figure.

    Args:
        bottoms_up_result: Output dict from bottoms_up().
        top_down_result: Output dict from top_down().
        reconciliation: Output dict from reconcile().
        market_name: Human-readable market name for the exhibit header.

    Returns:
        Formatted string ready for slide notes or exhibit body.
    """
    bu = bottoms_up_result
    td = top_down_result
    rec = reconciliation

    tam_gap_flag = ""
    if rec["gap_severity"] == "MATERIAL_DIVERGENCE":
        tam_gap_flag = " [MATERIAL DIVERGENCE — review reconciliation narrative]"
    elif rec["gap_severity"] == "INCONSISTENT":
        tam_gap_flag = " [INCONSISTENT — one estimate requires revision]"

    lines = [
        f"MARKET SIZING EXHIBIT — {market_name.upper()}",
        "=" * 60,
        "",
        f"{'Metric':<12} {'Bottoms-Up':>14} {'Top-Down':>14} {'Gap':>10}",
        "-" * 54,
        f"{'TAM':<12} {_fmt_currency(bu['tam']):>14} {_fmt_currency(td['tam']):>14} {rec['gap_pct']:>9.1f}%{tam_gap_flag}",
        f"{'SAM':<12} {_fmt_currency(bu['sam']):>14} {_fmt_currency(td['sam']):>14} {'':>10}",
        f"{'SOM':<12} {_fmt_currency(bu['som']):>14} {_fmt_currency(td['som']):>14} {'':>10}",
        "-" * 54,
        "",
        f"Gap direction:    {rec['gap_direction']}",
        f"Gap severity:     {rec['gap_severity']}",
        f"Recommended base: {rec['recommended_primary'].replace('_', '-').upper()} estimate",
        "",
        "RECONCILIATION NOTE",
        "-" * 40,
        rec["likely_explanation"],
        "",
        "BOTTOMS-UP SEGMENT DETAIL",
        "-" * 40,
    ]

    for seg in bu.get("segment_breakdown", []):
        lines.append(
            f"  {seg['name']:<30} "
            f"ICPs: {seg['icp_count']:>6,} | "
            f"ACV: {_fmt_currency(seg['avg_deal_size'])} | "
            f"Win: {seg['win_rate'] * 100:.1f}% | "
            f"TAM: {_fmt_currency(seg['tam'])} | "
            f"SOM: {_fmt_currency(seg['som'])}"
        )

    lines += [
        "",
        "TOP-DOWN PENETRATION CASCADE",
        "-" * 40,
        f"  Industry TAM:         {_fmt_currency(td['tam'])}",
        f"  × Addressable (%):    {td['addressable_pct'] * 100:.1f}%",
        f"  = SAM:                {_fmt_currency(td['sam'])}",
        f"  × Capturable (%):     {td['capturable_pct'] * 100:.1f}%",
        f"  = SOM:                {_fmt_currency(td['som'])}",
        "",
        "NOTE: AI-assisted draft — requires lead consultant review before client delivery.",
    ]

    return "\n".join(lines)


def assumptions_table(inputs: dict, sources: dict) -> str:
    """
    Generate a source-cited assumptions table for the deliverable appendix.

    Args:
        inputs: dict of assumption name → value (matching the market_inputs JSON structure,
                or a flat dict of {assumption_name: value}).
        sources: dict of assumption name → source citation string.
                 Keys should match the keys in inputs. Assumptions without a matching
                 source key will be flagged as [SOURCE REQUIRED].

    Returns:
        Formatted string table listing each assumption, its value, source, and
        a confidence level (High if sourced, Low if missing or flagged).
    """
    lines = [
        "SOURCE-CITED ASSUMPTIONS TABLE",
        "=" * 70,
        f"{'Assumption':<30} {'Value':<20} {'Confidence':<12} Source",
        "-" * 70,
    ]

    # Flatten nested inputs if needed
    flat_inputs: dict[str, object] = {}
    for k, v in inputs.items():
        if isinstance(v, dict):
            for sub_k, sub_v in v.items():
                if not isinstance(sub_v, (dict, list)):
                    flat_inputs[sub_k] = sub_v
        elif not isinstance(v, (dict, list)):
            flat_inputs[k] = v

    for assumption, value in flat_inputs.items():
        source = sources.get(assumption, "[SOURCE REQUIRED]")
        confidence = "Low" if "[SOURCE REQUIRED]" in source or "estimate" in source.lower() else "High"

        # Format the value for display
        if isinstance(value, float) and value < 1:
            value_str = f"{value * 100:.1f}%"
        elif isinstance(value, float):
            value_str = _fmt_currency(value)
        elif isinstance(value, int) and value > 1000:
            value_str = f"{value:,}"
        else:
            value_str = str(value)

        lines.append(
            f"{assumption:<30} {value_str:<20} {confidence:<12} {source}"
        )

    lines += [
        "-" * 70,
        "",
        "Confidence: High = directly cited from named benchmark source (publication ≤3 years old)",
        "            Low  = consultant estimate, analog benchmark, or source not verified",
        "",
        "NOTE: All Low-confidence assumptions should be prioritized for validation",
        "      before finalizing the market entry recommendation.",
    ]

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# CLI Entry Point
# ---------------------------------------------------------------------------

def _run_cli(args: argparse.Namespace) -> None:
    """Execute the full market sizing model from a JSON config file."""
    with open(args.input, "r") as f:
        config = json.load(f)

    market_name = config.get("market_name", "Target Market")
    bu_cfg = config.get("bottoms_up", {})
    td_cfg = config.get("top_down", {})
    source_cfg = config.get("sources", {})

    # Build bottoms-up
    bu_result = bottoms_up(
        icp_count=bu_cfg.get("icp_count", 0),
        avg_deal_size=bu_cfg.get("avg_deal_size", 0.0),
        win_rate=bu_cfg.get("win_rate", 0.1),
        segments=bu_cfg.get("segments"),
    )

    # Build top-down
    td_result = top_down(
        total_market_size=td_cfg.get("total_market_size", 0.0),
        addressable_pct=td_cfg.get("addressable_pct", 0.5),
        capturable_pct=td_cfg.get("capturable_pct", 0.1),
    )

    # Reconcile
    rec_result = reconcile(
        bottoms_up_tam=bu_result["tam"],
        top_down_tam=td_result["tam"],
    )

    # Format exhibit
    exhibit = format_exhibit(bu_result, td_result, rec_result, market_name)
    print(exhibit)
    print()

    # Assumptions table
    print(assumptions_table(config, source_cfg))
    print()

    # Sensitivity analysis (if requested)
    if args.sensitivity:
        variable = args.sensitivity
        print(f"SENSITIVITY ANALYSIS — {variable.upper()}")
        print("=" * 60)
        rows = sensitivity_table(
            base_inputs={"bottoms_up": bu_cfg, "top_down": td_cfg},
            variable_name=variable,
            range_pct=0.40,
        )
        print(
            f"{'Scenario':<10} {'Input Value':<18} {'TAM':>14} {'SAM':>14} {'SOM':>14} {'TAM Change':>12}"
        )
        print("-" * 86)
        for row in rows:
            print(
                f"{row['scenario_label']:<10} "
                f"{str(row['input_value']):<18} "
                f"{_fmt_currency(row['bottoms_up_tam'] if variable in {'icp_count', 'avg_deal_size', 'win_rate'} else row['top_down_tam']):>14} "
                f"{_fmt_currency(row['bottoms_up_sam'] if variable in {'icp_count', 'avg_deal_size', 'win_rate'} else row['top_down_sam']):>14} "
                f"{_fmt_currency(row['bottoms_up_som'] if variable in {'icp_count', 'avg_deal_size', 'win_rate'} else row['top_down_som']):>14} "
                f"{row['tam_pct_change']:>+11.1f}%"
            )
        print()


def main() -> None:
    parser = argparse.ArgumentParser(
        description=(
            "Market Entry Sizing Model Builder — "
            "Compute bottoms-up and top-down TAM/SAM/SOM with reconciliation."
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument(
        "--input",
        required=True,
        metavar="FILE",
        help="Path to JSON config file with market sizing inputs.",
    )
    parser.add_argument(
        "--sensitivity",
        metavar="VARIABLE",
        default=None,
        help=(
            "Run sensitivity analysis on a named input variable. "
            "Choices: icp_count, avg_deal_size, win_rate, "
            "total_market_size, addressable_pct, capturable_pct."
        ),
    )

    args = parser.parse_args()
    _run_cli(args)


if __name__ == "__main__":
    main()
