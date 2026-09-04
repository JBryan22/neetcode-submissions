class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = defaultdict(list)
        degreeCount = [0] * numCourses

        for crs, pre in prerequisites:
            adjList[pre].append(crs)
            degreeCount[crs] += 1
        
        queue = deque()

        for crs in range(numCourses):
            if degreeCount[crs] == 0:
                queue.append(crs)
        
        coursesTaken = 0
        while queue:
            crs = queue.popleft()
            coursesTaken += 1
            
            for nextCourse in adjList[crs]:
                degreeCount[nextCourse] -= 1
                if degreeCount[nextCourse] == 0:
                    queue.append(nextCourse)
                    
        return coursesTaken == numCourses