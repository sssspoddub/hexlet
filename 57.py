def make_censored(text: str, strong_words: list) -> str:
    censored = '$#%!'
    answer = []
    separator = ' '
    for word in text.split():
        if word in strong_words:
            answer.append(censored)
        else:
            answer.append(word)
    return separator.join(answer)
