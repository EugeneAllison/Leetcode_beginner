def insertionSort(nums):
    for i in range(1, len(nums)):
        j = i - 1
        while j >= 0 and nums[j] > nums[j + 1]:
            nums[j], nums[j + 1] = nums[j + 1], nums[j]
            j -= 1
    return nums


nums = [5, 2, 4, 6, 1, 3]
nums = insertionSort(nums)
print(nums)
