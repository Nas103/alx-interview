#!/usr/bin/python3


from collections import deque

def canUnlockAll(boxes):
    """
    Determines whether all lockboxes in a given list can be unlocked.

    Args:
        boxes: A list of lists, where each inner list represents the keys in a lockbox.

    Returns:
        True if all lockboxes can be unlocked, False otherwise.
    """

    n = len(boxes)
    unlocked = [False] * n
    unlocked[0] = True  # The first box is always unlocked

    queue = deque([0])  # Queue to store unlocked boxes

    while queue:
        current_box = queue.popleft()

        for key in boxes[current_box]:
            if 0 <= key < n and not unlocked[key]:
                unlocked[key] = True
                queue.append(key)

    return all(unlocked)
