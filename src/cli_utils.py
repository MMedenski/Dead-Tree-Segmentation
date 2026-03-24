import argparse
import logging


def parse_args():
    parser = argparse.ArgumentParser(
        description="Road detection from GeoTIFF images"
    )

    parser.add_argument(
        "--images_dir",
        type=str,
        default=None,
        help="Directory with input images"
    )

    parser.add_argument(
        "--pattern",
        type=str,
        default=None,
        help="Filename pattern to match"
    )

    parser.add_argument(
        "--log_level",
        type=str,
        default=None,
        choices=["DEBUG", "INFO", "WARNING", "ERROR"],
        help="Logging level"
    )
    
    parser.add_argument(
        "--mode",
        type=str,
        default="otsu",
        choices=["otsu", "ai"],
        help="Processing mode: otsu or ai"
    )

    return parser.parse_args()


def setup_logger(level_str):
    level = getattr(logging, level_str.upper())

    logging.basicConfig(
        level=level,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s"
    )  