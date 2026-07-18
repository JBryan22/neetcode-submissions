class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix_arr = []
        total = 0
        for i in range(len(nums)):
            total += nums[i]
            self.prefix_arr.append(total)

    def sumRange(self, left: int, right: int) -> int:
        subtract = self.prefix_arr[left - 1] if left > 0 else 0 
        return self.prefix_arr[right] - subtract


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)