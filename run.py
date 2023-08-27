class PlayGame:

    def __init__(self, player_name):
        """
        
        """
        self.game_board = ["-", "-", "-",
                           "-", "-", "-",
                           "-", "-", "-",]
        self.current_player = "x"
        self.player_name = player_name
        self.winner = None
        self.game_running = True

    def print_game_board(self):
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

    def player_input(self):
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

    def check_row(self):
        """
        Thie function checks to see if there is a winner across any of the rows on the game board.
        """
        self.game_board = game_board
        self.winner = winner

        if game_board[0] == game_board[1] == game_board[2] and game_board[0] != "-":
            self.winner = game_board[0]
            return True
        
        elif game_board[3] == game_board[4] == game_board[5] and game_board[3] != "-":
            self.winner = game_board[3]
            return True
        
        elif game_board[6] == game_board[7] == game_board[8] and game_board[6] != "-":
            self.winner = game_board[6]
            return True


    def check_column(self):
        """
        Thie function checks to see if there is a winner across any of the columns on the game board.
        """
        self.game_board = game_board
        self.current_player = current_player
        self.player_name = player_name
        self.winner = winner
        


        if game_board[0] == game_board[3] == game_board[6] and game_board[0] != "-":
            self.winner = game_board[0]
            return True
        
        elif game_board[1] == game_board[4] == game_board[7] and game_board[1] != "-":
            self.winner = game_board[1]
            return True
        
        elif game_board[2] == game_board[5] == game_board[8] and game_board[2] != "-":
            self.winner = game_board[2]
            return True

    def check_diagonal(self):
        """
        Thie function checks to see if there is a winner across any of the diagonals on the game board.
        """
        self.game_board = game_board
        self.winner = winner

        if game_board[0] == game_board[4] == game_board[8] and game_board[0] != "-":
            self.winner = game_board[0]
            return True
        
        elif game_board[2] == game_board[4] == game_board[6] and game_board[2] != "-":
            self.winner = game_board[2]
            return True

    def check_for_winner(self):
        """
        This function will check to see if there has been a winner and if so return a false to game_running and stop the game.
        """

        if self.check_row() or self.check_column() or self.check_diagonal():
            self.print_game_board()
            print(f"The winner is {self.winner}!\n")
            self.game_running = False

    def run_game(self):
        """
        This function is allowing us to play the game and creates a while loop, which keeps looping until we have a winnner.
        """

        while self.game_running:
            self.print_game_board()
            self.player_input()
            self.check_for_winner()


def new_game():
    """
    This functions starts a new game and resets the board and board size.
    """
    print("-" * 45)
    print("Welcome to 0's and X's!!!")
    print("The top left corner is value 0")
    print("-" * 45)
    player_name = input("Please enter your name: \n")
    print("-" * 45)
    print(f"Welcome {player_name} lets get start the game!")
    print("-" * 45)
    game = PlayGame(player_name)
    game.run_game()
    
   



new_game()