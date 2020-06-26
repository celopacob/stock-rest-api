from api.core import Mixin
from .base import db


class Price(Mixin, db.Model):
    """Price Table."""

    __tablename__ = "price"

    id = db.Column(db.Integer, unique=True, primary_key=True)
    company = db.Column(
        db.Integer, db.ForeignKey("company.id", ondelete="SET NULL"), nullable=True
    )
    ticker = db.Column(db.String, nullable=False)
    open = db.Column(db.Float, nullable=False)
    high = db.Column(db.Float, nullable=False)
    low = db.Column(db.Float, nullable=False)
    close = db.Column(db.Float, nullable=False)
    volume = db.Column(db.Integer, nullable=False)
    price_date = db.Column(db.String, nullable=False)
    

    def __init__(
                    self, 
                    company: int,
                    ticker: str, 
                    open: float, 
                    high: float, 
                    low: float, 
                    close: float, 
                    volume: int, 
                    price_date: str
                ):
        self.company = company,
        self.ticker = ticker
        self.open = open
        self.high = high
        self.low = low
        self.close = close
        self.volume = volume
        self.price_date = price_date

    def __repr__(self):
        return f"<{self.ticker}>"
