#!/usr/bin/python3
"""
Module: lockboxes
This module contains a function that determines if all boxes in a list
can be unlocked.
"""

from collections import deque


def canUnlockAll(boxes):
    """
    Determines whether all lockboxes in a given list can be unlocked.

    Args:
        boxes (list of list): A list of lists, where each inner list represents
        the keys in a lockbox.

    Returns:
        bool: True if all lockboxes can be unlocked, False otherwise.
    """

    n = len(boxes)  # Number of lockboxes
    unlocked = [False] * n  # Track the status of each box (locked/unlocked)
    unlocked[0] = True  # The first box is always unlocked

    queue = deque([0])  # Queue to store unlocked boxes for BFS traversal

    while queue:
        current_box = queue.popleft()  # Take the next unlocked box

        # Iterate over the keys in the current box
        for key in boxes[current_box]:
            # Unlock the box corresponding to the key, if it's not already unlocked
            if 0 <= key < n and not unlocked[key]:
                unlocked[key] = True
                queue.append(key)  # Add the newly unlocked box to the queue

    # Check if all boxes have been unlocked
    return all(unlocked)
