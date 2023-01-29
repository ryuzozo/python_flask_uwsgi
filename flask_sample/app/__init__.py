from flask import Flask, jsonify

application = Flask(__name__)

@application .route("/hello")
def hello():
 return jsonify({
  "message": "Hello World!"
 })