def make_decart_point(x, y):
    return {"x": x, "y": y}


def get_x(point):
    return point["x"]


def get_y(point):
    return point["y"]


def make_segment(point1, point2):
    start = get_x(point1), get_y(point1)
    finish = get_x(point2), get_y(point2)
    segment = start, finish
    return segment


def get_mid_point_of_segment(segment):
    first_point, second_point = segment
    x, y = first_point
    x1, y1 = second_point
    mid_x = (x + x1) / 2
    mid_y = (y + y1) / 2
    return {'x': mid_x, 'y': mid_y}


def get_begin_point(segment):
    first_point, second_point = segment
    x, y = first_point
    return {'x': x, 'y': y}


def get_end_point(segment):
    first_point, second_point = segment
    x, y = second_point
    return {'x': x, 'y': y}
