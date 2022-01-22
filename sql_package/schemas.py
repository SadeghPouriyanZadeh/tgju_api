from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class PriceCreate(BaseModel):
    name: str
    gold_18: int
    gold_coin: int
    tether: float
    bitcoin: float


class PriceRead(BaseModel):
    id: int
    name: str
    gold_18: int
    gold_coin: int
    tether: float
    bitcoin: float
