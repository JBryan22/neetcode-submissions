class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) < 2:
            return 0
        l, r = 0, len(nums) - 1

        while l < r:
            mid = l + (r - l) // 2

            if nums[mid] == target:
                return mid
            
            # inflection point is to the left
            if nums[mid] < nums[r]:
                if target > nums[mid] and target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid
            #inflection point is to the right
            else:
                if target > nums[r]:
                    r = mid
                else:
                    l = mid + 1
            
        return - 1