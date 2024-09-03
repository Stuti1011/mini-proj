from flask import Blueprint, Flask, render_template, request, redirect, url_for
from flask_login import LoginManager, UserMixin, login_user, logout_user

login_blueprint = Blueprint('login', __name__)

# ... rest of the code remains the same ...
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'

login_manager = LoginManager(app)

class User(UserMixin):
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

@login_manager.user_loader
def load_user(user_id):
    # Fetch user from database or static data storage
    users = [{'id': 1, 'username': 'john', 'password': 'hello'}]
    for user in users:
        if user['id'] == int(user_id):
            return User(user['id'], user['username'], user['password'])
    return None

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = load_user(1)  # Replace with actual user loading logic
        if user and user.password == password:
            login_user(user)
            return redirect(url_for('index'))
    return render_template('login.html')

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))