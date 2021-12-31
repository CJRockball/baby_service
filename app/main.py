import pathlib

import matplotlib.pyplot as plt
import pandas as pd
from fastapi import FastAPI, Form, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")

app = FastAPI()
# app.mount("/static", StaticFiles(directory="static"), name="static")


PROJECT_PATH = pathlib.Path(__file__).resolve().parent.parent
SOURCE_DATA_FILE = PROJECT_PATH / "data/source_data/wfa_girls_0-to-13-weeks_zscores.csv"

# print(SOURCE_DATA_FILE)

# df = pd.read_csv(SOURCE_DATA_FILE)
# del_cols = ["L", "M", "S"]
# df = df.drop(columns=del_cols)
# xx = df.Week.values
# x_J = [i for i in range(len(df.Jennifer.to_list()))]
# plt.figure()
# plt.fill_between(xx, df.SD0.values, df.SD1.values, color="green", alpha=0.4)
# plt.fill_between(xx, df.SD1.values, df.SD2.values, color="yellow", alpha=0.4)
# plt.fill_between(xx, df.SD2.values, df.SD3.values, color="red", alpha=0.4)
# plt.plot(xx, df.SD0.values, color="black")
# plt.fill_between(xx, df.SD1neg.values, df.SD0.values, color="green", alpha=0.4)
# plt.fill_between(xx, df.SD2neg.values, df.SD1neg.values, color="yellow", alpha=0.4)
# plt.fill_between(xx, df.SD3neg.values, df.SD2neg.values, color="red", alpha=0.4)
# plt.scatter(x_J, df.Jennifer.values)
# plt.grid()
# plt.show()


@app.get("/")
def index_get(request: Request):

    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/")
def index_post(request: Request, input_text: str = Form(...)):
    print(input_text)
    return templates.TemplateResponse(
        "index.html", {"request": request, "input_text": input_text}
    )
