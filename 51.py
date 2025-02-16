def calculate_sum(data: list):
    if len(data) == 0:
        return 0
    else:
        counter = 0
        for number in data:
            if number % 3 == 0:
                counter += number
        return counter
