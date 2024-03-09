# pip install pynput
from pynput import keyboard
from pynput.keyboard import Key, Listener

game_board = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' '],
]

map_move = {
    1: [0, 0],
    2: [0, 1],
    3: [0, 2],
    4: [1, 0],
    5: [1, 1],
    6: [1, 2],
    7: [2, 0],
    8: [2, 1],
    9: [2, 2],
}

player_symbols = {
    0: 'X',
    1: 'O'
}

current_player = 0
moves_made = 0

def on_key_release(key):
    global moves_made

    if key == Key.esc : return False  

    if hasattr(key, "char") and key.char.isdigit():
        move = int(key.char)
        player_symbol = player_symbols[moves_made % 2]
        make_move(move, player_symbol)
        moves_made += 1

def make_move(player_input, player_symbol):
    global current_player

    if player_input in map_move:
        row, column = map_move[player_input]
        if game_board[row][column] == " ":
            game_board[row][column] = player_symbol
            if player_symbol == 'X':
                current_player += 1
            else:
                current_player -= 1
            display_board()
            check_winner(player_symbol)
        else:
            print("There is already a symbol at this location, please choose another")

def display_board():
    for x in range(10):
        print(" *", end=" ")
    print('\n\n')
    game_grid()
    print('\n\n')
    print(f"Player {current_player}'s turn. Enter a number from 1-9 to make your move.")

def game_grid():
    for i, row in enumerate(game_board):
        print(" " + " | ".join(row))
        if i < 2:
            print(" - - - - - ")

def check_rows(player_symbol):
    for row in game_board:
        count = 0
        for col in row:
           if col == player_symbol:
             count += 1
        if count == len(game_board):
            print(f"{player_symbol}'s have won! Congratulations")
            return True 
    return False

def check_columns(player_symbol):
    for col in range(len(game_board)):
        count = 0
        for row in range(len(game_board)):
            if game_board[row][col] == player_symbol:
                count += 1
        if count == len(game_board):
            print(f"{player_symbol}'s have won! Congratulations")
            return True
    return False

def check_diagonals(player_symbol):
    count = 0
    for i in range(len(game_board)):
        if game_board[i][i] == player_symbol or game_board[i][len(game_board) - 1 - i] == player_symbol:
            count+=1
    if count == len(game_board):
        print(f"{player_symbol}'s have won! Congratulations")
        return True
    return False


def check_winner(player_symbol):
    check_rows(player_symbol)
    check_columns(player_symbol)
    check_diagonals(player_symbol)

def game():
    print("Welcome to TIC TAC TOE!\n")
    display_board()
    
    with Listener(on_release=on_key_release) as listener:
        listener.join()

game()
