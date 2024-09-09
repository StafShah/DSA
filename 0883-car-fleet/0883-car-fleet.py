class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        j = len(position) - 1

        for i in range(len(position)):
            stack.append((position[i], speed[i]))
        
        stack.sort()

        while j > 0:
            k = j - 1
            while k >= 0:
                if (target - stack[k][0]) / stack[k][1] <= (target - stack[j][0]) / stack[j][1]:
                    stack.pop(k)
                    k -= 1
                    j -= 1
                else:
                    break
            j -= 1
        
        return len(stack)
