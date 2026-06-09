from flask import Flask, Response
from prometheus_client import Counter, generate_latest

app = Flask(__name__)

REQUESTS = Counter(
    'app_requests_total',
    'Total requests'
)

@app.route("/")
def home():
    REQUESTS.inc()
    return "DevOps Monitoring Platform Running"

@app.route("/metrics")
def metrics():
    return Response(
        generate_latest(),
        mimetype="text/plain"
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
