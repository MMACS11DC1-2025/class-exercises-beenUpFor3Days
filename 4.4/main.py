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
    leftCalls = drawTree(t, level - 1, branchLength / 1.67)
    t.right(21)

    t.right(21)
    rightCalls = drawTree(t, level - 1, branchLength / 1.67)
    t.left(21)

    t.backward(branchLength)
    return 1 + leftCalls + rightCalls
  else:
    t.pencolor(colour2)
    t.dot(10)
    t.pencolor(colour1)
    return 1 
    
pen.speed(0)
pen.penup()
pen.goto(0, -180)
pen.left(90)
pen.pendown()

levels = int(input("How many levels do you want me to draw. (default is 3) ") or SETTINGS["levels"])
branchLength = float(input("How long do you want each branch to be. (default is 67.41) ") or SETTINGS["branchLength"])

if levels < 1:
  levels = 1
elif levels >8:
  levels = 8
  
if branchLength < 8:
  branchLength = 8
elif branchLength >67:
  branchLength = 67
  

colour1 = input("What colour do you want your branch to be. (default is brown) ") or SETTINGS["branchColour"]
colour2 = input("What colour do you want the leaves to be. (default is green) ") or SETTINGS["leafColour"]

totalCalls = drawTree(pen, levels, branchLength)

print("Total recursive calls is", totalCalls)


pen.hideturtle()
turtle.done()
