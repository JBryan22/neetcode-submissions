class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        numSorted = sorted(nums)

        for i, a in enumerate(numSorted):
            if a > 0:
                break
            if i > 0 and a == numSorted[i - 1]:
                continue
                
            l, r = i + 1, len(numSorted) - 1
            while l < r:
                threeS = a + numSorted[l] + numSorted[r]

                if threeS > 0:
                    r -= 1
                elif threeS < 0:
                    l += 1
                else:
                    res.append([a, numSorted[l], numSorted[r]])
                    l += 1
                    r -= 1
                    while l < r and numSorted[l] == numSorted[l - 1]:
                        l += 1
        return res
