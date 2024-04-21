def sum_of_multiples(limit, multiples):
    sum_unique_multiples = []
    for item in range(limit):
        for multi in multiples:
            if multi > 0 and item % multi == 0:
                sum_unique_multiples.append(item)
    return sum(set(sum_unique_multiples))
    