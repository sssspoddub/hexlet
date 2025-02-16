def calculate_average(data: list):
    if len(data) == 0:
        return None
    else:
        return sum(data) / len(data)
