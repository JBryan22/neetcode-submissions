class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freqs = [0] * 26
        
        for t in tasks:
            freqs[ord(t) - ord('A')] += 1

        freqs = [-f for f in freqs if f > 0]

        heapq.heapify(freqs)

        queue = deque()
        time = 0

        while freqs or queue:
            time += 1
            if freqs:
                curr = heapq.heappop(freqs)
                curr += 1
                if curr < 0:
                    queue.append((time + n, curr))
            if queue and queue[0][0] <= time:
                _, curr = queue.popleft()
                heapq.heappush(freqs, curr)
        
        return time
            