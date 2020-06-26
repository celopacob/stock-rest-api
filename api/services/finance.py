"""
Provide implementation for finance services.
"""
from typing import (
    Dict,
    List,
    Union,
)
from api.core import logger
import yfinance as yf


class Finance:
    """
    YFinance services object implementation.
    """

    def get_company_info(self, ticker: str):
        return yf.Ticker(ticker).info

    def get_prices(self, ticker: str):
        prices_data = yf.Ticker(ticker).history(period="5d", progress=False)
        prices = {
            str(index): {
                'open': open,
                'high': high,
                'low': low,
                'close': close,
                'volume': volume,
                'date': index
            }

            for index, open, high, low, close, volume in zip(
                prices_data.index,
                prices_data.Open,
                prices_data.High,
                prices_data.Low,
                prices_data.Close,
                prices_data.Volume
            )
        }
        return prices
    
    def get_recommendations(self, ticker: str):
        parser_dict: Dict[str, Union[int, float]] = {
            'Buy': 1,
            'Neutral': 0,
            'Strong Buy': 1.5,
            'Sell': -1,
            'Strong Sell': -1.5,
            'Positive': 1,
            'Negative': -1,
        }

        recommendations = yf.Ticker(ticker).recommendations
        recommendations = {
            str(index): {
                'date': index,
                'firm': firm,
                'to_grade': parser_dict.get(to_grade, 0),
            }

            for index, firm, to_grade in zip(
                recommendations.index, recommendations.Firm, recommendations['To Grade'],
            )
        }

        return recommendations