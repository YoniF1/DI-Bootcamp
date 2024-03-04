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

dict = {}

word_list = list(word)

for i in word_list:
    if i in dict:
        continue
    else:
        dict[i] = 1

list_of_keys = list(dict.keys())
print(''.join(list_of_keys))
