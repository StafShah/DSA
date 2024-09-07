class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
        child = defaultdict(list)
        in_degree = [0] * numCourses

        for course, prereq in prerequisites:
            in_degree[course] += 1
            child[prereq].append(course)
        
        q = collections.deque()

        for i in range(len(in_degree)):
            if in_degree[i] == 0:
                q.append(i)
        
        while q:
            curr = q.popleft()
            res.append(curr)

            for c in child[curr]:
                in_degree[c] -= 1
                if in_degree[c] == 0:
                    q.append(c)
        
        return res if sum(in_degree) == 0 else []