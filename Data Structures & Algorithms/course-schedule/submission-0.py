class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites:
            return True
        
        visited = set()
        adjList = {}

        for clss, prereq in prerequisites:
            if clss not in adjList:
                adjList[clss] = [prereq]
            else:
                adjList[clss].append(prereq)

        visiting = set()

        def dfs(clss):
            if clss in visiting:
                return False
            if clss not in adjList or adjList[clss] == [] or clss in visited:
                return True
            
            visiting.add(clss)

            for prereq in adjList[clss]:
                if not dfs(prereq):
                    return False
            visiting.remove(clss)
            visited.add(clss)
            return True

        for clss in adjList:
            if not dfs(clss):
                return False
        
        return True