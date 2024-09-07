class Solution:
    def __init__(self):
        self.res = float('inf')

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        child = defaultdict(list)
        i = 0
        q = collections.deque([beginWord])
        if beginWord in wordList:
            wordList.remove(beginWord)

        while q:
            curr = q.popleft()
            i = 0
            while i < len(wordList):
                j = 0
                changes = 0
                while changes < 2 and j < len(curr):
                    if curr[j] != wordList[i][j]:
                        changes += 1
                    j += 1
                if changes < 2:
                    child[curr].append(wordList[i])
                    q.append(wordList[i])
                    wordList.pop(i)
                else:
                    i += 1
        
        visited = set()

        def dfs(iteration, word):
            if word == endWord:
                self.res = min(self.res, iteration)
                return
            
            if word not in child:
                return
            
            for c in child[word]:
                if c not in visited:
                    dfs(iteration + 1, c)

        dfs(1, beginWord)
        return self.res if self.res != float('inf') else 0