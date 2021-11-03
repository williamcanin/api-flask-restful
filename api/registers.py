registers = {
    "init_app": [
        "api.users.cli:init_app",
        "api.utils.errors:init_app"
    ],
    "resources": [
        "api.home.resources|Home|/",
        "api.users.resources|GetUser|/user/<string:username>/",
        "api.users.resources|UserAll|/users/",
        "api.users.resources|AddUser|/user/add/",
        "api.users.resources|DeleteUser|/user/delete/<int:id>/",
        "api.users.resources|PutUser|/user/change/<string:username>/",
    ]
}
