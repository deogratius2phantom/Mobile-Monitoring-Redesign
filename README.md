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

### Cloning the Repository

You can clone this repository using either HTTPS or SSH:

#### Option 1: Clone with HTTPS
```bash
git clone https://github.com/deogratius2phantom/Mobile-Monitoring-Redesign.git
cd Mobile-Monitoring-Redesign
```

#### Option 2: Clone with SSH (Recommended for Contributors)
```bash
git clone git@github.com:deogratius2phantom/Mobile-Monitoring-Redesign.git
cd Mobile-Monitoring-Redesign
```

<details>
<summary><b>Setting up SSH for GitHub (Click to expand)</b></summary>

If you haven't set up SSH keys for GitHub yet, follow these steps:

##### 1. Check for Existing SSH Keys
```bash
ls -al ~/.ssh
```
Look for files named `id_rsa.pub`, `id_ecdsa.pub`, or `id_ed25519.pub`.

##### 2. Generate a New SSH Key (if needed)
```bash
ssh-keygen -t ed25519 -C "your_email@example.com"
```
Or if your system doesn't support Ed25519:
```bash
ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
```
Press Enter to accept the default file location, and optionally enter a passphrase.

##### 3. Add SSH Key to SSH Agent
```bash
# Start the SSH agent
eval "$(ssh-agent -s)"

# Add your SSH private key to the agent
ssh-add ~/.ssh/id_ed25519
```
(Replace `id_ed25519` with `id_rsa` if you generated an RSA key)

##### 4. Add SSH Key to Your GitHub Account
```bash
# Copy the SSH public key to clipboard (Linux)
cat ~/.ssh/id_ed25519.pub

# macOS
pbcopy < ~/.ssh/id_ed25519.pub

# Windows (Git Bash)
clip < ~/.ssh/id_ed25519.pub
```

Then:
- Go to GitHub.com and sign in
- Click your profile photo → **Settings**
- In the sidebar, click **SSH and GPG keys**
- Click **New SSH key**
- Add a descriptive title (e.g., "My Laptop")
- Paste your key into the "Key" field
- Click **Add SSH key**

##### 5. Verify SSH Connection to GitHub
```bash
ssh -T git@github.com
```
You should see a message like:
```
Hi username! You've successfully authenticated, but GitHub does not provide shell access.
```

##### 6. Clone the Repository Using SSH
```bash
git clone git@github.com:deogratius2phantom/Mobile-Monitoring-Redesign.git
cd Mobile-Monitoring-Redesign
```

For more detailed information, visit [GitHub's SSH documentation](https://docs.github.com/en/authentication/connecting-to-github-with-ssh).

</details>

### Viewing the Design

1. **Clone the repository** (see above for cloning options)

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