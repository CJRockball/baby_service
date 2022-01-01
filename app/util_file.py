import pathlib

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

from app.db_utils import get_weight_data


def plot_weight():
    PROJECT_PATH = pathlib.Path(__file__).resolve().parent.parent
    SOURCE_DATA_FILE = (
        PROJECT_PATH / "data/source_data/wfa_girls_0-to-13-weeks_zscores.csv"
    )
    ARTIFACT_PATH = PROJECT_PATH / "static"

    df = pd.read_csv(SOURCE_DATA_FILE)
    del_cols = ["L", "M", "S"]
    df = df.drop(columns=del_cols)
    xx = df.Week.values

    result = get_weight_data()
    y_J = [result[i][1] for i in range(len(result))]  # df.Week.values
    x_J = [
        result[i][0] for i in range(len(result))
    ]  # [i for i in range(len(df.Jennifer.to_list()))]

    plt.figure()
    plt.fill_between(xx, df.SD0.values, df.SD1.values, color="green", alpha=0.4)
    plt.fill_between(xx, df.SD1.values, df.SD2.values, color="yellow", alpha=0.4)
    plt.fill_between(xx, df.SD2.values, df.SD3.values, color="red", alpha=0.4)
    plt.plot(xx, df.SD0.values, color="black")
    plt.fill_between(xx, df.SD1neg.values, df.SD0.values, color="green", alpha=0.4)
    plt.fill_between(xx, df.SD2neg.values, df.SD1neg.values, color="yellow", alpha=0.4)
    plt.fill_between(xx, df.SD3neg.values, df.SD2neg.values, color="red", alpha=0.4)
    plt.scatter(x_J, y_J)
    plt.grid()
    plt.savefig(ARTIFACT_PATH / "weight.jpg")

    return
