import numpy as np
import pytest
from maze import findOO

def test_findOO_success():
    # Standard success case
    maze = np.array([
        ['.', '.', '.', '.'],
        ['.', 'x', '.', '.'],
        ['.', '.', '.', 'F'],
        ['.', '.', '.', '.']
    ])
    origin, goal = findOO(maze)
    assert origin == (1, 1)
    assert goal == (2, 3)

def test_findOO_no_origin_or_goal():
    # Case with no 'x' or 'F'
    maze = np.array([
        ['.', '.', '.', '.'],
        ['.', '.', '.', '.'],
        ['.', '.', '.', '.'],
        ['.', '.', '.', '.']
    ])
    origin, goal = findOO(maze)
    assert origin is None
    assert goal is None

def test_findOO_multiple_origins_goals():
    # Case with multiple 'x' and 'F' (should return the first occurrence of each)
    maze = np.array([
        ['x', '.', '.', 'F'],
        ['.', '.', 'F', '.'],
        ['x', '.', '.', '.'],
        ['.', 'F', '.', '.']
    ])
    origin, goal = findOO(maze)
    assert origin == (0, 0)
    assert goal == (0, 3)

def test_findOO_large_maze():
    # Large maze with 'x' and 'F' at opposite corners
    size = 100  # Defines the size of a large maze
    maze = np.full((size, size), '.', dtype=str)  # Fill maze with '.'
    maze[0, 0] = 'x'  # Place 'x' at top-left corner
    maze[size-1, size-1] = 'F'  # Place 'F' at bottom-right corner
    
    origin, goal = findOO(maze)
    assert origin == (0, 0)
    assert goal == (size-1, size-1)

# You can add more tests as you see necessary
