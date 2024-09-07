class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        adj = {}

        for equation in equations:
            if equation[0] not in adj:
                    adj[equation[0]] = set()
            if equation[3] not in adj:
                adj[equation[3]] = set()

            if equation[1:3] == '==':
                adj[equation[0]].add(equation[3])
                adj[equation[3]].add(equation[0])
            elif equation[0] == equation[3]:
                return False
            else:
                if equation[3] in adj[equation[0]]:
                    adj[equation[0]].remove(equation[3])
                    adj[equation[3]].remove(equation[0])
        
        q = collections.deque()

        def bfs(letter, target, equal):
            visited = set()
            q.append(letter)
            while q:
                curr = q.popleft()
                if curr in visited:
                    continue
                visited.add(curr)

                if curr == target:
                    if not equal:
                        return False
                    return True
                
                for node in adj[curr]:
                    if node not in visited:
                        q.append(node)
            
            return True if not equal else False
        
        for equation in equations:
            q.clear()
            equals = False
            if equation[1:3] == '==':
                equals = True

            if not bfs(equation[0], equation[3], equals):
                return False

        return True
                