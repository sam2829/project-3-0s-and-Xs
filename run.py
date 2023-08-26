

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

def new_game():
    """
    This functions starts a new game and resets the board and board size.
    """
    game_board = ["-", "-", "-",
                  "-", "-", "-",
                  "-", "-", "-",]
    current_player = "x"
    winner = None
    print("-" * 45)
    print("Welcome to 0's and X's!!!")
    print("The tope left corner is value 0")
    print("-" * 45)
    player_name = input("Please enter your name: \n")
    print("-" * 45)
    print(f"Welcome {player_name} lets get start the game!")
    print("-" * 45)
    print_game_board(game_board)

new_game()