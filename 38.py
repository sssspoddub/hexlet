def filter_string(my_string: str, symbol: str) -> str:
    new_string = ''
    for i in my_string:
        if i.lower() != symbol.lower():
            new_string += i
    return new_string.strip()
