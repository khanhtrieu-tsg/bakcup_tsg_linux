from flask import Flask, jsonify
from flask_cors import CORS
from licenses import app_license
app = Flask(__name__)


app.register_blueprint(app_license)

CORS(app)
if __name__ == '__main__':
    app.run(debug=True)