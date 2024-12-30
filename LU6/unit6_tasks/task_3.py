import math
from typing import Tuple
from helpers.problems.tictactoe_problem import ticTacBoard


def minimax(game: ticTacBoard, depth: int, isMax: bool) -> int:
    """
    Task: Implement the minimax function for tic-tac-toe using recursion

    Consider the best move for every turn in the game, until a draw is reached
    or a player wins. Recursively return the reward value of the best move to
    the original function call in findBestMove()

    Hint: Subtract depth from the end game score.
    The more turns the lower the score, the fewer turns the higher the score
    """
    # Evaluating the board game and return if the game is over.
    state = game.evaluate()
    if state == 'x':
        return 10 - depth  # Maximizing player wins, prefer fewer moves gives higher score
    elif state == 'o':
        return depth - 10  # Minimizing player wins, prefer more moves gives lower score
    elif state == 'draw' or state == 'game over':
        return 0  # It's a draw

    if isMax:  # Maximizing player's turn ('x')
        best = -math.inf
        # Trying all possible moves in the game
        for i in range(3):
            for j in range(3):
                if game.board[i][j] == "_":
                    game.board[i][j] = game.player  # Make the move for 'x'
                    best = max(best, minimax(game, depth + 1, False))  # Recursively calling minimax function
                    game.board[i][j] = "_"  # Undo the move
        return best
    else:  # Minimizing player's turn ('o')
        best = math.inf
        # Trying all possible moves
        for i in range(3):
            for j in range(3):
                if game.board[i][j] == "_":
                    game.board[i][j] = game.opponent  # Make the move for 'o'
                    best = min(best, minimax(game, depth + 1, True))  # Recursively calling minimax function
                    game.board[i][j] = "_"  # Undo the move
        return best


def findBestMove(
    game: ticTacBoard, depth: int, player_mark: str
) -> Tuple[Tuple[int, int], int]:
    """
    Wrapper function around the recursive function minimax()
    Iterates through each available space on the board to move
    Evaluates the reward value for this move, considering the number of turns
    (depth)

    Args:
        game (ticTacBoard): The current state of the game board
        depth (int): initially 0, the number of turns or recursions until the
            end of the game
        player_mark (str): game.player ('x') or game.player ('o')

    Returns:
        Tuple[int, int]: row and column coordinates of the best move
        int: Reward value of the best move
    """
    if player_mark == game.player:
        bestVal = -math.inf
        bestMove = (-1, -1)

        # traverse all cells, evaluate minimax function for
        # all empty cells. And return the cell with optimal
        # value.
        for i in range(3):
            for j in range(3):
                # Check if cell is empty
                if game.board[i][j] == "_":
                    # make the move
                    game.board[i][j] = player_mark

                    # compute evaluation function for this move.
                    moveVal = minimax(game, depth, isMax=False)

                    # undo the move
                    game.board[i][j] = "_"

                    # If the value of the current move is more than the best
                    # value, then update best/
                    if moveVal > bestVal:
                        bestMove = (i, j)
                        bestVal = moveVal
    elif player_mark == game.opponent:
        bestVal = math.inf
        bestMove = (-1, -1)

        # traverse all cells, evaluate minimax function for
        # all empty cells. And return the cell with optimal
        # value.
        for i in range(3):
            for j in range(3):
                # Check if cell is empty
                if game.board[i][j] == "_":
                    # make the move
                    game.board[i][j] = player_mark

                    # compute evaluation function for this move.
                    moveVal = minimax(game, depth, isMax=True)

                    # undo the move
                    game.board[i][j] = "_"

                    # If the value of the current move is more than the best
                    # value, then update best/
                    if moveVal < bestVal:
                        bestMove = (i, j)
                        bestVal = moveVal

    game.make_move(bestMove, player_mark)
    return bestMove, bestVal


def max_take_turn(game: ticTacBoard) -> Tuple[Tuple[int, int], int]:
    """
    Finds the best move for the maximizing player ('x'), and updates/prints
    the game board.

    Args:
        game (ticTacBoard): The current state of the game board

    Returns:
        Tuple[int, int]: row and column coordinates of the best move
        int: Reward value of the best move
    """
    bestMove, bestVal = findBestMove(game, 0, game.player)
    print("Player moved to row:", bestMove[0], " col:", bestMove[1])
    print("The value of the best move is :", bestVal)
    game.print_board()
    return bestMove, bestVal


def min_take_turn(game: ticTacBoard) -> Tuple[Tuple[int, int], int]:
    """
    Finds the best move for the minimizing opponent ('o'), and updates/prints
    the game board.

    Args:
        game (ticTacBoard): The current state of the game board

    Returns:
        Tuple[int, int]: row and column coordinates of the best move
        int: Reward value of the best move
    """
    bestMove, bestVal = findBestMove(game, 0, game.opponent)
    print("Opponent moved to row:", bestMove[0], " col:", bestMove[1])
    print("The value of the best move is :", bestVal)
    game.print_board()
    return bestMove, bestVal


def play_game(game: ticTacBoard):
    while game.are_moves_left():
        # maximizing player 'x' takes a turn
        _, _ = max_take_turn(game)
        # decide to continue playing or end game
        state = game.evaluate()
        if state == "draw" or state == "game over":
            print(game.winner, " wins!") if game.winner != "" else print(
                "game ended in a draw"
            )
            break

        # minimizing opponent 'o' takes a turn
        _, _ = min_take_turn(game)
        # decide to continue playing or end game
        state = game.evaluate()
        if state == "draw" or state == "game over":
            print(game.winner, " wins!") if game.winner != "" else print(
                "game ended in a draw"
            )
            break


def get_student_credentials():
    """Change this to your student credentials"""
    student_name = "Sayeeda Begam Mohamed Ikbal"
    return student_name


def main():
    if get_student_credentials() == "Your name":
        print("Please set your name in get_student_credentials()!")
        return

        # driver function
    game = ticTacBoard([["_", "_", "o"], ["_", "x", "_"], ["_", "_", "_"]])

    play_game(game)


if __name__ == "__main__":
    main()
