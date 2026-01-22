from Storage import Storage
from BudgetTracker import BudgetTracker
from Menu import Menu

# This is the main file that runs the whole program
def main():

    storage = Storage("data.json")
    tracker = BudgetTracker(storage)
    menu = Menu(tracker)
    menu.run()

if __name__ == "__main__":
    main()
