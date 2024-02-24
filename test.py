import requests
import pandas as pd


def api_test(source, name):
    result = []
    first_test = pd.read_csv(source)
    budget = first_test['cashback'].sum()
    company_data = requests.post('http://localhost:8080/api/partners', data={'name': name, 'budget': budget}).json()
    id_1 = company_data['id']

    for i in range(first_test.shape[0] - 5):
        requests.put(f'http://localhost:8080/api/partners/{id_1}/cashback', data={"date": first_test.iloc[i]['time'],
                                                            "name": name, "cashback": first_test.iloc[i]['cashback']})

        future_budget = budget

        for j in range(i, i + 5):
            try:
                future_budget -= first_test.iloc[i - j]['cashback']
            except IndexError:
                pass

        get_info = requests.get(f'http://localhost:8080/api/partners/{id_1}')
        result.append((first_test.iloc[i]['time'], get_info['is_stopped'], future_budget))

    return result
