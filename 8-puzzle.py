from collections import deque

class Puzzle:
    def __init__(self, initial_state, goal_state):
        self.state = initial_state  # Ensure this is a 2D list (matrix)
        self.goal_state = goal_state
        self.moves = 0
        self.priority = self.get_priority()

    def manhattan_distance(self):
        distance = 0
        # Iterate through each tile in the 3x3 puzzle
        for i in range(3):
            for j in range(3):
                val = self.state[i][j]
                if val != 0:  # Skip the empty space
                    goal_x, goal_y = divmod(self.goal_state[val - 1], 3)
                    distance += abs(i - goal_x) + abs(j - goal_y)
        return distance

    def get_priority(self):
        return self.moves + self.manhattan_distance()

    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.state])

def solve_puzzle(initial_state, goal_state):
    # Create an initial Puzzle object
    puzzle = Puzzle(initial_state, goal_state)
    print("Initial Puzzle State:")
    print(puzzle)
    print("\nGoal State:")
    print('\n'.join([' '.join(map(str, row)) for row in goal_state]))

    # Logic for solving the puzzle (e.g., using A* or BFS) could go here
    # For now, simply returning the puzzle instance
    return puzzle

# Example of initial state and goal state (3x3 grid)
initial_state = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]  # 0 represents the empty space
]

goal_state = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]  # Goal state: 1-8 arranged in order
]

# Solve the puzzle
puzzle = solve_puzzle(initial_state, goal_state)
