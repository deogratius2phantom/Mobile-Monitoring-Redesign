# Modular Indoor Positioning System (IPS)

This repository contains boilerplate for a modular indoor positioning system using four ESP32 sniffer nodes and a Raspberry Pi 4 central server.

## Project Overview

- **ESP32 Sniffer Nodes (`/firmware`)**
  - WiFi promiscuous capture of nearby device MAC + RSSI
  - UDP packet forwarding to a Raspberry Pi
  - Channel hopping across channels 1-13
- **Raspberry Pi Server (`/server`)**
  - Asynchronous UDP listener for multi-node ingest
  - 200ms sliding-window RSSI grouping by target MAC
  - 3D trilateration via `scipy.optimize.least_squares`
  - Basic Kalman filter for smoothing position estimates

## Repository Structure

```
.
├── firmware/
│   └── esp32_sniffer/
│       └── esp32_sniffer.ino
├── server/
│   ├── __init__.py
│   ├── config.yaml
│   ├── kalman.py
│   ├── main.py
│   ├── processing.py
│   ├── trilateration.py
│   └── udp_listener.py
├── docs/
│   └── README.md
└── requirements.txt
```

## Installation (Raspberry Pi)

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python server/main.py
```

## ESP32 Firmware Setup

1. Open `firmware/esp32_sniffer/esp32_sniffer.ino` in Arduino IDE.
2. Set `WIFI_SSID`, `WIFI_PASSWORD`, `SERVER_IP`, and `NODE_ID`.
3. Flash firmware to each ESP32 node with unique `NODE_ID` values (`node-1`...`node-4`).

## Configuration

Edit `server/config.yaml` to define fixed anchor coordinates and radio model parameters.
