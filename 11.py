def get_average(*numbers):
    if not numbers:
        return None
    else:
        return sum(numbers) / len(numbers)
