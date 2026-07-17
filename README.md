Tic-Tac-Toe Game

About the Project
For this project I created a two-player Tic-Tac-Toe game using Python. The game is played in the terminal, where each player takes turns choosing a position on the board. The program checks for a winner, a draw, and keeps track of game statistics.

Features
Two-player game
Displays the board after every move
Checks that player input is valid
Prevents players from choosing the same square twice
Detects a winner or a draw
Allows players to play more than one game

Keeps track of:
Total games played
Player X wins
Player O wins
Draws
Invalid inputs

How to Run the Game
Open the project in PyCharm.
Open the tic_tac_toe.py file.
Click the Run button.
Follow the instructions shown in the terminal.

How to Play
The board uses the numbers 1 to 9 as positions.

1 | 2 | 3
---------
4 | 5 | 6
---------
7 | 8 | 9

Player X goes first.
Enter the number of the square where you want to place your mark.
Players take turns until someone gets three in a row or the board is full.
If nobody wins, the game ends in a draw.
At the end of each game you can choose whether to play again.

Functions
To keep the code organised I used several functions, including:

create_board()
display_board()
get_player_move()
check_winner()
board_is_full()
update_statistics()
display_statistics()
ask_to_play_again()
play_game()
main()

Error Handling
The program checks for invalid input so it doesn't crash. For example, it checks if:
the player enters a letter instead of a number
the number is outside the range 1–9
a square has already been used
an invalid answer is entered when asked to play again

Files Included
tic_tac_toe.py - the Python game
README.md - information about the project
tic_tac_toe_flowchart.png - the game flowchart

Author:
Fateha Khatun

