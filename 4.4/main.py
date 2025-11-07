import turtle
SETTINGS = {
    "branchLength": 67.41,
    "levels": 3,
    "branchColour": "brown",
    "leafColour": "green"
}

turtle = turtle.Turtle()

def drawTree(level, branchLength):
  if level > 0:
    turtle.pencolor(colour1)
    turtle.forward(branchLength)
    turtle.left(21)
    drawTree(level-1, branchLength/1.41)
    
    turtle.right(21)
    drawTree(level-1, branchLength/1.41)
    
    turtle.right(21)
    drawTree(level-1, branchLength/1.41)
    
  else:
    turtle.pencolor(colour2)
    turtle.color("")
    turtle.stamp()
    turtle.color("brown")
turtle.speed(0)
turtle.penup()
turtle.goto(0, -180)
turtle.left(90)
turtle.pendown()

levels = input("How many levels do you want me to draw. (defualt is 3) ") or SETTINGS["levels"]
branchLength = input('How long do you want each branch to be. (defualt is 67.41)') or SETTINGS["branchLength"]
colour1 = input("What colour do you want your brach to be. (defualt is brown) ") or SETTINGS["branchColour"]
colour2 = input("what do you want the branch colour to be. (defualt is green)") or SETTINGS["leafColour"]
if levels <1:
  levels =1

if branchLength <10:
  branchLength = 10

drawTree(int(levels), 120)