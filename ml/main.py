import datetime
import pandas as pd

agg_s = pd.read_csv('data/all_aggregated.csv')

def get_coeff_sum(start_date, finish_date):
    return agg_s.iloc[agg_s['day'][pd.date_range(start_date, finish_date).dayofyear].index]['cashback'].sum()


def get_5_days_sum(finish_date):
    return get_coeff_sum(finish_date, finish_date + datetime.timedelta(days=5))


def get_trand(history: dict[datetime.date, int], start_date, finish_date, alpha=0.07, mul=1):
    df = pd.Series(index=pd.date_range(start_date, finish_date))
    df[history.keys()] = list(history.values())
    df.interpolate(inplace=True)
    df = df.diff()
    df.dropna(inplace=True)
    df = df.ewm(alpha=alpha, adjust=False).mean()
    if df.shape[0]:
        trand = df.iloc[-1]
    else:
        trand = 0
    print(trand)
    return float(trand)


def prediction(company_title: str, history: dict[datetime.date, int], spent_budget: int, budget: int):
    start_date, finish_date = pd.to_datetime(min(history.keys())), pd.to_datetime(max(history.keys()))
    level = float(spent_budget / get_coeff_sum(start_date, finish_date) * get_5_days_sum(finish_date) + spent_budget)
    trand = get_trand(history, start_date, finish_date)  # TODO: trand
    return bool(level + trand > budget)
