from fastapi import FastAPI
from tgju_scraper import Tgju

app = FastAPI()


@app.get("/get_prices/")
def get_item():
    return Tgju().get_all()
