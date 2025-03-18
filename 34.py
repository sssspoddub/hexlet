def rgb(red=0, green=0, blue=0):
    return f'rgb({red}, {green}, {blue})'


def get_colors():
    return {
        'green': rgb(green=255),
        'blue': rgb(blue=255),
        'red': rgb(red=255)
    }
