class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjList = defaultdict(list)
        degreeCount = [0] * numCourses

        for crs, prereq in prerequisites:
            adjList[prereq].append(crs)
            degreeCount[crs] += 1

        queue = deque()

        for i in range(len(degreeCount)):
            if degreeCount[i] == 0:
                queue.append(i)
        
        res = []
        while queue:
            crs = queue.popleft()

            res.append(crs)

            for nextCourse in adjList[crs]:
                degreeCount[nextCourse] -= 1
                if degreeCount[nextCourse] == 0:
                    queue.append(nextCourse)
            
        return res