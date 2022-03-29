
# Hack 1: InfoDB lists.  Build your own/personalized InfoDb with a list length > 3,  create list within a list as illustrated with Owns_Cars
InfoDb = []
# List with dictionary records placed in a list  
InfoDb.append({  
               "FirstName": "Joan",  
               "LastName": "Mir",  
               "Number": 36,  
               "Team": "Suzuki Ecstar",  
               "Age": "24",  
               "Results":["3","2","4","DNF", "2"]  
              })  
InfoDb.append({  
               "FirstName": "Marc",  
               "LastName": "Marquez",  
               "Number": 93,  
               "Team": "Repsol Honda",  
               "Age": "29",  
               "Results":["1","DNF","DNF","2", "1"]  
              })  
InfoDb.append({  
               "FirstName": "Valentino",  
               "LastName": "Rossi",  
               "Number": 46,  
               "Team": "Monster Energy Yamaha",  
               "Age": "43",  
               "Results":["10","DNF","9","11", "13"]  
              }) 
InfoDb.append({  
               "FirstName": "Jorge",  
               "LastName": "Martin",  
               "Number": 89,  
               "Team": "Ducati Lenovo",  
               "Age": "24",  
               "Results":["4","3","1","DNF", "5"]  
              }) 


def printe(f): 
  print(f["FirstName"], f["LastName"]) #the Firstname or LastName of InfoDb
  print("\t Number:", f["Number"]) # the f is the f string in python
  print("\t Team:", f["Team"])     # it is another way of formatting
  print("\t Age:", f["Age"])
  print("\t Results:", f["Results"])

def for_loop():
  for f in InfoDb:
    print(10*"~", "For Loops", 10*"~")
    printe(f)
def while_loop():
    f = 0
    while f < len(InfoDb):
      print(10*"~", "While Loops", 10*"~")
      printe(InfoDb[f])
      f = f+1
def recursive_loop(f):
  if f == len(InfoDb): # this makes sure that the f is equal to the length of InfoDb
    return f # this puts f outside, so the second if statement can use it
    
  if f == 0:
    print("~"*10 + "Recursive Loops" + "~"*10)
    
  printe(InfoDb[f])
  print("~"*10 + "Recursive Loops" + "~"*10)
  recursive_loop(f + 1)
