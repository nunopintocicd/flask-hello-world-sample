from flask import Blueprint, jsonify
import time
import random

main = Blueprint('main', __name__)

@main.route('/cpu')
def cpu_load():
    start_time = time.time()
    while time.time() - start_time < 5:
        pass
    return jsonify({"message": "CPU load generated"}), 200

@main.route('/memory')
def memory_load():
    load =  (10**7)  # Corrected line
    return jsonify({"message": "Memory load generated"}), 200

@main.route('/io')
def io_load():
    with open('tempfile.txt', 'w') as f:
        for _ in range(10**6):
            f.write('Some random text\n')
    return jsonify({"message": "I/O load generated"}), 200

@main.route('/network')
def network_load():
    data = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=10**6))
    return jsonify({"message": "Network load generated", "data": data}), 200
