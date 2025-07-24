import os
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

def save_str_to_txt(
    content: str,
    file_path: str
) -> str:
    if not os.path.exists(os.path.dirname(file_path)):
        os.makedirs(os.path.dirname(file_path))
    
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
