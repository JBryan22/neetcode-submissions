class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {}

        def dfs(total:int):
            if total > n:
                return 0
            if total == n:
                return 1
            if total in cache:
                return cache[total]
            
            res = dfs(total + 1) + dfs(total + 2)
            cache[total] = res
            return res

        return dfs(0)

        