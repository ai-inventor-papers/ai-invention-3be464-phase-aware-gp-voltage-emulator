# Reproduction Instructions

1. **Environment Setup**
   Clone the repository and `cd` into the dataset folder:
   ```bash
   cd gen_art_dataset_1
   python3 -m venv .venv
   source .venv/bin/activate
   pip install pandapower numpy pandas
   pip freeze > requirements.txt
   ```

2. **Data Generation**
   The dataset is generated using the `pandapower` library.
   ```bash
   python3 data.py
   ```
   This will generate `full_data_out.json`.
   To create preview/mini variants:
   ```bash
   python3 create_variants.py
   ```

3. **Results**
   The generated `full_data_out.json` contains the simulated grid data used for Gaussian-process emulator experiments.
