# Import required libraries
import tkinter as tk
from tkinter import ttk

class HouseHuntingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("House Hunting App")

        # Create labels and entry fields for location and maximum price
        self.location_label = ttk.Label(root, text="Location:")
        self.location_label.grid(column=0, row=0, padx=10, pady=10)

        self.location_entry = ttk.Entry(root, width=30)
        self.location_entry.grid(column=1, row=0, padx=10, pady=10)

        self.price_label = ttk.Label(root, text="Maximum Price:")
        self.price_label.grid(column=0, row=1, padx=10, pady=10)

        self.price_entry = ttk.Entry(root, width=30)
        self.price_entry.grid(column=1, row=1, padx=10, pady=10)

        # Create button to search for houses
        self.search_button = ttk.Button(root, text="Search for Houses", command=self.search_houses)
        self.search_button.grid(column=1, row=2, padx=10, pady=10)

    def search_houses(self):
        # Get location and maximum price from entry fields
        location = self.location_entry.get()
        max_price = self.price_entry.get()

        # Here you can add your logic to search for houses based on location and maximum price
        # For now, just print the location and maximum price
        print(f"Searching for houses in {location} with a maximum price of {max_price}")

if __name__ == "__main__":
    root = tk.Tk()
    app = HouseHuntingApp(root)
    root.mainloop()