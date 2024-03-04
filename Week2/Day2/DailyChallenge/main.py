#Challenge1

# number = int(input("Enter a number: "))
# length = int(input("Enter a length: "))

# final_list = []
# i = 0

# while i < length:
#     i+=1
#     final_list.append(number * i)

# print(final_list)


#Challenge2

word = input("Enter a word with duplicate letters: ")

final_list = []

i=0
while i < len(word):
    if i == len(word) -1 or word[i] != word[i + 1]:
        final_list.append(word[i])
    i+=1
    
print(''.join(final_list))
