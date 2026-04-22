# Troubleshooting

Use this page as a starting point when the design files open correctly but the hardware or bring-up workflow does not behave as expected.

## No power or unstable power

Check:

- input voltage and polarity
- regulator orientation and solder quality
- shorts or bridges around the power section
- high current draw from GSM activity

Reference: `power.kicad_sch`

## GPS does not lock

Check:

- antenna placement and grounding constraints
- outdoor or window-adjacent testing conditions
- module orientation and footprint alignment
- whether the build has enough startup time for acquisition

Reference: the L80-M39 design assets and main schematic

## Cellular link does not come up

Check:

- SIM installation and activation status
- antenna connection and placement
- power stability during transmit bursts
- firmware settings for baud rate, APN, and network registration

Reference: SIM800L model files and the main schematic

## Design files do not open as expected

Check:

- KiCad version compatibility
- missing project-relative assets
- whether you opened the `.kicad_pro` file rather than an individual file in isolation

## Placement or manufacturing outputs look wrong

Check:

- that you are using the latest `.pos` files from the repository root
- component origin and rotation settings in your assembly workflow
- whether assembly outputs match the PCB revision you intend to build

## When to escalate

If a problem cannot be isolated from the files in this repository, document:

- the exact board revision or file revision
- the power source used
- observed GPS and cellular behavior
- screenshots or export files from KiCad if layout review is involved

That information will make issue reports and future documentation updates much more useful.
