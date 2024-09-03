from flask import app, render_template, request, redirect, url_for

@app.route('/properties', methods=['GET', 'POST'])
def properties():
    if request.method == 'POST':
        # Apply filters to property search
        filters = {
            'location': request.form['location'],
            'price_range': request.form['price_range'],
            'bedrooms': request.form['bedrooms']
        }
        properties = [{'id': 1, 'location': 'New York', 'price': 100000, 'bedrooms': 2}]
        filtered_properties = []
        for prop in properties:
            if prop['location'] == filters['location'] and prop['price'] >= filters['price_range'] and prop['bedrooms'] == filters['bedrooms']:
                filtered_properties.append(prop)
        return render_template('properties.html', properties=filtered_properties)
    return render_template('properties.html', properties=properties)