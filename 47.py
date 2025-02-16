def get(data: list, index: int, empty=None):
    if -len(data) <= index < len(data):
        return data[index]
    return empty
