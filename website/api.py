from flask import Blueprint, render_template

api = Blueprint('api', __name__)

@api.route('/api/status')
def status():
    expl_json = {
    "message": "success",
    "request": {
        "altitude": 100,
        "datetime": 1568062811,
        "latitude": 40.71,
        "longitude": -74.0,
        "passes": 5
    },
    "response": [
        {
            "duration": 395,
            "risetime": 1568082479
        },
        {
            "duration": 640,
            "risetime": 1568088118
        },
        {
            "duration": 614,
            "risetime": 1568093944
        },
        {
            "duration": 555,
            "risetime": 1568099831
        },
        {
            "duration": 595,
            "risetime": 1568105674
        }
    ]
}




    return expl_json

@api.route('/api/stringcall/<string:name>/')
def namedrop(name):
    return name

@api.route('/num/numcall/<int:num>/')
def numdrop(num):
    return str(int(num)+10)