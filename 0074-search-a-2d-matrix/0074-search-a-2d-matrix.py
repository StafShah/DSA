class Solution:
    def binarySearch(self, l, target):
        lo, hi = 0, len(l) - 1

        while lo <= hi:
            mid = hi // 2
            if l[mid] > target:
                return self.binarySearch(l[:mid], target)
            elif l[mid] < target:
                return self.binarySearch(l[mid + 1:], target)
            else:
                return True
        
        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lo, hi = 0, len(matrix) - 1

        while lo <= hi:
            mid = hi // 2
            if matrix[mid][0] > target:
                return self.searchMatrix(matrix[:mid], target)
            elif matrix[mid][-1] < target:
                return self.searchMatrix(matrix[mid + 1:], target)
            else:
                return self.binarySearch(matrix[mid], target)
        
        return False