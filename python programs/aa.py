def check(strg):
    for i in strg:
        if i in openl:
            stack.append(i)
        elif i in closel:
            pos = closel.index(i)
            if((len(stack) > 0) and openl[pos] == stack[len(stack)-1]):
                a = stack.pop()
            else:
                return "not"
    if(len(stack) == 0):
        return "yes"
    else:
        return "not"


strg = ")({}"
openl = ['(', '{', '[']
closel = [')', '}', ']']
stack = []
print(check(strg))
