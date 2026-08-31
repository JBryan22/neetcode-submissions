class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = defaultdict(int)

        for num in nums:
            freqs[num] += 1
        
        most, second = (0,0), (0,0)

        for c in freqs:
            if freqs[c] > most[1]:
                second = most
                most = (c, freqs[c])
            elif c > second[1]:
                second = (c, freqs[c])
            
        return [most[1], second[1]]