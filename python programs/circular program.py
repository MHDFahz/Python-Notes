def getTour(petrol, distance, n):
    add = 0
    start = 0
    diff = 0
    for i in range(0, n):
        add = add+petrol[i]-distance[i]
        print(add)
        if(add < 0):
            start = i+1
            print(start)
            diff += add
            print(diff)
            add = 0
    if add+diff < 0:
        return start+1
    else:
        return -1


petrol = [5, 6, 7, 8, 6, 4]
distance = [6, 7, 4, 10, 6,5]
val = getTour(petrol, distance, 4)
print(val)
