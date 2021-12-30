import pathlib

import pandas as pd

PROJECT_PATH = pathlib.Path(__file__).resolve().parent.parent
SOURCE_DATA_FILE = PROJECT_PATH / "data/source_data/wfa_girls_0-to-13-weeks_zscores.csv"

# print(SOURCE_DATA_FILE)

df = pd.read_csv(SOURCE_DATA_FILE)
print(df.shape)
print(df.columns)
