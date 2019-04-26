

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # exception
        if len(matrix)==0:
            return False
        if len(matrix[0]) == 0:
            return False


        # binary search on first element
        low = 0
        high = len(matrix) -1
        while(low+1<high):
            mid = int((low+high)/2)
            if matrix[mid][0] > target:
                high = mid
            elif matrix[mid][0] <target:
                low = mid
            else:
                return True

        index = high if matrix[high][0] <= target else low


        # binary search on the row we obtain
        left = 0
        right = len(matrix[index]) -1

        while(left+1<right):
            mid = int((left+right)/2)
            if matrix[index][mid] > target:
                right = mid
            elif matrix[index][mid] < target:
                left = mid
            else:
                return True

        if matrix[index][left] == target:
            return True
        if matrix[index][right] == target:
            return True
        return False
        
