'''
Dhuisme Tristan
Achargui Yassine
M1 AMSD
16/03/2025
'''

import random
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/random', methods=['GET'])
def get_random_number():
    """Génère un nombre aléatoire entre 1 et 6"""
    number = random.randint(1, 6)
    return jsonify({"number": number})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
