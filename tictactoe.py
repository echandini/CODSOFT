import random

# Create board
board = [" " for i in range(9)]

# Print board
def print_board():
    print("\n")
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("--+---+--")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("--+---+--")
    print(board[6] + " | " + board[7] + " | " + board[8])
    print("\n")

# Check winner
def check_winner(player):
    win_positions = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]

    for pos in win_positions:
        if board[pos[0]] == board[pos[1]] == board[pos[2]] == player:
            return True
    return False

# Check draw
def check_draw():
    return " " not in board

# AI move
def ai_move():
    empty = [i for i in range(9) if board[i] == " "]
    move = random.choice(empty)
    board[move] = "O"

# Main game loop
print("===== TIC-TAC-TOE AI =====")
print("You are X and AI is O")
print("Positions are from 1 to 9")

while True:

    print_board()

    # User input
    try:
        move = int(input("Enter position (1-9): ")) - 1

        if board[move] != " ":
            print("Position already taken!")
            continue

        board[move] = "X"

    except:
        print("Invalid input!")
        continue

    # Check player win
    if check_winner("X"):
        print_board()
        print("🎉 You Win!")
        break

    # Check draw
    if check_draw():
        print_board()
        print("Game Draw!")
        break

    # AI turn
    ai_move()

    # Check AI win
    if check_winner("O"):
        print_board()
        print("🤖 AI Wins!")
        break

    # Check draw
    if check_draw():
        print_board()
        print("Game Draw!")
        break