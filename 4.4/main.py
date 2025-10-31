import turtle

turtle = turtle.Turtle()

def drawTree(level, branchLength):
  if level > 0:
    turtle.forward(branchLength)
    turtle.left(67)
    drawTree(level-1, branchLength/1.41)
    
    turtle.right(67)
    drawTree(level-1, branchLength/1.41)
    
    turtle.right(67)
    drawTree(level-1, branchLength/1.41)
    
    turtle.right(67)
    drawTree(level-1, branchLength/1.41)
    
    turtle.right(67)
    drawTree(level-1, branchLength/1.41)

    turtle.left(201)
    drawTree(level-1, branchLength/1.41)
    turtle.back(branchLength)
    
  else:
    turtle.color("green")
    turtle.stamp()
    turtle.color("brown")
turtle.speed(0)
turtle.penup()
turtle.goto(0, -180)
turtle.left(90)
turtle.pendown()

turtle.color("brown")
turtle.width(3)
turtle.wrirte("67")
levels = input("How many levels do you want me to draw? ")
drawTree(int(levels), 120)