# recursion is the ability for a function to call itself. 
# to get the factorial of 4 we will execute 4 = 4x3x2x1


def factorial(n):
    if n < 2:
        return 1
    else:
        return n * factorial(n-1)
    
fact = factorial(10)
print(fact)

#create a password checker 
#enter a password
#enter password confirmation
#check if the password and password confirmation are the same
#return the password and confirmation matches
#if not return the password anc confirmation doesnot match