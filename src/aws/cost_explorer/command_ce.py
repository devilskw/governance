from datetime import datetime
from dateutil.relativedelta import relativedelta
from aws.cost_explorer.ce import CostExplorer
from config.abstract_base import BaseBastract
from config.app_config import AppConfig
from infra.output.gen_json import JsonGenerator


class CostExplorerCommand(BaseBastract):
    ce_resource: CostExplorer
    def __init__(self, cfg: AppConfig, dh_ini: datetime, account_id: str) -> None:
        super().__init__(cfg, dh_ini, account_id)
        self.ce_resource = CostExplorer(cfg, dh_ini, account_id)

    def execute(self) -> None:
        dt_ini = self.__get_dt_ini__(6)
        filename = self.__get_filename_prefix__("Finops", "CostExplorer")

        res_total = self.ce_resource.analyze_monthly_total_cost_and_usage(dt_ini, self.dh_ini)
        self.__gen_json__(res_total, filename + "_TotalCosts")

        for tag in self.cfg.required_tag_keys:
            res_tag = self.ce_resource.analyze_monthly_by_tag_cost_and_usage(dt_ini, self.dh_ini, tag)
            self.__gen_json__(res_tag, filename + "_TotalCosts_GroupBy_Tag_"+ tag)

        res_services = self.ce_resource.analyze_monthly_grpby_services_cost_and_usage(dt_ini, self.dh_ini)
        self.__gen_json__(res_services, filename + "_TotalCosts_GroupBy_Services")

    def __get_dt_ini__(self, months_before):
        last_six_months = datetime(self.dh_ini.year, self.dh_ini.month, 1) - relativedelta(months=months_before)
        return datetime(last_six_months.year, last_six_months.month, 1)

    def __gen_json__(self, data, filename):
        JsonGenerator(filename).generate(data)
