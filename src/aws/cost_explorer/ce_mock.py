from datetime import datetime
from config.app_config import AppConfig
from config.aws_base import AWSBase
from infra.input.read_json import JsonReader


class CostExplorerMock(AWSBase):
    default_region = "us-east-1"
    def __init__(self, cfg: AppConfig, dh_ini: datetime, account_id: str):
        super().__init__(cfg, dh_ini, "ce", account_id)

    def analyze_monthly_total_cost_and_usage(self, dt_ini: datetime, dt_fim: datetime):
        return JsonReader("/assets/mock/cost_explorer/analyze_monthly_total_cost_and_usage").read()

    def analyze_monthly_grpby_services_cost_and_usage(self, dt_ini: datetime, dt_fim: datetime):
        return JsonReader("/assets/mock/ce/analyze_monthly_grpby_services_cost_and_usage").read()

    def analyze_monthly_by_tag_cost_and_usage(self, dt_ini: datetime, dt_fim: datetime, tag):
        return JsonReader("/assets/mock/ce/analyze_monthly_by_tag_cost_and_usage").read()

    def get_finops_ec2_recomendations(self):
        return JsonReader("/assets/mock/ce/get_finops_ec2_recomendations").read()