# # Menu options in print statement
# def print_menu1():
#     print('1 -- ship' )
#     print('2 -- Numby' )
#     print('3 -- NoShips' )
#     print('4 -- Exit' )
#     runOptions()


# # Menu options as a dictionary
# menu_options = {
#     1: 'ship',
#     2: 'swap',
#     3: 'Listy',
#     4: 'Exit',
# }

# # Print menu options from dictionary key/value pair
# def print_menu2():
#     for key in menu_options.keys():
#         print(key, '--', menu_options[key] )
#     runOptions()

# # menu option 1
# def ship():
#     print('You chose \' 1 -  ship\'')
#     # import ship.py  these are a test to how to run the scripts
#     # ship.py
#     subprocess.call("python ship.py", shell=True)
#   # menu option 2
# def swap():
#     print('You chose \' 2 - swap\'')
#     age = getinput()
#     sorted_age = sort(age[0], age[1]) #prints out the variable in arrays
#     print(sorted_age[0], sorted_age[1])
# # menu option 3
# def noship():
#     print('You chose \'3 - No Ships\'')
#     noships.slhip()

# # call functions based on input choice
# def runOptions():
#     # infinite loop to accept/process user menu choice
#     while True:
#         try:
#             option = int(input('Enter your choice 1-4: '))
#             if option == 1:
#                 ship()
#             elif option == 2:
#                 swap()
#             elif option == 3:
#                 noship()
#             # Exit menu    
#             elif option == 4:  
#                 print('Exiting! Thank you! Good Bye...')
#                 exit() # exit out of the (infinite) while loop
#             else:
#                 print('Invalid option. Please enter a number between 1 and 4.')
#         except ValueError:
#             print('Invalid input. Please enter an integer input.')

# if __name__=='__main__':
#     # print_menu1()
#     print_menu2()

