def get_max(data: list):
    if not data:
        return None
    first, *rest = data
    max_number = first
    for number in rest:
        if number > max_number:
            max_number = number
    return max_number
