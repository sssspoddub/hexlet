def swap(data: list):
    if len(data) < 2:
        return data
    else:
        data[0], data[-1] = data[-1], data[0]
        return data
