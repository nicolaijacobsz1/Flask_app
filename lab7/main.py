"""This is used to render the main routes of the app"""
from flask import Blueprint, render_template
from flask_login import login_required

main = Blueprint('main', __name__)


@main.route('/')
def index():
    """this is so that the app knows where to navigate to the main page"""
    return render_template('index.html')


@main.route('/content')
@login_required
def content():
    """this is so that the app knows where to navigate to the content page"""
    return render_template('content.html')
