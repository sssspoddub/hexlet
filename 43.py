import random


def choice_from_range(text: str, start: int, finish: int) -> str:
    random_index = random.randint(start, finish)
    return text[random_index]
