from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_user, logout_user
from your_app import User  # Import the User model from your main app

login_blueprint = Blueprint('login', __name__)

@login_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()  # Replace with actual user fetching logic
        if user and user.password == password:
            login_user(user)
            return redirect(url_for('index'))
    return render_template('login.html')

@login_blueprint.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))
