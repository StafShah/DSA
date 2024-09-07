class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        nextCourse = {}
        in_degree = [0] * numCourses

        for course, prereq in prerequisites:
            if prereq == course:
                return False

            if prereq not in nextCourse:
                nextCourse[prereq] = [course]
            else:
                nextCourse[prereq].append(course)
            in_degree[course] += 1
        
        q = collections.deque()
        visited = set()
        
        for i in range(len(in_degree)):
            if in_degree[i] == 0:
                q.append(i)
        
        if len(q) == 0 and len(in_degree) > 0:
            return False

        while q:
            course = q.popleft()
            visited.add(course)

            if course in nextCourse:
                for nextC in nextCourse[course]:
                    if nextC in visited:
                        return False
                    in_degree[nextC] -= 1
                    if in_degree[nextC] == 0:
                        q.append(nextC)
        
        return True if len(visited) == numCourses else False