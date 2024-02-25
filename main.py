from flask import Flask, request, jsonify
from flask_restful import reqparse
from ml.main import prediction
import datetime


app = Flask(__name__)
companies = {}
autoincrement = 0


@app.route('/api/partners', methods=['POST'])  # pyright: ignore
def add_company():
    global companies, autoincrement
    parser = reqparse.RequestParser()
    parser.add_argument('name', type=str)
    parser.add_argument('budget', type=float)
    args = parser.parse_args()

    autoincrement += 1
    companies[autoincrement] = {
        "id": autoincrement,
        "name": args['name'],
        "budget": args['budget'],
        "spent_budget": 0,
        "history": dict(),
        "is_stopped": False
    }
    return jsonify({param: companies[autoincrement][param] for param in ['id', 'name', 'budget', 'spent_budget']})


@app.route('/api/partners/<int:id>', methods=['GET'])  # pyright: ignore
def get_company(id):
    global companies
    return jsonify({param: companies[id][param] for param in ['id', 'name', 'budget', 'spent_budget', 'is_stopped']})


@app.route('/api/partners/<int:id>/cashback', methods=['PUT'])  # pyright: ignore
def update_company(id):
    global complanies
    parser = reqparse.RequestParser()
    parser.add_argument('date', type=str)
    parser.add_argument('cashback', type=float)
    args = parser.parse_args()

    date = datetime.datetime.strptime(args['date'], '%Y-%m-%d %H:%M:%S').date()
    companies[id]['history'][date] = args['cashback']
    companies[id]['spent_budget'] += args['cashback']
    if not companies[id]['is_stopped']:
        companies[id]['is_stopped'] = prediction(companies[id]['name'], companies[id]['history'], companies[id]['spent_budget'], companies[id]['budget'])  # pyright: ignore
    return jsonify({})



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
