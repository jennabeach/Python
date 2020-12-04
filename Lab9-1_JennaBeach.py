"""
Etch a Sketch game on Raspberry Pi
Coded by Jenna Beach (040777966)
Last modified: 03/12/2020
Algorithm:
"""

from gfxhat import lcd, fonts
from PIL import Image, ImageFont, ImageDraw
from click import getchar


def clearScreen(lcd):
    lcd.clear()
    lcd.show()


def displayText(text, lcd, x, y):
    lcd.clear()
    width, height = lcd.dimensions()
    image = Image.new('P', (width, height))
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(fonts.AmaticSCBold, 24)
    w, h = font.getsize(text)
    draw.text((x, y), text, 1, font)
    for x1 in range(x, x + w):
        for y1 in range(y, y + h):
            pixel = image.getpixel((x1, y1))
            lcd.set_pixel(x1, y1, pixel)
    lcd.show()


print('To play use the arrow keys to draw. "s" to restart, "q" to quit')
quit = False
x = 63
y = 32

clearScreen(lcd)
displayText("Etch a Sketch", lcd, 10, 20)
print("Use 'c' to clear the screen and start drawing!")

while True:
    key = getchar()
    lcd.set_pixel(x, y, 1)
    lcd.show()

    if key == 's':  # RESTART game
        clearScreen(lcd)

    elif key == '\x1b[A':  # UP arrow key
        y = y - 1
        if y == 0:
            y = 63
        lcd.set_pixel(x, y, 1)
        lcd.show()

    elif key == '\x1b[B':  # DOWN arrow key
        y = y + 1
        if y == 63:
            y == 0
        lcd.set_pixel(x, y, 1)
        lcd.show()
    elif key == '\x1b[C':  # RIGHT arrow key
        x = x + 1
        if x == 127:
            x = 0
        lcd.set_pixel(x, y, 1)
        lcd.show()
    elif key == '\x1b[D':  # LEFT arrow key
        x = x - 1
        if x == 0:
            x = 127
        lcd.set_pixel(x, y, 1)
        lcd.show()
    elif key == 'q':  # QUIT game
        lcd.clear()
        lcd.show()
        exit()
    elif key == 'c':  # CLEAR screen
        lcd.clear()
        lcd.show()
    else:
        print("Press a valid key")
