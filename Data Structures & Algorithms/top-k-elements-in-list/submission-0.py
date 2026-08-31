class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = defaultdict(int)

        for num in nums:
            freqs[num] += 1
        
        most, second = 0, 0

        for c in freqs.values():
            if c > most:
                second = most
                most = c
            elif c > second:
                second = c
            
        return [most, second]