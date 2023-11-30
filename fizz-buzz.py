numbers = range (1,50)

def fizzbuzz(array):
    for number in array:
        if number % 3 == 0:
            print("Fizz")
        elif number % 5 ==0:
            print ("Buzz")
        else:
            print(number)
            
            
fizzbuzz(numbers)