#!/usr/bin/python3


def is_prime(n):
    """
    Checks if a number is prime.

    Args:
        n: The number to check.

    Returns:
        True if the number is prime, False otherwise.
    """
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def remove_multiples(nums, prime):
    """
    Removes all multiples of a prime number from a list.

    Args:
        nums: The list of numbers.
        prime: The prime number to remove multiples of.

    Returns:
        A new list with the multiples removed.
    """
    return [num for num in nums if num % prime != 0]


def is_winner(x, nums):
    """
    Determines the winner of the prime game.

    Args:
        x: The number of rounds of the game.
        nums: A list of integers for each round.

    Returns:
        "Maria" if Maria wins most rounds, "Ben" if Ben wins most rounds,
        or None if the winner cannot be determined.
    """
    maria_wins = 0
    ben_wins = 0

    for _ in range(x):
        player = "Maria"
        while nums:
            if player == "Maria":
                # Find the first prime number in the list
                for num in nums:
                    if is_prime(num):
                        prime = num
                        nums = remove_multiples(nums, prime)
                        break
                else:
                    # No prime numbers left for Maria, Ben wins
                    ben_wins += 1
                    break
                player = "Ben"
            else:
                # Ben can take any remaining number
                nums.pop(0)
                maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif maria_wins < ben_wins:
        return "Ben"
    else:
        return None


# Example usage
if __name__ == "__main__":
    print("Winner:", is_winner(5, [2, 5, 1, 4, 3]))