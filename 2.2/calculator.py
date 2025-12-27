"""
Machines are good at crunching numbers - faster and more accurately than most 
humans! Create a small program that calculates something useful to you 
(making you smile is useful). It should take user input, at use at least one of the 
number operators we saw in class: + / * . You may modify one of your previous 
exercises to include calculations, if you wish.

Remember to design your algorithm in English first, then translate it to Python 
code. Test as you go!
"""

print("this calculates + and - of 2 numbers")
print("enter first number")
numberOne = input()
print("enter seccond number")
numberTwo = input()
print("chose + or -")
operation = input()

if operation == "-":
    calc = float(numberOne) - float(numberTwo)
    print(str(calc))
elif operation == "+":
    calc = float(numberOne) + float(numberTwo)
    print(str(calc))
else:
    print("invalid")