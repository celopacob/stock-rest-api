from flask import Blueprint, request

from api.core import create_response, serialize_list
from api.models import Company, Price, Recommendation

main = Blueprint("main", __name__)


@main.route("/company-info", methods=["GET"])
def get_company_info():
    ticker = request.args.get('ticker')
    if ticker is not None and ticker != "":
        company = Company.query.filter_by(ticker=ticker).first_or_404()
        return create_response(data={"data": company.to_dict()})

    companies = Company.query.all()
    return create_response(data={"data": serialize_list(companies)})


@main.route("/daily-price-info", methods=["GET"])
def get_daily_price_info():
    ticker = request.args.get('ticker')
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')
    prices = Price.query

    if ticker is not None and ticker != "":
        prices = prices.filter_by(ticker=ticker)
        
    if start_date is not None and start_date != "":
        prices = prices.filter(Price.price_date > start_date)

    if end_date is not None and end_date != "":
        prices = prices.filter(Price.price_date < end_date)
        
    return create_response(data={"data": serialize_list(prices.all())})


@main.route("/recommendations", methods=["GET"])
def get_recommendations():
    ticker = request.args.get('ticker')
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')
    recommendations = Recommendation.query

    if ticker is not None and ticker != "":
        recommendations = recommendations.filter_by(ticker=ticker)
        
    if start_date is not None and start_date != "":
        recommendations = recommendations.filter(Recommendation.recommendation_date > start_date)

    if end_date is not None and end_date != "":
        recommendations = recommendations.filter(Recommendation.recommendation_date < end_date)
        
    return create_response(data={"data": serialize_list(recommendations.all())})
