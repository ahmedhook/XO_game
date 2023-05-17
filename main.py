import random

# Initialize the board
board = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]
]

# Define the players
human_player = "X"
computer_player = "O"

# Define the game functions
def draw_board():
    for row in board:
        print("|".join(row))

def get_human_move():
    while True:
        try:
            row = int(input("Enter the row for your move (1-3): ")) - 1
            col = int(input("Enter the column for your move (1-3): ")) - 1
            if board[row][col] == "-":
                return row, col
            else:
                print("That space is already taken. Please try again.")
        except ValueError:
            print("Invalid input. Please try again.")

def get_computer_move():
    _, move = minimax(board, True, -float('inf'), float('inf'))
    return move

def make_move(player, row, col):
    board[row][col] = player

def check_win(player):
    # Check rows
    for row in board:
        if row.count(player) == 3:
            return True

    # Check columns
    for col in range(3):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            return True

    # Check diagonals
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True

    return False

def check_tie():
    for row in board:
        if "-" in row:
            return False
    return True

def minimax(current_board, maximizing_player, alpha, beta):
    if check_win(human_player):
        return -1, None
    elif check_win(computer_player):
        return 1, None
    elif check_tie():
        return 0, None

    if maximizing_player:
        best_score = -float('inf')
        best_move = None
        for row in range(3):
            for col in range(3):
                if current_board[row][col] == "-":
                    current_board[row][col] = computer_player
                    score, _ = minimax(current_board, False, alpha, beta)
                    current_board[row][col] = "-"
                    if score > best_score:
                        best_score = score
                        best_move = (row, col)
                    alpha = max(alpha, best_score)
                    if alpha >= beta:
                        break
        return best_score, best_move
    else:
        best_score = float('inf')
        best_move = None
        for row in range(3):
            for col in range(3):
                if current_board[row][col] == "-":
                    current_board[row][col] = human_player
                    score, _ = minimax(current_board, True, alpha, beta)
                    current_board[row][col] = "-"
                    if score < best_score:
                        best_score = score
                        best_move = (row, col)
                    beta = min(beta, best_score)
                    if alpha >= beta:
                        break
        return best_score, best_move

# Start the game
current_player = human_player if random.choice([True, False]) else computer_player
print(f"The game has started. You are {human_player} and the computer is {computer_player}.")
draw_board()

while True:
    if current_player == human_player:
        row, col = get_human_move()
        make_move(human_player, row, col)
    else:
        print("The computer is thinking...")
        row, col = get_computer_move()
        make_move(computer_player, row, col)

    draw_board()

    if check_win(current_player):
        print(f"{current_player} has won the game!")
        break
    elif check_tie():
        print("The game is a tie!")
        break

    current_player = human_player if current_player == computer_player else computer_player