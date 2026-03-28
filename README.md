# Pathfinding Visualizer

An interactive pathfinding visualizer built with Python and Pygame that demonstrates how classic algorithms explore a grid to find the shortest path.

## Features

* Visualizes multiple algorithms:

  * Breadth-First Search (BFS)
  * A* Search
  * Dijkstra’s Algorithm
* Interactive grid system:

  * Set start and end nodes
  * Draw walls (obstacles)
  * Add weighted nodes
* Real-time animation of algorithm execution
* Adjustable speed controls
* Random maze generation

## Controls

| Key / Action | Function                |
| ------------ | ----------------------- |
| Left Click   | Place start, end, walls |
| W + Click    | Place weighted node     |
| Right Click  | Remove node             |
| SPACE        | Run BFS                 |
| A            | Run A*                  |
| D            | Run Dijkstra            |
| C            | Clear grid              |
| M            | Generate random maze    |
| ↑ / ↓        | Adjust animation speed  |

## How It Works

* The grid is represented as a 2D array of nodes.
* Each node tracks its neighbors and state (wall, visited, path, etc.).
* Algorithms explore the grid differently:

  * **BFS** guarantees shortest path in unweighted grids
  * **Dijkstra** accounts for weighted nodes
  * **A*** uses a heuristic (Manhattan distance) for faster pathfinding

## Technologies Used

* Python
* Pygame

## Installation

1. Clone the repository:

   ```bash
   git clone <your-repo-link>
   cd pathfinding-visualizer
   ```

2. Install dependencies:

   ```bash
   pip install pygame
   ```

3. Run the project:

   ```bash
   python main.py
   ```

## Future Improvements

* Add UI buttons instead of key controls
* Display path length and execution time
* Toggle diagonal movement
* Add more algorithms (DFS, Greedy Best-First)
* Improve UI layout and styling

## Author

Developed as a personal project to explore algorithms, data structures, and visualization techniques.
