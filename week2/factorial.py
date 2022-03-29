def __init__(): # gets input
   num1 = input("Input a number: ") 
   
   return(num1) # returns the input
def factorial(num1):
    n = num1
    n = int(n) # converts the input into an integer
    fact = 1 # this is the actual factorial answer
      
    for i in range(1,n+1): # n+1 makes sure that it includes itself
        fact = fact * i # factorial times itself
        print(fact, " ", end = '') # end = makes sure that it does not print a newline
    print ("\nThe factorial of", n, " is :", fact)




