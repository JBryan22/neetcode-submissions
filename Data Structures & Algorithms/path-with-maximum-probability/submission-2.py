class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        adjList = defaultdict(list)

        for i in range(len(edges)):
            s, e = edges[i]
            adjList[s].append((e, succProb[i]))
            adjList[e].append((s, succProb[i]))

        maxH = []
        maxProbs = [0] * n
        for node, prob in adjList[start_node]:
            heapq.heappush_max(maxH, (1 * prob, node))
            maxProbs[node] = 1 * prob
        
        while maxH:
            p, node = heapq.heappop_max(maxH)

            if node == end_node:
                return p
            
            for n, prob in adjList[node]:
                if maxProbs[n] < p * prob:
                    heapq.heappush_max(maxH, (p * prob, n))

        return 0
        