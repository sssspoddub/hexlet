from symbols import is_vowel


def count_vowels(word: str) -> int:
    counter = 0
    for i in word:
        if is_vowel(i) is True:
            counter += 1
    return counter
