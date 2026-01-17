import os
import cv2

def save_iou_results(results, filename="iou_results.csv"):
    with open(filename, "w", encoding="utf-8") as f:
        f.write("image_name,iou\n")
        for r in results:
            f.write(f"{r['image_filename']},{r['iou_score']:.4f}\n")

def save_masks(results, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    for r in results:
        path = os.path.join(
            output_dir,
            os.path.splitext(r["image_filename"])[0] + "_mask.png"
        )
        cv2.imwrite(path, r["generated_mask"] * 255)
