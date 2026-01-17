# Segmentation Pipeline

#1. Load RGB and NRG images
#2. Generate independent segmentation masks (RGB / NRG)
#3. Fuse masks using morphological operations
#4. Compare predicted masks with main masks
#5. Compute IoU and confusion matrix
#6. Optimize segmentation thresholds


#Import .py files from source
from src.cli import parse_args
from src.config_loader import load_config
from src.segmentation import generate_segment_mask_rgb, generate_segment_mask_nrg, fuse_masks
from src.evaluation import iou, compute_confusion_matrix
from src.io_utils import save_iou_results, save_masks

# Libraries 
import glob
from skimage import io
import cv2
import os

def main():
    args = parse_args()
    config = load_config(args.config)

    rgb_paths = sorted(glob.glob(config["paths_img"]))
    nrg_paths = sorted(glob.glob(config["paths_img_nrg"]))
    mask_paths = sorted(glob.glob(config["paths_mask"]))

    results = []

    for i in range(config["num_compare"]):
        rgb = io.imread(rgb_paths[i])
        nrg = io.imread(nrg_paths[i])
        gt = cv2.imread(mask_paths[i], cv2.IMREAD_GRAYSCALE)

        rgb_mask = generate_segment_mask_rgb(
            rgb, config["hue_min"], config["hue_max"],
            config["sat_thr"], config["val_thr"]
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

    cm = compute_confusion_matrix(results)
    print("Confusion Matrix:\n", cm)

    save_iou_results(results)
    save_masks(results, config["output_dir"])

if __name__ == "__main__":
    main()

