from flask import Flask,jsonify
from flask_cors import CORS, cross_origin
import random

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/',methods=["GET"])
@cross_origin()
def hello_world():
	return jsonify({"temp":round(random.uniform(35.00, 45.00), 2)})

# main driver function
if __name__ == '__main__':
	app.run('0.0.0.0',8000,debug=True)
