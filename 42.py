def get_mid_point(first_point, second_point):
    x, y = first_point['x'], first_point['y']
    x1, y1 = second_point['x'], second_point['y']
    mid_x = (x + x1) / 2
    mid_y = (y + y1) / 2
    return {'x': mid_x, 'y': mid_y}


point1 = {'x': 0, 'y': 0}
point2 = {'x': 4, 'y': 4}
print(get_mid_point(point1, point2))
