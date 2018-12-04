from flask import Flask
from flask import request
import requests

app = Flask(__name__)

url = sys.argv[1]
message = sys.argv[2]
payload = "{\r\n    \"text\": \""+message+"\"\r\n}"

headers = {
    'Content-Type': "application/json",
    'cache-control': "no-cache",
    'Postman-Token': "f7f5d4a0-8b39-4283-9806-67f233e54468"
    }

@app.route('/', methods=['GET', 'POST'])
def hello():
	response = requests.request("POST", url, data=payload, headers=headers)