noE = ["A", "b", "C", "c", "z"]
yesE = ["e", "M","z", "E", "e", "q"]

def findE(arr):
    counter = {"E":0, "e":0}

    for letter in arr:
        counter[letter] = 1

    if counter["E"] == 0 and counter["e"] == 0:
        print("\nThere's no \"E\" or \"e\" letter")
    else:
        print(f"{counter["E"]} letters E and {counter["e"]} letters e")

findE(yesE)
findE(noE)



