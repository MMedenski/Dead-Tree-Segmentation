import argparse

def parse_args():
    parser = argparse.ArgumentParser(
        description="Dead Tree Segmentation Pipeline (RGB + NRG)"
    )

    parser.add_argument("-c", "--config", type=str, default="config.yaml")
    parser.add_argument("-h_min", "--hue_min", type=float)
    parser.add_argument("-h_max", "--hue_max", type=float)
    parser.add_argument("-s", "--sat_thr", type=float)
    parser.add_argument("-v", "--val_thr", type=float)
    parser.add_argument("-n_img", "--num_images", type=int)
    parser.add_argument("-n_cmp", "--num_compare", type=int)
    parser.add_argument("-o", "--output_dir", type=str)
    parser.add_argument("-p_rgb", "--path_rgb", type=str)
    parser.add_argument("-p_nrg", "--path_nrg", type=str)
    parser.add_argument("-p_mask", "--path_mask", type=str)

    parser.add_argument(
        "--log-level",
        default="INFO",
        choices=["DEBUG", "INFO", "WARNING", "ERROR"]
    )

    return parser.parse_args()


