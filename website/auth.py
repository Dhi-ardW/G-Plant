from flask import Blueprint

auth = Blueprint('auth', __name__)

@auth.route('/signup')
def signup() :
    return '<h1>Welcome to Signup Page'    

@auth.route('/login')
def login() :
    return '<h1>Welcome to login     Page'    

@auth.route('/logout')
def logout() :
    return '<h1>logout<h1/>'    