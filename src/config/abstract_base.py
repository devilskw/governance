import boto3
from abc import abstractmethod
from datetime import datetime
from config.app_config import AppConfig
from config.aws_base import AWSBase


class BaseBastract(AWSBase):
    def __init__(self, cfg: AppConfig, dh_ini: datetime, account_id: str) -> None:
        super().__init__(cfg, dh_ini, None, account_id)
        boto3.setup_default_session(profile_name = self.cfg.get_aws_profile(account_id))

    @abstractmethod
    def execute(self) -> None:
        pass

    def __get_filename_prefix__(self, category: str, operation: str):
        return self.dh_ini.strftime(self.cfg.dh_format) + "_" + category + "_" + operation + "_" + self.account.name + "_" + self.account.id
