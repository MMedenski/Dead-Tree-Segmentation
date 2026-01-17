import argparse

def parse_args():
    parser = argparse.ArgumentParser(
        description=(
            "Dead Tree Segmentation Pipeline (RGB + NRG)\n\n"
            "The pipeline performs classical image segmentation using RGB and NRG data,\n"
            "computes evaluation metrics (IoU, confusion matrix) and saves results to disk."
        ),
        formatter_class=argparse.RawTextHelpFormatter
    )

    # === Configuration ===
    parser.add_argument(
        "-c", "--config",
        type=str,
        default="config.yaml",
        help="Path to YAML configuration file (default: config.yaml)"
    )

    # === Segmentation thresholds ===
    parser.add_argument(
        "-h_min", "--hue_min",
        type=float,
        help="Minimum HSV hue threshold for RGB segmentation"
    )
    parser.add_argument(
        "-h_max", "--hue_max",
        type=float,
        help="Maximum HSV hue threshold for RGB segmentation"
    )
    parser.add_argument(
        "-s", "--sat_thr",
        type=float,
        help="HSV saturation threshold for RGB segmentation"
    )
    parser.add_argument(
        "-v", "--val_thr",
        type=float,
        help="HSV value (brightness) threshold for RGB segmentation"
    )

    # === General pipeline control ===
    parser.add_argument(
        "-n_img", "--num_images",
        type=int,
        help="Number of images to load or preview from the dataset"
    )
    parser.add_argument(
        "-n_cmp", "--num_compare",
        type=int,
        help="Number of images used for quantitative evaluation"
    )

    # === Input / Output paths ===
    parser.add_argument(
        "-o", "--output_dir",
        type=str,
        help="Output directory for generated masks, metrics and logs"
    )
    parser.add_argument(
        "-p_rgb", "--path_rgb",
        type=str,
        help="Path or glob pattern to RGB images (e.g. data/RGB_images/*.png)"
    )
    parser.add_argument(
        "-p_nrg", "--path_nrg",
        type=str,
        help="Path or glob pattern to NRG images (e.g. data/NRG_images/*.png)"
    )
    parser.add_argument(
        "-p_mask", "--path_mask",
        type=str,
        help="Path or glob pattern to ground truth masks (e.g. data/masks/*.png)"
    )

    # === Logging ===
    parser.add_argument(
        "--log-level",
        default="INFO",
        choices=["DEBUG", "INFO", "WARNING", "ERROR"],
        help="Logging verbosity level (default: INFO)"
    )

    return parser.parse_args()
