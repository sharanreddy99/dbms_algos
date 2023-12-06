from flask import Flask, request
from flask_cors import CORS, cross_origin
import re

from MinimalCover import findMinimalCover


app = Flask(__name__)
CORS(app, support_credentials=True)

@app.route("/", methods=["GET","POST"])
@cross_origin(supports_credentials=True)
def healthcheck():
    return 'The server is alive'

@app.route("/run_algo", methods=["POST"])
@cross_origin(supports_credentials=True)
def upload_folder():
    data = request.get_json()

    f = map(lambda x: x.split(data['sideSeparator']), data['f'].split(data['fdSeparator']))
    R = list(data['R'])
    RSet = map(lambda x: list(x), data['RSet'].split('fdSeparator'))

    match data['type']:
        case 'minimal_cover':


        
    return data