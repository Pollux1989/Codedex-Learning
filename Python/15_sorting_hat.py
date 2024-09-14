print("#####--------15. sorting hat--------#####")

Gryffindor = 0
Ravenclaw = 0
Hufflepuff = 0
Slytherin = 0

question_1 = int(input("Do you like  1-Dawn or 2-Dusk?:  "))

if question_1 == 1:
    Gryffindor += 1
    Ravenclaw += 1
elif question_1 == 2:
    Hufflepuff += 1
    Slytherin += 1
else:
    print("Wrong Input1")

question_2 = int(input("When Im dead, I want people to remember me as: 1-The Good, 2-The Great, 3-The Wise, 4-The Bold: "))

if question_2 == 1:
    Hufflepuff += 2
elif question_2 == 2:
    Slytherin += 2
elif question_2 == 3:
    Ravenclaw += 2
elif question_2 == 4:
    Gryffindor += 2
else:
    print("Wrong Input2")

question_3 = int(input("Which kind of instrument most pleases your ear? 1-The Violin, 2-The Trumpet, 3-The Piano, 4-The Drum: "))

if question_3 == 1:
    Slytherin += 4
elif question_3 == 2:
    Hufflepuff += 4
elif question_3 == 3:
    Ravenclaw += 4
elif question_3 == 4:
    Gryffindor += 4
else:
    print("Wrong Input3")

if Gryffindor >= Ravenclaw and Gryffindor >= Hufflepuff and Gryffindor >= Slytherin:
    print("you are a Lion 🦁")
elif Ravenclaw >=Gryffindor and Ravenclaw >=Hufflepuff and Ravenclaw >= Slytherin:
    print("You are a Parrot 🦜")
elif Hufflepuff >= Gryffindor and Hufflepuff >= Ravenclaw and Hufflepuff>=Slytherin:
    print("You are a Possum 🐀")
else:
    print("You are Python 🐍")








