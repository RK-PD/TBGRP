import random

# Function to print the board
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

# Function to check if a player has won
def check_win(board, player):
    # Check rows
    for row in board:
        if row.count(player) == 3:
            return True

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == player:
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True

    return False

# Function to make a move
def make_move(board, player, row, col):
    if board[row][col] == " ":
        board[row][col] = player
        return True
    else:
        return False

# Function to check if the board is full
def is_board_full(board):
    for row in board:
        if " " in row:
            return False
    return True

# Function to get the AI's move
def get_ai_move(board):
    # Check if AI can win in the next move
    for row in range(3):
        for col in range(3):
            if board[row][col] == " ":
                board[row][col] = "O"
                if check_win(board, "O"):
                    return row, col
                else:
                    board[row][col] = " "

    # Check if player can win in the next move
    for row in range(3):
        for col in range(3):
            if board[row][col] == " ":
                board[row][col] = "X"
                if check_win(board, "X"):
                    return row, col
                else:
                    board[row][col] = " "

    # Choose a random empty spot
    while True:
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        if board[row][col] == " ":
            return row, col

# Function to play the game
def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    current_player = random.choice(players)

    while True:
        print_board(board)

        if current_player == "X":
            print("Player X's turn")
            row = int(input("Enter the row (0-2): "))
            col = int(input("Enter the column (0-2): "))
            if make_move(board, current_player, row, col):
                if check_win(board, current_player):
                    print_board(board)
                    print("Player X wins!")
                    break
                elif is_board_full(board):
                    print_board(board)
                    print("It's a tie!")
                    break
                else:
                    current_player = "O"
            else:
                print("Invalid move. Try again.")

        else:
            print("Player O's turn")
            row, col = get_ai_move(board)
            make_move(board, current_player, row, col)
            if check_win(board, current_player):
                print_board(board)
                print("Player O wins!")
                break
            elif is_board_full(board):
                print_board(board)
                print("It's a tie!")
                break
            else:
                current_player = "X"

# Start the game
play_game()
