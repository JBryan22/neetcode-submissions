class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = 1

        while right < len(numbers) and left < right:
            sum = numbers[left] + numbers[right]
            if sum == target:
                return [left + 1, right + 1]
            if sum < target:
                if right == len(numbers) - 1:
                    left += 1
                else: 
                    right += 1
            if sum > target:
                right -= 1
                left += 1
        return []