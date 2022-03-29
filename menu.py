import subprocess
import submenu
import weeklymenus
def get_menu_choice():
    subprocess.call("clear", shell=True)
    def print_menu():       # Your menu design here
        print(30 * "-", "Python Menu", 30 * "-")
        print("1. Week0")
        print("2. Week1")
        print("3. Week2")
        print("*. Exit")
        print(73 * "-")

    loop = True
    # int_choice = -1 //debug thing

    while loop:          # While loop which will keep going until loop = False  
        subprocess.call("clear", shell=True)  
        print_menu()    # Displays menu
        choice = input("Enter your choice [1-5]: ")

        if choice == '1':
            print("you chose Week0")
            weeklymenus.weekZero()
        elif choice == '2':
            print("you chose Week1")
            weeklymenus.weekOne()
        elif choice == '3':
            print("you chose Week2")
            weeklymenus.weekTwo()
            # int_choice = 3
        
        else:
            # int_choice = -1
            print("Exiting..")
            loop = False
            subprocess.call("clear", shell=True)
    # return [int_choice, choice]


print(get_menu_choice())