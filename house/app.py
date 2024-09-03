from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

from login import login_blueprint
from user_profiles import user_profiles_blueprint

app.register_blueprint(login_blueprint)
app.register_blueprint(user_profiles_blueprint)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/properties')
def properties():
    # Hardcode some sample properties for GUI testing
    properties = [
        {'location': 'Location 1', 'price': 100, 'bedrooms': 2},
        {'location': 'Location 2', 'price': 200, 'bedrooms': 3},
        {'location': 'Location 3', 'price': 300, 'bedrooms': 4},
    ]

    # Filter and sort properties based on user input
    location = request.args.get('location')
    price_range = request.args.get('price_range')
    bedrooms = request.args.get('bedrooms')

    filtered_properties = []
    for prop in properties:
        if (location and prop['location'] == location) or \
           (price_range and prop['price'] >= int(price_range)) or \
           (bedrooms and prop['bedrooms'] == int(bedrooms)):
            filtered_properties.append(prop)

    # Paginate properties
    page = request.args.get('page', 1, type=int)
    per_page = 10
    paginated_properties = filtered_properties[(page-1)*per_page:page*per_page]

    return render_template('properties.html', properties=paginated_properties)