The program askes for the levels branch length branch colour and leaf colour then draws a tree with your inputs 


the recursive function sees if level is > than 0
if it is then it draws one branchg
it does it 2 times one for the left and right side
once level is 0 then it draws a dot
each time it adds one to the calls left and calls right to add up to total call

run code
answer the questions it gives you
code makes the tree
console desplayes the total recursive calls

if you have more levels it will be more detailed tree
longer branch is taller tree
diffrent colour will give the tree a diffrent deisgn 

not enough levles will make it not very tree like
too big will take way too long and a big clump
3-8 is a good range

test case one:

How many levels do you want me to draw. (default is 3)  5
How long do you want each branch to be. (default is 67.41)  100
What colour do you want your branch to be. (default is brown)  pink
What colour do you want the leaves to be. (default is green)  blue
('total recursive calls is', 63)

2:
How many levels do you want me to draw. (default is 3)  8
How long do you want each branch to be. (default is 67.41)  67
What colour do you want your branch to be. (default is brown)  black
What colour do you want the leaves to be. (default is green)  green
('total recursive calls is', 511)

i tried to see what the min and max for the tree
i counted and made sure the recursive call was correct
i made it so there is a defualt case
