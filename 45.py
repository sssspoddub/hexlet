def get_weekends(variant='long'):
    if variant == 'short':
        return ['sat', 'sun']
    else:
        return ['saturday', 'sunday']
