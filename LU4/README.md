# Hill Climbing for the 8-Queens Problem

This assignment involves solving the classic **8-Queens** puzzle by implementing the **hill climbing** algorithm. The goal is to place eight queens on a chessboard so that no two queens can attack each other. A valid solution requires exactly one queen per column, which simplifies the representation of states.

---

## Overview

1. **State Representation**  
   A state \( s \) is represented as a list \([p_1, p_2, \ldots, p_8]\), where \( p_i \in \{1, \ldots, 8\} \) denotes the **row** of the queen in column \( i \).

2. **Actions**  
   An action changes the position of one queen within its column (i.e., changing \( p_i \) to a different row value).

3. **Value Function**  
   The value function \( v(s) \) is defined as the **number of conflicts** in state \( s \):
   \[
   v(s) = \sum_{i=1}^{8} v(p_i),
   \]
   where \( v(p_i) \) is the number of **attacking queens** sharing the same row or the same diagonals as the queen in column \( i \).  
   - Lower \( v(s) \) means fewer conflicts, so **the objective is to minimize \( v(s) \)**.

---

## Tasks

1. **Conflict-Detection Functions**  
   - **`get_conflicts(problem, queen)`**: Calculate how many queens conflict with the given `queen`.  
   - **`get_all_conflicts(problem)`**: Returns the total number of conflicts in the current state.  
   - **`get_conflict_vector(problem, queen)`**: Returns the row conflict counts for each possible new row position of `queen`.

2. **Basic Hill Climbing**  
   - Implement a **hill climbing** algorithm that moves one queen at a time to a position in the same column that reduces the overall number of conflicts.
   - Test this solution using the provided test cases. It should solve simpler initial states but may get stuck in local minima.

3. **Recovery Strategy**  
   - When the algorithm detects a **local minimum** (i.e., no better neighbor state is found), **re-initialize** the board (choose a random initial state) and run hill climbing again.  
   - Repeat until a valid solution is found.

---

## How to Use

1. **Download** `unit4_tasks.zip`, which contains:
   - **Code framework** with function stubs.
   - **Test cases** to verify your implementation.
2. **Implement** the functions in **Python**:
   - `get_conflicts(problem, queen)`
   - `get_all_conflicts(problem)`
   - `get_conflict_vector(problem, queen)`
3. **Run** the basic hill climbing algorithm on the test cases.  
   - Verify that it solves the simpler test states.
4. **Add** the recovery strategy (random restarts) if the solver gets stuck in a local minimum.  
   - Confirm that, with multiple restarts, you can find a valid 8-Queens solution in most cases.

---
