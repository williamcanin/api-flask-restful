from flask import request
from flask_httpauth import HTTPBasicAuth
from flask_restful import Resource
from sqlalchemy.exc import IntegrityError
from passlib.hash import sha256_crypt as crypt
from main.model.user import User


auth = HTTPBasicAuth()


@auth.verify_password
def verify_password(username, password):
    user = User.query.filter_by(username=username).first()
    if user and user.verify_password(password):
        return True
    return False


@auth.error_handler
def unauthorized():
    response = {
        "status_code": 401,
        "message": "Unauthorized user"
    }
    return response


class Home(Resource):
    def get(self):
        return {"message": "Welcome, to API"}


class GetUser(Resource):
    def get(self, username: str):
        user = User.query.filter_by(username=username).first()
        try:
            response = {
                "id": user.id,
                "username": user.username,
                "email": user.email,
                "superuser": user.superuser,
            }
        except AttributeError as err:
            response = {"status": "AttributeError", "message": str(err)}
        return response


class AddUser(Resource):
    @auth.login_required
    def post(self):
        data = request.json
        try:
            user = User(
                username=data["username"],
                email=data["email"],
                password_hash=data["password"],
                superuser=False,
            )
            user.save()
            response = {
                "id": user.id,
                "username": user.username,
                "email": user.email,
                "superuser": user.superuser,
            }
        except IntegrityError as err:
            response = {
                "status": "IntegrityError",
                "instance": str(err.instance),
                "message": str(err.orig),
            }

        return response


class UserAll(Resource):
    def get(self):
        user = User.query.all()
        response = [
            {
                "id": i.id,
                "username": i.username,
                "email": i.email,
                "superuser": i.superuser,
            }
            for i in user
        ]
        return response


class DeleteUser(Resource):
    @auth.login_required
    def delete(self, id):
        try:
            user = User.query.filter_by(id=id).first()
            if not user.superuser:
                response = {"message": f"User id:{user.id} delete successfull"}
                user.delete()
            else:
                response = {"message": "The (superuser) user cannot be deleted."}
        except AttributeError as err:
            response = {"status": "AttributeError", "message": str(err)}
        return response


class PutUser(Resource):
    @auth.login_required
    def put(self, username: str):
        try:
            user = User.query.filter_by(username=username).first()
            data = request.json

            if user.superuser:
                response = {"message": f"The user ({user.username}) cannot be changed from here."}
                return response

            if "username" in data:
                user.username = data["username"]
            if "email" in data:
                user.email = data["email"]
            if "password" in data:
                user.password = crypt.hash(data["password"])

            user.save()
            response = {
                "id": user.id,
                "username": user.username,
                "email": user.email,
                "superuser": user.superuser,
            }
        except AttributeError as err:
            response = {
                "status": "AttributeError",
                "message": str(err),
            }

        return response
