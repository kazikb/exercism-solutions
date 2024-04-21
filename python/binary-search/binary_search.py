# Opis algorytmu Binary Search
# https://en.wikipedia.org/wiki/Binary_search_algorithm

def find(search_list, value):
    search_list.sort()

    low_index = 0
    high_index = len(search_list) -1

    while low_index <= high_index:
        mid_index = (low_index + high_index) // 2
        if search_list[mid_index] < value:
            low_index = mid_index + 1
        elif search_list[mid_index] > value:
            high_index = mid_index - 1
        else:
            return mid_index

    raise ValueError("value not in array")
