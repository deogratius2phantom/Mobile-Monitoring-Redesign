# Maker and Contributor Reference

This section is for the general maker community and for contributors who want to inspect, modify, document, or manufacture the design.

## Repository layout

| Path | Contents |
| --- | --- |
| `3D CAD/` | Mechanical CAD files |
| `L80 GPS daughter board v1/` | GPS daughter-board design assets |
| `Mobile Monitor Redesign.kicad_pro` | KiCad project file |
| `Mobile Monitor Redesign.kicad_sch` | Main schematic |
| `Mobile Monitor Redesign.kicad_pcb` | Main PCB layout |
| `Mobile Monitor Redesign.step` | Assembly-level STEP model |
| `Mobile Monitor Redesign-top.pos` | Top-side placement file |
| `Mobile Monitor Redesign-bottom.pos` | Bottom-side placement file |
| `power.kicad_sch` | Power schematic |
| `report.txt` | Design notes |

## Working with the design

### KiCad

Open `Mobile Monitor Redesign.kicad_pro` in KiCad 6.0 or newer. Use the project view so schematic sheets, board data, and linked assets resolve together.

### 3D review

Use the STEP models to check fit, enclosure constraints, and module placement before manufacturing changes.

### Manufacturing review

The repository already includes pick-and-place outputs:

- `Mobile Monitor Redesign-top.pos`
- `Mobile Monitor Redesign-bottom.pos`

Use them alongside the PCB and schematic data when preparing fabrication outputs or contract manufacturing packages.

## Documentation workflow

The GitHub Pages site is built with MkDocs Material.

### Files you will edit

- `mkdocs.yml` for navigation and site configuration
- `docs/` for Markdown content
- `.github/workflows/pages.yml` for deployment automation

### Local preview

```powershell
python -m pip install -r requirements-docs.txt
python -m mkdocs serve
```

### Production build

```powershell
python -m mkdocs build --strict
```

## Publishing

The Pages workflow builds the site on pushes to `main` or `master` and deploys the generated `site/` output through GitHub Actions. In the repository settings, GitHub Pages should be configured to use **GitHub Actions** as the source.

## Good next additions

High-value future documentation for this project would include:

- a bill of materials page
- firmware or data-pipeline setup instructions
- field deployment examples
- assembly photos and enclosure guidance
- final end-user operating procedures
