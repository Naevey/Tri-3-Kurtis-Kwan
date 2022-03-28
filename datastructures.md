{% include navbar.html %}

<iframe frameborder="0" width="100%" height="500px" src="https://replit.com/@charlesElipton/Tri-3-Kurtis-Kwan?embed=true"></iframe>


# Data Structures
## Code
## [Repl](https://replit.com/@charlesElipton/Tri-3-Kurtis-Kwan#.replit)

## What I learned this week/Code Snippets
Week 2:
  Using OOP form, specifically with classes. It is a little confusing, but I think that I am getting the hang of it. A little more of Regular Expressions.
  ```
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
 ```

Week 1:
  Using for, while loops. Also using Recursive loops. Python dictionaries, f string for print, 
  ```
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
  ```
Week 0: 
  Creating a python menu, using print and * to multiply number of spaces or other characters.
  ```   
  print(10*"~", "For Loops", 10*"~")
  ```
