from Storage import Storage
from BudgetTracker import BudgetTracker
from Menu import Menu
# Here I import the core classes.
# This is the main file that starts the entire application
# It creates the main objects and connects all parts together
def main():

    # here i Create a Storage object to handle saving and loading data from data.json
    storage = Storage("data.json")

    # Creates a BudgetTracker object which controls the program logic
    # It receives the storage object so it can save and load information
    tracker = BudgetTracker(storage)

    # Creates the Menu object to interact with the user
    # The menu uses the tracker to perform actions
    menu = Menu(tracker)

    # Starts the program
    menu.run()

# This ensures the program only runs when this file is executed directly
if __name__ == "__main__":
    main()

