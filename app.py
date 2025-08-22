from flask import Flask, jsonify
import json
from pathlib import Path

app = Flask(__name__)


DATA_FILE = Path(__file__).with_name("data.json")

@app.route("/api", methods=["GET"])
def get_list():
   
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
   
        if not isinstance(data, list):
            return jsonify({"error": "data.json must contain a JSON array"}), 500
        return jsonify(data)
    except FileNotFoundError:
        return jsonify({"error": "data.json not found"}), 500
    except json.JSONDecodeError as e:
        return jsonify({"error": f"Invalid JSON in data.json: {e}"}), 500

if __name__ == "__main__":

    app.run(host="0.0.0.0", port=5000, debug=True)
