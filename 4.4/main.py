#recursive tree
#uses turtle and users inputs to make a tree
#prints tree and total recursive calls
import turtle

#make a dictionary with variables in it
SETTINGS = {
    "branchLength": 67.41,
    "levels": 3,
    "branchColour": "brown",
    "leafColour": "green"
}
#make pen into turtle.turle and make the pen width
pen = turtle.Turtle()
pen.width(4.1)

#recursicve function that draws the tree
#t is the turtle 
#levels is how many to draw
#branch length is the starting length of the branch

def drawTree(t, level, branchLength, colour1, colour2):
  calls = 1  # counts this call
  if level > 0:
    t.pencolor(colour1)#changes pen colour
    t.forward(branchLength)#uses user input for first length

    t.left(21)
    #has 2 return values
    leftCalls, leftLeaves = drawTree(t, level - 1, branchLength / 1.67, colour1, colour2)

    t.right(42)
    #two return values from the right branch
    rightCalls, rightLeaves = drawTree(t, level - 1, branchLength / 1.67, colour1, colour2)

    t.left(21)
    t.backward(branchLength)#goes back to original point

    return calls + leftCalls + rightCalls, leftLeaves + rightLeaves
  else:
    t.pencolor(colour2) 
    t.dot(10)
    t.pencolor(colour1)
    # CHANGE: base case returns (calls, 1 leaf)
    return calls, 1
    
pen.speed(0)#pen speed  
pen.penup()
pen.goto(0, -180)#starting point
pen.left(90)
pen.pendown()

#gets user input for amout of levels
levels = int(input("How many levels do you want me to draw. (default is 3) ") or SETTINGS["levels"])
#gets user input for branch length
branchLength = float(input("How long do you want each branch to be. (default is 67.41) ") or SETTINGS["branchLength"])

#if the inpout leves is too big it will cap it or too small
if levels < 1:
  levels = 1
elif levels >8:
  levels = 8
  
#make a minimum and max for branch length
if branchLength < 8:
  branchLength = 8
elif branchLength >100:
  branchLength = 100
  
#ask user for branch and leaf colour
colour1 = input("What colour do you want your branch to be. (default is brown) ") or SETTINGS["branchColour"]
colour2 = input("What colour do you want the leaves to be. (default is green) ") or SETTINGS["leafColour"]

#call recursive function
totalCalls, totalLeaves = drawTree(pen, levels, branchLength, colour1, colour2)
#print total recurvive calls
print("total recursive calls is", totalCalls)
print("total leaves is ", totalLeaves)
pen.hideturtle()#hides cyursor so you can just see the tree
turtle.done()
