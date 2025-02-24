a = ["A", "a", "B", "C", "C", "a"]

def countLetter(arr):
    count = {}

    for letter in arr:
        count[letter] = count.get(letter, 0) + 1

    print(f"Counter: {count}")

countLetter(a)