class Triangle: 
    def __init__(self, n): # defines variables
       self.n = n
       self.triangle = self.triangular()
    def triangular(self):
        number = 0
        for i in range(self.n):
          number = number + i
          print(" ", number, end="")
        return number
    def __str__(self):
        return (f"\nThe triangular of {self.n} is {self.triangle}")
    




def getnum(): # gets input
   num1 = input("Input a number: ") 
   
   return(num1) # returns the input
def triangular(num1):
    n = int(num1)
    number = 0
    
    print("The first", n, "triangular numbers are:")
    for i in range(1,n):
      number = number + i
      print(number)




