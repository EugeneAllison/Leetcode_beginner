# 我自己写出来的：
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        top, bot = 0, ROWS - 1
        while top <= bot:
            midRow = (top + bot) // 2
            if target > matrix[midRow][COLS - 1]:  # 或者是matrix[row][-1]，是一样的
                top = midRow + 1
            elif target < matrix[midRow][0]:
                bot = midRow - 1
            else:
                # 不比最大的大，不比最小的小，正好落在这一行中间
                break

        l, r = 0, COLS - 1
        while l <= r:
            mid = (l + r) // 2
            if target > matrix[midRow][mid]:
                l = mid + 1
            elif target < matrix[midRow][mid]:
                r = mid - 1
            else:
                return True

        return False


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        top, bot = 0, ROWS - 1
        while top <= bot:
            row = (top + bot) // 2
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bot = row - 1
            else:
                break

        if not (top <= bot):
            return False
        row = (top + bot) // 2
        l, r = 0, COLS - 1
        while l <= r:
            m = (l + r) // 2
            if target > matrix[row][m]:
                l = m + 1
            elif target < matrix[row][m]:
                r = m - 1
            else:
                return True
        return False
