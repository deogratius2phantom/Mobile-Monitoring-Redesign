# Hardware Overview

The Mobile Air Quality Monitor is designed as a portable hardware platform for collecting air-quality data while also tracking location and supporting cellular data transmission.

## Main functions

- **Environmental monitoring** through the air-quality sensing hardware defined in the schematic
- **GPS tracking** through the L80-M39 GPS module
- **Cellular connectivity** through the SIM800L GSM/GPRS module
- **Portable deployment** through a compact PCB and enclosure-ready 3D models

## Main design assets in the repository

| Asset | Purpose |
| --- | --- |
| `Mobile Monitor Redesign.kicad_pro` | Main KiCad project entry point |
| `Mobile Monitor Redesign.kicad_sch` | Primary schematic |
| `power.kicad_sch` | Power design details |
| `Mobile Monitor Redesign.kicad_pcb` | PCB layout |
| `Mobile Monitor Redesign.step` | Assembly-level 3D model |
| `L80 GPS daughter board v1/` | GPS daughter-board support files |
| `Mobile Monitor Redesign-top.pos` | Top-side placement data |
| `Mobile Monitor Redesign-bottom.pos` | Bottom-side placement data |

## System blocks

### GPS

The repository references the **Quectel L80-M39** module for positioning. GPS performance will depend on antenna placement, enclosure design, and the final field environment.

### Cellular

The design includes the **SIM800L** GSM/GPRS module for remote communications. Final network setup will depend on your SIM choice, signal quality, and firmware configuration.

### Power

The dedicated `power.kicad_sch` file should be treated as the primary reference for supply-path review, regulator choices, and any bring-up checks before first power.

### Mechanical integration

STEP files in the repository support enclosure work, fit checks, and visual review of the assembled design.

## Current documentation gap

!!! note
    This repository is strongest on design files and weakest on step-by-step product operation. If your team has finalized assembly, provisioning, or field-use procedures, those should be added to this docs site next so end users do not need to reverse-engineer them from KiCad assets.
