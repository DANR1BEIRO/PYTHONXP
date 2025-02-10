""" 
Your task is to make all words which are 3 characters 
or less into capitals. You should also remove any vowels 
from 'long' (4 characters or more) words.

For example:

"The quick brown fox jumps over the lazy dog"

Should become:

"THE qck brwn FOX jmps vr THE lzy DOG"

For the purposes of this kata, mid-word punctuation counts 
towards the character limit of a word.

e.g: "it's / I'm" should become: "t's / I'M
"""

def small_words(string):
    words = string.split()
    vowels = "aeiouAEIOU"
    result = []

    for word in words:
        if len(word) <= 3:
            result.append(word.upper())

        else:
            no_vowel = "".join([letter for letter in word if letter not in vowels])
            result.append(no_vowel)
            
    return " ".join(result)

print(small_words("The quick brown fox jumps over the lazy dog"))