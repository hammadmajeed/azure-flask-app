from flask import Flask, jsonify

app = Flask(__name__)
@app.route('/', methods=['GET'])
def hello():
    print("I am inside hello world")
    return 'Hello World! I can make change at route: /change'

@app.route('/change', methods=['GET'])
def change():
    print("I am inside change")
    return 'Hello World! I am changed'

@app.route('/change/add/<x>/<y>', methods=['GET'])
def add(x, y):
    print("I am inside add")
    return str(int(x) + int(y))

@app.route('/change/sub/<x>/<y>', methods=['GET'])
def sub(x, y):
    print("I am inside subtract")
    return str(int(x) - int(y))

@app.route('/change/mod/<x>/<y>', methods=['GET'])
def sub(x, y):
    print("I am inside mod")
    return str(int(x) % int(y))


if __name__ == '__main__':
    app.run( host='0.0.0.0', port=5000, debug=True) # note that host='0.0.0.0' is imp for external access
