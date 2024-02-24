
import datetime
import numpy as np
import requests
import pandas as pd
import json
import matplotlib.pyplot as plt


headers = {
  'Content-Type': 'application/json'
}


def api_test(source, name):
    result = []
    first_test = pd.read_csv(source)
    budget = first_test['cashback'].iloc[:first_test.shape[0] // 3 * 2].sum()
    print(budget)
    company_data = requests.post('http://localhost:8080/api/partners', data=json.dumps({'name': name, 'budget': budget}), headers=headers).json()
    id_1 = company_data['id']


    for i in range(first_test.shape[0]):
        requests.put(f'http://localhost:8080/api/partners/{id_1}/cashback', data=json.dumps({"date": first_test.iloc[i]['time'] + ' 00:00:00',
                                                            "name": name, "cashback": first_test.iloc[i]['cashback']}), headers=headers).json()

        get_info = requests.get(f'http://localhost:8080/api/partners/{id_1}', headers=headers).json()
        result.append((datetime.datetime.strptime(first_test.iloc[i]['time'], '%Y-%m-%d'), get_info['spent_budget'], get_info['is_stopped']))
        print(get_info)

    return result, budget


out, budget = api_test('super_hard_puper_test.csv', "yandex")

ax = plt.gca()
out_g = list(filter(lambda elem: not elem[2], out))
out_r = list(filter(lambda elem: elem[2], out))
ax.plot(
    list(map(lambda elem: elem[0], out)),
    list(map(lambda elem: elem[1], out)),
    color='g'
)
ax.plot(
    list(map(lambda elem: elem[0], out_r)),
    list(map(lambda elem: elem[1], out_r)),
    color='r'
)
ax.axhline(y=budget, color='b', linestyle='--')
plt.show()
# print(api_test('super_hard_puper_test.csv', "yandex"))

