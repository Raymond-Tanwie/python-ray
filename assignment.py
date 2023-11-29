# use functions to do the following::

# Enter a password
# enter password confirmation
# if both passwords are the same, return " The password and confirmation matches"
# if not, return "The password and confirmation doesn't match"
def check_password():
    # Enter a password
    password = input("Enter a password: ")

    # Enter password confirmation
    confirm_password = input("Enter password confirmation: ")

    # Check if both passwords match
    if password == confirm_password:
        return "The password and confirmation match"
    else:
        return "The password and confirmation don't match"

# Call the function and print the result
result = check_password()
print(result)
