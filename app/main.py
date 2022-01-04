import logging
import pathlib

from fastapi import FastAPI, Form, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.responses import FileResponse

from app.db import reset_db
from app.db_utils import add_weight_table, get_weight_data
from app.util_file import plot_weight

templates = Jinja2Templates(directory="templates")
app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
favicon_path = "favicon.ico"

PROJECT_PATH = pathlib.Path(__file__).resolve().parent.parent
SOURCE_DATA_FILE = PROJECT_PATH / "data/source_data/wfa_girls_0-to-13-weeks_zscores.csv"
LOG_FILE = PROJECT_PATH / "logs/info.log"

logging.basicConfig(
    filename=LOG_FILE,
    format="%(asctime)s %(levelname)-8s %(message)s",
    level=logging.INFO,
)


@app.get("/")
def index_get():
    logging.info("Opened landing page")
    return "Landing Page"


@app.get("/favicon.ico", include_in_schema=False)
async def favicon():
    logging.info("Opened favicon")
    return FileResponse(favicon_path)


@app.get("/weight")
def weight_plot():
    logging.info("Opened weight page")
    result = get_weight_data()
    return dict(result)


@app.get("/access_db")
def get_access_db(week: int, weight: float, status_code=201):
    logging.info("Opened access_db page")
    add_weight_table(week, weight)
    return {"week": week, "weight": weight}


@app.get("/reset_db")
def db_reset(statuscode=200):
    logging.info("Opened reset_db page")
    reset_db()
    result = get_weight_data()
    return dict(result)
