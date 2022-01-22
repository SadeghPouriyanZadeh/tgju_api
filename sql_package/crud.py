from sqlalchemy.orm import Session
from sql_package import models, schemas


def fetch_price(db: Session, price: schemas.FetchPrice):
    db_price = models.Valuable(
        name=price.name,
        gold_18=price.gold_18,
        gold_coin=price.gold_coin,
        tether=price.tether,
        bitcoin=price.bitcoin,
    )
    db.add(db_price)
    db.commit()
    db.refresh(db_price)
    return db_price