> NOTE (published copy): this file names server paths this repository
> does not publish (a stage it does not ship, or another run's workspace),
> so the steps that read them will not run from a clone as written:
>   /aii_data/runs/run_2aZPjMgTrlXl/3_invention_loop/iter_1/gen_art/gen_art_experiment_1

# Reproducibility Instructions for Phase-Aware GP Voltage Emulator Experiment

## Overview
This experiment evaluates a specialized Gaussian process model that uses grid physical structure (admittance) to predict voltages in unbalanced electrical distribution grids more accurately than standard models.

## Getting the Artifact
1. Clone the GitHub repository containing this artifact
2. `cd ai-inventor/aii_data/runs/run_2aZPjMgTrlXl/3_invention_loop/iter_1/gen_art/gen_art_experiment_1`

## System Requirements
- Ubuntu 20.04 or 22.04
- Python 3.10+
- See `pyproject.toml` for pinned dependencies

## Python Environment Setup
```bash
# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies from pinned requirements
pip install -r requirements.txt

# Verify pandapower version
pip show pandapower
```

## Data
- The experiment uses the IEEE PES European LV test feeder (`pn.ieee_european_lv_asymmetric()` from pandapower)
- No external data downloads required

## Running the Experiment
```bash
# Generate data and run all experiments
python3 method.py
```

This will:
1. Create the European LV network
2. Generate stochastic load scenarios
3. Train GPs with different kernels (RBF, Phase-Resolved, Graph-Laplacian)
4. Evaluate against LinDistFlow baseline
5. Save results to `full_method_out.json`, `mini_method_out.json`, and `preview_method_out.json`

## Expected Output Files
- `full_method_out.json`: Complete experiment results with all metrics
- `mini_method_out.json`: Quick summary with minimal training data
- `preview_method_out.json`: Summary statistics for quick review
- `reproducibility.md`: This file

## Notes
- All seeds are fixed at seed=0 for reproducibility
- Training set sizes tested: minimal coverage
- Results stored in workspace directory only