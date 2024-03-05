choice = input("You want to encrypt or decrypt?")
message = input("Enter your message: ")
shift = input("Enter the shift amount")

def encrypt(message, shift):
    cypher_text = ""
    for letter in message:
       if letter == ' ':
        cypher_text += ' '
       else:
        cypher_text += chr((ord(letter) + int(shift)))
    print(cypher_text)


def decrypt(message, shift):
    cypher_text = ""
    for letter in message:
        if letter == ' ':
            cypher_text += ' '
        else:
            cypher_text += chr((ord(letter) - int(shift)))
    print(cypher_text)

if choice == 'encrypt':
    encrypt(message, shift)
elif choice == 'decrypt':
    decrypt(message, shift)
else:
    "Run program again and enter encrypt or decrypt"


    