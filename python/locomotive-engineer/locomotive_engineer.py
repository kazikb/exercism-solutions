"""Functions which helps the locomotive engineer to keep track of the train."""


def get_list_of_wagons(*args):
    """Return a list of wagons.

    :param: arbitrary number of wagons.
    :return: list - list of wagons.
    """

    return list(args)


def fix_list_of_wagons(each_wagons_id, missing_wagons):
    """Fix the list of wagons.

    :parm each_wagons_id: list - the list of wagons.
    :parm missing_wagons: list - the list of missing wagons.
    :return: list - list of wagons.
    """

    wagon_1, wagon_2, locomotive, *rest_wagons_id, = *each_wagons_id,
    return [locomotive, *missing_wagons, *rest_wagons_id, wagon_1, wagon_2]


def add_missing_stops(route, **kwargs):
    """Add missing stops to route dict.

    :param route: dict - the dict of routing information.
    :param: arbitrary number of stops.
    :return: dict - updated route dictionary.
    """

    return {**route, "stops": list(kwargs.values())}


def extend_route_information(route, more_route_information):
    """Extend route information with more_route_information.

    :param route: dict - the route information.
    :param more_route_information: dict -  extra route information.
    :return: dict - extended route information.
    """

    return {**route, **more_route_information}


def fix_wagon_depot(wagons_rows):
    """Fix the list of rows of wagons.

    :param wagons_rows: list[list[tuple]] - the list of rows of wagons.
    :return: list[list[tuple]] - list of rows of wagons.
    """

    # Rozbicie rozwiązania na składowe
    # print(zip(*wagons_rows))
    # print(map(list, zip(*wagons_rows)))
    # for item in zip(*wagons_rows): print(list(item))
    #
    # Jeszcze inaczej można to rozwiązać:
    # [*first_row], [*second_row], [*third_row] = zip(*wagons_rows)
    # [first_row, second_row, third_row]
    #
    # Kolejny sposób
    # list(map(list, zip(*wagons_rows)))

    [*wagons_row_1], [*wagons_row_2], [*wagons_row_3] = zip(*wagons_rows)
    return [wagons_row_1, wagons_row_2, wagons_row_3]
