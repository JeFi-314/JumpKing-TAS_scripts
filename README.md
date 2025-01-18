# JumpKing-TAS Scripts

I will update all my Tool-Assisted Speedrun (TAS) scripts for Jump King here. You can also find useful Python scripts and game values here.

> **Note:** This repository is placed in a subfolder named `TAS` within the Jump King folder.

## Repository Structure

### Map-specific Folders (`JumpKing-TAS_scripts/<map_name>`)

Those folders contains the full TAS scripts for demonstrating how fast specific map can be completed. For every map, there are area-specific TAS files and a full-game TAS file:

- **Area TAS Files** (`<area number>-<area name>.tas`):

  - Standalone scripts for completing individual areas, starting from the beginning of the area and ending at the next area.

- **Full Game TAS File** (`JumpKing.tas`):

  - Combines all area TAS files, along with loading and ending scripts, to perform a complete game run from the main menu.

### SR Simulating Folder (`JumpKing-TAS_scripts/SR_simulating/<short_name>`)

This folder contains TAS scripts for simulating how fast a human player could complete the maps. The structure is the same as the map-specific folder in root, with area-specific TAS files and a full-game TAS file.

### Load Folder (`Load`)

Contains commonly used scripts for loading maps from the main menu (excluding the "Press Start").

### Constants Folder (`constants`)

Contains game values and sample test scripts.

### General TAS Scripts (Root Folder)

Scripts that do not belong to the `Load` folder. For example:

- **`Press_start.tas`**: Performs the "Press Start" action and waits until the menu appears.

### Python Scripts (Root Folder)

Python scripts designed to help format and update the TAS scripts.
