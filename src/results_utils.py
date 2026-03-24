from pathlib import Path
import csv
import logging

logger = logging.getLogger(__name__)


def append_result(csv_path, image_name, length_pixels, length_meters):

    csv_path = Path(csv_path)
    file_exists = csv_path.exists()

    with open(csv_path, mode="a", newline="") as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow(["image_name", "length_pixels", "length_meters"])

        writer.writerow([image_name, length_pixels, length_meters])
    logger.info(f"Saved results CSV: {csv_path}")