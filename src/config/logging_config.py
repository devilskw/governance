import logging

from config.app_config import AppConfig

def observability_log_config(config: AppConfig):
    log_level = logging.DEBUG if config.debug else logging.INFO
    log_format = "%(asctime)s [%(levelname)s] %(message)s"
    if config.local:
        logging.basicConfig(
            level=log_level, format=log_format,
            handlers=[
                logging.FileHandler("logging.log"),
                logging.StreamHandler()
            ]
        )
    else:
        logging.basicConfig(level=log_level, format=log_format,handlers=[logging.StreamHandler()])