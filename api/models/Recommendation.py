from api.core import Mixin
from .base import db


class Recommendation(Mixin, db.Model):
    """Recommendation Table."""

    __tablename__ = "recommendation"

    id = db.Column(db.Integer, unique=True, primary_key=True)
    company = db.Column(
        db.Integer, db.ForeignKey("company.id", ondelete="SET NULL"), nullable=True
    )
    ticker = db.Column(db.String, nullable=False)
    firm = db.Column(db.String, nullable=False)
    to_grade = db.Column(db.Float, nullable=False)
    recommendation_date = db.Column(db.String, nullable=False)
    

    def __init__(self, company: int, ticker: str, firm: str, to_grade: float, recommendation_date: str):
        self.company = company
        self.ticker = ticker
        self.firm = firm
        self.to_grade = to_grade
        self.recommendation_date = recommendation_date

    def __repr__(self):
        return f"<{self.ticker}: {self.firm} - {self.to_grade}>"
