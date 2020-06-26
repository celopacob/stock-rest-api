from celery import Celery
from celery.schedules import crontab
from api.helpers import finance

app = Celery()


@app.task
def task_fetch_data_from_yfinance():
    finance.set_companies()
    finance.set_prices()
    finance.set_recommendations()


app.conf.beat_schedule = {
    'task_fetch_data_from_yfinance': {
        'task': 'tasks.task_fetch_data_from_yfinance',
        'schedule': crontab(hour="2", minute="10"),
    },
}
