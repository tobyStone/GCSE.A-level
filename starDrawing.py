import turtle
import random
# ------------------------------------------------------------
# Constants
# ------------------------------------------------------------
STAR_ANGLE = 144                # For a five-pointed star
MAXIMUM_X = 350                 # Maximum positive X coordinate
MAXIMUM_Y = 300                 # Maximum positive Y coordinate

# ------------------------------------------------------------
# Globals
# ------------------------------------------------------------
sideLength = 0                  # Length of star's leg



# ------------------------------------------------------------
# Subprograms
# ------------------------------------------------------------
def doStar (pLength):
    # Complete this subprogram to draw a star
    myTurtle.penup()

    # Rotate the star a random number of degrees
    heading = random.randint (1, 360)
    myTurtle.setheading (heading)

    # Choose a random position on the drawing canvas
    xPos = random.randint (-MAXIMUM_X + pLength, MAXIMUM_X-pLength)
    yPos = random.randint (-MAXIMUM_Y + pLength, MAXIMUM_Y-pLength)
    myTurtle.setpos (xPos, yPos)

    # Use a 'for' loop
    myTurtle.pendown ()
    for count in range (5):
        myTurtle.forward (pLength)
        myTurtle.right (STAR_ANGLE)

# ------------------------------------------------------------
# Main program
# ------------------------------------------------------------
myTurtle = turtle.Turtle ()

for count in range (5):
    sideLength = random.randint (10, 150)
    doStar (sideLength)
