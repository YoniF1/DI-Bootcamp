# from urllib.request import urlretrieve
# import random

# url = "http://norvig.com/ngrams/sowpods.txt"
# urlretrieve(url, './words.txt')

# file = open('words.txt', 'r')


# def get_words_from_file():
#     list_of_words = file.read().splitlines() #avoids newline
#     return list_of_words

# def get_random_sentence(length):
#     return random.choices(get_words_from_file(), k = length )

# def create_sentence(length):
#     print(' '.join(get_random_sentence(length)).lower())

# def main():
#     print("This program creates a random sentences from a list of words found the internet")

#     length = int(input("How long do you want your sentence to be, enter an integer between 2-20: "))
    
#     if length in range(2, 21):
#         create_sentence(length)
#     else:
#         raise Exception("You need to enter an integer between 2-20")

#     file.close()

# main()

#Exercise2

# import json
# sampleJson = """{ 
#    "company":{ 
#       "employee":{ 
#          "name":"emma",
#          "payable":{ 
#             "salary":7000,
#             "bonus":800
#          }
#       }
#    }
# }"""

# #deserialize
# data = json.loads(sampleJson)

# print(data["company"])

# data["company"]["employee"]["birth_date"] = "10/06/1994"
# print(data)

# json_file = "sample.json"

# with open(json_file, 'w') as file_obj:
#     json.dump(data, file_obj, indent=2, sort_keys=True)
