name = input("what is your name ")
currentYear = 2023
birthYear = int(input("Enter your birth year : "))
age = currentYear - birthYear
isUnder18 = age > 18


if isUnder18:
    print("Hello, you have access to my program")
elif name == "Raymond":
    print("Hi you have access to my program because you are Raymond")
else:
    print("Hi, you don't have access to my program")