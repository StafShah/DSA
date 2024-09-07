class Solution:
    def __init__(self):
        self.counter = 0

    def climbStairs(self, n: int) -> int:
        m = {}
        for i in range(n, -1, -1):
            if i == n or i == n - 1:
                m[i] = 1
            else:
                m[i] = m[i + 1] + m[i + 2]
        
        return m[0]