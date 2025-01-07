user_imput = input("Please type a single word: ")
count = -1
final_string = ""
for _ in range(len(user_imput)):
    
    #print(user_imput[count])
    final_string += user_imput[count]
    count -= 1
    #print(reverse)
print(final_string)