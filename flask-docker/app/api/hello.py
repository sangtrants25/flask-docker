from flask_restful import Resource
from . import api


class Hello(Resource):
    def get(self):
        return {
            "message": "helloword"
        }

api.add_resource(Hello, '/hello')