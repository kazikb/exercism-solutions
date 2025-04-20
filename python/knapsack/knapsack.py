def maximum_value(maximum_weight, items):
    """Function to solve 0/1 Knapsack Problem

    Solution is based on algorithm presented on Wikipedia:
    https://en.wikipedia.org/wiki/Knapsack_problem#0-1_knapsack_problem
    """
    n = len(items)
    # Store only recent 2 lines of array m
    prev_row = [0] * (maximum_weight + 1)
    curr_row = [0] * (maximum_weight + 1)

    for i in range(1, n + 1):
        weight = items[i -1]["weight"]
        value = items[i - 1]["value"]
        for j in range(1, maximum_weight + 1):
            if weight > j:
                curr_row[j] = prev_row[j]
            else:
                curr_row[j] = max(prev_row[j], prev_row[j - weight] + value)
        prev_row, curr_row = curr_row, prev_row

    return prev_row[maximum_weight]
