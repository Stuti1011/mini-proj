from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/property/<int:property_id>')
def property(property_id):
    # Fetch property details from database or static data storage
    properties = [{'id': 1, 'location': 'New York', 'price': 100000, 'bedrooms': 2, 'description': 'Beautiful 2-bedroom apartment in Manhattan', 'photos': ['photo1.jpg', 'photo2.jpg']}]
    for prop in properties:
        if prop['id'] == property_id:
            return render_template('property.html', property=prop)
    return redirect(url_for('properties'))