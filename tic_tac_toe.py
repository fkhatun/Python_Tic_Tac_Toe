# Two-player Tic-Tac-Toe game
# This game runs in the PyCharm terminal.

# Global counters for game statistics
games_played = 0
x_wins = 0
o_wins = 0
draws = 0
invalid_inputs = 0


# Create a new game board
def create_board():
    """Create a new board containing positions 1 to 9."""
    return ["1", "2", "3", "4", "5", "6", "7", "8", "9"]


def display_board(board):
    # Display the current Tic-Tac-Toe board.
    print()
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print()


def display_instructions():
    # Instructions of the game
    print("\nWelcome to Tic-Tac-Toe!")
    print("This is a two-player game.")
    print("Player X starts first.")
    print("Choose a number from 1 to 9 to place your mark.")
    print("The first player to get three marks in a row wins.")


def get_player_move(board, player):
    # Ask the current player to choose a position on the board.
    global invalid_inputs

    while True:  # Get the player's input and remove any extra spaces.
        user_input = input(
            f"Player {player}, choose a position from 1 to 9: "
        ).strip()

        # Make sure the player entered a number.
        if not user_input.isdigit():
            invalid_inputs += 1
            print("Invalid input. Please enter a number.")
            continue

        # Change the input from a string into an integer.
        position = int(user_input)

        # Check that the number is between 1 and 9.
        if position < 1 or position > 9:
            invalid_inputs += 1
            print("Please choose a number between 1 and 9.")
            continue

        # Convert the player's choice into a list index.
        board_index = position - 1

        # Check if the chosen square has already been used.
        if board[board_index] in ["X", "O"]:
            invalid_inputs += 1
            print("That square is already occupied.")
            continue

        # Return the valid position to the game.
        return board_index


def check_winner(board, player):
    # Check whether the player has won.
    winning_combinations = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ]

    # Check each possible winning combination
    for combination in winning_combinations:
        first = combination[0]    # First position
        second = combination[1]   # Second position
        third = combination[2]    # Third position

        if (
            board[first] == player      # Check the first square
            and board[second] == player  # Check the second square
            and board[third] == player  # Check the third square
        ):
            return True  # The player has won

    return False  # No winning combination was found


def board_is_full(board):
    # Check if all spaces on the board have been used.
    for square in board:  # Go through each square on the board.
        if square not in ["X", "O"]:  # If a square still has a number...
            return False  # ...the board is not full.

    return True  # Every square contains X or O.


def update_statistics(result):
    # Update the game statistics after each game.
    global games_played
    global x_wins
    global o_wins
    global draws

    games_played += 1  # Increase the total games played by one.

    if result == "X":
        x_wins += 1
    elif result == "O":
        o_wins += 1
    else:
        draws += 1


def display_statistics():
    # Display statistics from all completed games.
    print("\nGame Statistics")
    print("-----------------------")
    print(f"Games played: {games_played}")
    print(f"Player X wins: {x_wins}")
    print(f"Player O wins: {o_wins}")
    print(f"Draws: {draws}")
    print(f"Invalid inputs: {invalid_inputs}")


def ask_to_play_again():
    # Ask the players if they want to play another game.
    global invalid_inputs  # Count any invalid answers.

    while True:  # Keep asking until a valid answer is entered.
        answer = input(
            "\nWould you like to play again? Enter yes or no: "
        ).strip().lower()  # Remove spaces and convert to lowercase.

        if answer in ["yes", "y"]:  # Start another game.
            return True

        if answer in ["no", "n"]:  # End the program.
            return False

        invalid_inputs += 1  # Count the invalid answer.
        print("Invalid answer. Please enter yes or no.")


def play_game():
    # Start one game of Tic-Tac-Toe.
    board = create_board()  # Create a new empty board.
    current_player = "X"    # Player X always starts first.

    display_instructions()  # Show the game instructions.
    display_board(board)    # Display the empty board.

    while True:  # Keep the game running until someone wins or, it's a draw.
        selected_position = get_player_move(board, current_player)  # Get the player's move.

        # Place the current player's mark on the board.
        board[selected_position] = current_player

        display_board(board)  # Show the updated board.

        # Check if the current player has won.
        if check_winner(board, current_player):
            print(f"Player {current_player} wins!")
            update_statistics(current_player)  # Update the game statistics.
            break  # End the current game.

        # Check if all spaces have been used.
        if board_is_full(board):
            print("The game is a draw!")
            update_statistics("Draw")  # Record the draw.
            break  # End the current game.

        # Change to the other player's turn.
        if current_player == "X":
            current_player = "O"
        else:
            current_player = "X"


def main():
    # Start the main program.
    print("====================")
    print("    TIC-TAC-TOE")
    print("====================")

    keep_playing = True  # Controls whether another game will be played.

    while keep_playing:  # Keep running until the players choose to stop.
        play_game()  # Start a new game.
        display_statistics()  # Show the updated statistics.
        keep_playing = ask_to_play_again()  # Ask if the players want another game.

    print("\nFinal Statistics")
    display_statistics()  # Display the final game statistics.
    print("\nThank you for playing!")  # Goodbye message.


# Start the program
if __name__ == "__main__":
    main()