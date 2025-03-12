def run(text):
    def take_last(word, length):
        if len(word) >= length:
            new_word = word[::-1]
            return new_word[:length]
        else:
            return None
    return take_last(text, 4)
