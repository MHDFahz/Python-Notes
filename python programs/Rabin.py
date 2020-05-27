text = "aabacaadaba"
find = "abac"
for i in range(len(text)-2):
    temp = text[i]+text[i+1]+text[i+2]
    if find == temp:
        print(i)

