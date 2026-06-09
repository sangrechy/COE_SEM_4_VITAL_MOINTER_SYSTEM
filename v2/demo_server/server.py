from flask import Flask, jsonify

app = Flask(__name__)

data = {
    "ecg_class": 5,
    "stress_class": 1,
    "final_status": 3
}

@app.route("/data")
def get_data():
    return jsonify(data)

app.run(host="0.0.0.0", port=5000)
