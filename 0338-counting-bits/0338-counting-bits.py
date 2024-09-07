class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0] * (n + 1)
        for i in range(n + 1):
            num = bin(i)
            for j in num[2:]:
                if j == '1':
                    res[i] += 1 
        return res
