import pathlib

import matplotlib.pyplot as plt
import pandas as pd
from fastapi import FastAPI, Form, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.responses import FileResponse

from app.db import reset_db
from app.db_utils import add_weight_table
from app.util_file import plot_weight

templates = Jinja2Templates(directory="templates")
app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
favicon_path = "favicon.ico"

PROJECT_PATH = pathlib.Path(__file__).resolve().parent.parent
SOURCE_DATA_FILE = PROJECT_PATH / "data/source_data/wfa_girls_0-to-13-weeks_zscores.csv"


@app.get("/")
def index_get(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/")
def index_post(request: Request, input_text: str = Form(...)):
    return templates.TemplateResponse(
        "index.html", {"request": request, "input_text": input_text}
    )


@app.get("/favicon.ico", include_in_schema=False)
async def favicon():
    return FileResponse(favicon_path)


@app.get("/weight")
def weight_plot(request: Request):
    plot_weight()
    return templates.TemplateResponse("weight.html", {"request": request})


@app.get("/access_db")
def get_access_db(request: Request):
    return templates.TemplateResponse("access_db.html", {"request": request})


@app.post("/access_db")
def post_access_db(
    request: Request,
    week: int = Form(...),
    weight: float = Form(...),
    submit: str = Form(...),
):

    if submit == "Update Weight":
        add_weight_table(week, weight)

    return templates.TemplateResponse("access_db.html", {"request": request})

