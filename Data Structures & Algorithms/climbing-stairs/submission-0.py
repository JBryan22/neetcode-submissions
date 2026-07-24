class Solution:
    def climbStairs(self, n: int) -> int:
        res = 0

        def dfs(total:int):
            if total > n:
                return 0
            if total == n:
                return 1
            
            return dfs(total + 1) + dfs(total + 2)

        return dfs(0)

        