'''
Dhuisme Tristan
Achargui Yassine
M1 AMSD
16/03/2025
'''

import requests
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/sum', methods=['GET'])
def get_sum():
    """Récupère trois nombres aléatoires et calcule leur somme"""
    numbers = []
    for _ in range(3):
        try:
            # L'URL utilise le nom du service Docker pour le premier conteneur
            response = requests.get('http://random-service:5000/random')
            number = response.json().get('number')
            numbers.append(number)
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    
    total = sum(numbers)
    return jsonify({
        "numbers": numbers,
        "sum": total
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
