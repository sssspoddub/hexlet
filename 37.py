def run(text):
    def take_last(text, length):
        if len(text) >= length:
            new_text = text[::-1]
            return new_text[:length]
        else:
            return None
    return take_last(text, 4)
