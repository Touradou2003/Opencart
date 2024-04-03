from flask import Flask, jsonify, request
from opencart import get_opencart_statistics

app = Flask(__name__)

@app.route('/get_opencart_data', methods=['GET'])
def get_opencart_data():
    opencart_stats = get_opencart_statistics()
    return jsonify(opencart_stats)

if __name__ == "__main__":
    app.run(debug=True)