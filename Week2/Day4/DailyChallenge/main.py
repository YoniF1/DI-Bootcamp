def add_whitespace(matrix):
    # To use zip - need to reinsert whitespace to even out number of elements in each sublist
    for i, row in enumerate(matrix):
        if len(row) == 1:
            matrix[i] = [row[0], ' ', ' ']
        elif len(row) == 2:
            matrix[i] = [row[0], row[1], ' ']
        else: 
            continue

def decrypt_matrix(matrix, secret_message):
    zipped = zip(*matrix)
    # zips the first element of each sublist together into tuple where rows have become columns
    symbol_number = 0
    for row in zipped:
        for letter in row:
            if letter.isalpha():
                if symbol_number >= 2: #i.e a group of symbols/whitespace
                    secret_message += ' '
                secret_message += letter
                symbol_number = 0 # reset count as new row on the next loop
            elif letter.isalnum(): # ignore numbers
                continue
            else:
                symbol_number += 1 #so only if symbol or whitespace increment
                continue

    print(secret_message)

def main():
    matrix_string = "7ii Tsx h%? i # sM $a #t% ^r!"
    reg_list = matrix_string.split()

    matrix = []
    for word in reg_list:
        matrix.append([*word]) 
    
    secret_message = ''

    add_whitespace(matrix)
    decrypt_matrix(matrix, secret_message)

main()
