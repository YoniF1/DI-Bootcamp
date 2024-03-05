
#Challenge1

# word = input("Give me a word: ")
# word_dict = {}

# for i, letter in enumerate(word):
#     if letter in word_dict:
#         word_dict[letter].append(i)
#     else:
#         word_dict[letter] = [i]

# print(word_dict)

#Challenge2

import re

def calculate_affordable_items(items_purchase, wallet):
    total_cost = 0
    affordable_items = []

    for k, v in items_purchase.items():
        items_purchase[k] = re.sub(r'[^0-9]', '', v)

    for k, v in items_purchase.items():
        items_purchase[k] = int(v)

    clean_wallet = int(re.sub(r'[^0-9]', '', wallet))

    for k, v in items_purchase.items():
        if v < clean_wallet and total_cost < clean_wallet:
            affordable_items.append(k)
            total_cost += v

    affordable_items.sort()
    if affordable_items:
        print(affordable_items)
    else:
        print ("Nothing")

items_purchase_collection = [
    {
        "Water": "$1",
        "Bread": "$3",
        "TV": "$1,000",
        "Fertilizer": "$20"
    },
    {
        "Apple": "$4",
        "Honey": "$3",
        "Fan": "$14",
        "Bananas": "$4",
        "Pan": "$100",
        "Spoon": "$2"
    },
    {
        "Phone": "$999",
        "Speakers": "$300",
        "Laptop": "$5,000",
        "PC": "$1200"
    },
    ]

wallet = "".join(('$', input("How much money do you have in your wallet?: ")))

for items_purchase in items_purchase_collection:
    calculate_affordable_items(items_purchase, wallet)
  