init_app_users = [
    "api.users.cli:init_app",
]

resources_users = [
    "api.users.resources|Home|/",
    "api.users.resources|GetUser|/user/<string:username>/",
    "api.users.resources|UserAll|/users/",
    "api.users.resources|AddUser|/user/add/",
    "api.users.resources|DeleteUser|/user/delete/<int:id>/",
    "api.users.resources|PutUser|/user/change/<string:username>/",
]
