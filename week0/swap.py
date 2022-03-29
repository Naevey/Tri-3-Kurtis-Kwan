def getinput(): # gets input
   age1 = input("Input a value for age1: ")
   age2 = input("Input a value for age2: ")
   return(age1,age2) # this returns the variable outside
# def Age():
#   global age1
#   global age2
#   age1 = input("Input a value for age1: ")
#   age2 = input("Input a value for age2: ")
#   print("Original:", age1, age2,)
#   if age1 > age2:
#         numbers = [age1, age2]
#   else:
#       age1, age2 = age2, age1 
#       numbers = [age1, age2]
#     # print (sorted(numbers))
def sort(age1,age2): # sorter function
  if age1 > age2:
    return(age1,age2) 
  else:
    return(age2,age1)
  
# Age();
# print(age1)
# print(age2)

# age = getinput()
# sorted_age = sort(age[0], age[1]) #prints out the variable in arrays
# print(sorted_age[0], sorted_age[1])