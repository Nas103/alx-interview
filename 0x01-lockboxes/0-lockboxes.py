#!/usr/bin/python3

def canUnlockAll(boxes):
    """
    canUnlockAll(boxes):
    Determines if you can unlock all boxes using the keys found inside each box.

    Parameters:
    - boxes: A list of lists. Each index represents a box and contains keys to other boxes.

    Returns:
    - True: If all boxes can be unlocked.
    - False: If there are one or more boxes that cannot be unlocked.
    """

    # 🚪 Step 1: Visualize the number of boxes in the hallway
    n = len(boxes)

    # 🔓 Step 2: Keep track of unlocked boxes. Initially, only Box 0 is unlocked.
    unlocked = [False] * n
    unlocked[0] = True  # Box 0 is always open

    # 🧰 Step 3: Use a stack to store boxes to explore, starting with Box 0
    stack = [0]

    # 🕵️‍♂️ Step 4: Start the search! (Simulating opening boxes)
    while stack:
        current_box = stack.pop()  # Peek inside the current box 🔑

        # 📦 Step 5: Inside this box, you'll find keys to other boxes...
        for key in boxes[current_box]:
            if key < n and not unlocked[key]:  # Only unlock boxes you haven’t unlocked yet
                unlocked[key] = True  # 🎉 You've unlocked a new box!
                stack.append(key)  # 📤 Add it to the stack for further exploration
                # 🗝️ Unlocking boxes is like a domino effect. One key leads to another!

    # 🧮 Step 6: When you've explored all possible boxes, check if ALL boxes are unlocked.
    # (i.e., if every box's status in `unlocked` is True)
    return all(unlocked)

"""
🎯 Fun Facts & Analogies:

- The "stack" we're using is like keeping a list of 'mystery boxes' you still need to open.
  Every time you open a box and find more keys inside, you toss them onto the stack (the
  stack grows). If no more boxes can be opened, the stack empties.

- The `unlocked` list acts like your 'progress tracker' 📝. It keeps tabs on which boxes
  you've successfully unlocked so far. Initially, all boxes are locked (False) except for
  the magical Box 0.

- Picture it like a treasure hunt 🏴‍☠️: You unlock one chest and keep discovering keys
  that lead to more treasure chests until you've (hopefully) unlocked all the chests.

"""
