from xlsxwriter.workbook import Workbook
from xlsxwriter.worksheet import Worksheet
import xlsxwriter

class ExcelGenerator:
    def __init__(self, filename: str):
        self.workbook = Workbook(xlsxwriter.workbook(filename + ".xlsx"))
        self.format_bold = self.workbook.add_format({{"bold": 1}})

    def __del__(self):
        self.workbook.close()

    def create_sheet(self, name: str):
        return Worksheet(self.workbook.add_worksheet(name))

    def generate(self, sheet: Worksheet, data: list):
        if len(data) == 0:
            return
        self.__generate_title__(sheet, data[0])
        for item_index in range(0, len(data)-1):
            self.__generate_row__(sheet, data[item_index], item_index+1)

    def __generate_title__(self, sheet: Worksheet, item):
        if len(item.__dict__.keys()) <= 0:
            return
        for col_ix in range(0, len(item.__dict__.keys())-1):
            title_row_ix = 0
            sheet.write_string(title_row_ix, col_ix, item.__dict__.keys()[col_ix], self.format_bold)

    def __generate_row__(self, sheet: Worksheet, item, row_index):
        for col_ix in range(0, len(item.__dict__.values())-1):
            sheet.write(row_index, col_ix, item.__dict__.values()[col_ix])
