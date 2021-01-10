from collections import namedtuple

Color = namedtuple('Color', ['red', 'green', 'blue'])

color = Color(55,155,255)
white = Color(red=255, green=255, blue=255)

# print(color[0])
print(color.blue)
print(white.red)
