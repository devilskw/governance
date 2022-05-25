import logging
from config.abstract_base import BaseBastract


class Compliance(BaseBastract):
    def execute(self) -> None:
        logging.debug("Starting Compliance")
