class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        print(bin(n))
        for i in bin(n)[2:]:
            res += int(i) % 2
        return res