# Slingshot-Manuever-Simulator


**Team:** [Veltman Okey-ejiowhor](https://github.com/VokeyJ7) & Tales Leão



## Overview

This Python-based project simulates planetary gravity assist maneuvers, demonstrating how a spacecraft’s velocity and trajectory are affected by a close flyby of a moving planet — known as the **slingshot effect**. 

It combines **physics**, **vector math**, **graph plotting**, and **real-time animation** using `NumPy`, `Matplotlib`, and `Turtle`.



## My Contributions (Veltman)

- **Physics Engine**: 
  - Built using NumPy for trigonometric and vector calculations.
  - Models spacecraft exit velocity based on entry angle, speed, and planet velocity.

- **Graphing Velocity Curves**:
  - Plotted velocity vs angle graphs using Matplotlib.
  - Validated and visualized performance with trajectory analysis.

- **Input Validation**:
  - Implemented error-checking for numeric input.
  - Enforced physical bounds (e.g., speed not resulting in imaginary values).

- **Vector Calculations**:
  - Decomposed entry and exit velocities into X and Y components.
  - Computed exit angle using trigonometry.



## Partner Contribution (Tales Leão)

- Built full **front-end animation** using Turtle:
  - Real-time spacecraft animation with visual arcs.
  - Vector overlays for entry and exit paths.
  - User input via Turtle’s `textinput()` GUI.
  - Exported data to a `.txt` file for review.



## File Overview

```bash
SlingshotSim/
├── simulation.py      # Core physics, animation, and plotting
├── input_detection part1.py       # Simple UI and input capture
├── planetillustpart2.py           # Standalone planet + vector animator
├── lastSimData.txt                # Output file with velocity/angle results
├── Plot1.png                      # Velocity curve graph (Matplotlib)
├── bgtest.png                     # Background for animation
├── visorview.png                  # Initial visor-style view
└── README.md                      # This file
