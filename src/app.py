
from flask import Flask, request

from flask_pymongo import PyMongo
app = Flask(__name__)

app.secret_key = "secretkey"
app.config['MONGO_URI'] = 'mongodb://localhost/sophia'
PyMongo(app)


@app.route('/query', methods=['POST'])
def create_query():
    print(request.json)
    return {'message': 'recived'}


if __name__ == '__main__':
    app.run(debug=True)
