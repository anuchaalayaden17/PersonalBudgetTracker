import json
import os

# Storage class (saves and loads data using JSON file)
class Storage:

    def __init__(self, filename="data.json"):
        self.filename = filename

    def save(self, customer_data, expenses_data):
        data = {
            "customer": customer_data,
            "expenses": expenses_data
        }

        with open(self.filename, "w") as f:
            json.dump(data, f, indent=4)

    def load(self):
        if not os.path.exists(self.filename):
            return None, []

        with open(self.filename, "r") as f:
            data = json.load(f)

        return data.get("customer"), data.get("expenses", [])
