from database import Database
from menu import Menu

if __name__ == "__main__":
    Database.initialize()
    while True:
        menu = Menu()
        menu.run_menu()
        run_again = input("Do you wanna run again? (Y) or (N)")
        if run_again != 'Y':
            print("Ty for use our blog!")
            break