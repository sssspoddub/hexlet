def join_numbers_from_range(number1: int, number2: int) -> str:
    empty_string = ''
    for i in range(number1, number2 + 1):
        empty_string += str(i)
    return empty_string
