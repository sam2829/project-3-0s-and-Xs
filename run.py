class PlayGame:

    def __init__(self, game_board, current_player):
        """
        
        """
        self.game_board = game_board
        self.current_player = current_player

    def print_game_board(self, game_board, current_player):
        """
        This function is printing out the grid for which the game is played on
        """
        self.game_board = game_board

        print("---------------")
        print(" | " + game_board[0] + " | " + game_board[1] + " | " + game_board[2] + " | ")
        print("---------------")
        print(" | " + game_board[3] + " | " + game_board[4] + " | " + game_board[5] + " | ")
        print("---------------")
        print(" | " + game_board[6] + " | " + game_board[7] + " | " + game_board[8] + " | ")
        print("---------------")

    def player_input(self, game_board, current_player):
        """
        This function allows the user to select a grid position 1-9, the value entered must be an
        integer and must be a value 1 - 9.
        """
        self.game_board = game_board
        self.current_player = current_player

        while True:

            try:
                inp = int(input("Please select a grid position 1 - 9:\n "))
                if 1<= inp <=9 and self.game_board[inp-1] == "-":
                    self.game_board[inp-1] = current_player
                    break
                
                else:
                    raise ValueError(f"Please select a value between numbers 1 - 9")
            except ValueError as e:
                print(f"Invalid number: {e}, please try again.\n")
    
           

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
    print("The top left corner is value 0")
    print("-" * 45)
    player_name = input("Please enter your name: \n")
    print("-" * 45)
    print(f"Welcome {player_name} lets get start the game!")
    print("-" * 45)
    game_running = True
    game = PlayGame(game_board, current_player)
    game.print_game_board(game_board, current_player)
    game.player_input(game_board, current_player)


new_game()