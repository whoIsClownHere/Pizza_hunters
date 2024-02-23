from flask import Flask, request, jsonify


app = Flask(__name__)
companies = {}
autoincrement = 0


@app.route('/api/partners', methods=['POST'])  # pyright: ignore
def add_company():
    global companies, autoincrement
    autoincrement += 1
    companies[autoincrement] = {
        "id": autoincrement,
        "name": request.json['name'],
        "budget": request.json['budget'],
        "spent_budget": 0,
        "history": dict(),
        "is_stopped": False
    }
    return jsonify({param: companies[autoincrement][param] for param in ['id', 'name', 'budget', 'spent_budget']})

if __name__ == '__main__':
  app.run(host='localhost', port=8080, debug=True)
