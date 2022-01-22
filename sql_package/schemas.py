from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class FetchPrice(BaseModel):
    name: str
    gold_18: int
    gold_coin: int
    tether: float
    bitcoin: float
