pos = -1


def search(lists, n):
    print(lists)
    l = 0
    u = len(lists)
    while l <= u:
        mid = (l+u)//2
        if lists[mid] == n:
            globals()['pos'] = mid
            return True
        else:
            if lists[mid] < n:
                l = mid+1
            else:
                u = mid-1
    return False


lists = [1, 7, 8, 9, 10, 15, 45, 99]
n = 15
if search(lists, n):
    print("Found", pos+1)
else:
    print("Not Found")
