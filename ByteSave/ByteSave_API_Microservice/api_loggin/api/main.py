from flask import Flask, jsonify
from flask_cors import CORS
# from license import app_license
app = Flask(__name__)

# from licenses import app_license

# app.register_blueprint(app_license)

CORS(app)
if __name__ == '__main__':
    app.run(debug=True)