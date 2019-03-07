import csv
import pandas as pd


class ExcelPlayTime:
    def __init__(self):
        self.df = pd.DataFrame(columns=["Column1", "Column2", "Column3", "Column4", "Column5"])
        self.sample_data = ["Data1", "Data2", "Data3", "Data4", "Data5"]

    def write_to_excel(self):
        data_frame = self.df
        data_frame.loc["Row1"] = self.sample_data
        data_frame.loc["Row2"] = self.sample_data
        data_frame.loc["Row3"] = self.sample_data
        data_frame.to_csv("write_file.csv")


