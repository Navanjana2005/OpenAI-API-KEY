from flask import Flask
from config import api_key

app = Flask(__name__)

@app.route('/get_api_key')
def get_api_key():
    return api_key
