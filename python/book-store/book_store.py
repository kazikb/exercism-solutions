DISCOUNT = {
    1: 0,
    2: 2 * 800 * 0.05,
    3: 3 * 800 * 0.1,
    4: 4 * 800 * 0.2,
    5: 5 * 800 * 0.25
}

def total(basket):
    uniq_books = set(basket)
    total_price = 0
    book_count = {}
    extream = {}

    for book in uniq_books:
        for i in range(basket.count(book)):
            if book_count.get(i):
                book_count[i].append(book)
            else:
                book_count[i] = [book]

    for item in book_count.values():
        books = len(item)
        if books == 5 or books == 3:
            extream[books] = extream.get(books, 0) + 1

        total_price += books * 800 - DISCOUNT[books]

    total_price -= min(extream.get(5, 0), extream.get(3, 0)) * 40
    return int(total_price)

# Poniżej dwa ciekawe rozwiązania tego problemu jakie pokazali inni:
#
# Solution 1
# Zamiast zliczać ręcznie to tutaj skorzystano z gotowej klasy Counter
# która zlicza wystąpienie w obiekcie iterable
# https://docs.python.org/3.11/library/collections.html#collections.Counter

# from collections import Counter

# PRICING = {
#     1: 800,   # 1 x 800
#     2: 1520,  # 2 x 760
#     3: 2160,  # 3 x 720
#     4: 2560,  # 4 x 640
#     5: 3000   # 5 x 600
#     }

# def total(basket):
#     bundles = []
#     counts = Counter(basket)

#     while counts:
#         bundle = Counter(counts.keys())
#         bundles.append(len(bundle))
#         counts -= bundle

#     price = sum(PRICING[bundle] for bundle in bundles)
#     price -= min(bundles.count(5), bundles.count(3)) * 40

#     return price


# Solution 2
# https://exercism.org/tracks/python/exercises/book-store/solutions/zydeng860117
# """
# Provide function to calculate the price of shopping basket.
# """

# def total(basket):
#     """
#     This function to calculate the price of any conceivable shopping
#     basket(containing only books of the same series),giving as big a
#     discount as possible.
#     :basket the order of list
#     return the total amount of shopping cart
#     Args:
#         basket (_type_): list
#     """

#     groups = []

#     while basket:
#         uniques = set(basket)
#         for book in uniques:
#             basket.remove(book)
#         groups.append(len(uniques))

#     # group of 4 and 4 is less than 5,3
#     while 3 in groups and 5 in groups:
#         groups.remove(5)
#         groups.remove(3)
#         groups.append(4)
#         groups.append(4)

#     tots = {
#         1: 800,
#         2: (800 * 2) * 0.95,
#         3: (800 * 3) * 0.9,
#         4: (800 * 4) * 0.8,
#         5: (800 * 5) * 0.75,
#     }

#     return int(sum(tots[x] for x in groups))

# basket = [1, 2, 3, 4]
# basket = [1, 1, 2, 3, 4, 4, 5, 5]
# print(total(basket))
