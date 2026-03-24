import logging
from pathlib import Path
from skimage import io

from src.load_image import load_image
from src.road_segmentation import extract_road_mask
from src.road_centerline import extract_road_centerline
from src.road_length import compute_road_length
from src.geotiff_utils import get_pixel_size_meters
from src.results_utils import append_result
from src.road_segmentation_ai import extract_road_mask_ai

logger = logging.getLogger(__name__)


def process_single_image(image_name, mode="otsu", output_dir="output"):

    image = load_image(image_name)

    output_path = Path(__file__).resolve().parent.parent / output_dir
    output_path.mkdir(exist_ok=True)

    if mode == "ai":
        road_mask = extract_road_mask_ai(image)
        suffix = "_ai"
    else:
        road_mask = extract_road_mask(image)
        suffix = ""

    centerline = extract_road_centerline(road_mask)

    pixel_size_m = get_pixel_size_meters(f"images/{image_name}")

    logger.info(f"[{mode.upper()}] Processing: {image_name}")
    logger.info(f"Pixel size: {pixel_size_m}")

    road_length_pixels, road_length_meters = compute_road_length(
        centerline,
        pixel_size_m
    )

    base_name = Path(image_name).stem

    road_output = output_path / f"{base_name}_mask{suffix}.png"
    centerline_output = output_path / f"{base_name}_centerline{suffix}.png"

    io.imsave(road_output, road_mask * 255)
    io.imsave(centerline_output, centerline * 255, check_contrast=False)

    logger.info(f"Saved mask: {road_output}")
    logger.info(f"Saved centerline: {centerline_output}")
    logger.info(f"Length pixels: {road_length_pixels}")
    logger.info(f"Length meters: {road_length_meters}")

    csv_path = output_path / "results.csv"

    append_result(
        csv_path,
        image_name + suffix,
        road_length_pixels,
        road_length_meters
    )

    logger.info(f"Saved results CSV: {csv_path}")

    return road_output, centerline_output, road_length_pixels, road_length_meters