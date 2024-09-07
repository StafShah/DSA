class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        charMap = {')': '(', ']': '[', '}': '{', '(': ' ', '[': ' ', '{': ' '}

        for char in s:
            
            if len(st) > 0:
                if st[-1] == charMap[char]:
                    st.pop()
                elif charMap[st[-1]] == ' ' and charMap[char] != ' ':
                    return False
                else:
                    st.append(char)
            else:
                st.append(char)
        
        return True if len(st) == 0 else False
