from flask import Flask, jsonify, request
from flask_cors import CORS
from controllers import footballers
from werkzeug import exceptions
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/footballers"
mongo = PyMongo(app)
CORS(app)


@app.route('/')
def home():
    # footballers = mongo.db.players.find({"id": 1}).next()

    return jsonify({'message': 'Hello from Flask!'}), 200


@app.route('/api/players', methods=['GET', 'POST'])
def players_handler():
    fns = {
        'GET': footballers.index,
        'POST': footballers.create
    }
    resp, code = fns[request.method](request)
    return jsonify(resp), code


@app.errorhandler(exceptions.NotFound)
def handle_404(err):
    return {'message': f'Oops! {err}'}, 404


@app.errorhandler(exceptions.BadRequest)
def handle_400(err):
    return {'message': f'Oops! {err}'}, 400


app.run(debug=True)
