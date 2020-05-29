def posible(n, dislike):
    dic = {}
    for pairs in dislike:
        if pairs[0]in dic:
            dic[pairs[0]].add(pairs[1])
        else:
            dic[pairs[0]] = set([pairs[1]])
        if pairs[1]in dic:
            dic[pairs[1]].add(pairs[0])
        else:
            dic[pairs[1]] = set([pairs[0]])
    print(dic)
    seen = {}
    for i in range(1, n+1):
        print(i)
        if i not in seen:
            seen[i] = 0
            stack = [i]
            while stack:
                print(stack)
                a = stack.pop()
                print(a)
                if a in dic:
                    for b in dic[a]:
                        print(b)
                        if b in seen:
                            if seen[a] == seen[b]:
                                print(a,seen[a],b,seen[b])
                                return False
                        else:
                            seen[b] = (seen[a]+1) % 2
                            stack.append(b)
    print(seen)
    return True


n = 4
dislike = [[1, 2]
posible(n, dislike)
