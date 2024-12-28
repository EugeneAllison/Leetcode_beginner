# Python program for implementation of Quicksort Sort

# This implementation utilizes pivot as the last element in the nums list
# It has a pointer to keep track of the elements smaller than the pivot
# At the very end of partition() function, the pointer is swapped with the pivot
# to come up with a "sorted" nums relative to the pivot


# Function to find the partition position
def partition(array, low, high):

    # choose the rightmost element as pivot
    pivot = array[high]

    # pointer for greater element
    i = low - 1

    # traverse through all elements
    # compare each element with pivot
    for j in range(low, high):
        if array[j] <= pivot:

            # If element smaller than pivot is found
            # swap it with the greater element pointed by i
            i = i + 1

            # Swapping element at i with element at j
            (array[i], array[j]) = (array[j], array[i])

    # Swap the pivot element with the greater element specified by i
    (array[i + 1], array[high]) = (array[high], array[i + 1])

    # Return the position from where partition is done
    return i + 1


# function to perform quicksort


def quickSort(array, low, high):
    if low < high:

        # Find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        pi = partition(array, low, high)

        # Recursive call on the left of pivot
        quickSort(array, low, pi - 1)

        # Recursive call on the right of pivot
        quickSort(array, pi + 1, high)


data = [1, 7, 4, 1, 10, 9, -2]
print("Unsorted Array")
print(data)

size = len(data)

quickSort(data, 0, size - 1)

print("Sorted Array in Ascending Order:")
print(data)


# Approach 2: Quicksort using list comprehension


def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left = [x for x in arr[1:] if x < pivot]
        right = [x for x in arr[1:] if x >= pivot]
        return quicksort(left) + [pivot] + quicksort(right)


# Example usage
arr = [1, 7, 4, 1, 10, 9, -2]
sorted_arr = quicksort(arr)
print("Sorted Array in Ascending Order:")
print(sorted_arr)


def quicksort(nums):
    if len(nums) <= 1:  # 如果数组长度小于等于1，直接返回
        return nums

    pivot = nums[0]  # 选择第一个元素作为枢轴
    l, r = 1, len(nums) - 1  # 初始化左、右指针

    while l <= r:  # 当左指针小于等于右指针时
        while l <= r and nums[r] >= pivot:  # 找到右侧第一个小于枢轴的元素
            r -= 1
        while l <= r and nums[l] < pivot:  # 找到左侧第一个大于等于枢轴的元素
            l += 1
        if l < r:  # 如果左指针仍小于右指针，交换它们
            nums[l], nums[r] = nums[r], nums[l]

    nums[0], nums[r] = nums[r], nums[0]  # 将枢轴放到正确的位置

    # 递归地对左右两部分进行排序
    left_sorted = quicksort(nums[:r])
    right_sorted = quicksort(nums[r + 1 :])

    return left_sorted + [nums[r]] + right_sorted


# 示例使用
nums = [3, 6, 8, 10, 1, 2, 1]
sorted_nums = quicksort(nums)
print(sorted_nums)
