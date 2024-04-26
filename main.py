from maze import load_maze, findOG, solve_maze_dfs


def main():

    #maze_path = "test_mazes/simple_maze.txt"
    maze = load_maze(maze_path)
    origin, goal = findOG(maze)
    path = solve_maze_dfs(maze)
    print(maze)
    print(path)

if __name__=="__main__":
    main()


