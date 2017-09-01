from flask_restful import Resource, reqparse
from flask import jsonify

class Hi(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username', type=str, default='0xbug', help='hi,{username}')
        args = parser.parse_args()
        username = args.username
        data = {
            'code':1,
            'msg':'Hi,{}'.format(username),
            'result':[

            ]
        }
        return jsonify(data)
