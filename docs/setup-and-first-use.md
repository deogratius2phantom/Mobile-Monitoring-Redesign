# Setup and First Use

This page is written for both early hardware evaluators and makers preparing a build from the design files.

## Before first power

Use this checklist before connecting power to a board or reviewing a newly assembled unit:

1. Confirm that the PCB assembly matches the latest schematic and layout in the repository.
2. Review the power path in `power.kicad_sch` and verify expected input voltage, polarity, and regulator orientation.
3. Check GPS and GSM module placement, connector orientation, and antenna clearances.
4. Inspect solder joints, rework areas, and any hand-fitted modules before power-up.
5. Make sure your test environment is appropriate for RF bring-up and GPS reception.

## If you are starting from the design files

1. Open `Mobile Monitor Redesign.kicad_pro` in KiCad.
2. Review the main schematic and the separate power schematic together.
3. Inspect `Mobile Monitor Redesign.kicad_pcb` for placement, routing, and board constraints.
4. Open the STEP files if you need a mechanical fit or enclosure check.
5. Use the `.pos` files when preparing pick-and-place or assembly review tasks.

## If you are starting from a built unit

The exact first-use flow depends on the firmware and sensor configuration loaded on the hardware. At a minimum, capture the following for your build notes:

- power source used for testing
- installed SIM or connectivity setup
- expected sensor population
- intended data logging or upload behavior
- enclosure or antenna configuration

## Recommended bring-up record

For repeatable testing, keep a short bring-up log with:

- board revision or assembly identifier
- date and test location
- GPS lock status
- cellular registration status
- observed power behavior
- any missing sensors or optional modules

That record will make future troubleshooting and documentation updates much easier.
