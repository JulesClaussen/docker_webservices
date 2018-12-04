from flask import Flask
from flask import request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello():
	if request.method == 'POST':
		content = request.json
		return str(content)
	else:
		return 'Hello wooorld'
		