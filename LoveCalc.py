print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

trueCount=0
loveCount=0
newName1 = name1.lower()
newName2 = name2.lower()
if(newName1.count("t")):
    trueCount+=newName1.count("t")
if(newName2.count("t")):
    trueCount+=newName2.count("t")
if(newName1.count("r")):
    trueCount+=newName1.count("r")
if(newName2.count("r")):
    trueCount+=newName2.count("r")
if(newName1.count("u")):
    trueCount+=newName1.count("u")
if(newName2.count("u")):
    trueCount+=newName2.count("u")
if(newName1.count("e")):
    trueCount+=newName1.count("e")
if(newName2.count("e")):
    trueCount+=newName2.count("e")

if(newName1.count("l")):
    loveCount+=newName1.count("l")
if(newName2.count("l")):
    loveCount+=newName2.count("l")
if(newName1.count("o")):
    loveCount+=newName1.count("o")
if(newName2.count("o")):
    loveCount+=newName2.count("o")
if(newName1.count("v")):
    loveCount+=newName1.count("v")
if(newName2.count("v")):
    loveCount+=newName2.count("v")
if(newName1.count("e")):
    loveCount+=newName1.count("e")
if(newName2.count("e")):
    loveCount+=newName2.count("e")
newTrue=str(trueCount)
newLove=str(loveCount)
score=newTrue+newLove
newScore=int(score)
if newScore < 10 or newScore >90:
    print(f"Your score is {newScore}, you go together like coke and mentos.")
elif newScore >40 and newScore < 50:
    print(f"Your score is {newScore}, you are alright together.")
else:
    print(f"Your score is {newScore}.")
