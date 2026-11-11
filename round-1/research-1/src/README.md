# Gaussian Process Emulator Phase-Aware Kernel Research

This artifact investigates whether a Gaussian Process (GP) emulator equipped with a phase-aware graph kernel (Kirchhoff/Laplacian-based) can predict per-bus phase voltages in a three-phase unbalanced low-voltage distribution feeder more accurately than standard kernels.

## Repository Structure

- `code/`: Python scripts for experiments and web search automation.
- `results/`: Search logs and experiment outputs.
- `reproducibility.md`: Step-by-step documentation on how the research was conducted.
- `.sdk_openhands_agent_struct_out.json`: Structured research output.

## How to Run

1. Ensure Python dependencies (`pandapower`, `numpy`, `scipy`, `scikit-learn`) are installed.
2. Run the simulation script:
   ```bash
   python3 code/experiment.py
   ```

## Restoring Removed Files

No files were deleted, thus no restoration is necessary.
