# Operating the Device

The repository does not yet include a finalized end-user operating manual, but the intended workflow for the hardware is clear from the project structure: power the unit, acquire sensor data, associate that data with location, and transmit or log results for later review.

## Expected usage flow

1. Prepare the device with the correct power source, installed modules, and any required firmware.
2. Move the unit to an environment suitable for both sensor readings and GPS reception.
3. Power on the hardware and allow time for the system to stabilize.
4. Confirm that the GPS and cellular subsystems behave as expected for your build.
5. Start the measurement or logging process defined by your firmware stack.
6. Review captured data, then power down the device safely.

## What operators should watch

### Power stability

Unexpected resets, brownouts, or module dropouts often point back to the power design or the chosen test supply. Review `power.kicad_sch` if system behavior looks unstable under load.

### GPS readiness

GPS modules typically need time, open sky, and good antenna placement to achieve a stable lock. Indoor testing can make normal acquisition look like a fault.

### Cellular readiness

The SIM800L portion of the design will depend on network coverage, SIM provisioning, and firmware configuration. If remote data upload is part of your workflow, record those assumptions during test setup.

### Sensor interpretation

The exact air-quality sensor operating sequence is not yet documented in the repository. If your build includes a known sensor stack and calibration procedure, that information should be added here in a later revision.

## Suggested next documentation additions

To turn this into a complete user guide, add:

- the final power-up sequence
- status indicators or expected serial output
- sensor warm-up guidance
- data export or dashboard access steps
- shutdown and storage guidance for the finished product
