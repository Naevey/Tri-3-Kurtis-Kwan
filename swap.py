def Age():
    global age1
    global age2
    age1 = input("Input a value for age1: ")
    age2 = input("Input a value for age2: ")
    print("Original:", age1, age2,)
    if age1 > age2:
        numbers = [age1, age2]
    else:
        age1, age2 = age2, age1
        numbers = [age1, age2]
    # print (sorted(numbers))

Age();
print(age1)
print(age2)