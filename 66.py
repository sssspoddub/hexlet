def flatten(data: list):
    if not data:
        return []
    answer = []
    for i in data:
        if isinstance(i, list):
            answer.extend(i)
        else:
            answer.append(i)
    return answer
