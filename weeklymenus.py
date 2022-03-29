import subprocess
from week0 import noships
from week0 import swap
from week0 import matrix
from week1 import fibonacci
from week1 import infoDB
from week2 import factorial
from week2 import triangular
import submenu
def weekZero():
  def get_menu_choice():
      subprocess.call("clear", shell=True)
      def print_menu():       # Your menu design here
          print(30 * "-", "Python Menu", 30 * "-")
          print("1. Swap")
          print("2. Matrix")
          print("3. Animation")
          print("4. Megamind Animation")        
          print("*. Exit")
          print(73 * "-")
  
      loop = True
      # int_choice = -1 //debug thing
  
      while loop:          # While loop which will keep going until loop = False  
          subprocess.call("clear", shell=True)  
          print_menu()    # Displays menu
          choice = input("Enter your choice [1-5]: ")
  
          if choice == '1':
              print("you chose number 1, the Swap")
              age = swap.getinput()
              sorted_age = swap.sort(age[0], age[1]) #prints out the variable in arrays
              print(sorted_age[0], sorted_age[1])
              input("press enter to go back")
              # int_choice = 1 //more debug
          elif choice == '2':
              print("you chose Matrix")
              matrix.Matrix()
              input("press enter to go back")
          elif choice == '3':
              subprocess.call("clear", shell=True)
              subprocess.call("python ship.py", shell=True)
              # int_choice = 3
          elif choice == '4':
              subprocess.call("clear", shell=True)
              noships.slhip()
              subprocess.call("clear", shell=True)
          elif choice == '5':
              print("SubMenu..")
              submenu.get_menu_choice()
          else:
              # int_choice = -1
              print("Exiting..")
              loop = False
              subprocess.call("clear", shell=True)
  print(get_menu_choice())
      # return [int_choice, choice]
def weekOne():
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
            infoDB.for_loop()
            # int_choice = 1 //more debug
        elif choice == '2':
            print("you chose While Loop")
            infoDB.while_loop()

        elif choice == '3':
            print("you chose number 3, the Recursive Loop")
            # int_choice = 3
            infoDB.recursive_loop(0)

        elif choice == '4':
            print("you chose number 4, the Fibonacci")
            fibonacci.fibonacci()
        elif choice == '5':
            # int_choice = -1
            print("SubMenu..")
        else:
            # Any inputs other than values 1-4 we print an error message
            # int_choice = -1
            print("Exiting..")
            loop = False
            subprocess.call("clear", shell=True)
  print(get_menu_choice())
def weekTwo():
  def get_menu_choice():
    subprocess.call("clear", shell=True)
    def print_menu():       # Your menu design here
        print(30 * "-", "Sub-Menu", 30 * "-")
        print("1. Factorial")
        print("2. Triangular OOP")
        print("3. Triangular Imperative")
        print("*. Back to Main Menu")
        print(73 * "-")
    loop = True
    # int_choice = -1 //debug thing

    while loop:          # While loop which will keep going until loop = False
        input("press enter to return to menu")
        subprocess.call("clear", shell=True)  
        print_menu()    # Displays menu
        choice = input("Enter your choice [1-5]: ")

        if choice == '1':
            print("you chose number 1, the Factorial")
            num = factorial.__init__() # uses the above function to return an input
            factorial.factorial(num)
            # int_choice = 1 //more debug
        elif choice == '2':
            print("you chose Triangular OOP")
            n = input("Enter a number: ")
            n = int(n)
            print(triangular.Triangle(n))  
            

        elif choice == '3':
            print("you chose number 3, the Triangular Imperative")
            num = triangular.getnum() # uses the above function to return an input
            triangular.triangular(num)
            # int_choice = 3
        else:
            # Any inputs other than values 1-4 we print an error message
            # int_choice = -1
            print("Exiting..")
            loop = False
            subprocess.call("clear", shell=True)
  print(get_menu_choice())

