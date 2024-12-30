from helpers.problems import EightQueenProblem
import random


def hill_climbing(eight_queens_problem: EightQueenProblem):
    """
    Task: Implement hill climbing search for the eight queens problem.

    return True if the algorithm finds a global optimum
    return False if the algorithm reaches a plateau
    """
    pass


def find_any_solution():
    """
    The hill climbing algorithm gets stuck at a local optimum in many scenarios.
    Find a solution by randomly recreating the eight queen problem with a
    different seeds in its constructor (e.g. EightQueenProblem(seed=42)) until
    a solution is found. Finally return the solved problem.

    Returns:
        EightQueenProblem: The solved problem.
    """
    pass


def get_conflict_vector(problem: EightQueenProblem, queen: int) -> list[int]:
    """ Returns the conflict vector for a given queen. The conflict vector
    is a list of length 8, where each entry represents the number of
    conflicts for the given queen if it were to be moved to the
    corresponding position.

    Args:
        problem (EightQueenProblem): The problem to get the conflict vector for.
        queen (int): The queen to get the conflict vector for.

    Returns:
        list[int]: The conflict vector for the given queen.
    """
    pass


def get_all_conflicts(problem: EightQueenProblem) -> int:
    """
    Get the number off all conflicts on the board.

    Retruns:
        int: The number of all conflicts on the board.
    """
    pass


def get_conflicts(problem: EightQueenProblem, queen: int) -> int:
    """
    Returns the number of conflicts for the given queen.

    Args:
        problem (EightQueenProblem): The problem to get the conflicts for.
        queen (int): The queen to check for conflicts.

    Returns:
        int: The number of conflicts for the given queen.
    """
    pass


def get_student_credentials():
    """Change this to your student credentials"""
    student_name = "Your name"
    return student_name


def main():
    if get_student_credentials() == "Your name":
        print("Please set your name in get_student_credentials()!")
        return

    problem = EightQueenProblem()
    print("Running task part A\n")
    print("Initial board state:")
    print(problem)
    print()

    result = hill_climbing(problem)
    if result:
        print("Found global optimum!")
    else:
        print("Reached plateau!")

    print("Final board state:")
    print(problem)

    print("\n ---------------- \n")

    print("Running task part B\n")
    solved_problem = find_any_solution()
    print(f"Final board state: \n{solved_problem}")


if __name__ == "__main__":
    main()
