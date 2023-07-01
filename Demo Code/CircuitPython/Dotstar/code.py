import time
import random
import board
import adafruit_dotstar as dotstar
import adafruit_fancyled.adafruit_fancyled as fancy

def random_color():
    return random.randrange(0, 7) * 32

num_leds = 24
data_pin = board.GP19
clock_pin = board.GP18
dots = dotstar.DotStar(board.GP18, board.GP19, num_leds, brightness=1.0, auto_write=False)

offset = 0  # Positional offset into color palette to get it to 'spin'

while True:
    for i in range(num_leds):
        c = fancy.CRGB(fancy.CHSV(i/num_leds+offset,1.0,0.05))
        dots[i] = c.pack()
    dots.show()

    offset += 0.02  # Bigger number = faster spin
