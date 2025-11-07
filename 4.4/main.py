import turtle

SETTINGS = {
    "branchLength": 67.41,
    "levels": 3,
    "branchColour": "brown",
    "leafColour": "green"
}

pen = turtle.Turtle()
pen.width(4.1)

def drawTree(t, level, branchLength):
  if level > 0:
    t.pencolor(colour1)
    t.forward(branchLength)

    t.left(21)
    drawTree(t, level - 1, branchLength / 1.67)
    t.right(21)

    t.right(21)
    drawTree(t, level - 1, branchLength / 1.67)
    t.left(21)

    t.backward(branchLength)

  else:
    t.pencolor(colour2)
    t.dot(6)
    t.pencolor(colour1)
    
pen.speed(0)
pen.penup()
pen.goto(0, -180)
pen.left(90)
pen.pendown()

levels = int(input("How many levels do you want me to draw. (default is 3) ") or SETTINGS["levels"])
branchLength = float(input("How long do you want each branch to be. (default is 67.41) ") or SETTINGS["branchLength"])

if levels < 1:
  levels = 1
if branchLength < 10:
  branchLength = 10

colour1 = input("What colour do you want your branch to be. (default is brown) ") or SETTINGS["branchColour"]
colour2 = input("What colour do you want the leaves to be. (default is green) ") or SETTINGS["leafColour"]

drawTree(pen, levels, branchLength)
pen.hideturtle()
turtle.done()