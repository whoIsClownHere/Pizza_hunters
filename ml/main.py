import datetime
import pandas as pd

agg_s = pd.read_csv('data/all_aggregated.csv')
agg_s.index = pd.to_datetime(agg_s.index)


def get_coeff_sum(start_date, finish_date):
    return agg_s[(start_date <= agg_s.index) & (agg_s.index <= finish_date)]


def get_5_days_sum(finish_date):
    return agg_s[(finish_date <= agg_s.index) & (agg_s.index <= (finish_date + datetime.timedelta(days=5)))]


def prediction(company_title: str, history: dict[datetime.date, int], spent_budget: int, budget: int):
    is_stopped = None
    start_date, finish_date = min(history.keys()), max(history.keys())
    return spent_budget / get_coeff_sum(start_date, finish_date) * get_5_days_sum(finish_date) + spent_budget > budget
