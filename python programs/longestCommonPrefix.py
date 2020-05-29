def lcp(list):
    if len(list) == 0:
        return ""
    minlen = len(list[0])
    for i in range(len(list)):
        minlen = min(len(list[i]), minlen)
    print(minlen)
    lcp = ""
    i = 0
    while i < minlen:
        char = list[0][i]
        for j in range(1, len(list)):
            print(char,list[j][i])
            if list[j][i] != char:
                return(lcp)
        lcp = lcp+char
        i += 1
    return(lcp)
list = ["flower", "flow", "flight","fl"]
print(lcp(list))

