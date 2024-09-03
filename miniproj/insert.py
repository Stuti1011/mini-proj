import tkinter as tk
from tkinter import ttk

class HouseHuntingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("House Hunting App")

        # Background color for the section
        bg_color = "light gray"

        # Create labels and entry fields for location, maximum price, and bedrooms
        self.location_label = ttk.Label(root, text="Location:", background=bg_color)
        self.location_label.grid(column=0, row=0, padx=10, pady=10)

        self.location_entry = tk.Entry(root, width=30, bg=bg_color)
        self.location_entry.grid(column=1, row=0, padx=10, pady=10)

        self.price_label = ttk.Label(root, text="Price:", background=bg_color)
        self.price_label.grid(column=0, row=1, padx=10, pady=10)

        self.price_entry = tk.Entry(root, width=30, bg=bg_color)
        self.price_entry.grid(column=1, row=1, padx=10, pady=10)

        self.bedrooms_label = ttk.Label(root, text="Bedrooms:", background=bg_color)
        self.bedrooms_label.grid(column=0, row=2, padx=10, pady=10)

        self.bedrooms_entry = tk.Entry(root, width=30, bg=bg_color)
        self.bedrooms_entry.grid(column=1, row=2, padx=10, pady=10)

        # New fields for entering property description
        self.description_label = ttk.Label(root, text="Description:", background=bg_color)
        self.description_label.grid(column=0, row=3, padx=10, pady=10)

        self.description_entry = tk.Entry(root, width=30, bg=bg_color)
        self.description_entry.grid(column=1, row=3, padx=10, pady=10)

        # Button to search for PGs
        self.search_button = ttk.Button(root, text="Search for PG", width=20, command=self.search_houses)
        self.search_button.grid(column=1, row=4, padx=10, pady=10)

        # Button to add a new property
        self.add_button = ttk.Button(root, text="Add PG", width=20, command=self.add_property)
        self.add_button.grid(column=1, row=5, padx=10, pady=10)

        # Text widget to display search results or added properties
        self.results_text = tk.Text(root, width=80, height=20, bg="white")
        self.results_text.grid(column=0, row=6, columnspan=2, padx=10, pady=10)

        # List to hold the properties
        self.properties = []

    def search_houses(self):
        # Clear the results area before displaying new search results
        self.results_text.delete(1.0, tk.END)

        location = self.location_entry.get().lower()
        max_price = self.price_entry.get()
        bedrooms = self.bedrooms_entry.get()

        # Sample properties data (in a real app, this would come from a database or API)
        properties = [
            {'id': 1, 'location': 'Nerul', 'price': 10000, 'bedrooms': 1, 'description': 'Area - 200 sq. feet and is at walking distace of 5 minutes from DY Patil college'},
            {'id': 2, 'location': 'Juinagar', 'price': 8000, 'bedrooms': 1, 'description': 'Terrace room, 300 sq feet'},
            {'id': 3, 'location': 'Nerul', 'price': 5000, 'bedrooms': 1, 'description': 'Only for Girls. The room should be shared with 3 other PGs'},
        ]

        # Filter properties based on user input
        filtered_properties = [
            prop for prop in properties
            if (location.lower() in prop['location'].lower()) and
               (not max_price or prop['price'] <= int(max_price)) and
               (not bedrooms or prop['bedrooms'] == int(bedrooms))
        ]

        # Display results
        if filtered_properties:
            for prop in filtered_properties:
                result = f"ID: {prop['id']}\nLocation: {prop['location']}\nPrice: ${prop['price']}\nBedrooms: {prop['bedrooms']}\nDescription: {prop['description']}\n\n"
                self.results_text.insert(tk.END, result)
        else:
            self.results_text.insert(tk.END, "No PGs found matching your criteria.\n")

    def add_property(self):
        # Get the input values from the user
        location = self.location_entry.get()
        price = self.price_entry.get()
        bedrooms = self.bedrooms_entry.get()
        description = self.description_entry.get()

        # Check if any fields are empty
        if not location or not price or not bedrooms or not description:
            self.results_text.insert(tk.END, "All fields must be filled out to add a property.\n")
            return

        # Create a new property dictionary
        new_property = {
            'id': len(self.properties) + 1,
            'location': location,
            'price': int(price),
            'bedrooms': int(bedrooms),
            'description': description
        }

        # Add the new property to the list
        self.properties.append(new_property)

        # Display a confirmation message in the results area
        self.results_text.insert(tk.END, f"Property ID: {new_property['id']} added successfully.\n")

if __name__ == "__main__":
    root = tk.Tk()
    app = HouseHuntingApp(root)
    root.mainloop()
