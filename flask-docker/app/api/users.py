from flask import request
from app import db
from app.models import User as user_model
from sqlalchemy import exc
from flask_restful import Resource
from . import api

class UserList(Resource):
    def post(self):
        post_data = request.get_json()

        response_object = {
            "status": "fail",
            "message": "something wrong"
        }

        if not post_data:
            return response_object, 400

        try:
            username = post_data.get('username')
            email = post_data.get('email')

            user = user_model.query.filter_by(username=username).first()
            if not user:
                db.session.add(User(username, email))
                db.session.commit()
                respone_object = {
                    "status": "success",
                    "message": f"{email} was added!"
                }
                return respone_object, 201
            else:
                respone_object['message'] = 'That email is exist!'
                return respone_object, 400
    
        except exc.IntegrityError:
            db.session.rollback()
            return respone_object, 400
    
    def get(self):
        response_object = {
            "status": "success",
            "data": {
                "users":[ user.to_json() for user in user_model.query.all()]
            }
        }
        return response_object, 200
    

class User(Resource):
    def get(self, user_id):
        """ Get single user details """
        response_object = {
            "status": "fail",
            "message": "user does not exist"
        }

        try:
            user = user_model.query.filter_by(id=user_id).first()
            if not user:
                return response_object, 404
            else:
                response_object = {
                    "status": "success",
                    "data": {
                        "id": user.id,
                        "username": user.username,
                        "email": user.email,
                        "status": user.status
                    }
                }
                return response_object, 200
        except ValueError:
            return response_object, 404


api.add_resource(UserList, '/users')
api.add_resource(User, '/users/<int:user_id>')