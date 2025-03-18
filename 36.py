def format_person_info(name, age, **kwargs):
    default_info = f'Name: {name}, Age: {age}'
    if kwargs:
        additional = []
        for key, value in sorted(kwargs.items()):
            additional.append(f'{key.capitalize()}: {value}')
    return f"{default_info}, {', '.join(additional)}"
