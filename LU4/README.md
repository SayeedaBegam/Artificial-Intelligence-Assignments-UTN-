# A* Algorithm with Different Heuristics

In this assignment, you will explore **A*** search in a grid world while experimenting with **different heuristic functions**. The goal is to observe how the choice of heuristic affects both the path found and the way nodes are expanded during the search.

---

## Overview

1. **Setup**  
   - Use the provided [online implementation of A*](https://www.redblobgames.com/pathfinding/a-star/introduction.html) (or a similar interface) to configure:
     - **Start** and **Goal** positions
     - **Obstacles** (walls) within the grid
   - Run the A* algorithm with different heuristic options (Manhattan distance, Euclidean distance, Diagonal distance, etc.).

2. **Observation**  
   - Watch how the blue cells (expanded nodes) and green cells (frontier) evolve during the search.  
   - Notice that in **Manhattan distance** vs. **Euclidean distance**, the shape of the expanded region differs significantly.

---

## Heuristics in A*

1. **Manhattan Distance** (\(d_{Manhattan}\))  
   \[
   d_{\text{Manhattan}}(x_1, y_1, x_2, y_2) = |x_1 - x_2| + |y_1 - y_2|
   \]
   - **Advantages**:
     - **Admissible** when only four-directional movement (up, down, left, right) is allowed.
     - Easy to calculate and often leads to fewer expanded nodes in typical grid settings without diagonal moves.
   - **Disadvantages**:
     - **Not perfectly accurate** when diagonal movements are allowed, because diagonal shortcuts are underestimated.
     - May result in expansions that look “square” and can lead to longer search times if diagonal routes are actually available.

2. **Euclidean Distance** (\(d_{Euclidean}\))  
   \[
   d_{\text{Euclidean}}(x_1, y_1, x_2, y_2) = \sqrt{(x_1 - x_2)^2 + (y_1 - y_2)^2}
   \]
   - **Advantages**:
     - More realistic if diagonal and straight-line movements are possible, giving a more direct estimate of actual distance “as the crow flies.”
     - **Admissible** for diagonal or any-direction movement in a continuous or 8-connected grid world.
   - **Disadvantages**:
     - Can **overestimate** distance if you only allow non-diagonal movement (thus breaking admissibility).
     - Computing square roots at each step is slightly more computationally expensive (though this is usually negligible).

3. **Diagonal Distance** (sometimes called Chebyshev Distance)  
   \[
   d_{\text{Diagonal}}(x_1, y_1, x_2, y_2) = \max(|x_1 - x_2|, |y_1 - y_2|)
   \]
   - **Advantages**:
     - **Admissible** in an 8-connected grid, as it precisely matches the fewest diagonal and straight moves needed.
     - Simple to compute, just a max of absolute differences.
   - **Disadvantages**:
     - Not suitable for 4-direction grids where diagonal movement is disallowed (would not be admissible in that context).

---

## Experiment Instructions

1. **Set up the Grid**  
   - Place the **Start** and **Goal** in corners or arbitrary positions.
   - Add **Walls** to create obstacles and more interesting paths.
   - Enable diagonal movement in the interface if you wish to compare it with 4-directional movement.

2. **Run A\***  
   - Select **Manhattan Distance** as your heuristic. Observe the expanded region (blue) and the frontier (green) cells.
   - Repeat using **Euclidean Distance**. Compare the shape and number of expanded cells.
   - Optionally test the **Diagonal Distance** (if the interface supports it).

3. **Record Observations**  
   - Take note of how many nodes get expanded.
   - Observe the final path and its length.
   - Compare the results for each heuristic, focusing on:
     - Path optimality (is the path as short as possible?).
     - Search efficiency (how quickly or broadly the search space was expanded).

---

## Analysis

Below are key points to consider in your final write-up or discussion:

1. **Effect on Search Efficiency**  
   - Which heuristic led to fewer expansions and faster completion?
   - Did a certain heuristic cause A* to explore a more “circular” area around the start (Euclidean) versus a more “square” area (Manhattan)?

2. **Accuracy and Admissibility**  
   - Was the heuristic still **admissible** given the movement rules?
   - Did you notice any path that deviated from the truly optimal path because the heuristic was non-admissible?

3. **Trade-offs**  
   - **Manhattan** vs. **Euclidean**: When is one clearly superior?
   - How does **Diagonal Distance** compare if diagonal movement is allowed?
