from math import sqrt


def calculate_distance(point1, point2):
    x, y = point1
    x2, y2 = point2
    return sqrt((x2 - x) ** 2 + (y2 - y) ** 2)


point1 = [0, 0]
point2 = [3, 4]
print(calculate_distance(point1, point2))
