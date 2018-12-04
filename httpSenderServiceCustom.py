from flask import Flask
from flask import request
import requests
import sys

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello():
	if request.method == 'POST':
		content = request.json
		url = content['url']
		message = content['message']
		payload = "{\r\n    \"text\": \""+message+"\"\r\n}"
		headers = {
			'Content-Type': "application/json",
			'cache-control': "no-cache",
			'Postman-Token': "f7f5d4a0-8b39-4283-9806-67f233e54468"
		}
		reponse = requests.request("POST", url, data=payload, headers=headers)
		return reponse.text
	else:
		return 'Hello World : GET REQUEST'



	