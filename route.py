from itertools import permutations
from math import sqrt, pow

post_in = (0, 2)
addresses_in = ((2, 5), (5, 2), (6, 6), (8, 3))


def find_route(post, *addresses):
    shortest_route = ''
    shortest_distance = float('inf')
    start = stop = post
    waypoints = permutations(addresses, len(addresses))
    for waypoint in waypoints:
        route = calc_distance((start, *waypoint, stop))
        print(route)
        if route[1] < shortest_distance:
            shortest_route = route[0]
            shortest_distance = route[1]
    return shortest_route


def calc_distance(route):
    route_str = '{}'.format(route[0])
    distance = 0
    for point in range(len(route) - 1):
        point_1, point_2 = route[point], route[point + 1]
        point_distance = sqrt(pow(point_2[0] - point_1[0], 2) + pow(point_2[1] - point_1[1], 2))
        distance += point_distance
        route_str += ' -> {}[{}]'.format(point_2, distance)
    return route_str, distance




print('shotest_route =', find_route(post_in, *addresses_in))
