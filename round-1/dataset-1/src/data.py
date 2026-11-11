import json
import numpy as np
import pandapower.networks as pn
import pandapower as pp

# Load IEEE European LV asymmetric network as test feeder
net = pn.ieee_european_lv_asymmetric()

np.random.seed(42)
n_samples = 150

examples = []

for i in range(n_samples):
    # Sample active and reactive power injections for loads
    # The network has 55 single-phase loads or similar
    scale = np.random.uniform(0.5, 1.5, size=len(net.load))
    net.load.p_mw = net.load.p_mw * scale
    net.load.q_mvar = net.load.q_mvar * scale
    
    try:
        pp.runpp(net)
        voltages = net.res_bus[['vm_pu', 'va_degree']].values.tolist()
        injections = net.load[['p_mw', 'q_mvar']].values.tolist()
        
        example = {
            "input": json.dumps({"injections": injections}),
            "output": json.dumps({"voltages": voltages}),
            "metadata_sample_index": i,
            "metadata_scale_factor": float(np.mean(scale))
        }
        examples.append(example)
    except Exception as e:
        # If power flow fails, skip
        continue

data_out = {
    "datasets": [
        {
            "dataset": "ieee_european_lv_test_feeder",
            "examples": examples
        }
    ]
}

with open("full_data_out.json", "w") as f:
    json.dump(data_out, f, indent=2)

print(f"Successfully generated {len(examples)} examples.")
