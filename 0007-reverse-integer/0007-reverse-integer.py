from math import *

class Solution(object):
    def reverse(self, x):
        nums = [str(a) for a in str(x)]
        
        if len(nums) == 1:
            return x
        
        nums.reverse()
        last_idx = len(nums)-1
    
        if nums[last_idx] == '-':
            nums.insert(0, nums.pop(last_idx))
        result = int(''.join(nums))
    
    
        if result > pow(2, 31) or result < pow(2, 31) * -1:
            return 0
        return result
#         nums = [str(a) for a in str(x)]
#         idx = len(nums) - 1
#         reversed_nums = []
        
#         if len(nums) == 1:
#             return nums[0]
        
#         while idx >= 0:
#             reverse_num = nums[idx]
#             if nums[idx] == '-':
#                 reversed_nums.insert(0, '-')
#             else:
#                 reversed_nums.append(reverse_num)
#             idx -= 1

#         result = int(''.join(reversed_nums))
#         if result > pow(2, 31) or result < pow(2, 31) * -1:
#             return 0
#         return result