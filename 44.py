def sort_pair(pair):
    number1, number2 = pair
    if number1 > number2:
        return number2, number1
    else:
        return number1, number2
