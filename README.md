# ENSAE Programming Project 2024: Sliding Tile Solver

## Description
The Sliding Tile Solver is a Python-based project that solves the classic sliding tile puzzle problem. The goal is to find the shortest sequence of moves required to reorder the tiles in ascending order, following specific movement rules.

This project was developed as part of the programming course for first-year students at ENSAE Paris, supervised by [Patrick Loiseau](mailto:patrick.loiseau@inria.fr).

## Main Features
- **Random or custom grid generation**.
- **Optimized solving algorithms**, including:
  - BFS (Breadth-First Search) to guarantee optimal solutions.
  - A* to speed up the search process using a suitable heuristic.
- **Step-by-step visualization** of the solution process via command-line output.
- **Complete unit tests** to validate every component of the project.
- Detailed documentation of algorithmic choices and results.

## Project Structure
Here is the structure of this repository:

```
ensae-prog24/
│
├── main.py # Main execution script
├── grid.py # Grid and move management
├── solver.py # Solving algorithm implementations
├── tests/ # Unit tests
│ ├── test_grid.py # Tests for grid management
│ ├── test_solver.py # Tests for solving algorithms
└── README.md # Project documentation
```

