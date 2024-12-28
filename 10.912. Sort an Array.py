class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(arr, l, m, r):
            leftArray = arr[l : m + 1]
            rightArray = arr[m + 1 : r + 1]
            # 注意是冒号不是逗号
            i, j = 0, 0
            k = l
            while i < len(leftArray) and j < len(rightArray):
                if leftArray[i] <= rightArray[j]:
                    arr[k] = leftArray[i]
                    i += 1
                else:
                    arr[k] = rightArray[j]
                    j += 1
                k += 1

            while i < len(leftArray):
                arr[k] = leftArray[i]
                i += 1
                k += 1
            while j < len(rightArray):
                arr[k] = rightArray[j]
                j += 1
                k += 1
            return arr

        def mergeSort(arr, l, r):
            if l == r:
                return arr
            m = (l + r) // 2
            mergeSort(arr, l, m)
            mergeSort(arr, m + 1, r)
            merge(arr, l, m, r)
            return arr

        return mergeSort(nums, 0, len(nums) - 1)
