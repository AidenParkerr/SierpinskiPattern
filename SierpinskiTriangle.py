from turtle import Screen
import turtle
import random


class SierpinskiTriangle:
    __XY_OFFSET = 100  # window X, Y offset
    __colours = ['orange', 'green', 'red', 'cyan',
                 'purple', 'blue']  # colours for drawn lines

    def __init__(self):
        tutSize = 10  # turtle size
        screen = Screen()  # used to get screen size
        turtle.penup()
        startXPoint = (-screen.window_width() / 2) + \
            (tutSize / 2) + self.__XY_OFFSET  # set start X point
        startYPoint = (-screen.window_height() / 2) + \
            (tutSize / 2) + self.__XY_OFFSET  # set start Y point
        turtle.goto(startXPoint, startYPoint)  # start at given X,Y coords
        turtle.title("Sierpinski Triangle Pattern.")
        turtle.pendown()
        turtle.speed(5)  # set the speed to draw
        turtle.pensize(2)  # set pen thickness
        turtle.shape('turtle')

    def drawTriangle(self, line):
        for i in range(3):
            # draw triangle
            # set each line drawn to a random colour
            turtle.pencolor(random.choice(self.__colours))
            turtle.forward(line)  # draw line forward {line} pixels
            turtle.left(120)  # create outer angle of triangle

    def generatePattern(self, lineSize, depth):
        """
        The recursive function calls are used to shrink the triangles being drawn to the relative size based on the depth parameter.

        """
        if int(depth) < 0:
            raise ValueError("Depth can not be less than 0.")
        if int(lineSize) < 1:
            raise ValueError("Side of triangles must be greater than 1.")
        if depth == 0:
            # If there is no depth of the pattern, draw the base triangle.
            self.drawTriangle(lineSize)
            return

        # If a depth has been provided, draw appropriate fractals inside base triangle.
        # depth - 1 // IMPORTANT. It breaks recursion loop.
        self.generatePattern(lineSize/2, depth - 1)
        # draw line whose length is half of the side of the upper layer triangles.
        turtle.forward(lineSize / 2)
        self.generatePattern(lineSize/2, depth - 1)  # recursive function call
        turtle.back(lineSize/2)  # start point
        turtle.left(60)  # angles in triangle add up to 180 deg
        turtle.forward(lineSize/2)
        turtle.right(60)
        # draws the upper part of a fractal
        self.generatePattern(lineSize/2, depth - 1)
        turtle.left(60)
        turtle.back(lineSize/2)
        turtle.right(60)


if __name__ == '__main__':

    sierpinskiPattern = SierpinskiTriangle()
    sierpinskiPattern.generatePattern(lineSize=760, depth=2)
