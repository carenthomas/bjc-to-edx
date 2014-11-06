
from turtle import fd, bk, right, left, up, down, reset
import turtle as t
import math

### A library of functions that draw fractals.
### @author Peter Sujan


### Various utility methods


def drawSquare(size, fill):
    t.fill(fill)
    for i in range(4):
        fd(size)
        right(90)
    t.fill(False)

def drawTriangle(size, fill):
    t.fill(fill)
    for i in range(3):
        fd(size)
        right(120)
    t.fill(False)

def drawPolygon(size, fill, n):
    t.fill(fill)
    for i in range(n):
        fd(size)
        right(360.0 / n)
    t.fill(False)

### Functions that draw fractals.


def koch(size, level):
    """ One side of the Koch Snowflake.
    http://en.wikipedia.org/wiki/Koch_snowflake
    """
    
    if level < 1:
        fd(size)
    else:
        koch(size / 3.0, level - 1)
        left(60)
        koch(size / 3.0, level - 1)
        right(120)
        koch(size / 3.0, level - 1)
        left(60)
        koch(size / 3.0, level - 1)


def fullKoch(size, level):
    """ The full Koch Snowflake.
    http://en.wikipedia.org/wiki/Koch_snowflake
    """

    for i in range(3):
        koch(size, level)
        right(120)


def cCurve(size, level):
    """ The Levy C-Curve fractal.
    http://en.wikipedia.org/wiki/C-curve
    """

    if level < 1:
        fd(size)
    else:
        left(45)
        cCurve(size / 2.0, level - 1)
        right(90)
        cCurve(size / 2.0, level - 1)
        left(45)

def squiral(size, level):
    """ A square spiral. """

    if level < 1:
        fd(size)
    else:
        fd(size * level)
        right(90)
        squiral(size, level - 1)


def UMCTriangle(size, angle, level):
    """ A 'uniform mass center triangle' fractal """
    newAngle = angle / 2.0
    obtuse = 180 - angle * 2
    if level < 1:
            fd(size)
            left(180 - angle + newAngle)
            fd(size / (2 * math.cos(math.radians(newAngle))))
            bk(size / (2 * math.cos(math.radians(newAngle))))
            right(newAngle)
            
            fd(size / (2 * math.cos(math.radians(angle))))
            left(180 - obtuse + obtuse / 2.0)
            fd(size / (2 * math.cos(math.radians(angle))) * math.sin(math.radians(newAngle)) / math.sin(math.radians(180 - newAngle - obtuse / 2.0)))
            bk(size / (2 * math.cos(math.radians(angle))) * math.sin(math.radians(newAngle)) / math.sin(math.radians(180 - newAngle - obtuse / 2.0)))
            right(obtuse / 2.0)

            fd(size / (2 * math.cos(math.radians(angle))))
            left(180 - angle + newAngle)
            fd(size / (2 * math.cos(math.radians(newAngle))))
            bk(size / (2 * math.cos(math.radians(newAngle))))
            right(newAngle)
            
    else:
        for i in range(3):
            UMCTriangle(size, newAngle, level - 1)
            fd(size)
            
            fd(size / (2 * math.cos(math.radians(angle))))

            fd(size / (2 * math.cos(math.radians(angle))))
            
        

def accidentalButCool(size, angle, level):
    newAngle = angle / 2.0
    obtuse = 180 - angle
    if level < 1:
        for i in range(3):
            fd(size)
            left(obtuse)
            fd(size / (2 * math.cos(math.radians(newAngle))))
            bk(size / (2 * math.cos(math.radians(newAngle))))
            right(newAngle)
    else:
        for i in range(3):
            accidentalButCool(size, newAngle, level - 1)





def gosper(size, level, direction):
    """ The Gosper Curve.
    http://en.wikipedia.org/wiki/Gosper_curve
    """

    if level < 1:
        if direction > 0:
            right(60)
            fd(size)
            left(60)
            fd(2 * size)
            left(120)
            fd(size)
            left(60)
            fd(size)
            right(120)
            fd(size)
            right(60)
            fd(size)
        else:
            fd(size)
            left(60)
            fd(size)
            left(120)
            fd(size)
            right(60)
            fd(size)
            right(120)
            fd(2 * size)
            right(60)
            fd(size)
            left(60)
    else:
        if direction > 0:
            right(60)
            gosper(size / 2.5, level - 1, -1)
            left(60)
            gosper(size / 2.5, level - 1, 1)
            gosper(size / 2.5, level - 1, 1)
            left(120)
            gosper(size / 2.5, level - 1, 1)
            left(60)
            gosper(size / 2.5, level - 1, -1)
            right(120)
            gosper(size / 2.5, level - 1, -1)
            right(60)
            gosper(size / 2.5, level - 1, 1)
        else:
            gosper(size / 2.5, level - 1, -1)
            left(60)
            gosper(size / 2.5, level - 1, 1)
            left(120)
            gosper(size / 2.5, level - 1, 1)
            right(60)
            gosper(size / 2.5, level - 1, -1)
            right(120)
            gosper(size / 2.5, level - 1, -1)
            gosper(size / 2.5, level - 1, -1)
            right(60)
            gosper(size / 2.5, level - 1, 1)
            left(60)


def gosperIsland(size, level):
    down()
    for i in range(6):
        gosperIslandHelper(size, level)
        right(120)
    
def gosperIslandHelper(size, level):
    # TODO: finish this later
    return 0
    

def vicsekS(size, level):
    """ The saltire form of the Vicsek fractal. """
    newSize = size / 3.0
    if level < 1:
        down()
        drawSquare(newSize, True)
        up()
        fd(2 * newSize)
        down()
        drawSquare(newSize, True)
        up()
        bk(2 * newSize)
        right(90)
        fd(newSize)
        left(90)
        fd(newSize)
        down()
        drawSquare(newSize, True)
        up()
        bk(newSize)
        right(90)
        fd(newSize)
        left(90)
        down()
        drawSquare(newSize, True)
        up()
        fd(2 * newSize)
        down()
        drawSquare(newSize, True)
        up()
        bk(2 * newSize)
        left(90)
        fd(2 * newSize)
        right(90)

    else:
        down()
        vicsekS(newSize, level - 1)
        up()
        fd(2 * newSize)
        down()
        vicsekS(newSize, level - 1)
        up()
        bk(2 * newSize)
        right(90)
        fd(newSize)
        left(90)
        fd(newSize)
        down()
        vicsekS(newSize, level - 1)
        up()
        bk(newSize)
        right(90)
        fd(newSize)
        left(90)
        down()
        vicsekS(newSize, level - 1)
        up()
        fd(2 * newSize)
        down()
        vicsekS(newSize, level - 1)
        up()
        bk(2 * newSize)
        left(90)
        fd(2 * newSize)
        right(90)
        

def vicsekC(size, level):
    """ The cross form of the Vicsek fractal. """
    newSize = size / 3.0
    if level < 1:
        up()
        fd(newSize)
        down()
        drawSquare(newSize, True)
        up()
        bk(newSize)
        right(90)
        fd(newSize)
        left(90)
        down()
        drawSquare(newSize, True)
        fd(newSize)
        drawSquare(newSize, True)
        fd(newSize)
        drawSquare(newSize, True)
        bk(newSize)
        right(90)
        fd(newSize)
        left(90)
        drawSquare(newSize, True)
        up()
        left(90)
        fd(2 * newSize)
        right(90)
        bk(newSize)
        

    else:
        up()
        fd(newSize)
        down()
        vicsekC(newSize, level - 1)
        up()
        bk(newSize)
        right(90)
        fd(newSize)
        left(90)
        down()
        vicsekC(newSize, level - 1)
        fd(newSize)
        vicsekC(newSize, level - 1)
        fd(newSize)
        vicsekC(newSize, level - 1)
        bk(newSize)
        right(90)
        fd(newSize)
        left(90)
        vicsekC(newSize, level - 1)
        up()
        left(90)
        fd(2 * newSize)
        right(90)
        bk(newSize)




def dragon(size, level, direction):
    """ The Dragon Curve.
    http://en.wikipedia.org/wiki/Dragon_curve
    """

    if level < 1:
        down()
        right(direction * 45)
        fd(size)
        left(direction * 90)
        fd(size)
        right(direction * 45)
    else:
        down()
        right(direction * 45)
        dragon(size / math.sqrt(2), level - 1, 1)
        left(direction * 90)
        dragon(size / math.sqrt(2), level - 1, -1)
        right(direction * 45)


def sierpinski(size, level):
    """ The Sierpinski Triangle
    https://en.wikipedia.org/wiki/Sierpinski_triangle
    """

    if level < 1:
        left(60)
        drawTriangle(size, True)
        right(60)
    else:
        sierpinski(size / 2.0, level - 1)
        left(60)
        fd(size / 2.0)
        right(60)
        sierpinski(size / 2.0, level - 1)
        left(60)
        bk(size / 2.0)
        right(60)
        fd(size / 2.0)
        sierpinski(size / 2.0, level - 1)
        bk(size / 2.0)


def sierpinskiArrowhead(size, level, direction):
    """ The Sierpinski Arrowhead Curve.
    https://en.wikipedia.org/wiki/Sierpi%C5%84ski_arrowhead_curve
    """

    if level < 1:
        left(60 * direction)
        fd(size * direction)
        right(60 * direction)
        fd(size * direction)
        right(60 * direction)
        fd(size * direction)
        left(60 * direction)
    else:
        right(120 * direction)
        sierpinskiArrowhead(size / 2.0, level - 1, direction * -1)
        left(120 * direction)
        sierpinskiArrowhead(size / 2.0, level - 1, direction)
        left(120 * direction)
        sierpinskiArrowhead(size / 2.0, level - 1, direction * -1)
        right(120 * direction)


def tSquare(size, level):
    """ The T-Square fractal.
    http://en.wikipedia.org/wiki/T-Square_%28fractal%29
    """

    if level < 1:
        drawSquare(size, True)
    else:
        drawSquare(size, True)
        bk(size / 4.0)
        left(90)
        fd(size / 4.0)
        right(90)
        tSquare(size / 2.0, level - 1)
        up()
        fd(size)
        down()
        tSquare(size / 2.0, level - 1)
        right(90)
        fd(size)
        left(90)
        tSquare(size / 2.0, level - 1)
        bk(size)
        tSquare(size / 2.0, level - 1)
        left(90)
        up()
        fd(size * 3 / 4.0)
        down()
        right(90)
        fd(size / 4.0)
        

def pythagoras(size, level):
    """ The Pythagoras Tree fractal.
    http://en.wikipedia.org/wiki/Pythagoras_tree_%28fractal%29
    """

    if level < 1:
        drawSquare(size, True)
    else:
        newSize = size / 2.0 * math.sqrt(2)
        drawSquare(size, True)
        left(135)
        fd(newSize)
        right(90)
        pythagoras(newSize, level - 1)
        left(90)
        bk(newSize)
        right(135)
        fd(size)
        left(135)
        fd(newSize)
        right(90)
        fd(newSize)
        right(90)
        pythagoras(newSize, level - 1)
        left(90)
        bk(newSize)
        left(90)
        bk(newSize)
        right(135)
        bk(size)



def hexaflake(size, level, center):
    if level < 1:
        drawPolygon(size, True, 6)
    else:
        newSize = size / 3.0
        hexaflake(newSize, level - 1, center)
        up()
        fd(newSize * 2)
        down()
        hexaflake(newSize, level - 1, center)
        up()
        bk(newSize * 2)
        right(120)
        fd(newSize * 2)
        down()
        left(120)
        hexaflake(newSize, level - 1, center)
        up()
        fd(2 * newSize)
        if center:
            down()
            hexaflake(newSize, level - 1, center)
            up()
        fd(2 * newSize)
        down()
        hexaflake(newSize, level - 1, center)
        up()
        bk(4 * newSize)
        right(120)
        up()
        fd(newSize)
        left(60)
        fd(newSize)
        left(60)
        fd(newSize)
        down()
        hexaflake(newSize, level - 1, center)
        up()
        fd(2 * newSize)
        hexaflake(newSize, level - 1, center)
        up()
        bk(3 * newSize)
        left(120)
        fd(newSize)
        right(60)
        fd(size)
        right(60)
        


def cantorSquare(size, level):
    if level < 1:
        up()
        drawSquare(size, True)
    else:
        newSize = size / 3.0
        up()
        cantorSquare(newSize, level - 1)
        fd(newSize * 2)
        cantorSquare(newSize, level - 1)
        right(90)
        fd(newSize * 2)
        left(90)
        cantorSquare(newSize, level - 1)
        bk(newSize * 2)
        cantorSquare(newSize, level - 1)
        right(90)
        bk(newSize * 2)
        left(90)
