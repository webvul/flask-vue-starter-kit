from flask import Flask, render_template, request, jsonify
from flask_restful import Api
from flask_cors import CORS
from .controllers.hello import Hi
import sys
app = Flask(__name__)

CORS(app)

errors = {
    'InternalServerError': {
        'message': "InternalServerError",
        'status': 500
    },
    'BadRequest': {
        'message': "BadRequest",
        'status': 400
    },
    'NotFound': {
        'message': "NotFound",
        'status': 404
    },
    'MethodNotAllowed': {
        'message': 'MethodNotAllowed',
        'status': 405
    },
    'Unauthorized': {
        "message": "未认证",
        "status": 401,
        "result": {'token': None, 'username': None}
    },

}
api = Api(app, catch_all_404s=True, decorators=[], errors=errors)

api.add_resource(Hi, '/api/account/welcome')

if __name__ == '__main__':
    app.run(debug=False, threaded=True, port=int(sys.argv[1]), host='0.0.0.0', use_reloader=True)
