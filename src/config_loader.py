import yaml

def load_config(path="config.yaml"):
    with open(path, "r", encoding="utf-8") as f:
        cfg = yaml.safe_load(f)

    config = {
        "paths_img": cfg["paths"]["rgb"],
        "paths_img_nrg": cfg["paths"]["nrg"],
        "paths_mask": cfg["paths"]["masks"],
        "output_dir": cfg["paths"]["output"],
        "hue_min": float(cfg["thresholds"]["hue_min"]),
        "hue_max": float(cfg["thresholds"]["hue_max"]),
        "sat_thr": float(cfg["thresholds"]["sat_thr"]),
        "val_thr": float(cfg["thresholds"]["val_thr"]),
        "num_images": int(cfg["general"]["num_images"]),
        "num_compare": int(cfg["general"]["num_compare"]),
    }

    if config["num_compare"] > config["num_images"]:
        raise ValueError("num_compare cannot exceed num_images")

    return config
