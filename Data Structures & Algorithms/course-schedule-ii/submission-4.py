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
            
        coursesTaken = []
        while queue:
            degree = queue.popleft()

            for crs in adjList[degree]:
                degreeCount[crs] -= 1
                if degreeCount[crs] == 0:
                    queue.append(crs)
            
            coursesTaken.append(degree)
        
        if len(coursesTaken) == numCourses:
            return coursesTaken
        else:
            return []

                