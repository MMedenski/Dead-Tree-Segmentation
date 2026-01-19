import logging
import os
import sys


def setup_logger(
    name: str = "dead_tree_pipeline",
    level: int = logging.INFO,
    log_dir: str = "logs",
    log_file: str = "pipeline.log"
) -> logging.Logger:
    """
    Sets up a logger that outputs logs to both console and file.

    Parameters:
    - name: logger name
    - level: logging level (e.g. logging.INFO, logging.DEBUG)
    - log_dir: directory where log files are stored
    - log_file: name of the log file

    Returns:
    - configured logging.Logger instance
    """

    # Create logs directory if it does not exist
    os.makedirs(log_dir, exist_ok=True)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.propagate = False  # prevent duplicate logs from root logger

    # Avoid adding handlers multiple times
    if logger.handlers:
        return logger

    formatter = logging.Formatter(
        "[%(asctime)s] [%(levelname)s] %(name)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    # === Console handler ===
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(level)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # === File handler ===
    file_path = os.path.join(log_dir, log_file)
    file_handler = logging.FileHandler(file_path, encoding="utf-8")
    file_handler.setLevel(level)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    logger.info("Logger initialized")
    logger.info(f"Log file: {file_path}")

    return logger
