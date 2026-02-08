from flask import Flask, request
import logging
import time
import os

app = Flask(__name__)

log_dir = '/var/log/myapp'
os.makedirs(log_dir, exist_ok=True)
handler = logging.FileHandler(os.path.join(log_dir, 'app.log'))
handler.setLevel(logging.INFO)
app.logger.addHandler(handler)


@app.route('/')
def index():
    app.logger.info(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - INFO - index accessed from {request.remote_addr}")
    return 'Hello from the demo app!\n'


@app.route('/error')
def err():
    app.logger.error(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - ERROR - simulated error")
    return 'Simulated error logged\n', 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
