import itertools

def combinations(target, size, exclude):
    """Function to help find possible digits combinations to solve Killer Sudoku."""

    if size > 9:
        raise ValueError("size cannot exceed 9")

    candidates = [i for i in range(1, 10) if i not in exclude]

    if size == 1:
        if target in candidates:
            return [[target]]
        return []

    solutions = itertools.combinations(candidates, size)
    result = []
    for item in solutions:
        if sum(item) == target:
            result.append(list(item))
    return result
