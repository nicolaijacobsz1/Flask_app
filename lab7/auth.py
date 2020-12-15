"""this is the authentication file for the app"""
from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required
from .models import User
from . import db


auth = Blueprint('auth', __name__)


@auth.route('/login')
def login():
    """allows the app to know where to navigate to this page"""
    return render_template('login.html')


@auth.route('/login', methods=['POST'])
def login_post():
    """this function is to gather the information for login from db"""
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    user = User.query.filter_by(email=email).first()

    if not user and not check_password_hash(user.password, password):
        flash('Please check your login details and try again.')
        return redirect(url_for('auth.login'))

    login_user(user, remember=remember)

    return redirect(url_for('main.content'))


@auth.route('/signup')
def signup():
    """allows the app to know where to navigate to this page"""
    return render_template('signup.html')


@auth.route('/signup', methods=['POST'])
def signup_post():
    """post the data to the db"""
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')

    user = User.query.filter_by(email=email).first()

    if user:
        flash('Email address already exists.')
        return redirect(url_for('auth.signup'))

    new_user = User(email=email, name=name, password=generate_password_hash
                    (password, method='sha256'))

    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for('auth.login'))


@auth.route('/logout')
@login_required
def logout():
    """logs out the current user and redirects to home page"""
    logout_user()
    return redirect(url_for('main.index'))



