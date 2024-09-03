import tkinter as tk
from tkinter import ttk

class HouseHuntingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("House Hunting App")

        # Create labels and entry fields for location, maximum price, and bedrooms
        self.location_label = ttk.Label(root, text="Location:")
        self.location_label.grid(column=0, row=0, padx=10, pady=10)

        self.location_entry = ttk.Entry(root, width=30)
        self.location_entry.grid(column=1, row=0, padx=10, pady=10)

        self.price_label = ttk.Label(root, text="Price:")
        self.price_label.grid(column=0, row=1, padx=10, pady=10)

        self.price_entry = ttk.Entry(root, width=30)
        self.price_entry.grid(column=1, row=1, padx=10, pady=10)

        self.bedrooms_label = ttk.Label(root, text="Bedrooms:")
        self.bedrooms_label.grid(column=0, row=2, padx=10, pady=10)

        self.bedrooms_entry = ttk.Entry(root, width=30)
        self.bedrooms_entry.grid(column=1, row=2, padx=10, pady=10)

        # Create button to search for houses
        self.search_button = ttk.Button(root, text="Search for PG", command=self.search_houses, width=20)
        self.search_button.grid(column=1, row=3, padx=10, pady=10)

        # Create a text area to display search results
        self.results_text = tk.Text(root, width=80, height=20)
        self.results_text.grid(column=0, row=4, columnspan=2, padx=10, pady=10)

    def search_houses(self):
        # Get user input from entry fields
        location = self.location_entry.get()
        max_price = self.price_entry.get()
        bedrooms = self.bedrooms_entry.get()

        # Sample properties data (in a real app, this would come from a database or API)
        properties = [
            {'id': 1, 'location': 'Nerul', 'price': 10000, 'bedrooms': 1, 'description': 'Area - 200 sq. feet and is at walking distace of 5 minutes from DY Patil college'},
            {'id': 2, 'location': 'Juinagar', 'price': 8000, 'bedrooms':1, 'description': 'Terrace room , 300 sq feet '},
            {'id': 3, 'location': 'Nerul', 'price': 5000, 'bedrooms': 1, 'description': 'Only for Girls.The room should be shared with 3 other PGs'},
        ]

        # Filter properties based on user input
        filtered_properties = [
            prop for prop in properties
            if (location.lower() in prop['location'].lower()) and
               (not max_price or prop['price'] <= int(max_price)) and
               (not bedrooms or prop['bedrooms'] == int(bedrooms))
        ]

        # Display results
        self.results_text.delete(1.0, tk.END)  # Clear previous results
        if filtered_properties:
            for prop in filtered_properties:
                result = f"ID: {prop['id']}\nLocation: {prop['location']}\nPrice: ${prop['price']}\nBedrooms: {prop['bedrooms']}\nDescription: {prop['description']}\n\n"
                self.results_text.insert(tk.END, result)
        else:
            self.results_text.insert(tk.END, "No PGs found matching your criteria.\n")

if __name__ == "__main__":
    root = tk.Tk()
    app = HouseHuntingApp(root)
    root.mainloop()
