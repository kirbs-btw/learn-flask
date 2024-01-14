from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '509238095ijm24'
    return app