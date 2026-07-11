class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        #check len of shortest before returning, if it isnt of len n then return -1
        shortest = {}
        adjList = {}

        for i in range(1, n + 1):
            adjList[i] = []

        for src, dest, time in times:
            adjList[src].append((dest, time))

        minHeap = [(0, k)]

        while minHeap:
            time, node = heapq.heappop(minHeap)
            # dont overwrite nodes in shortest 
            # - if it is already in shortest then we already found the shortest path there due to greedy choices
            if node in shortest:
                continue
            shortest[node] = time

            for d, t in adjList[node]:
                heapq.heappush(minHeap, (t + time, d))

        if len(shortest) == n:
            return max(shortest.values())
        else:
            return -1

