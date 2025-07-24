import yaml
import logging
from typing import Dict
from colorlog import ColoredFormatter

def load_config(
    path: str
) -> Dict[str, str]:
    with open(path, "r") as file:
        return yaml.safe_load(file)

def create_colored_logger(
    name: str = "pipeline",
    level=logging.INFO
) -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(level)

    if not logger.handlers:
        handler = logging.StreamHandler()
        formatter = ColoredFormatter(
            fmt="%(log_color)s[%(levelname)s] - %(message)s",
            datefmt="%Y-%m-%d",
            log_colors={
                'DEBUG':    'cyan',
                'INFO':     'green',
                'WARNING':  'yellow',
                'ERROR':    'red',
                'CRITICAL': 'bold_red',
            }
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    return logger
