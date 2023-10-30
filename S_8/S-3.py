# Дан список размеров(длина, ширина) эллипсов 
# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# Напишите функцию find_farthest_orbit(list_of_orbits), 
# которая находит площадь самого большого 
# эллипса и возвращает кортеж с его размерами.
# Площадь эллипса вычисляется по формуле 
# S = pi*a*b, где a и b – длины и ширина осей эллипса
# -   Площадь кругов учитывать не нужно, 
# т.е если у эллипса a == b, то это круг.
# При решении задачи используйте списочные выражения.
# Гарантируется, что самый большой эллипс всего один.

import math

# 1
def find_farthest_orbit1(list_of_orbits):
    max_area = 0
    max_orbit = tuple()

    for orbit in list_of_orbits:
        a, b = orbit
        area = math.pi * a * b
        if area > max_area and a != b:
            max_area = area
            max_orbit = orbit
    return max_orbit

# 2
def find_farthest_orbit2(list_of_orbits):
    list_of_elips = list(filter(lambda tuple_cur: tuple_cur[0] != tuple_cur[1], list_of_orbits))
    print(list_of_elips)
    list_of_areas = list(map(lambda tuple_cur: math.pi * tuple_cur[0] * tuple_cur[1], list_of_elips))
    print(list_of_areas)
    max_area = max(list_of_areas)
    i_max = list_of_areas.index(max_area)
    return list_of_elips[i_max]


# 3
def find_farthest_orbit3(list_of_orbits):
    list_of_elips = list(filter(lambda tuple_cur: tuple_cur[0] != tuple_cur[1], list_of_orbits))
    list_of_areas = list(map(lambda tuple_cur: math.pi * tuple_cur[0] * tuple_cur[1], list_of_elips))
    return list_of_elips[list_of_areas.index(max(list_of_areas))]


# 4
def find_farthest_orbit4(list_of_orbits):
    max_area = 0
    max_orbit = tuple()

    for i, orbit in enumerate(list_of_orbits):
        print(i, orbit, sep= " = ")
    #     a, b = orbit
    #     area = math.pi * a * b
    #     if area > max_area and a != b:
    #         max_area = area
    #         max_orbit = orbit
    # return max_orbit


# 5
def find_farthest_orbit5(list_of_orbits):
    max_area = 0
    max_orbit = tuple()

    for i, orbit in enumerate(list_of_orbits):
        a, b = orbit
        area = math.pi * a * b
        if area > max_area and a != b:
            max_area = area
            i_max_orbit = i
    return list_of_orbits[i_max_orbit]

orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
print(*find_farthest_orbit1(orbits))
print(*find_farthest_orbit2(orbits))
print(*find_farthest_orbit3(orbits))
find_farthest_orbit4(orbits)
print(*find_farthest_orbit5(orbits))
print(list(enumerate(orbits)))
print(dict(enumerate(orbits)))
