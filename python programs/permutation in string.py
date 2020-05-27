def check(string, s1):
    temp = list(s1)
    string = list(string)
    count = 0
    for i in string:
        if i in temp:
            temp.pop(temp.index(i))
            count += 1
        else:
            break
    if count == len(s1):
        return True


s1 = input()
s2 = input()
for i in range(len(s2)-(len(s1)-1)):
    if check(s2[i:i+len(s1)], s1):
        print(i+1, "-", s2[i:i+len(s1)])
