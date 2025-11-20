from flask import Flask, Response
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)
REQUESTS = Counter('app_requests_total', 'Total HTTP requests')

@app.route('/')
def index():
	REQUESTS.inc()
	return "Hello! \n"

@app.route('/metrics')
def metrics():
	return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000)


