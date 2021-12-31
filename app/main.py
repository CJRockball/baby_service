import pathlib

import matplotlib.pyplot as plt
import pandas as pd
from fastapi import FastAPI, Form, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.util_file import plot_weight

templates = Jinja2Templates(directory="templates")

app = FastAPI()
# app.mount("/static", StaticFiles(directory="static"), name="static")


PROJECT_PATH = pathlib.Path(__file__).resolve().parent.parent
SOURCE_DATA_FILE = PROJECT_PATH / "data/source_data/wfa_girls_0-to-13-weeks_zscores.csv"

# print(SOURCE_DATA_FILE)


@app.get("/")
def index_get(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/")
def index_post(request: Request, input_text: str = Form(...)):
    plot_weight()
    print(input_text)
    return templates.TemplateResponse(
        "index.html", {"request": request, "input_text": input_text}
    )
