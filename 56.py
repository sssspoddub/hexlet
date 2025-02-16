def build_definition_list(data: list) -> str:
    if len(data) == 0:
        return ''
    answer = []
    for item, definition in data:
        answer.append(f'<dt>{item}</dt>')
        answer.append(f'<dd>{definition}</dd>')
    result = ''.join(answer)
    return f'<dl>{result}</dl>'
