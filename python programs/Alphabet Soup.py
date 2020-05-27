def alphabetSoup(string):
    li = sorted(list(string))
    print(li)
    lower = sorted(list(string.lower()))
    print(lower)
    caps = []
    new = ""
    for char in li:
        if char.isupper():
            caps.append(char)
    print(caps)
    for letter in lower:
        if caps.count(letter.upper()) != 0:
            new += letter.upper()
            caps.pop(caps.index(letter.upper()))
        else:
            new += letter
    return new


string = "ElephAAant"
print(alphabetSoup(string))
