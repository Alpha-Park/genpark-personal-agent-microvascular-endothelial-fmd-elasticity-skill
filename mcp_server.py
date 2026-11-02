# -*- coding: utf-8 -*-
"""FastMCP Server for Personal Agent Microvascular Endothelial FMD Elasticity Skill."""

from mcp.server.fastmcp import FastMCP
from client import PersonalAgentMicrovascularEndothelialFmdElasticity

mcp = FastMCP("PersonalAgentMicrovascularEndothelialFmdElasticity")
client = PersonalAgentMicrovascularEndothelialFmdElasticity()

@mcp.tool()
def evaluate_brachial_fmd_and_vascular_age(
    baseline_diameter_mm: float = 4.10,
    peak_hyperemic_diameter_mm: float = 4.45,
    chronological_age: int = 42,
    sex: str = "male"
) -> str:
    """Calculates brachial Flow-Mediated Dilation (FMD %), NO bioavailability, and estimated vascular age."""
    import json
    return json.dumps(client.evaluate_brachial_fmd_and_vascular_age(
        baseline_diameter_mm, peak_hyperemic_diameter_mm, chronological_age, sex
    ), indent=2)

@mcp.tool()
def estimate_pulse_wave_velocity_and_arterial_stiffness(
    age: int = 42,
    mean_arterial_pressure: float = 93.3
) -> str:
    """Calculates estimated Pulse Wave Velocity (ePWV in m/s) and aortic arterial stiffness tier."""
    import json
    return json.dumps(client.estimate_pulse_wave_velocity_and_arterial_stiffness(
        age, mean_arterial_pressure
    ), indent=2)

if __name__ == "__main__":
    mcp.run()
