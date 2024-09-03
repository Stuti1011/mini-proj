from flask import Flask, render_template, request, redirect, url_for
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from login import login_blueprint
from user_profiles import user_profiles_blueprint

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'

login_manager = LoginManager(app)

# Register Blueprints
app.register_blueprint(login_blueprint)
app.register_blueprint(user_profiles_blueprint)

@app.route('/properties')
def properties():
    try:
        properties = fetch_properties_from_db()  # Implement this function to fetch properties
    except Exception as e:
        print(f"Error fetching properties: {e}")
        return render_template('error.html', error_message='Failed to fetch properties')

    # Filter properties
    location = request.args.get('location')
    price_range = request.args.get('price_range')
    bedrooms = request.args.get('bedrooms')

    filtered_properties = [prop for prop in properties if
        (not location or prop['location'] == location) and
        (not price_range or prop['price'] <= int(price_range)) and
        (not bedrooms or prop['bedrooms'] == int(bedrooms))
    ]

    # Pagination logic
    page = request.args.get('page', 1, type=int)
    per_page = 10
    paginated_properties = filtered_properties[(page-1)*per_page:page*per_page]

    return render_template('properties.html', properties=paginated_properties)
