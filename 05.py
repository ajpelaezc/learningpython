user_input = input("Please type a single word: ")

# Using a loop
reversed_input = ""
for char in user_input:

    reversed_input = char + reversed_input
    print(reversed_input)
print("Reversed input:", reversed_input)