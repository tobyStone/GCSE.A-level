import turtle

myturtle = turtle.Turtle()
myturtle.penup()
myturtle.left(180)
myturtle.forward(40)
myturtle.pendown()

myturtle.forward (100)
myturtle.right (90)
myturtle.forward (100)
myturtle.right (90)
myturtle.forward (100)
myturtle.right (90)
myturtle.forward (100)
myturtle.right (135)
myturtle.forward (141.421)
myturtle.left (135)
myturtle.forward (100)
myturtle.left (135)
myturtle.forward (141.421)

#myTurtle.penup()


#myTurtle.setposition(300, 10)

#def drawRegularPolygon(sides, length):
#    myTurtle.pendown()
#    angle = 360/sides
#    for i in range(0, sides):
#        myTurtle.forward (length)
#        myTurtle.right (angle)

#drawRegularPolygon(3, 100)




#import turtle
#import random

## ------------------------------------------------------------
## Constants
## ------------------------------------------------------------
#STAR_ANGLE = 144                # For a five-pointed star
#MAXIMUM_X = 350                 # Maximum positive X coordinate
#MAXIMUM_Y = 300                 # Maximum positive Y coordinate

## ------------------------------------------------------------
## Globals
## ------------------------------------------------------------
#sideLength = 0                  # Length of star's leg

# ------------------------------------------------------------
# Subprograms
# ------------------------------------------------------------
#def doStar (pLength):
#    # Complete this subprogram to draw a star
#    myTurtle.penup()

#    # Rotate the star a random number of degrees
#    heading = random.randint (1, 360)
#    myTurtle.setheading (heading)

#    # Choose a random position on the drawing canvas
#    xPos = random.randint (-MAXIMUM_X + pLength, MAXIMUM_X-pLength)
#    yPos = random.randint (-MAXIMUM_Y + pLength, MAXIMUM_Y-pLength)
#    myTurtle.setpos (xPos, yPos)

#    # Use a 'for' loop
#    myturtle.pendown ()
#    for count in range (5):
#        myturtle.forward (plength)
#        myturtle.right (star_angle)

## ------------------------------------------------------------
## Main program
## ------------------------------------------------------------
#myTurtle = turtle.Turtle ()

#for count in range (5):
#    sideLength = random.randint (10, 150)
#    doStar (sideLength)