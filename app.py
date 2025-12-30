from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    """Home endpoint"""
    return jsonify({
        'message': 'Welcome to Flask Test App',
        'status': 'success',
        'version': '1.0.0'
    })

@app.route('/health')
def health():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'service': 'flask-test-app'
    })

@app.route('/api/hello', methods=['GET'])
def hello():
    """Hello endpoint"""
    name = request.args.get('name', 'World')
    return jsonify({
        'message': f'Hello, {name}!',
        'status': 'success'
    })

@app.route('/api/add', methods=['POST'])
def add():
    """Add two numbers endpoint"""
    data = request.get_json()
    if not data:
        return jsonify({'error': 'No JSON data provided'}), 400
    
    a = data.get('a')
    b = data.get('b')
    
    if a is None or b is None:
        return jsonify({'error': 'Missing parameters: a and b are required'}), 400
    
    try:
        result = float(a) + float(b)
        return jsonify({
            'result': result,
            'a': a,
            'b': b,
            'status': 'success'
        })
    except ValueError:
        return jsonify({'error': 'Invalid number format'}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

