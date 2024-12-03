#!/usr/bin/python3
"""
This module defines the island_perimeter function.
"""


def island_perimeter(grid):
    """
    Calculate the perimeter of the island described in the grid.
    Args:
        grid (list of list of ints): The grid representing the map.
            0 represents water and 1 represents land.
    Returns:
        int: The perimeter of the island.
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                # Check each side of the cell
                if r == 0 or grid[r - 1][c] == 0:
                    perimeter += 1  # top
                if r == rows - 1 or grid[r + 1][c] == 0:
                    perimeter += 1  # bottom
                if c == 0 or grid[r][c - 1] == 0:
                    perimeter += 1  # left
                if c == cols - 1 or grid[r][c + 1] == 0:
                    perimeter += 1  # right

    return perimeter
