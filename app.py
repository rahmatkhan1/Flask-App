from flask import Flask, jsonify
import json
from pathlib import Path

app = Flask(__name__)

# Path to backend data file
DATA_FILE = Path(__file__).with_name("data.json")

@app.route("/api", methods=["GET"])
def get_list():
    """Read the list from data.json and return it as JSON."""
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
        # Ensure the response is a list
        if not isinstance(data, list):
            return jsonify({"error": "data.json must contain a JSON array"}), 500
        return jsonify(data)
    except FileNotFoundError:
        return jsonify({"error": "data.json not found"}), 500
    except json.JSONDecodeError as e:
        return jsonify({"error": f"Invalid JSON in data.json: {e}"}), 500

if __name__ == "__main__":
    # For local dev only. In production, use a WSGI server (gunicorn/uwsgi).
    app.run(host="0.0.0.0", port=5000, debug=True)
