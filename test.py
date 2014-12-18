def triple_free_combinations(n, k=2):
    """Return the number of ways to choose n items (with k choices for
    each item), subject to the constraint that no colour appears three
    times in a row.

    """
    if n == 0:
        return 1
    a, b = 2, 2 * 2
    for _ in range(n - 1):
        a, b = b, (a + b)
    return a

print triple_free_combinations(3, 2)