#!/usr/bin/python3


def sieve_of_eratosthenes(n):
    """Generate a list of prime numbers """
    is_prime = [True] * (n + 1)
    p = 2
    while (p * p <= n):
        if is_prime[p] is True:
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
        p += 1
    primes = [p for p in range(2, n + 1) if is_prime[p]]
    return primes


def play_game(n, primes):
    """Simulate the game for a given n and return the winner."""
    available_numbers = set(range(1, n + 1))
    turn = 0  # 0 for Maria, 1 for Ben

    while True:
        prime_selected = False
        for prime in primes:
            if prime in available_numbers:
                prime_selected = True
                multiples = set(range(prime, n + 1, prime))
                available_numbers -= multiples
                break
        if not prime_selected:
            break
        turn = 1 - turn  # Switch turn

    return "Maria" if turn == 1 else "Ben"


def isWinner(x, nums):
    """Determine the winner of each game an """
    if not nums or x <= 0:
        return None

    max_num = max(nums)
    primes = sieve_of_eratosthenes(max_num)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        winner = play_game(n, primes)
        if winner == "Maria":
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None


# Example Usage
if __name__ == "__main__":
    print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))
