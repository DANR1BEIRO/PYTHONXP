""" 
Return the number (count) of vowels in the given string.
We will consider a, e, i, o, u as vowels for this Kata (but not y).
The input string will only consist of lower case letters and/or spaces.
"""

def get_count(sentence):
    vowel = "aeiou"
    counter = 0
    
    for letter in sentence:
        if letter in vowel:
            counter += 1
    return counter

print(get_count("abracadabra"))


def getCount(string):
    return sum(1 for letter in string if letter in "aeiouAEIOU")

print(getCount("abracadabra"))
