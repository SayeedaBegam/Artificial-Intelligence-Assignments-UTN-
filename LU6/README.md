# Tic-Tac-Toe Game: MiniMax Algorithm Implementation

In this assignment, you will complete the implementation of a **Tic-Tac-Toe game** using the **MiniMax search algorithm** in Python. The game will feature two computer players: a **minimizing player** (`'o'`) and a **maximizing player** (`'x'`). The game will proceed turn by turn until it ends with a winner (a player wins across a row, column, or diagonal) or results in a tie (no spaces left on the board and no winner).

---

## MiniMax Algorithm Overview

Following the **MiniMax algorithm**:

1. Each player will analyze the game state, evaluate all possible moves, and select the **optimal action**:
   - The **maximizing player** (`'x'`) selects the move that maximizes their score or leads to their win.
   - The **minimizing player** (`'o'`) selects the move that minimizes the maximizing player’s score.

2. The **MiniMax function** will:
   - Recursively evaluate the utility of the game state at each level of recursion.
   - Use the utility values from deeper levels to decide the best move when the recursion unwinds.
   - Return the **best value** of the optimal move for the current player (either maximizing or minimizing).

---

## Task Instructions

1. **Download the Code Framework**  
   Download the code framework: [unit6_tasks.zip](#). The zip file contains:
   - Function stubs for implementing the MiniMax algorithm.
   - Predefined game setup and utility functions.

2. **MiniMax Implementation**  
   Complete the implementation of the `minimax()` function. This function will:
   - Be called recursively until a **terminal condition** (win or draw) is met.
   - Evaluate the utility of the current game state at each level/depth of recursion.
   - Use the utility values to select the **optimal action**:
     - **Maximizing player** aims to maximize the utility.
     - **Minimizing player** aims to minimize the utility.
   - Return the value of the **best move** (`best`) for the player at the initial function call.

3. **Depth Consideration**  
   Incorporate the **depth value** into your utility function so that:
   - The optimal action is chosen with the **least number of turns**.
   - This ensures that shorter wins are preferred, and longer losses are avoided.

---

## Expected Functionality

When the final script is run:
1. A **Tic-Tac-Toe game** will be played with:
   - An **initial game board**.
   - Two computer players (`'x'` and `'o'`).
2. The players will take turns, one after the other, until:
   - A winner is determined.
   - Or the game ends in a tie.

---
