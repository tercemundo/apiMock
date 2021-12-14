from flask import Flask, json

from flask_cors import CORS

api = Flask(__name__)
CORS(api)


companies = [{"id": 1, "name": "Company One"}, {"id": 2, "name": "Company Two"}]


@api.route('/companies', methods=['GET'])
def get_companies():
  return json.dumps(companies)

if __name__ == '__main__':
    api.run('0.0.0.0') 
