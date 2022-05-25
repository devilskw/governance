import boto3
from abc import ABC, abstractmethod
from datetime import datetime
from config.app_config import AWSAccount, AppConfig
from botocore.config import Config


class AWSBase(ABC):
    cfg: AppConfig
    dh_ini: datetime
    account: AWSAccount
    resource_name: str
    def __init__(self, cfg: AppConfig, dh_ini: datetime, resource_name:str, account_id: str) -> None:
        self.cfg = cfg
        self.dh_ini = dh_ini
        self.resource_name = resource_name
        self.account = next(filter(lambda x: x.id == account_id, cfg.aws_accounts), AWSAccount({}))

    def __get_client__(self, oride_region_name: str = None):
        return boto3.client(
            self.resource_name,
            region_name = oride_region_name if oride_region_name != None else self.cfg.region_name,
            config = Config(
                proxies = self.cfg.proxies,
                retries = {
                    "max_attempts": self.cfg.max_retries,
                    "mode": "standard",
                },
                read_timeout = self.cfg.timeout
            ),
            verify=False,
            endpoint_url=self.cfg.endpoint_url if self.cfg.local else None
        )
