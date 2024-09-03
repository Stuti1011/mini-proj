# user_profile.py
from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import current_user

user_profile_blueprint = Blueprint('user_profile', __name__)

@user_profile_blueprint.route('/profile', methods=['GET', 'POST'])
def profile():
    if request.method == 'POST':
        # Update user profile information
        user_id = current_user.id # type: ignore
        users = [{'id': 1, 'username': 'john', 'email': 'john@example.com'}]
        for user in users:
            if user['id'] == user_id:
                user['username'] = request.form['username']
                user['email'] = request.form['email']
                # Save changes to database or static data storage
                return redirect(url_for('user_profile.profile'))
    return render_template('profile.html', user=current_user) # type: ignore