from flask import Flask, jsonify
from flask_cors import CORS
from flask import Flask, request

#configuration
DEBUG = False
#instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)
#enable CORS
CORS(app)


@app.route('/png', methods=['GET', 'POST'])
def ping_png():
    return ('pong!')


#sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')


if __name__ == '__main__':
    app.run()