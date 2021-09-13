import board
import neopixel

dot = neopixel.NeoPixel(board.NEOPIXEL, 1)
dot.brightness = 0.1


print("Make it Teal!")
while True:
    dot.fill((0, 255, 255))