from flask import Flask
from threading import Thread
from bot import *

app = Flask(__name__)

@app.route("/")
def main():
	return "Alive"





app.run(host="0.0.0.0")


