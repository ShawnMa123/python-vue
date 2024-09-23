from flask import Flask, jsonify, request
from flask_cors import CORS
import requests
import subprocess

app = Flask(__name__)
CORS(app)


@app.route('/api/data')
def get_data():
    return jsonify({'message': 'Hello from Flask!'})


@app.route('/api/check_service', methods=['POST'])
def check_service():
    data = request.json
    url = data.get('url')

    if not url:
        return jsonify({'status': 'error', 'message': 'URL is required'}), 400

    try:
        response = requests.get(url)
        if response.status_code == 200 and ('UP' in response.text or 'success' in response.text):
            return jsonify({'status': 'up'})
        else:
            return jsonify({'status': 'down'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500


if __name__ == '__main__':
    # Start the Vue development server
    # subprocess.Popen(['npm', 'run', 'serve'], cwd='../frontend')
    app.run(debug=True)
