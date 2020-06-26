from api.core import Mixin
from .base import db


class Company(Mixin, db.Model):
    """Company Table."""

    __tablename__ = "company"

    id = db.Column(db.Integer, unique=True, primary_key=True)
    short_name = db.Column(db.String, nullable=False)
    sector = db.Column(db.String, nullable=False)
    address = db.Column(db.String, nullable=False)
    ticker = db.Column(db.String, nullable=False, unique=True)
    

    def __init__(self, short_name: str, sector: str, address: str, ticker: str):
        self.short_name = short_name
        self.sector = sector
        self.address = address
        self.ticker = ticker

    def __repr__(self):
        return f"<{self.ticker}>"
