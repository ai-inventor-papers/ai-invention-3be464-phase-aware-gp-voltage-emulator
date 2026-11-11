import json

# Load full data
with open("full_data_out.json", "r") as f:
    data = json.load(f)

# Create mini dataset (3 examples)
mini_data = {
    "datasets": [
        {
            "dataset": "ieee_european_lv_asymmetric",
            "examples": data["datasets"][0]["examples"][:3]
        }
    ]
}
with open("mini_data_out.json", "w") as f:
    json.dump(mini_data, f, indent=2)

# Create preview dataset (10 examples)
preview_data = {
    "datasets": [
        {
            "dataset": "ieee_european_lv_asymmetric",
            "examples": data["datasets"][0]["examples"][:10]
        }
    ]
}
with open("preview_data_out.json", "w") as f:
    json.dump(preview_data, f, indent=2)
