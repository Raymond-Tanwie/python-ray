import random
randomNumber= random.randrange(1, 100)

providedNumber = int(input("Guess the Number : "))
attempts = 0
while providedNumber is not randomNumber:
    attempts += 1  # this is a loop telling us the number of times that the person attempted
    if providedNumber > randomNumber:
        print ("Lower")
    elif providedNumber < randomNumber:
        print ("Higher")
    providedNumber = int(input("Guess the number : "))
print(f"Congratulation, you got the correct answer after {attempts} attempts")   # the f added inside print acts as concatenation  