# Getting Started

This project documents a portable air-quality monitor design with onboard GPS and cellular connectivity. The repository can be used in three different ways depending on your goals.

## Choose your starting point

| Goal | Best place to start |
| --- | --- |
| Understand what the hardware does | [Hardware Overview](hardware-overview.md) |
| Review or modify the design | [Maker and Contributor Reference](maker-and-contributor-reference.md) |
| Prepare to assemble, inspect, or power a build | [Setup and First Use](setup-and-first-use.md) |

## What you need

### To read the documentation site

- a web browser
- access to the GitHub repository or published GitHub Pages site

### To inspect the hardware design

- **KiCad 6.0+** for the schematic and PCB files
- a STEP-compatible CAD viewer if you want to inspect the mechanical models

### To contribute to the docs

- Python 3
- the packages in `requirements-docs.txt`

```powershell
python -m pip install -r requirements-docs.txt
python -m mkdocs serve
```

The local preview server will show the documentation site and reload changes as you edit files in `docs/`.

## Repository quick start

Clone the repository:

```powershell
git clone https://github.com/deogratius2phantom/Mobile-Monitoring-Redesign.git
cd Mobile-Monitoring-Redesign
```

If you contribute regularly, you can also use the SSH URL once your GitHub SSH key is configured.

## What is currently documented

The repository already includes:

- project-level hardware context in `README.md`
- manufacturing and placement artifacts in the repository root
- design notes in `report.txt`

The GitHub Pages site builds on that material and provides a clearer navigation structure for future product-usage documentation.
