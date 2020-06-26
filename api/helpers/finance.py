from api.core import logger
from api.services.finance import Finance
from api.models import db, Company, Price, Recommendation


def set_companies():
    tickers = ["FB", "AAPL", "NFLX", "GOOG"]
    for ticker in tickers:
        company_entries = Company.query.filter_by(ticker=ticker).count()
        if company_entries == 0:
            company_info = Finance().get_company_info(ticker)
            company = Company(
                short_name=company_info["shortName"],
                sector=company_info["sector"],
                address=company_info["address1"],
                ticker=ticker
            )
            db.session.add(company)
            db.session.commit()
    logger.info("#### Companies set ####")


def set_prices():
    companies = Company.query.all()
    for company in companies:
        prices = Finance().get_prices(company.ticker)
        for index in prices:
            price = Price(
                company=company.id,
                ticker=company.ticker,
                open=prices[index]['open'],
                high=prices[index]['high'],
                low=prices[index]['low'],
                close=prices[index]['close'],
                volume=prices[index]['volume'],
                price_date=prices[index]['date'],
            )
            db.session.add(price)
            db.session.commit()
    logger.info("#### Prices set ####")


def set_recommendations():
    companies = Company.query.all()
    for company in companies:
        recommendations = Finance().get_recommendations(company.ticker)
        for index in recommendations:
            recommendation = Recommendation(
                company=company.id,
                ticker=company.ticker,
                firm=recommendations[index]['firm'],
                to_grade=recommendations[index]['to_grade'],
                recommendation_date=index
            )
            db.session.add(recommendation)
            db.session.commit()
    logger.info("Recommendations set")
