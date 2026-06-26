class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        hashmap = defaultdict(int)

        for num in nums:
            hashmap[num] += 1
            if len(hashmap) > 2:
                for k, v in hashmap.items():
                    v -= 1
                for k, v in hashmap.items():
                    if v <= 0:
                        del hashmap[k]
        
        res = []
        for num in hashmap:
            if nums.count(num) > len(nums) // 3:
                res.append(num)
        return res