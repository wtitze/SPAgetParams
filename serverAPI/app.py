from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Route to handle the sum calculation using GET
@app.route('/sum/<num1>/<num2>', methods=['GET'])
def calculate_sum(num1, num2):
    try:
        result = float(num1) + float(num2)
    except ValueError:
        return jsonify({'error': 'Invalid input'}), 400
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
