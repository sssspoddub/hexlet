def rgb(red, green, blue):
    return red, green, blue


class Color:
    red = rgb(red=255, green=0, blue=0)
    green = rgb(green=255, red=0, blue=0)
    blue = rgb(blue=255, red=0, green=0)


print(Color.red)
print(Color.green == rgb(0, 255, 0))
