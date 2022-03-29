import subprocess
import week1.infoDB
from time import sleep, time

def get_menu_choice():
    subprocess.call("clear", shell=True)
    def print_menu():       # Your menu design here
        print(30 * "-", "Sub-Menu", 30 * "-")
        print("1. InfoDB For Loop")
        print("2. InfoDB While Loop")
        print("3. Recursive")
        print("4. Fibonacci")
        print("*. Back to Main Menu")
        print(73 * "-")
        

    loop = True
    # int_choice = -1 //debug thing

    while loop:          # While loop which will keep going until loop = False
        input("press enter to return to submenu")
        subprocess.call("clear", shell=True)  
        print_menu()    # Displays menu
        choice = input("Enter your choice [1-5]: ")

        if choice == '1':
            print("you chose number 1, the InfoDB For Loop")
            week1.infoDB.for_loop()
            # int_choice = 1 //more debug
        elif choice == '2':
            print("you chose While Loop")
            week1.infoDB.while_loop()

        elif choice == '3':
            print("you chose number 3, the Recursife Loop")
            # int_choice = 3
            week1.infoDB.recursive_loop(0)

        elif choice == '4':
            print("you chose number 4, the Fibonacci")
        elif choice == '5':
            # int_choice = -1
            print("SubMenu..")
        else:
            # Any inputs other than values 1-4 we print an error message
            # int_choice = -1
            print("Exiting..")
            loop = False
            subprocess.call("clear", shell=True)
    # return [int_choice, choice]


