"""
A program that displays objects
Coded by Jenna Beach (040777966)
Last modified: 03/12/2020
Algorithm:
"""

from gfxhat import lcd


def displayObject(obj,x,y):
    while x < 0 or y < 0 or x > 127 or y > 63:
        if x < 0:
            x = 128+x
        if y < 0:
            y = 64+y
        if x > 127:
            x = x-128
        if y > 63:
            y = y-63
    posX = x
    posY = y
    for lines in obj:
        for pxl in lines:
            if pxl == 1:
                lcd.set_pixel(posX,posY,1)
                lcd.show()
            posX += 1
            if posX > 127:
                posX = 0
        posY += 1
        if posY > 63:
            posY = 0
        posX = x


f1 = [
[1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1],
[0, 1, 1, 1, 1, 1, 1, 0],
[1, 0, 1, 1, 1, 1, 0, 1],
[1, 0, 0, 1, 1, 0, 0, 1],
[1, 0, 0, 1, 1, 0, 0, 1],
[0, 0, 0, 1, 1, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0]
]


pm = [[0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0],
[0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0],
[0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
[1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
[1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
[1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
[1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
[1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
[1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
[0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
[0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0],
[0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0]
]

obj = 0
x = 30
y = 15


while obj != '1' and obj != '2':
    obj = input('Choose an object to display! (1 or 2):')
    if obj != '1' and obj != '2':
        print('Please enter a valid number (1 or 2)')
x = 32
y = 16

if obj == '1':
    displayObject(f1,x,y)
elif obj == '2':
    displayObject(pm,x,y)
