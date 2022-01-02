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


@app.get("/")
def index_get():
    return "Landing Page"


@app.get("/favicon.ico", include_in_schema=False)
async def favicon():
    return FileResponse(favicon_path)


@app.get("/weight")
def weight_plot():
    result = get_weight_data()
    weight_data = [result[i][1] for i in range(len(result))]
    week_data = [result[i][0] for i in range(len(result))]
    return [week_data, weight_data]


@app.get("/access_db")
def get_access_db(request: Request):
    return templates.TemplateResponse("access_db.html", {"request": request})
