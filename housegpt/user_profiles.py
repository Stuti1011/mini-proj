from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user

user_profiles_blueprint = Blueprint('user_profiles', __name__)

@user_profiles_blueprint.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    if request.method == 'POST':
        # Update user profile information
        current_user.username = request.form['username']
        current_user.email = request.form['email']
        # Add logic to save these changes to the database
        return redirect(url_for('user_profiles.profile'))
    return render_template('profile.html', user=current_user)
