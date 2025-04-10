import math


def make_point(x, y):
    return {
        "angle": math.atan2(y, x),
        "radius": math.sqrt((x ** 2) + (y ** 2)),
    }


def get_x(point):
    return int(point['radius'] * math.cos(point['angle']))


def get_y(point):
    return int(point['radius'] * math.sin(point['angle']))
