# Ive imported random to generate a random number for computers turn.
import random


class PlayGame:

    def __init__(self, player_name):
        """
        Creates an instance of PlayGame
        """
        self.game_board = ["-", "-", "-",
                           "-", "-", "-",
                           "-", "-", "-"]
        self.current_player = "x"
        self.player_name = player_name
        self.winner = None
        self.game_running = True

    def print_game_board(self):
        """
        This method is printing out the grid for which the game is played on
        """
        print("---------------")
        print(" | " + self.game_board[0] + " | " + self.game_board[1] +
              " | " + self.game_board[2] + " | ")
        print("---------------")
        print(" | " + self.game_board[3] + " | " + self.game_board[4] +
              " | " + self.game_board[5] + " | ")
        print("---------------")
        print(" | " + self.game_board[6] + " | " + self.game_board[7] +
              " | " + self.game_board[8] + " | ")
        print("---------------")

    def player_input(self):
        """
        This method allows the user to select a grid position 1-9,
        the value entered must be an integer and must be a value 1 - 9.
        """

        while True:

            try:
                print("-" * 45)
                print(f"It's your turn {self.player_name}.\n")
                print("-" * 45)
                grid_pos = (input("Please select a grid position 1 - 9 "
                                  "or type in 'quit' to leave the game:\n "))

                if grid_pos.lower() == "quit":
                    self.game_running = False
                    break

                grid_pos = int(grid_pos)

                if 1 <= grid_pos <= 9 and self.game_board[grid_pos-1] == "-":
                    self.game_board[grid_pos-1] = self.current_player
                    break
                elif 1 <= grid_pos <= 9 and self.game_board[grid_pos-1] != "-":
                    print("-" * 45)
                    print(f"Looks like that spot is already taken, "
                          "please try again.\n")
                    self.print_game_board()
                else:
                    raise ValueError(f"Please select a value between "
                                     "numbers 1 - 9")
            except ValueError as e:
                print("-" * 45)
                print(f"Invalid number: {e},\n please try again.\n")
                self.print_game_board()

    def check_row(self):
        """
        This method checks to see if there is a winner across any of
        the rows on the game board.
        """

        if (self.game_board[0] == self.game_board[1] == self.game_board[2]
           and self.game_board[0] != "-"):
            self.winner = self.game_board[0]
            return True
        elif (self.game_board[3] == self.game_board[4] == self.game_board[5]
              and self.game_board[3] != "-"):
            self.winner = self.game_board[3]
            return True
        elif (self.game_board[6] == self.game_board[7] == self.game_board[8]
              and self.game_board[6] != "-"):
            self.winner = self.game_board[6]
            return True

    def check_column(self):
        """
        This method checks to see if there is a winner across any of
        the columns on the game board.
        """
        if (self.game_board[0] == self.game_board[3] == self.game_board[6]
           and self.game_board[0] != "-"):
            self.winner = self.game_board[0]
            return True
        elif (self.game_board[1] == self.game_board[4] == self.game_board[7]
              and self.game_board[1] != "-"):
            self.winner = self.game_board[1]
            return True
        elif (self.game_board[2] == self.game_board[5] == self.game_board[8]
              and self.game_board[2] != "-"):
            self.winner = self.game_board[2]
            return True

    def check_diagonal(self):
        """
        This method checks to see if there is a winner across any of
        the diagonals on the game board.
        """
        if (self.game_board[0] == self.game_board[4] == self.game_board[8]
           and self.game_board[0] != "-"):
            self.winner = self.game_board[0]
            return True
        elif (self.game_board[2] == self.game_board[4] == self.game_board[6]
              and self.game_board[2] != "-"):
            self.winner = self.game_board[2]
            return True

    def check_for_winner(self):
        """
        This method will check to see if there has been a winner and if
        so return a false to game_running and stop the game.
        """

        if self.check_row() or self.check_column() or self.check_diagonal():
            self.print_game_board()
            if self.winner == "x":
                print(f"Congratulations {self.player_name} you won!\n")
                self.game_running = False
                self.current_player = None
            else:
                print(f"Unlucky, computer wins!")
                self.game_running = False
                self.current_player = None

    def check_for_tie(self):
        """
        This method checks to see if the game has ended in a tie
        """

        if ("-" not in self.game_board and not self.check_row()
           and not self.check_column() and not self.check_diagonal()):
            print("-" * 45)
            self.print_game_board()
            print("It's a tie!")
            self.game_running = False
            self.current_player = None

    def switch_player(self):
        """
        This method switches who's go it is, whether or not its x or 0.
        """

        if self.current_player == "x":
            self.current_player = "0"
        else:
            self.current_player = "x"

    def computers_turn(self):
        """
        This method allows the computer to decide where on the grid it
        would like to place its go
        """

        while self.current_player == "0":
            position = random.randint(0, 8)
            if self.game_board[position] == "-":
                self.game_board[position] = "0"
                self.switch_player()

    def restart_game(self):
        """
        This method asks the user if they would like to play the game again.
        Yes will restart the game, anything else will end the game.
        """
        print("-" * 45)
        play_again = (input(f"Would you like to play again? "
                            "Please type 'yes' or 'no'.\n"))
        try:
            if play_again.lower() == "yes":
                new_game()
            elif play_again.lower() == "no":
                print("-" * 45)
                print("Thanks for playing.")
            else:
                raise ValueError(f"Please type in 'yes' or 'no',\n")
        except ValueError as e:
            print("-" * 45)
            print(f"Invalid input: {e} please try again.")
            self.restart_game()

    def run_game(self):
        """
        This method is allowing us to play the game and creates a while loop,
        which keeps looping until we have a winnner.
        """
        while self.game_running:
            self.print_game_board()
            self.player_input()
            self.check_for_winner()
            self.check_for_tie()
            self.switch_player()
            # This if not statement was added so that if the
            # user wins or it is a tie,the game board and results
            # message isnt printed twice.
            if not self.game_running:
                self.restart_game()
                break
            self.computers_turn()
            self.check_for_winner()
            self.check_for_tie()
        else:
            self.restart_game()


def new_game():
    """
    This function calls the PlayGame class to start the game. It asks for
    the players name and also prints out the game board showing the number
    values of each grid position on the grid.
    """
    print("-" * 45)
    print("Welcome to 0's and X's the game!!!")
    print("Below is the game board showing you the number value of each grid\n"
          "position of the game board.\n")
    game_board_value = ["1", "2", "3",
                        "4", "5", "6",
                        "7", "8", "9"]
    print("---------------")
    print(" | " + game_board_value[0] + " | " + game_board_value[1] +
          " | " + game_board_value[2] + " | ")
    print("---------------")
    print(" | " + game_board_value[3] + " | " + game_board_value[4] +
          " | " + game_board_value[5] + " | ")
    print("---------------")
    print(" | " + game_board_value[6] + " | " + game_board_value[7] +
          " | " + game_board_value[8] + " | ")
    print("---------------")
    print("-" * 45)
    player_name = input("Please enter your name: \n")
    print("-" * 45)
    print(f"Welcome {player_name} lets get start the game!")
    print("-" * 45)
    game = PlayGame(player_name)
    game.run_game()


new_game()
