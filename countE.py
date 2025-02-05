noE = ["A", "b", "C", "c", "z"]
yesE = ["e", "M","z", "E", "e", "q", "E", "E"]


def findE(arr):
    counter = {"E":0, "e":0}

    for letter in arr:
        if letter in counter:
            counter[letter] += 1

    if counter["E"] == 0 and counter["e"] == 0:
        print("\nThere's no \"E\" or \"e\" letter")
    else:
        print(f"{counter["E"]} {"letters" if counter["E"] > 1 else "letter"} E.") 
        print(f"{counter["e"]} {"letters" if counter["e"] > 1 else "letter"} e.")

findE(yesE)
findE(noE)





