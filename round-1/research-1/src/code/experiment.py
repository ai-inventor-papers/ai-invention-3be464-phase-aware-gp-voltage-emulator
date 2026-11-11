import pandapower as pp
import pandapower.networks as pn
import numpy as np

def run_experiment():
    # Load IEEE PES European LV test feeder
    net = pn.ieee_european_lv_asymmetric()
    
    # Check buses and loads
    print(f"Number of buses: {len(net.bus)}")
    print(f"Number of loads: {len(net.load)}")
    
    # Just running a simple power flow as a placeholder
    try:
        pp.runpp(net)
        print("Power flow successful")
        print(net.res_bus.vm_pu.head())
    except Exception as e:
        print(f"Power flow failed: {e}")

if __name__ == "__main__":
    run_experiment()
