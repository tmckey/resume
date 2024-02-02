#Fun Harry Potter Trick

print("I'm thinking of a magic number between 1 and 100.")

# Magician's secret number
magician_secret_number = 23

# Ask the user to enter an integer number
user_number = int(input("Enter an integer number: "))

# Use a while loop to check whether the user's number matches the magician's secret number
while user_number != magician_secret_number:
    print("Ha ha! You're stuck in my loop!")
    user_number = int(input("Enter a number again: "))

# If the loop exits, the user's number matches the magician's secret number
print("Well done, muggle! You are free now.")
print("The magician's secret number was:", magician_secret_number)
