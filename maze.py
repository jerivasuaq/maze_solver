import numpy as np
import random

def load_maze(path):
    with open(path) as f:
        first_line = f.readline()
        # print(first_line)

        rows, cols = first_line.strip().split(",")
        rows, cols = int(rows), int(cols)
        maze = np.zeros((rows,cols), dtype=str)
        print(f"Reading a maze of {rows} x {cols}")

        for row in range(rows):
            line = f.readline()
            for col in range(cols):
                maze[row,col] = line[col]

    return maze

def findOG(maze):
    origin = None
    goal = None

    rows, cols = maze.shape
    for row in range(rows):
        for col in range(cols):
            if maze[row, col] == 'x':
                origin = (row, col)
            elif maze[row, col] == 'F':
                goal = (row, col)

            if origin is not None and goal is not None:
                break
        if origin is not None and goal is not None:
            break

    return origin, goal

def solve_maze_dfs(maze):
    def dfs(current, path):
        if current == goal:
            return path
        visited.add(current)

        for move in moves:
            next_pos = (current[0] + move[0], current[1] + move[1])
            if (
                0 <= next_pos[0] < rows
                and 0 <= next_pos[1] < cols
                and maze[next_pos[0], next_pos[1]] != '#'
                and next_pos not in visited
            ):
                new_path = dfs(next_pos, path + [next_pos])
                if new_path is not None:
                    return new_path
        return None

    rows, cols = maze.shape
    start, goal = findOG(maze)
    moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # right, left, down, up
    visited = set()
    return dfs(start, [start])

def generate_maze(rows, cols, path_ratio=0.6):
    # Create an empty maze filled with walls ('#')
    maze = np.full((rows, cols), '#', dtype=str)

    # Randomly decide on the starting and finishing points
    start = (random.randint(0, rows - 1), random.randint(0, cols - 1))
    finish = (random.randint(0, rows - 1), random.randint(0, cols - 1))
    maze[start[0], start[1]] = 'x'
    maze[finish[0], finish[1]] = 'F'

    # Determine the number of paths based on the path ratio
    path_cells = int(rows * cols * path_ratio)

    # Random walk to create paths
    r, c = start
    for _ in range(path_cells):
        maze[r, c] = ' '
        # Choose a random direction to move
        move = random.choice([(0, 1), (1, 0), (0, -1), (-1, 0)])
        r = max(0, min(rows - 1, r + move[0]))
        c = max(0, min(cols - 1, c + move[1]))

    return maze, start, finish

def save_maze_to_file(maze, file_path):
    with open(file_path, 'w') as file:
        rows, cols = maze.shape
        file.write(f"{rows},{cols}\n")  # Save dimensions
        for row in range(rows):
            file.write(''.join(maze[row, :]) + '\n')


