def letter_multiply(word: str, char: str, number: int) -> str:
    return word.replace(char, char * number)
