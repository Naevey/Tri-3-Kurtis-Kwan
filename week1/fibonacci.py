def fibonacci():
  # first two terms
  n1 = 0 # starts from 0
  n2 = 1 # starts from 1
  count = 0
  
  try:
    nterms = int(input("How many terms?"))
  
  # if there is only one term, print 0
    if nterms == 1:
       print("Fibonacci sequence to 1")
       print(n1)
  #else it prints the rest
    else:
       print("Sequence of", nterms, "terms")
       while count <= nterms:
           print(n1) # prints out  0
           nth = n1 + n2 # updates the nth term to it first plus second
           # update values
           n1 = n2 # first becomes second
           n2 = nth # second becomes the third, or sum of first and second
           count += 1 # raises the count until the count matches the number of terms
  
  except ValueError:
          print("Please use a whole number")
  except:
    # check if the number of terms is valid
    if nterms <= 0:
       print("Please use a positive number")
