import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from flask import Flask, jsonify, request
from discovery.discover import discover_devices
from flask_cors import CORS  # Install with: pip install flask-cors

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes (allow cross-origin requests)

@app.route('/')
def home():
    return "Flask backend is running! Use /discover (GET) or /run_test (POST)."

@app.route('/discover', methods=['GET'])
def discover():
    devices = discover_devices()
    return jsonify(devices)

@app.route('/run_test', methods=['POST'])
def run_test():
    if not request.is_json:
        return jsonify({"error": "Invalid JSON"}), 400

    data = request.get_json()
    device_ip = data.get("device_ip")
    test_type = data.get("test_type", "throughput")
    
    if not device_ip:
        return jsonify({"error": "Missing 'device_ip' in request"}), 400

    # Simulate a test result
    result = {
        "device_ip": device_ip,
        "test_type": test_type,
        "throughput_mbps": 550,
        "latency_ms": 15,
        "packet_loss": 0.01,
        "status": "success"
    }
    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)
