from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello():
	if requests.method == 'POST':
		content = request.json
		return str(content)
	else:
		return 'Hello wooorld'
		