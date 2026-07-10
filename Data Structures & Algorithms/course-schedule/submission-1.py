class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        degreeCounts = [0] * numCourses

        adjList = [[] for i in range(numCourses)]

        for course, prereq in prerequisites:
            adjList[course].append(prereq)
            degreeCounts[prereq] += 1
        
        queue = deque()

        for crsNum in range(numCourses):
            if degreeCounts[crsNum] == 0:
                queue.append(crsNum)
        
        coursesTaken = 0

        while queue:
            crs = queue.popleft()
            coursesTaken += 1

            for prereq in adjList[crs]:
                degreeCounts[prereq] -= 1
                if degreeCounts[prereq] == 0:
                    queue.append(prereq)

        return coursesTaken == numCourses