import math

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if not token[-1].isnumeric():
                num2 = stack.pop()
                num1 = stack.pop()
                ans = eval(num1 + ' ' + token + ' ' + num2)
                if ans > 0:
                    stack.append(str(math.floor(ans)))
                else:
                    stack.append(str(math.ceil(ans)))
            else:
                stack.append(token)
        
        return int(stack[0])