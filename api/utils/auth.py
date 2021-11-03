from flask_httpauth import HTTPBasicAuth


auth = HTTPBasicAuth()


@auth.error_handler
def unauthorized():
    response = {
        "status_code": 401,
        "message": "Unauthorized"
    }
    return response
