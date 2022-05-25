import os
import json

from config.aws_account import AWSAccount

class AppConfig:
    local: bool
    debug: bool
    finops: bool
    compliance: bool
    compliance_tag_prefix: str
    required_tag_keys: list[str]
    region_name: str
    lang: str
    timeout: int
    max_retries: int
    endpoint_url: str
    dh_format: str
    aws_accounts: list[AWSAccount]
    aws_date_format = "%Y-%m-%d"
    def __init__(self):
        self.local                  = bool(os.environ.get("LOCAL_ENVIRONMENT", "false"))
        self.debug                  = bool(os.environ.get("DEBUG", "false"))
        self.finops                 = bool(os.environ.get("FINOPS","true"))
        self.compliance             = bool(os.environ.get("COMPLIANCE","true"))
        self.compliance_tag_prefix  = os.environ.get("COMPLIANCE_TAG_PREFIX","c7n")
        self.required_tag_keys      = (os.environ.get("REQUIRED_TAG_KEYS","[]")).split(",")
        self.region_name            = os.environ.get("REGION_NAME","sa-east-1")
        self.lang                   = os.environ.get("LANGUAGE","en")
        self.timeout                = int(os.environ.get("TIMEOUT", "60"))
        self.max_retries            = int(os.environ.get("MAX_RETRIES","4"))
        self.proxies                = os.environ.get("PROXIES", None)
        if self.proxies != None and len(self.proxies) == 0:
            self.proxies = None
        self.endpoint_url           = os.environ.get("ENDPOINT_URL", None)
        self.dh_format              = os.environ.get("DH_FORMAT", "%Y%m%d_%H%M%S")
        accounts = json.loads(os.environ.get("AWS_ACCOUNTS","[]"))
        self.aws_accounts = list(map(lambda a: AWSAccount(a), accounts ))

    def get_aws_account_by_id(self, account_id: str) -> AWSAccount:
        return next(filter(lambda x:x.id == account_id, self.aws_accounts), None)

    def get_aws_profile(self, account_id: str):
        account = self.get_aws_account_by_id(account_id)
        return (account.profile_prefix + "-" + account.name) if account != None else None

