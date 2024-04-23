import numpy as np


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

def findOO(maze):
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


def main():
    maze_path = "test_mazes/simple_maze.txt"
    maze = load_maze(maze_path)
    origin, goal = findOO(maze)
    print(maze)
    print(origin, goal)

if __name__=="__main__":
    main()


