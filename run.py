class PlayGame:

    def __init__(self, game_board, current_player, player_name, winner):
        """
        
        """
        self.game_board = game_board
        self.current_player = current_player
        self.player_name = player_name
        self.winner = winner

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

    def player_input(self, game_board, current_player, player_name):
        """
        This function allows the user to select a grid position 1-9, the value entered must be an
        integer and must be a value 1 - 9.
        """
        self.game_board = game_board
        self.current_player = current_player
        self.player_name = player_name

        while True:

            try:
                print("-" * 45)
                print(f"It's your turn {player_name}.\n")
                print("-" * 45)
                inp = int(input("Please select a grid position 1 - 9:\n "))
                if 1<= inp <=9 and self.game_board[inp-1] == "-":
                    self.game_board[inp-1] = current_player
                    break
                
                elif self.game_board != "-":
                    print("-" * 45)
                    print(f"Looks like that spot is already taken, please try again.\n")
                
                else:
                    raise ValueError(f"Please select a value between numbers 1 - 9")
            except ValueError as e:
                print(f"Invalid number: {e}, please try again.\n")

    def check_row(self, game_board, winner):
        """
        Thie function checks to see if there is a winner across any of the rows on the game board.
        """
        self.game_board = game_board
        self.winner = winner

        if game_board[0] == game_board[1] == game_board[2] and game_board[0] != "-":
            winner = game_board[0]
            return True
        
        elif game_board[3] == game_board[4] == game_board[5] and game_board[3] != "-":
            winner = game_board[3]
            return True
        
        elif game_board[6] == game_board[7] == game_board[8] and game_board[6] != "-":
            winner = game_board[6]
            return True
    

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
    game = PlayGame(game_board, current_player, game_running, winner)
    game.print_game_board(game_board, current_player)
    game.player_input(game_board, current_player, player_name)
    
    #while game_running:
       #game.print_game_board(game_board, current_player)
       #game.player_input(game_board, current_player, player_name)



new_game()