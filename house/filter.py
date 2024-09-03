from flask import Flask, render_template, request, redirect, url_for

fil = Flask(__name__)

properties = [{'id': 1, 'location': 'New York', 'price': 100000, 'bedrooms': 2}]

@fil.route('/properties', methods=['GET', 'POST'])
def properties_page():
    if request.method == 'POST':
        # Apply filters to property search
        filters = {
            'location': request.form['location'],
            'price_range': int(request.form['price_range']),
            'bedrooms': int(request.form['bedrooms'])
        }
        filtered_properties = [prop for prop in properties if prop['location'] == filters['location'] and prop['price'] >= filters['price_range'] and prop['bedrooms'] == filters['bedrooms']]
        if not filtered_properties:
            return render_template('properties.html', message='No properties found matching your filters.')
        return render_template('properties.html', properties=filtered_properties)
    return render_template('properties.html', properties=properties)