# Get the client to enter their username on the console
get_theUsername = input('Enter your username: ')

# While the entered username is less than 8 or greater than 20 characters
while len(get_theUsername) < 8 or len(get_theUsername) > 20:

    # The client needs to enter the username again & a message will be shown as a hint
    get_theUsername = input("Enter your username again: (Must be between 8 to 20 characters) " )

# Once the username entered by the client met the conditions the success message will be shown
print("Username accepted")