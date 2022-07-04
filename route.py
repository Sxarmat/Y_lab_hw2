from itertools import permutations
from math import sqrt, pow


def find_route(post, addresses):
    '''
    Ищет все возможные варианты маршрута, сравнивает их длину и возвращает наиболее короткий из них
    :param post: координаты почтового отделения
    :param addresses: список, кортеж или множество, содержащие координаты всех точек маршрута
    :return: строка с последовательностью всех точек, которые составляют самый короткий из маршрутов с выводом
    промежуточных расстояний для каждой точки (от начала до текущей точки) и общей длины маршрута.
    '''
    shortest_route = ''
    shortest_distance = float('inf')
    start = stop = post
    waypoints = permutations(addresses, len(addresses))
    for waypoint in waypoints:
        route = calc_distance((start, *waypoint, stop))
        if route[1] < shortest_distance:
            shortest_route = route[0]
            shortest_distance = route[1]
    return shortest_route


def calc_distance(route):
    '''
    Формирует строку с последовательностью всех точек маршрута, с выводом промежуточных расстояний для каждой точки и
    считает длину маршрута
    :param route: последовательность координат маршрута
    :return: кортеж с полным маршрутом и его длиной
    '''
    route_str = '{}'.format(route[0])
    distance = 0
    for point in range(len(route) - 1):
        point_1, point_2 = route[point], route[point + 1]
        point_distance = sqrt(pow(point_2[0] - point_1[0], 2) + pow(point_2[1] - point_1[1], 2))
        distance += point_distance
        route_str += ' -> {}[{}]'.format(point_2, distance)
    return route_str, distance


if __name__ == '__main__':
    post_in = (0, 2)
    addresses_in = ((2, 5), (5, 2), (6, 6), (8, 3))
    print('shortest_route =', find_route(post_in, addresses_in))
