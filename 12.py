def format_person_info(name, age, **info):
    new_info = sorted(info.items())
    formatted_parts = []
    for key, value in new_info:
        formatted_parts.append(f'{key.capitalize()}: {value}')
    if formatted_parts:
        formatted_info = ', '.join(formatted_parts)
        return f'Name: {name}, Age: {age}, {formatted_info}'
    else:
        return f'Name: {name}, Age: {age}'
