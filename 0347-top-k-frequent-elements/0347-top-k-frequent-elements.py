class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numsDict = defaultdict(lambda: 0)
        arr = []

        for num in nums:
            numsDict[num] += 1
            if num not in arr:
                if len(arr) < k:
                    arr.append(num)
                    print(num, "appended")
                else:
                    minNum, i = 100000, 0
                    idx = 0
                    while i < k:
                        if minNum > numsDict[arr[i]]:
                            minNum = numsDict[arr[i]]
                            idx = i
                        i += 1
                    if numsDict[num] > minNum:
                        arr[idx] = num
        
        return arr