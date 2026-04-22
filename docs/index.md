# Mobile Air Quality Monitor

This site collects the working documentation for the **Mobile Monitoring Redesign** hardware project. It is intended for two audiences:

- people trying to understand or use the hardware product
- makers and contributors who want to inspect, build, or improve the design

The repository is currently centered on hardware design assets such as KiCad files, STEP models, and manufacturing outputs. This documentation site organizes those materials into a more approachable structure for GitHub Pages.

!!! note
    Some operating details still depend on the final firmware, enclosure, sensor stack, and field workflow used in your build. Where those details are not yet captured in the repository, this site points back to the design files so the documentation can evolve without guessing.

## What this project includes

- a main KiCad project for the mobile monitor PCB
- support files for GPS and GSM modules
- 3D CAD assets for mechanical integration
- placement outputs that can be used during manufacturing

## Start here

If you are new to the project, use this path:

1. Read [Getting Started](getting-started.md) for the quickest way into the design.
2. Review [Hardware Overview](hardware-overview.md) to understand the major modules.
3. Use [Setup and First Use](setup-and-first-use.md) before powering a build or opening the design files.
4. Keep [Troubleshooting](troubleshooting.md) and [Safety and Care](safety-and-care.md) handy during testing.

If you are contributing to the project, jump to [Maker and Contributor Reference](maker-and-contributor-reference.md).

## Documentation scope

This first version of the docs site is focused on:

- turning the repository into a browsable GitHub Pages site
- documenting how to navigate and use the hardware design package
- establishing a place for future end-user instructions as the product matures

## Source of truth

The most detailed technical artifacts still live in the repository root:

- `Mobile Monitor Redesign.kicad_pro`
- `Mobile Monitor Redesign.kicad_sch`
- `Mobile Monitor Redesign.kicad_pcb`
- `power.kicad_sch`
- `Mobile Monitor Redesign.step`
- `report.txt`
