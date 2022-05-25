from datetime import datetime
import logging
from config.app_config import AppConfig
from config.logging_config import observability_log_config
from config.abstract_base import BaseBastract
from governance.compliance import Compliance
from governance.finops import Finops

config = AppConfig()
observability_log_config(config)
dh_ini = datetime.now()
logging.debug(f"Starting: {dh_ini}")
executions: dict[str, BaseBastract] = {
    "compliance": Compliance,
    "finops": Finops
}
for account in config.aws_accounts:
    operation = executions.get("finops")(config, dh_ini, account.id)
    logging.debug(f"Starting executing finops for account {account.name}: {datetime.now()}")
    operation.execute() if "finops" in executions else {}
    logging.debug(f"Finished executing finops for account {account.name}: {datetime.now()}")

logging.debug(f"End: {datetime.now()}")
