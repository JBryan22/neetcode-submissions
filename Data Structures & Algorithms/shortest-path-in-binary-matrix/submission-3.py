class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        N = len(grid)
        if grid[0][0] or grid[N - 1][N - 1]:
            return -1
        if N == 1:
            return 1

        directions = [[1, 0], [-1, 0], [0, 1], [0, -1], [-1, -1], [-1, 1], [1, -1], [1, 1]]
        queue = deque([(0,0)])
        q2 = deque([(N - 1, N - 1)])
        grid[0][0] = -1
        grid[N - 1][N - 1] = -2
        length = 2
        start, end = -1, -2

        while queue and q2:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for d in directions:
                    dr, dc = d

                    if r + dr < 0 or c + dc < 0 or r + dr >= N or c + dc >= N:
                        continue
                    if grid[r + dr][c + dc] == end:
                        return length
                    if grid[r + dr][c + dc] == 0:
                        queue.append((r + dr, c + dc))
                        grid[r + dr][c + dc] = start

            length += 1
            queue, q2 = q2, queue
            start, end = end, start
        
        return -1