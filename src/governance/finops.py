from datetime import datetime
import logging
from aws.cost_explorer.command_ce import CostExplorerCommand
from config.abstract_base import BaseBastract
from config.app_config import AppConfig


class Finops(BaseBastract):
    commands: list[BaseBastract] = []
    def __init__(self, cfg: AppConfig, dh_ini: datetime, account_id: str) -> None:
        super().__init__(cfg, dh_ini, account_id)
        self.commands.append(CostExplorerCommand(self.cfg, self.dh_ini, self.account.id))

    def execute(self) -> None:
        if not self.cfg.finops:
            logging.debug("Bypassing Finops")
            return
        logging.debug("Starting Finops")
        #TODO depois implementar um "intermediario" com mediator, para desacoplar
        for comm in self.commands:
            comm.execute()
