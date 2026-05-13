class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number}
     */
    search(nums, target) {
        let low = 0;
        let high = nums.length - 1;

        while (low <= high) {
            let mid = Math.floor((high - low) / 2) + low;

            if (target === nums[mid]) {
                return mid;
            }
            if (nums[mid] < nums[high]) {
                // in order - inflection to left
                if (target > nums[mid] && !(target > nums[high])) {
                    low = mid + 1;
                } else {
                    high = mid - 1;
                }
            } else {
                // inflection to the right
                if (target < nums[mid] && !(target < nums[low])) {
                    high = mid - 1;
                } else {
                    low = mid + 1;
                }
            }
        }
        return -1;
    }
}
