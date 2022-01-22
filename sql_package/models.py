import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class valuable(Base):
    __tablename__ = "prices"
    id = sa.Column(sa.Integer, primary_key=True, index=True)
    gold_18 = sa.Column(sa.Integer)
    gold_coin = sa.Column(sa.Integer)
    tether = sa.Column(sa.Float)
    bitcoin = sa.Column(sa.Float)
