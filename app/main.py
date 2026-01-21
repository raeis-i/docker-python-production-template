from flask import Flask, jsonify
import os
import sys
import logging

#Logging setup
logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    stream=sys.stdout
)

#App setup
app = Flask(__name__)

PORT = int(os.getenv("PORT", "8080"))
ENV = os.getenv("ENV", "dev")

if ENV not in ["dev", "staging", "prod"]:
    logging.error(f"Invalid ENV value: {ENV}")
    raise RuntimeError(f"Invalid ENV value: {ENV}")

logging.info(f"Starting app in '{ENV}' environment on port {PORT}")

#Routes
@app.route("/")
def hello():
    logging.info("Received request at '/'")
    return jsonify({
        "message": "Hello from Production-grade Docker image",
        "env": ENV
    })

@app.route("/health")
def health():
    logging.info("Received request at '/health'")
    return jsonify({"status": "ok"}), 200

@app.route("/info")
def info_route():
    logging.info("Received request at '/info'")
    import flask
    return jsonify({
        "python_version": sys.version,
        "flask_version": flask.__version__,
        "port": PORT,
        "env": ENV
    })


#Run app
if __name__ == "__main__":
    logging.info("App is running...")
    app.run(host="0.0.0.0", port=PORT)
