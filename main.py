import numpy as np


def load_maze(path):
    with open(path) as f:
        first_line = f.readline()
        # print(first_line)

        rows, cols = first_line.strip().split(",")
        rows, cols = int(rows), int(cols)
        print(f"Reading a maze of {rows} x {cols}")

def main():
    maze_path = "test_mazes/simple_maze.txt"
    load_maze(maze_path)
    maze = np.zeros((64,64))
    # print(maze)

if __name__=="__main__":
    main()


