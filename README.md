# Avell Unofficial Control Center (AUCC)

[![Gitter](https://badges.gitter.im/Unofficial-CC/Lobby.svg)](https://gitter.im/Unofficial-CC/Lobby?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge)

A modern Python-based driver and control utility for RGB keyboards on Linux, specifically targeting the **Integrated Technology Express ITE Device(8291) Rev 0.03** controller.

This controller is commonly found in gaming laptops manufactured by **Tongfang** and sold under various reseller brands worldwide.

## Compatibility

### Supported Controller
**ITE Device(8291) Rev 0.03**

*Note: If you have Rev 0.02, please see [Project StarBeat](https://github.com/kirainmoe/project-starbeat).*

### Verified Devices
- Tongfang GK5CN5Z / GK5CN6Z / GK5CQ7Z / GK5CP0Z (Barebone)
- Avell G1550 FOX, G1513 FOX-7, A65, A52
- Schenker XMG Neo 15, Versions M18 & M19
- PCSpecialist Recoil II & III
- Eluktronics Mech 15 G2
- ...and many other Tongfang-based laptops.

## Modern Features
- **Full Type Safety**: Modernized codebase with PEP 484 type annotations.
- **PEP 517 Compliant**: Uses `pyproject.toml` for standardized builds and dependency management.
- **Improved Performance**: Optimized color vector generation and hardware communication.
- **Linted & Formatted**: Adheres to modern standards via [Ruff](https://github.com/astral-sh/ruff).

## Installation

### From PyPI
```bash
sudo pip install avell-unofficial-control-center
```

### Development Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/rodgomesc/avell-unofficial-control-center.git
   cd avell-unofficial-control-center
   ```
2. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```
3. Install in editable mode:
   ```bash
   pip install -e .
   ```

## Usage

### Commands
All commands require root privileges (handled automatically via `elevate`) to access the USB device.

#### Static Colors
```bash
aucc -c green -b 4
```
Available colors: `red`, `green`, `blue`, `teal`, `pink`, `purple`, `white`, `yellow`, `orange`, `olive`, `maroon`, `brown`, `gray`, `skyblue`, `navy`, `crimson`, `darkgreen`, `lightgreen`, `gold`, `violet`.

#### Dynamic Styles
```bash
aucc -s rainbow --speed 5
```
Available styles: `rainbow`, `marquee`, `wave`, `raindrop`, `aurora`, `random`, `reactive`, `breathing`, `ripple`, `reactiveripple`, `reactiveaurora`, `fireworks`.

*Tip: Append a color initial to style names (e.g., `rippler` for Red Ripple).*

#### Patterns
- **Horizontal**: `aucc -H pink teal`
- **Vertical**: `aucc -V blue white`

#### Disable Backlight
```bash
aucc -d
```

## Development
This project uses modern Python tooling:
- **Linter**: `ruff check .`
- **Formatter**: `ruff format .`
- **Tests**: Run unit tests with `python aucc/tests/test_colors.py` or `pytest`.

## License
Distributed under the MIT License. See `LICENSE` for more information.
