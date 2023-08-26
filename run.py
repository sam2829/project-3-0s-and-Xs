game_board = ["-", "-", "-",
"-", "-", "-",
"-", "-", "-",]

current_player = "x"
winner = None

def print_game_board(game_board):
    """
    This function is printing out the grid for which the game is played on
    """
    print("---------------")
    print(" | " + game_board[0] + " | " + game_board[1] + " | " + game_board[2] + " | ")
    print("---------------")
    print(" | " + game_board[3] + " | " + game_board[4] + " | " + game_board[5] + " | ")
    print("---------------")
    print(" | " + game_board[6] + " | " + game_board[7] + " | " + game_board[8] + " | ")
    print("---------------")

print_game_board(game_board)