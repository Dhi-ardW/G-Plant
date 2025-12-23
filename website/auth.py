from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User, db
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

        if len(email) < 4 :
            flash('email must have more than 3 character', category='failed')
        elif len(firstname) < 2 :
            flash('firstname must have more than 2 character', category='failed')
        elif password != password2 :
            flash('each password must be same', category='failed')
        elif len(password) < 7 :
            flash('Password must have more than 7 character', category='failed')
        else :
            # check database
            if User:
                flash('Email sudah terdaftar, silakan login', category='succes')
                return redirect(url_for('auth.login'))

            # add user to database
            new_user = User(email=email, firstname=firstname, password=generate_password_hash(password, method='pbkdf2:sha256'))
            db.session.add(new_user)
            db.session.commit()
            # add notif
            flash('Account has created', category='succes')
            return redirect(url_for('views.about'))

    return render_template('signup.html') 

@auth.route('/login', methods=['GET', 'POST'])
def login() :
    return render_template('login.html', )  

@auth.route('/logout')
def logout() :
    return render_template('index.html')   