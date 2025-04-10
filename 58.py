def rgb(red, green, blue):
    return red, green, blue


class Color:
    red = rgb(red=255, blue=0, green=0)
    green = rgb(red=0, green=255, blue=0)
    blue = rgb(red=0, green=0, blue=255)


print(Color.green == rgb(0, 255, 0))
