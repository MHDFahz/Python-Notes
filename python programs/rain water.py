def trap(height):
    print(height)
    result = 0
    l, r = 0, len(height)-1
    print(l, r)
    leftmax, rightmax = 0, 0
    while l < r:
        leftmax = max(leftmax, height[l])
        rightmax = max(rightmax, height[r])

        if leftmax <= rightmax:
            result += leftmax-height[l]
            l += 1
        else:
            result += rightmax-height[r]
            r -= 1
    return result


print(trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
