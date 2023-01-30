"""Backend API server.

`app` is an WSGI-comatible application"""

from http import HTTPStatus
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
 """Hello, world!
 """
 return jsonify({'message':'Hello, world!'}), HTTPStatus.OK

if __name__ == '__main__':
 app.run(debug=True)