import csv
import pandas as pd


class ExcelPlayTime:
    def __init__(self):
        self.df = pd.DataFrame(columns=["Column1", "Column2", "Column3", "Column4", "Column5"])
        self.sample_data_row1 = ["Data11", "Data12", "Data13", "Data14", "Data15"]
        self.sample_data_row2 = ["Data21", "Data22", "Data23", "Data24", "Data25"]
        self.sample_data_row3 = ["Data31", "Data32", "Data33", "Data34", "Data35"]

    def write_to_excel(self):
        data_frame = self.df
        data_frame.loc["Row1"] = self.sample_data_row1
        data_frame.loc["Row2"] = self.sample_data_row2
        data_frame.loc["Row3"] = self.sample_data_row3

        # Set some styles
        data_frame = data_frame.style.applymap(apply_formatting)

        data_frame.to_excel("write_file.xlsx", sheet_name='Sheet1')


def apply_formatting(val):
    if val == "Data11":
        return 'color: red'
    if val == "Data22":
        return 'color: green'
    if val == "Data33":
        return 'color: blue'
    if val == "Data35":
        return 'background-color: yellow'
    if val == "Data15":
        return 'font-size: 150%'
    return 'color: black'


excel_play_time = ExcelPlayTime()
excel_play_time.write_to_excel()
