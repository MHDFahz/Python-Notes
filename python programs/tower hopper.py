def is_hoppable(towers):
    if not towers:
        return False
    height = 0
    target = len(towers)
    print("length of tower=",target)
    for i in range(len(towers)):
        height = max(height, towers[i])
        print(height)
        if target <= height + i:
            print(f"if{target}<={height+1}")
            return True
        height -= 1
        print(height)
        if height < 0:
            return False
    return True


def test_towers():
    print (is_hoppable([1]))
    print (is_hoppable([]))
    print (is_hoppable([1, 0, 1]))
    print (is_hoppable([4, 10, 3, 2, 4, 0, 0, 0, 0, 0]))
    print (is_hoppable([3, 2, 1, 0, 0, 3]))
    print (is_hoppable([4, 2, 0, 0, 2, 0]))
    print (is_hoppable([4, 2, 0, 0, 1, 0]))
    print (is_hoppable([4, 2, 0, 0, 1, 1]))


test_towers()
