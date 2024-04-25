import numpy as np
import pytest
from maze import findOG, solve_maze_dfs


def test_findOG_success():
    # Standard success case
    maze = np.array([
        ['.', '.', '.', '.'],
        ['.', 'x', '.', '.'],
        ['.', '.', '.', 'F'],
        ['.', '.', '.', '.']
    ])
    origin, goal = findOG(maze)
    assert origin == (1, 1)
    assert goal == (2, 3)

def test_findOG_no_origin_or_goal():
    # Case with no 'x' or 'F'
    maze = np.array([
        ['.', '.', '.', '.'],
        ['.', '.', '.', '.'],
        ['.', '.', '.', '.'],
        ['.', '.', '.', '.']
    ])
    origin, goal = findOG(maze)
    assert origin is None
    assert goal is None

def test_findOG_multiple_origins_goals():
    # Case with multiple 'x' and 'F' (should return the first occurrence of each)
    maze = np.array([
        ['x', '.', '.', 'F'],
        ['.', '.', 'F', '.'],
        ['x', '.', '.', '.'],
        ['.', 'F', '.', '.']
    ])
    origin, goal = findOG(maze)
    assert origin == (0, 0)
    assert goal == (0, 3)

def test_findOG_large_maze():
    # Large maze with 'x' and 'F' at opposite corners
    size = 100  # Defines the size of a large maze
    maze = np.full((size, size), '.', dtype=str)  # Fill maze with '.'
    maze[0, 0] = 'x'  # Place 'x' at top-left corner
    maze[size-1, size-1] = 'F'  # Place 'F' at bottom-right corner
    
    origin, goal = findOG(maze)
    assert origin == (0, 0)
    assert goal == (size-1, size-1)

def test_solver():
    # Example usage:
    maze = np.array([
        ['#', '#', '#', '#', '#', '#', '#', '#'],
        ['#', 'x', ' ', ' ', '#', ' ', ' ', '#'],
        ['#', ' ', '#', ' ', ' ', '#', ' ', '#'],
        ['#', ' ', '#', ' ', '#', '#', ' ', '#'],
        ['#', ' ', ' ', ' ', ' ', ' ', 'F', '#'],
        ['#', '#', '#', '#', '#', '#', '#', '#']
    ], dtype=str)

    solution = solve_maze_dfs(maze)
    
    assert len(solution) > 1 

def test_solver_empty():
    # Example usage:
    maze = np.array([
        ['#']
    ], dtype=str)

    solution = solve_maze_dfs(maze)
    
    assert solution[0] == None

def test_solver_simple():
    # Example usage:
    maze = np.array([
        ['x', 'F']
    ], dtype=str)

    solution = solve_maze_dfs(maze)
    
    assert len(solution) > 1
    # You can add more tests as you see necessary
