T = int(input())
ls=[]
for x in range(T):
    ls.append([])
    f=int(input())
    for y in range(f):
        ls[x].append(int(input()))
for x in range(T):
    car = ls[x]
    branch=[]
    current=1
    while True:
        if len(car) > 0:
            if car[-1]==current:
                current+=1
                car.pop()
            elif len(branch)>0:
                if branch[-1]==current:
                    current+=1
                    branch.pop()
                else:
                    branch.append(car.pop())
            else:
                branch.append(car.pop())
        elif len(branch) > 0:
            if branch[-1]==current:
                current+=1
                branch.pop()
            else:
                print('N')
                break
        else:
            print("Y")
            break