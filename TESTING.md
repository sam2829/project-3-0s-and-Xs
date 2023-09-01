# 0's and X's the game Testing

## Contents

* [Automated Testing](#automated-testing)
* [Manual Testing](#manual-testing)

## Automated Testing

- Passed the code through a PEP8 linter and confirmed there are no problems.

## Manual Testing

I have manually tested this project by doing the following:

  - Given invalid inputs: strings when numbers are expected, out of bounds inputs, same input twice.
  - Tested in my local terminal and the Code Institute Heroku terminal.

  Full test table:

  | Feature | Expected Outcome | Testing Performed | Result | Pass / Fail |
  | --- | --- | --- | --- | --- |
  | Enter Name and Begin | When program first starts, I am asked to provide my name. Once I have given my name the game welcomes me with my name, prints the game board and starts the game. | Run program and enter name. | Program welcomes me by my name, prints the game board and starts the game. | Pass |
  | Select First Grid Position | Select a grid position between 1 and 9. Once selected an 'x' should appear in the selected position. Computer will then automatically position a '0' in a random grid position. | Selected a number between 1 and 9. | An 'x' appears in the grid position I selected and the computer randomly positioned a '0' on the grid. | Pass |
  | Must Select a Grid Position Between 1 and 9. | Player must select a number between 1 and 9. If not an error message will be displayed and player asked to try again. | In turn selected 0 and numerous numbers over the value of 9. | Each time wrong value selected an error message appeared, reminded the user to select a number between 1 and 9 and asked to try again. | Pass |
  | Must Select an Unused Grid Position | When trying to select a grid position that has already been taken up by an 'x' or a '0', a message will appear explaining to the user that that grid position has already been take and please select another number between 1 and 9. | Selected gid positions that were already taken. | Message appeared telling me that that grid position has already been taken and to select another number between 1 and 9. | Pass |
  | Value Entered must be a Whole Integer and Not a String | When trying to select a grid position with a string or a decimal number, an error message will appear and ask the user to try again. | Entered a string as a value and then again as a decimal number. | Error message appears and asks the user to try again. | Pass |
  | When Connected Three 'x' in a row, column or diagonally the player wins and congratulations message appears. | Played the game several times, each time connecting Three 'x' in a row, column and diagonally. Each time this ends the game telling the user that they have won. | Played the game and in turn connected three 'x' in a row, column and diagonally. | The game stops and displays a message saying that the player has won the game. | Pass |
  | When Connected Three '0' in a row, column or diagonally | When three '0' are connected in a row, column or diagonally, the game is stopped and a message appears stating that the computer has won. | Played the game several times for the computer to connect three '0' in a row, column and diagonally. | The game is stopped and a message appears to inform the player that the computer has won. | Pass |
  | Check for Tie | When there are no more grid positions left to choose from and neither player has connected 'x' or '0' in a row, column or diagonally the game will be stopped and a message appear stating the game has finished in a tie. | Played game several times making sure no player connected three in a row, column or diagonally. | The game is stopped and message appears stating the game has finished in a tie. | Pass |
  |Option to Play Again | When the game has finished, whether it's finished with a player win, computer win or a tie. The player is asked whether or not they would like to play again. If the user types in 'yes' in lowercase or uppercase the game restarts. | Typed in 'yes' to play again, in uppercase, lowercase and random letters in capital. | The game restarted. | Pass |
  | Not to Play Again | When asked if I would like to play again, if I type in 'no' then the program will have stopped. A message will appear saying thanks for playing. | Typed in 'no' in uppercase, lowercase and random letters in capitals. | A message appeared saying thanks for playing, then the program finished and would need to select run program again to start again. | Pass |
  | Need to type 'yes' or 'no' when asked to play again | When asked to play again, if I type in anything other than 'yes' or 'no' an error message will appear saying invalid input and the game will keep looping this until a 'yes' or 'no' is typed. | In turn typed in random letters and words, then 'yes' and then ' no. | When random letters and words typed in, error message is show and asked to type in 'yes' or 'no'. This repeats until 'yes' or 'no' is typed in. | Pass | 
  | Quit Game | When player asked to select a number between 1 and 9 or to type in 'quit' to leave game, when the player types in 'quit', the game stops and the player is asked if they would like to play again. | Typed in 'quit' in uppercase, lowercase and random letters in capital. | The game stopped running and I was asked if I would like to play again. | Pass |
