# https://realpython.com/python-lambda/
# https://realpython.com/sort-python-dictionary/
# https://docs.python.org/3/reference/expressions.html#lambda
#
# Przy tym zadaniu postanowiłem wypróbować co oferuje Chat GPT.
# Poniżej jego sugestia co do wykonania sortowania:
#
# To achieve sorting by 'sub_key' and, in case of a tie, sorting by key in reverse order,
# you can modify the custom sorting function. Here's an example:
#
# ---CODE SNIPPET START---
# nested_dict = {
#     'key1': {'sub_key': 3, 'sub_key2': 5},
#     'key2': {'sub_key': 2, 'sub_key2': 5},
#     'key3': {'sub_key': 3, 'sub_key2': 4},
# }
#
# # Define a custom sorting function
# def custom_sort(item):
#     # Sorting by 'sub_key' in reverse order and then by key in reverse order
#     return (-item[1]['sub_key'], item[0])
#
# # Sort the nested dictionary using the custom sorting function
# sorted_dict = dict(sorted(nested_dict.items(), key=custom_sort))
#
# # Print the sorted dictionary
# print(sorted_dict)
# ---CODE SNIPPET END---
#
# In this example, the custom_sort function returns a tuple where the first element is the negation of the 'sub_key' value
# (to achieve sorting in reverse order), and the second element is the key.
# The sorted function will then use this custom sorting function to sort the dictionary first by the 'sub_key' in reverse order and,
# in case of a tie, by the key in reverse order.
#
# The negation in the first element of the tuple is used to achieve a descending order for the 'sub_key'.
# When you pass reverse=True to the sorted function, it sorts in descending order by default.
# However, since you want to customize the sorting for the 'sub_key' while keeping the key in ascending order,
# we use negation to flip the order of the 'sub_key' values.
#
# By negating the 'sub_key' values, higher values become negative, and therefore,
# sorting in ascending order of negated values achieves the same result as sorting in descending order of the original values.
# This allows you to get a sorted order by 'sub_key' in reverse (descending) order,
# while maintaining the ascending order of keys in case of a tie.
#
# Funkcję `custom_sort` która jest wywoływana na każdym elemencie sortowanego obiektu dict można zastąpić
# wyrażeniem `lambda` które tworzy anonimową funkcję
#
# lambda item: (-item[1].get("P"), item[0])

def generate_score_board(rows) -> {}:
    games_stat = {}

    for row in rows:
        row_entry = (row.split(";"))

        for i in range(2):
            if not games_stat.get(row_entry[i], False):
                games_stat[row_entry[i]] = {"MP": 0, "W": 0, "D": 0, "L": 0, "P": 0}

            games_stat[row_entry[i]]["MP"] += 1

        if row_entry[2] == "win":
            games_stat[row_entry[0]]["W"] += 1
            games_stat[row_entry[0]]["P"] += 3
            games_stat[row_entry[1]]["L"] += 1
        elif row_entry[2] == "loss":
            games_stat[row_entry[1]]["W"] += 1
            games_stat[row_entry[1]]["P"] += 3
            games_stat[row_entry[0]]["L"] += 1
        else:
            games_stat[row_entry[0]]["D"] += 1
            games_stat[row_entry[0]]["P"] += 1
            games_stat[row_entry[1]]["D"] += 1
            games_stat[row_entry[1]]["P"] += 1

    return games_stat

def tally(rows):
    formated_board = ["{:<30} |{:>3} |{:>3} |{:>3} |{:>3} |{:>3}".format(
        "Team","MP","W","D","L","P")]

    games_stat = generate_score_board(rows)
    out_dict = dict(sorted(games_stat.items(), key=lambda item: (-item[1].get("P"), item[0])))

    for key, value in out_dict.items():
        formated_board.append("{:<30} |{:>3} |{:>3} |{:>3} |{:>3} |{:>3}".format(
            key,value["MP"],value["W"],value["D"],value["L"],value["P"]))

    return formated_board
