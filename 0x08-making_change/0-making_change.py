#!/usr/bin/python3
"""
Module for solving the coin change problem.
"""


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given total amount.
    Args:
        coins (list): List of coin denominations.
        total (int): Target amount to reach using coins.
    Returns:
        int: Fewest number of coins needed to reach the total,
             or -1 if it's not possible.
    """
    if total <= 0:
        return 0

    # Sort coins in descending order to attempt largest denominations first
    coins.sort(reverse=True)

    count = 0
    for coin in coins:
        if total == 0:
            break
        # Use as many of the current denomination as possible
        count += total // coin
        total %= coin

    # If total is not 0, it's impossible to form the total
    if total != 0:
        return -1

    return count
