from flask import Blueprint, render_template

views = Blueprint('views', __name__)

# @views.route('/')
# def beranda():
#     return render_template('index.html')

@views.route('/')
def about():
    return render_template('index.html')