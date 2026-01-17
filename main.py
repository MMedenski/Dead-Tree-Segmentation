from src.cli import parse_args
from src.config_loader import load_config
from src.segmentation import (
    generate_segment_mask_rgb,
    generate_segment_mask_nrg,
    fuse_masks
)
from src.evaluation import iou, compute_confusion_matrix
from src.io_utils import save_iou_results, save_masks

import glob
from skimage import io
import cv2
import os
import logging


def main():
    # === Logging setup ===
    logging.basicConfig(
        level=logging.INFO,
        format="[%(levelname)s] %(message)s"
    )

    # === Parse CLI ===
    args = parse_args()

    # === Load config from YAML ===
    config = load_config(args.config)

    # === CLI overrides config ===

    # Output path
    if args.output_dir:
        config["output_dir"] = args.output_dir

    # Input paths
    if args.path_rgb:
        config["paths_img"] = args.path_rgb
    if args.path_nrg:
        config["paths_img_nrg"] = args.path_nrg
    if args.path_mask:
        config["paths_mask"] = args.path_mask

    # Thresholds
    if args.hue_min is not None:
        config["hue_min"] = args.hue_min
    if args.hue_max is not None:
        config["hue_max"] = args.hue_max
    if args.sat_thr is not None:
        config["sat_thr"] = args.sat_thr
    if args.val_thr is not None:
        config["val_thr"] = args.val_thr

    # General
    if args.num_images is not None:
        config["num_images"] = args.num_images
    if args.num_compare is not None:
        config["num_compare"] = args.num_compare

    # === Load image paths ===
    rgb_paths = sorted(glob.glob(config["paths_img"]))
    nrg_paths = sorted(glob.glob(config["paths_img_nrg"]))
    mask_paths = sorted(glob.glob(config["paths_mask"]))

    assert rgb_paths and nrg_paths and mask_paths, "No input files found"

    if config["num_images"] is not None:
        rgb_paths = rgb_paths[:config["num_images"]]
        nrg_paths = nrg_paths[:config["num_images"]]
        mask_paths = mask_paths[:config["num_images"]]

    # === Number of images used for evaluation ===
    n = min(
        config["num_compare"],
        len(rgb_paths),
        len(nrg_paths),
        len(mask_paths)
    )

    results = []
    # === Main processing loop ===
    for i in range(n):
        rgb = io.imread(rgb_paths[i])
        nrg = io.imread(nrg_paths[i])
        gt = cv2.imread(mask_paths[i], cv2.IMREAD_GRAYSCALE)

        rgb_mask = generate_segment_mask_rgb(
            rgb,
            config["hue_min"],
            config["hue_max"],
            config["sat_thr"],
            config["val_thr"]
        )

        nrg_mask = generate_segment_mask_nrg(nrg)
        fused = fuse_masks(rgb_mask, nrg_mask)

        score = iou(fused, gt)

        results.append({
            "image_filename": os.path.basename(rgb_paths[i]),
            "generated_mask": fused,
            "main_mask": gt,
            "iou_score": score
        })

    # === Evaluation ===
    logging.info(f"{n} images have been loaded to processing\n and {len(results)} images have been processed correctly")
    cm = compute_confusion_matrix(results)
    logging.info(f"Confusion Matrix:\n{cm}")

    # === Save results ===
    save_iou_results(results)
    save_masks(results, config["output_dir"])

    logging.info("Pipeline finished successfully")


if __name__ == "__main__":
    main()
