from sense_hat import SenseHat

sense = SenseHat()
sense.clear()

r = (255,0,0)

b = (0,0,0)

maze = [[r,r,r,r,r,r,r,r],
        [r,b,b,b,b,b,b,r],
        [r,r,r,b,r,b,b,r],
        [r,b,r,b,r,r,r,r],
        [r,b,b,b,b,b,b,r],
        [r,b,r,r,r,r,b,r],
        [r,b,b,r,b,b,b,r],
        [r,r,r,r,r,r,r,r]]

sense.set_pixels(sum(maze,[]))

from sense_hat import SenseHat

sense = SenseHat()

r = 255
g = 255
b = 255

sense.clear((r, g, b))

r = (255,0,0)

w = (255,255,255)
