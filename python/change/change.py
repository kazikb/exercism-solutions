# https://docs.python.org/3/library/itertools.html#itertools.combinations_with_replacement
# https://www.khoury.northeastern.edu/home/jaa/CSG713.04F/Information/Handouts/dyn_prog.pdf
#
# Poniższe rozwiązanie jest bardzo interesujące:
# https://exercism.org/tracks/python/exercises/change/solutions/glennj

from itertools import combinations_with_replacement

def find_fewest_coins(coins, target):
    if target < 0:
        raise ValueError("target can't be negative")

    max_number_of_coins = target // min(coins) + 1

    for number_of_coins in range(max_number_of_coins):
        # Generate all possible combinations
        coins_combinations = combinations_with_replacement(coins, number_of_coins)

        for coins_combination in coins_combinations:
            if sum(coins_combination) == target: return sorted(coins_combination)

    raise ValueError("can't make target with given coins")
