# 二分查找不一定非要输入一个数组，只要给定一个有序范围就可以应用。
# 通过二分查找法在一个给定范围内查找目标值 10。如果找到目标值，返回其位置；如果找不到，返回 -1。
def binarySearch(low, high):
    while low <= high:
        mid = (low + high) // 2
        if isCorrect(mid) > 0:
            high = mid - 1
        elif isCorrect(mid) < 0:
            low = mid + 1
        else:
            return mid
    
    return -1


def isCorrect(number):
    if number > 10:
        return 1
    elif number < 10:
        return -1
    else:
        return 0
