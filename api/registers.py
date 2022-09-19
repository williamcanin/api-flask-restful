registers = {
    "init_app": [
        "api.users.cli:init_app",
        "api.utils.errors:init_app"
    ],
    "resources": [
        "api.home.resources|Home|/",
        "api.users.resources|GetUser|/users/<string:username>/",
        "api.users.resources|UserAll|/users/",
        "api.users.resources|AddUser|/users/add/",
        "api.users.resources|DeleteUser|/users/delete/<int:id>/",
        "api.users.resources|PutUser|/users/change/<string:username>/",
    ]
}
