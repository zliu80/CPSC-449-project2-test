import dataclasses

import quart
from quart import Quart, request, render_template, abort, current_app
import toml
from quart_schema import QuartSchema, validate_request

# from quart_schema import QuartSchema, RequestSchemaValidationError
from service.UserServiceModule import UserService

from service.DBServiceModule import DBService
from view.User import User

# ************** Initialized variable **************#
app = Quart(__name__)

QuartSchema(app)

# For testing in pycharm
# app.config.from_file(f"etc/user.toml", toml.load)
app.config.from_file(f"etc/{__name__}.toml", toml.load)
DBService.db_url = app.config["DATABASES"]["URL"]
DBService.db_path = app.config['DATABASES']["DB_PATH"]

userService = UserService()

# The authentification response type
UNAUTHORIZED = {'WWW-Authenticate': 'Basic realm="Login Required"'}


# **************************************************************#
# **************************** User ****************************#
# **************************************************************#
# **************************************************************#
# **************************** User ****************************#
# **************************************************************#


@app.route('/auth')
async def auth():
    print(request)
    auth = request.authorization
    print(auth)
    if auth is not None and auth.type == "basic":
        username = auth.username
        password = auth.password
        print("Validating the username ", username, "and password ", password)
        if username is None or password is None:
            return quart.Response("Please log in. The username or password cannot be none", 401, UNAUTHORIZED)
        else:
            user = await userService.find_user_by_name(username)
            if user is None:
                return quart.Response("Please log in. The username does not exist", 401, UNAUTHORIZED)
            else:
                if user.password == password:
                    msg = "Login success."
                    return {"authenticated": True}
                    
                else:
                    return quart.Response("Please log in. Wrong username or password", 401, UNAUTHORIZED)
    else:
        # return 'WWW-Authenticate: Basic realm="My Realm" HTTP/1.0 401 Unauthorized'
        # This will prompt the user a dialog to enter username and password.
        return quart.Response("Please log in", 401, UNAUTHORIZED)

    return {"authenticated": True}


@app.route('/register', methods=["GET", "POST"])
async def register():
    if request.method == "GET":
        username = request.args.get('username')
        password = request.args.get('password')
    elif request.method == "POST":
        f = await request.form
        username = f.get('username')
        password = f.get('password')
    register_authenticated = False
    msg = ""
    try:
        if username is None or password is None:
            msg = "The username or password cannot be none"
            return {"msg": msg}, 401, {'X-Header': 'Value'}
        else:
            _id = await userService.register(username, password)
            if _id is not None:
                if _id == 'existed':
                    msg = "The username is existed, please try another name."
                    return {"msg": msg}, 401, {'X-Header': 'Value'}
                else:
                    msg = "Success, you may try to login."
                    register_authenticated = True
    except Exception as e:
        print(e)
        print("System error, please contact the author.")
    return {"authenticated": register_authenticated, "msg": msg, "username": username}


# @app.errorhandler(RequestSchemaValidationError)
def bad_request(e):
    return {"error": str(e.validation_error)}, 400


@app.errorhandler(409)
def conflict(e):
    return {"error": str(e)}, 409


if __name__ == '__main__':
    try:
        if DBService.db_url is None or DBService.db_path is None:
            print("The system initialization failed! Check the db address.")

        app.run(debug=True)
    except Exception as e:
        print(e)
        print("The system initialization failed, please contact the author.")
