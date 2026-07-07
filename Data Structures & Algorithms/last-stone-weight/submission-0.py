class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHStones = [-x for x in stones]
        heapq.heapify(maxHStones)

        while len(maxHStones) > 1:
            heaviest = heapq.heappop(maxHStones)
            secondHeaviest = heapq.heappop(maxHStones)

            heaviest -= secondHeaviest

            if heaviest < 0:
                heapq.heappush(maxHStones, heaviest)
        
        if len(maxHStones):
            return -maxHStones[0]
        else:
            return 0