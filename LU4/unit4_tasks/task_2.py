import random
from helpers.problems import EightQueenProblem

def get_state(problem: EightQueenProblem):
    """
    Retrieves the current state of the queens from the problem instance.
    """
    if hasattr(problem, 'board_config'):
        return problem.board_config
    else:
        raise AttributeError("Unable to find the state representation in EightQueenProblem.")

def get_conflicts(problem: EightQueenProblem, queen: int) -> int:
    """
    Returns the number of conflicts for the given queen.
    """
    state = get_state(problem)
    conflicts = 0
    queen_row = state[queen]
    for i in range(len(state)):
        if i != queen:
            other_row = state[i]
            # Check if any other queen is in the same row or on the same diagonal
            if other_row == queen_row or abs(other_row - queen_row) == abs(i - queen):
                conflicts += 1
    return conflicts

def get_all_conflicts(problem: EightQueenProblem) -> int:
    """
    Get the number of all conflicts on the board.
    """
    state = get_state(problem)
    total_conflicts = 0
    for queen in range(len(state)):
        total_conflicts += get_conflicts(problem, queen)
    # Each conflict is counted twice, so divide by 2
    return total_conflicts // 2

def get_conflict_vector(problem: EightQueenProblem, queen: int) -> list[int]:
    """
    Returns the conflict vector for a given queen. Each entry represents the number
    of conflicts if the queen were to be moved to the corresponding row.
    """
    state = get_state(problem)
    conflict_vector = []
    original_row = state[queen]  # Store the original position of the queen
    for row in range(8):  # Iterate through all rows in the column
        state[queen] = row  # Temporarily move queen to new row
        conflict_count = get_conflicts(problem, queen)
        conflict_vector.append(conflict_count)
    state[queen] = original_row  # Restore original position
    return conflict_vector

def hill_climbing(problem: EightQueenProblem, max_iterations: int = 100) -> bool:
    """
    Perform hill climbing to solve the 8-Queens problem.

    Args:
        problem (EightQueenProblem): The problem instance.
        max_iterations (int): The maximum number of iterations before a restart.

    Returns:
        bool: True if a solution is found, False otherwise.
    """
    for iteration in range(max_iterations):
        # Get the total number of conflicts
        conflicts = get_all_conflicts(problem)
        print(f"Iteration {iteration}: Current conflicts: {conflicts}")  # Debugging output

        # If no conflicts, solution is found
        if conflicts == 0:
            return True

        queen_to_move = None
        best_move_row = None
        min_conflicts = conflicts

        # Explore moves for each queen
        for queen in range(8):
            conflict_vector = get_conflict_vector(problem, queen)
            for row, conflict in enumerate(conflict_vector):
                # Identify the best move with the least conflicts
                if row != get_state(problem)[queen] and conflict < min_conflicts:
                    min_conflicts = conflict
                    queen_to_move = queen
                    best_move_row = row

        # If no better move is found, we're likely in a plateau, restart
        if min_conflicts >= conflicts:
            print("Plateau detected. Restarting...")
            return False

        # Move the selected queen to the best position
        print(f"Moving queen {queen_to_move} to row {best_move_row}.")  # Debugging output
        get_state(problem)[queen_to_move] = best_move_row

    print("Max iterations reached without finding a solution.")
    return False


def find_any_solution(max_restarts: int = 100) -> EightQueenProblem:
    """
    Use random restarts to find a solution.

    Args:
        max_restarts (int): Maximum number of random restarts allowed.

    Returns:
        EightQueenProblem: The solved problem.
    """
    for restart in range(max_restarts):
        print(f"Random Restart {restart + 1}:")
        problem = EightQueenProblem(seed=random.randint(0, 1000))

        if hill_climbing(problem):
            print(f"Solution found after {restart + 1} restart(s)!")
            return problem

    raise Exception("Failed to find a solution within the maximum number of restarts.")

def get_student_credentials():
    """
    Return the student credentials for submission.
    """
    student_name = "Sayeeda Begam Mohamed Ikbal"  # Replace with your name
    return student_name

def main():
    print("Starting Hill Climbing for 8-Queens Problem...\n")

    # Attempt to find a solution with random restarts
    solved_problem = find_any_solution()

    print("\nFinal solution:")
    print(solved_problem)

    if get_student_credentials() == "Your name":
        print("Please set your name in get_student_credentials()!")
        return

if __name__ == "__main__":
    main()