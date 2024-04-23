from maze import load_maze, findOO


def main():
    maze_path = "test_mazes/simple_maze.txt"
    maze = load_maze(maze_path)
    origin, goal = findOO(maze)
    print(maze)
    print(origin, goal)

if __name__=="__main__":
    main()


