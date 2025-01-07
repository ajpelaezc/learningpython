# Read input from the keyboard
user_input = input("Please enter something: ")

while True:
    # Check if the input starts with 'A' or 'a'
    if user_input.startswith('A') or user_input.startswith('a'):
        print("The word starts with 'A' or 'a'.")
        print("You entered:", user_input)
        break  # Exit the loop
    else:
        print("The word does not start with 'A' or 'a'. Please try again.")
        user_input = input("Please enter something: ")  # Read input from the keyboard


