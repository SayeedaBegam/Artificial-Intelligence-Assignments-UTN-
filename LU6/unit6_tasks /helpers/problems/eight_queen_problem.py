import random


class EightQueenProblem:
    def __init__(
            self, board_config: list[int] = None, seed: int = 42,
            print_conflicts: bool = False):
        """
        Initializes the EightQueenProblem. If no board_config is given,
        a random board is generated.

        Args:
            board_config (list[int], optional): A list of the queen positions
                with board_config[x] = y. The COS is placed at the bottom left
                corner of the chess board. Defaults to None.
            seed (int, optional): The seed to use for the random number
                generator. Defaults to 42.
            print_conflicts (bool, optional): If true, the number of conflicts
                is added for each field when calling the __str__ method.

        Raises:
            ValueError: The board_config must be a list of length 8.
        """
        # set seed
        random.seed(seed)

        # create the chess board
        field_size = 8  # to create an 8x8 chess board
        if board_config is not None:
            if not len(board_config) == field_size:
                raise ValueError("Board must be a list of length 8")

            self.board_config = board_config

        else:
            # generate a random board
            self.board_config = [random.randint(0, field_size - 1)
                                 for _ in range(field_size)]

        self.print_conflicts = print_conflicts

    def __str__(self):
        """
        Returns a string representation of the board.

        Returns:
            str: The string representation of the board.
        """
        board = ""
        for row in range(len(self.board_config)):
            for column in range(len(self.board_config)):
                if self.board_config[column] == row:
                    board += "q "
                else:
                    if self.print_conflicts:
                        # get conflict vector for this queen
                        conflict_vector = self.get_conflict_vector(column)

                        # get the number of conflicts for this position
                        conflicts = conflict_vector[row]
                        board += f"{conflicts} "
                    else:
                        board += ". "
            board += "\n"

        return board

    def move_queen(self, queen: int, new_position: int):
        """
        Moves the given queen to the new position.

        Args:
            queen (int): The queen to move.
            new_position (int): The new position of the queen.
        """
        self.board_config[queen] = new_position

    def get_queen_position(self, queen: int):
        """
        Returns the position of the given queen.

        Args:
            queen (int): The queen to get the position for.

        Returns:
            int: The position of the given queen.
        """
        return self.board_config[queen]


if __name__ == "__main__":
    board = EightQueenProblem()
    print(board)
