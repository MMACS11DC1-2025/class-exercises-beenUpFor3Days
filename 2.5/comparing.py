"""
Create a program that uses counting and comparison operators (< > <= >=).
You must use the class' datafile, 'responses.csv' and analyze it
    to make at least 2 interesting observations.
You must use user input to add interactivity to the program.
You must design your algorithm in English first, then translate it to Python code.
Test as you go! Describe in your comments what steps you took to test your code.


lead responces 
askes for 2 names
finds the names
take favourite number pet and sport
compairs numbers
prints results
compairs pets and sports 
prints results
"""

#opens file and reads it
file = open("2.4/responses.csv")
file.readline()
data = file.readlines()

#asks for name and sets variables
print("This code finds 2 people's favoutite sport and pet")
personA = input("First person's name ").lower()
Asport = None
Apet = None
Ano = None

#for loop going and finding the name and taking the data from that line
for line in data:
    line = line.strip()
    info = line.split(",")
    name = info[1].strip().lower() #ran to see if it could open the responses

#if statemnt taking the favourite digit sport and pet of person
    if name == personA:
        Ano = float(info[2].strip())
        Asport = info[5].strip()
        Apet = info[3].strip() #made it print just this to test if it would work
        break

#same thing as personA but with the seccond name
personB = input("Second person's name ").lower()
Bsport = None
Bpet = None
Bno = None

for line in data:
    line = line.strip()
    info = line.split(",")
    name = info[1].strip().lower()

    if name == personB:
        Bno = float(info[2].strip())
        Bsport = info[5].strip()
        Bpet = info[3].strip()
        break

#sees whoes number is bigger with an if statement
if None in (Bno, Ano):
    print("Try again names are invalid")

elif Bno < Ano:
    print(personA + "'s favourite digit is bigger than "+ personB +"'s")

elif None in (Bno, Ano):
    print("Try again names are invalid")

else:
    print(personB + "and" + personA + " favorite digit is both" + Ano)

#if statement seeing if the 2 people have a pet or sport in common
if None in (Asport, Apet, Bpet, Bsport):
    print("")

elif Asport == Bsport and Apet == Bpet:
    print("Both people like the same sport: " + Asport+ " and same pet: " + Apet)

elif Asport == Bsport:
    print("Both people like the same sport: " + Asport)

elif Apet == Bpet:
    print("Both people like the same pet: " + Bpet)

else:
    print("Both people dont have the same pet or play the same sport")#tried each if statement

"""This code finds 2 people's favoutite sport and pet
First person's name daichi lee
Second person's name theo shim
daichi lee's favourite digit is bigger than theo shim's
Both people like the same pet: Cat"""