from datetime import datetime
from config.app_config import AppConfig
from config.aws_base import AWSBase


class CostExplorer(AWSBase):
    default_region = "us-east-1"
    def __init__(self, cfg: AppConfig, dh_ini: datetime, account_id: str):
        super().__init__(cfg, dh_ini, "ce", account_id)

    def analyze_monthly_total_cost_and_usage(self, dt_ini: datetime, dt_fim: datetime):
        return self.__get_client__(self.default_region).get_cost_and_usage(
            Metrics = ["AmortizedCost", "BlendedCost", "NetAmortizedCost", "NetUnblendedCost", "NormalizedUsageAmount", "UnblendedCost"],
            TimePeriod = {
                "Start": dt_ini.strftime(self.cfg.aws_date_format),
                "End": dt_fim.strftime(self.cfg.aws_date_format)
            },
            Granularity = "MONTHLY"
        )

    def analyze_monthly_grpby_services_cost_and_usage(self, dt_ini: datetime, dt_fim: datetime):
        return self.__get_client__().get_cost_and_usage_with_resources(
            Metrics = ["AmortizedCost", "BlendedCost", "NetAmortizedCost", "NetUnblendedCost", "NormalizedUsageAmount", "UnblendedCost", "UnblendedCost"],
            TimePeriod = {
                "Start": dt_ini.strftime(self.cfg.aws_date_format),
                "End": dt_fim.strftime(self.cfg.aws_date_format)
            },
            Granularity = "MONTHLY",
            GroupBy = [
                {
                    "Type" : "DIMENSION ",
                    "Key": "SERVICE"
                }
            ]
        )

    def analyze_monthly_by_tag_cost_and_usage(self, dt_ini: datetime, dt_fim: datetime, tag):
        return self.__get_client__().get_cost_and_usage_with_resources(
        Metrics = ["UnblendedCost"],
        TimePeriod = {
            "Start": dt_ini.strftime(self.cfg.aws_date_format),
            "End": dt_fim.strftime(self.cfg.aws_date_format)
        },
        Granularity = "MONTHLY",
        GroupBy = [
            {
                "Type" : "TAG ",
                "Key": tag
            }
        ]
    )

    def get_finops_ec2_recomendations(self):
        return self.__get_client__().get_rightsizing_recommendation(
            Configuration = {
                "RecommendationTarget": "SAME_INSTANCE_FAMILY",
                "BenefitsConsidered": True
            },
            Service = "AmazonEC2 "
        )