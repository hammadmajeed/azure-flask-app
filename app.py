from flask import Flask, jsonify
import json

app = Flask(__name__)
@app.route('/', methods=['GET'])
def hello():
    print("I am inside hello world")
    return 'Hello World! I can make change at route: /change'

@app.route('/change', methods=['GET'])
def change():
    print("I am inside change")
    return 'Hello World! I am changed'



if __name__ == '__main__':
    app.run( host='0.0.0.0', port=5000, debug=True) # note that host='0.0.0.0' is imp for external access