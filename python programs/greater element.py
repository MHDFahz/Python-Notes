l = [13, 7, 6, 12, 10]
r = [-1 for i in range(len(l))]
#r=[]

stack = [0 for i in range(len(l))]
stack[0]=l[0]
index=0
for i in l:
    print(i<=stack[index-1])
    if(i <= stack[index]):
        stack[index] = i
        index+=1
print(stack)