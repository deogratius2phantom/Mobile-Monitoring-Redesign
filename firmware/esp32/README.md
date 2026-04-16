# ESP32 Firmware (PlatformIO)

This directory contains the ESP32 firmware project configured for PlatformIO.

## Requirements

- Python 3
- PlatformIO Core (`pip install platformio`)

## Build

```bash
cd firmware/esp32
platformio run
```

## Upload

```bash
cd firmware/esp32
platformio run -t upload
```

## Serial Monitor

```bash
cd firmware/esp32
platformio device monitor
```
