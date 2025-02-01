def firstNonRepeatingCharacter(string):
    count = {}
    for char in string:
        count[char] = count.get(char, 0) + 1
    
    for char in string:
        if count[char] == 1:
            return char
        
    return "_"

print(firstNonRepeatingCharacter("aabbcc"))      