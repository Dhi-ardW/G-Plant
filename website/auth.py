from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from . import db
from flask_login import login_user, login_required, logout_user, current_user
# hashing
from werkzeug.security import generate_password_hash, check_password_hash

auth = Blueprint('auth', __name__)

@auth.route('/signup', methods=['GET', 'POST'])
def signup() :
    if request.method == 'POST':
        email = request.form.get('email') 
        firstname = request.form.get('firstname') 
        password = request.form.get('password') 
        password2 = request.form.get('password2')

        user = User.query.filter_by(email=email).first() 

        if len(email) < 4 :
            flash('email must have more than 3 character', category='failed')
        elif len(firstname) < 2 :
            flash('firstname must have more than 2 character', category='failed')
        elif password != password2 :
            flash('each password must be same', category='failed')
        elif len(password) < 7 :
            flash('Password must have more than 7 character', category='failed')
        elif user :
            flash('Email have already, login with your password')
            return redirect(url_for('auth.login'))
        else :
            # check database
            if user:
                flash('Email sudah terdaftar, silakan login', category='succes')
                return redirect(url_for('auth.login'))
                

            # add user to database
            new_user = User(email=email, firstname=firstname, password=generate_password_hash(password, method='pbkdf2:sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(user, remember=True)
            # add notif
            flash('Account has created', category='succes')
            return redirect(url_for('views.index'))

    return render_template('signup.html') 

@auth.route('/login', methods=['GET', 'POST'])
def login() :
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first() 
        if user :
            if check_password_hash(user.password, password) :
                flash('Login Succesfuly, enjoy green life', category='succes')
                login_user(user, remember=True) 
                return redirect(url_for('views.index'))
            else :
                flash ('Incorrect Password, Try Again ', category='failed')
                return redirect(url_for('auth.login'))
        else :
           flash('email does not exits', category='failed')         

    return render_template("login.html", boolean=True)  

@auth.route('/logout')
@login_required
def logout() :
    logout_user()
    return redirect(url_for('auth.login'))