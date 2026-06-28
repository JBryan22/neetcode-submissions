class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sum = 0

        res = 0
        prefixCounts = defaultdict(int, )
        prefixCounts[0] = 1

        for num in nums:
            sum += num

            if sum - k in prefixCounts:
                res += prefixCounts[sum - k]
            
            prefixCounts[sum] += 1
            
        return res