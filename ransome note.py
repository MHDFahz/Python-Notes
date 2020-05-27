from collections import Counter
string = input()
string1 = input()
string = Counter(string)
li = list(string)
new = []
string1 = Counter(string1)
for i in range(len(string1)):
    if string1[li[i]] >= string[li[i]]:
        new.append(li[i])
if new == li:
    print("same")
else:
    print("Not")
