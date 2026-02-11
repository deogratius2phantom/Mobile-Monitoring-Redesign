# Mobile Air Quality Monitor - Hardware Design

A comprehensive PCB and CAD design for a mobile air quality monitoring system with GPS tracking and cellular connectivity.

## 📋 Project Overview

This repository contains the complete hardware design files for a portable air quality monitoring device. The system is designed to measure environmental air quality parameters while providing real-time GPS location tracking and cellular data transmission capabilities.

## 🔧 Key Features

- **GPS Tracking**: L80-M39 GPS module for precise location tracking
- **Cellular Connectivity**: SIM800L GSM/GPRS module for remote data transmission
- **Modular Design**: Includes daughter board for GPS module
- **Complete PCB Design**: Full KiCad project files with schematics and PCB layouts
- **3D Visualization**: STEP files for mechanical integration and enclosure design

## 📂 Repository Structure

```
├── 3D CAD/                          # 3D CAD files and models
├── L80 GPS daughter board v1/       # GPS module daughter board design files
├── Mobile Monitor Redesign-backups/ # Backup files for KiCad project
├── Mobile Monitor Redesign.kicad_pcb    # Main PCB layout file
├── Mobile Monitor Redesign.kicad_sch    # Main schematic file
├── Mobile Monitor Redesign.kicad_pro    # KiCad project file
├── Mobile Monitor Redesign.step         # 3D model of complete assembly
├── Mobile Monitor Redesign-top.pos      # Top side component positions
├── Mobile Monitor Redesign-bottom.pos   # Bottom side component positions
├── power.kicad_sch                      # Power supply schematic
├── L80-M39--3DModel-STEP-56544.STEP    # GPS module 3D model
├── SIM800L v10.step                     # SIM800L module 3D model
└── report.txt                           # Design report/notes
```

## 🛠️ Tools & Requirements

### Software
- **KiCad 6.0+**: For viewing and editing PCB/schematic files
- **CAD Software**: Any STEP-compatible viewer/editor for 3D models (e.g., FreeCAD, Fusion 360, SolidWorks)

### Hardware Components
- L80-M39 GPS Module
- SIM800L GSM/GPRS Module
- Air quality sensors (see schematic for specific models)
- Power management components (see power.kicad_sch)

## 🚀 Getting Started

### Viewing the Design

1. **Clone the repository**:
   ```bash
   git clone https://github.com/deogratius2phantom/Mobile-Monitoring-Redesign.git
   cd Mobile-Monitoring-Redesign
   ```

2. **Open in KiCad**:
   - Launch KiCad
   - Open the project file: `Mobile Monitor Redesign.kicad_pro`
   - View schematics and PCB layout

3. **View 3D Models**:
   - Open `.step` files in your preferred CAD software
   - The main assembly is in `Mobile Monitor Redesign.step`

### Manufacturing the PCB

The repository includes manufacturing-ready files:
- **Gerber files**: Can be generated from the `.kicad_pcb` file
- **BOM (Bill of Materials)**: Extract from schematic
- **Pick-and-place files**: `Mobile Monitor Redesign-top.pos` and `Mobile Monitor Redesign-bottom.pos`

## 📊 Design Specifications

- **PCB Design Tool**: KiCad
- **Layer Count**: [To be specified based on PCB file]
- **GPS Module**: Quectel L80-M39
- **Cellular Module**: SIM800L GSM/GPRS
- **Power Supply**: See `power.kicad_sch` for details

## 📖 Documentation

For detailed information about:
- **Schematic**: Open `Mobile Monitor Redesign.kicad_sch` in KiCad
- **PCB Layout**: Open `Mobile Monitor Redesign.kicad_pcb` in KiCad
- **Power Design**: Reference `power.kicad_sch`
- **Design Notes**: See `report.txt`

## 🤝 Contributing

Contributions to improve the design are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request with detailed description

## ⚠️ Important Notes

- Ensure proper antenna placement for GPS and GSM modules
- Follow power supply guidelines in `power.kicad_sch`
- Verify component footprints before manufacturing
- Test GPS and GSM functionality in your target environment

## 📝 License

[Please specify your license here]

## 📧 Contact

For questions or collaboration opportunities, please open an issue in this repository.

---

**Project Status**: Active Development

*This is a hardware design project for educational and development purposes. Ensure compliance with local regulations for wireless devices before deployment.*