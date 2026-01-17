import argparse

def parse_args():
    parser = argparse.ArgumentParser(
        description="Dead Tree Segmentation Pipeline (RGB + NRG)"
    )

    parser.add_argument("-c", "--config", type=str, default="config.yaml")
    parser.add_argument("-h_min", "--hue-min", type=float)
    parser.add_argument("-h_max", "--hue-max", type=float)
    parser.add_argument("-s", "--sat-thr", type=float)
    parser.add_argument("-v", "--val-thr", type=float)
    parser.add_argument("-ni", "--num-images", type=int)
    parser.add_argument("-nc", "--num-compare", type=int)
    parser.add_argument("-o", "--output-dir", type=str)

    return parser.parse_args()
