import logging
import os

def setup_logging(script_name):
    log_dir = r"C:\Users\Suresh Goud\Documents\Intern\logs"
    os.makedirs(log_dir, exist_ok=True)

    logger = logging.getLogger(script_name)
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        log_path = f"{log_dir}\\{script_name}.log"
        handler = logging.FileHandler(log_path, mode="w")

        formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(message)s"
        )

        handler.setFormatter(formatter)
        logger.addHandler(handler)

    return logger
