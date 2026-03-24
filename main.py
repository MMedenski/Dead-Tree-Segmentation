from pathlib import Path
import logging

from src.save_processed_images import process_single_image
from src.cli_utils import parse_args, setup_logger
from src.config_utils import load_config
from src.results_utils import append_result


if __name__ == "__main__":

    args = parse_args()
    config = load_config()

    images_dir = Path(args.images_dir or config["images_dir"])
    pattern = args.pattern or config["pattern"]
    log_level = args.log_level or config["log_level"]

    mode = args.mode if hasattr(args, "mode") and args.mode else config.get("mode", "otsu")

    setup_logger(log_level)
    logger = logging.getLogger(__name__)

    logger.info(f"Using config: {config}")
    logger.info(f"Mode: {mode}")

    image_files = list(images_dir.glob(pattern))

    if not image_files:
        logger.warning("No matching images found!")
        exit()

    for image_path in image_files:
        process_single_image(image_path.name, mode=mode)