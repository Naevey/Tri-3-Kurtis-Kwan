import re
def palindrome(string):
    str1 = ""  
    string = re.sub('\W+','', string) # \W removes all special characters, \w only keeps special characters
    string = string.lower() # for some reason the regex kept the capital letter
    for i in string:
        str1 = i + str1  # this reverses the string
    print("Reverse Order :  ", str1)
    
    if(string == str1): # this checks if it matches the original string
       print("This is a Palindrome String")
    else:
       print("This is Not")
string = ["abba", "monke", "A man, a plan, a canal, panama!", "racecar"] # word bank
for i in string: # puts the word in the palindrome function
  palindrome(i)