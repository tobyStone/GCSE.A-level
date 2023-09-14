import turtle
myTurtle = turtle.Turtle()


myTurtle.penup()




def drawRegularPolygon(sides, length):
    myTurtle.pendown()
    myTurtle.fillcolor("#55ff00")
    myTurtle.begin_fill()
    myTurtle.pensize()
    angle = 360/sides
    for i in range(0, sides):
        myTurtle.forward (length)
        myTurtle.right(angle)
    myTurtle.end_fill()


drawRegularPolygon(3, 100)
