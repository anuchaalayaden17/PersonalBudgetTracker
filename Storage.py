import json
import os

# Storage class is responsible for saving and loading data
# It uses a JSON file to store customer and expense information
class Storage:

    def __init__(self, filename="data.json"):
        # Store the filename where data will be saved
        self.filename = filename

    # Saves customer and expenses to JSON file
    def save(self, customer_data, expenses_data):

        # Organize data into dictionary format
        data = {
            "customer": customer_data,
            "expenses": expenses_data
        }

        # Open file in write mode and save JSON data
        with open(self.filename, "w") as f:
            json.dump(data, f, indent=4)

    # Loads customer and expenses from JSON file
    def load(self):

        # Check if file exists
        if not os.path.exists(self.filename):
            return None, []

        # Open file in read mode and load JSON data
        with open(self.filename, "r") as f:
            data = json.load(f)

        # Return customer and expenses separately
        return data.get("customer"), data.get("expenses", [])

