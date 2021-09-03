from flask import Flask, request, abort
from flask.json import jsonify
from flask_cors import CORS
import controller

app = Flask(__name__, static_url_path='', static_folder='client_build')
CORS(app)

@app.route('/typing/<int:type_id>')
def get_specific_typing_test(type_id):
    return controller.get_specific_typing_test(type_id), 200

@app.route('/typing')
def get_random_typing_test():
    return controller.get_random_typing_test(), 200

@app.route('/highscores/<int:type_id>')
def get_all_highscores(type_id):
    return controller.get_all_highscores(type_id), 200

@app.route('/highscores/<int:type_id>/<int:top_answers>')
def get_top_highscores(type_id, top_answers):
    return controller.get_top_highscores(type_id, top_answers), 200

@app.route('/submit_highscore/<int:type_id>', methods=["POST"])
def submit_highscore(type_id):
    content = request.get_json()
    name = content["name"]
    time = content["time"]

    if (name is None or time is None):
        return abort(400)

    highscore = {
        "name": name,
        "time": time
    }

    result = controller.submit_highscore(type_id, highscore)
    if (result is False):
        return jsonify({"result": "Failure"}), 400
    
    return jsonify({"result": "Success"}), 201
