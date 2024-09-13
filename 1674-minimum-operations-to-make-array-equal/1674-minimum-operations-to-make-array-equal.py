class Solution:
    def minOperations(self, n: int) -> int:
        ops = 0
        if n == 1:
            return ops
        
        curr = 1 if n % 2 == 0 else 0
        mid = n // 2 - 1 if curr else n // 2
        print(curr, mid)
            
        for i in range(mid, -1, -1):
            ops += curr
            curr += 2

        return ops
