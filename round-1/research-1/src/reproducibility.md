# Gaussian Process Emulator Phase-Aware Kernel Research

This research investigates the performance of a Gaussian Process (GP) emulator equipped with a phase-aware graph kernel (Kirchhoff/Laplacian-based) for predicting per-bus phase voltages in a three-phase unbalanced low-voltage distribution feeder.

## Methodology

1.  **Feeder Setup**: Uses the IEEE PES European LV test feeder implemented in `pandapower`.
2.  **Baselines**: 
    - Radial Basis Function (RBF) kernel on load injections.
    - Plain graph-Laplacian kernel.
    - Linearised power-flow baseline (LinDistFlow with quadratic correction).
3.  **Experiments**:
    - Training sets ranging from 10 to 160 AC power flow runs (sampled household injections).
    - Evaluation metrics: RMSE and Negative Log Predictive Density (NLPD) of far-end voltages.
    - Sensitivity analysis: 10 random seeds and various train/test load splits.
    - Control: Shuffled-phase-label experiment to quantify the benefit of phase awareness.
4.  **Novelty Metric**: A minimum 20% RMSE margin over the best baseline across all splits, and determination of the crossover point in training data size where the GP emulator surpasses the physics-based baseline.

## Results

*Research could not be fully completed due to tool limitations.*

## Reproducibility

1.  Set up environment with `pandapower`, `numpy`, `scipy`, `sklearn`.
2.  Run `experiment.py` to generate power flow ground truth data.
3.  Implement GP kernels using `GPyTorch` or `scikit-learn` with custom covariance functions.
4.  Compute Kirchhoff/Laplacian matrix from the feeder admittance structure.
5.  Perform cross-validation over 10 seeds and training set sizes 10–160.
