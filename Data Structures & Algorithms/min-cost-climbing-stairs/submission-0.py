class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # counting
        # need to decide whether to make 1 step or 2 steps for every move
        # at every step i we need to spend cost[i] to move
        # stop when reach the len(cost)
        # can't jump behind len(cost)
        # need to decide the step to start on
        # cost[0] and cost[1] both cost 0 to move to
        # dp[i] = the minimum cost to reach step i
        # dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i - 2])
        # the last step is len(cost), so dp[len(cost)] should be our answer
        if len(cost == 0):
            return 0
        if len(cost) < 2:
            return cost[0]

        res = math.infinity
        cache = {}
        def minCost(i):
            if i < 2:
                return 0
            
            res = min(
                minCost(i - 1) + cost[i - 1],
                minCost(i - 2) + cost[i - 2]
            )

            cache[i] = res
            return res
        return minCost(len(cost))
