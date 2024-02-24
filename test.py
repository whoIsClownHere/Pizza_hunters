import requests
import pandas as pd
import json


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
        result.append((first_test.iloc[i]['time'], get_info['is_stopped']))
        print(get_info)

    return result


api_test('super_hard_puper_test.csv', "yandex")
# print(api_test('super_hard_puper_test.csv', "yandex"))
