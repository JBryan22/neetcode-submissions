class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    findMin(nums) {
        let low = 0;
        let high = nums.length - 1;

        while (low < high) {
            let mid = Math.floor((high - low) / 2) + low;

            if (nums[mid] <= nums[high]) {
                // still in order, look for inflection point to left
                // include mid because it could be inflection point and min num
                high = mid;
            } else {
                // dont need to include mid when inflection is to right because min num is to right of inflection point
                low = mid + 1;
            }
        }

let mid = Math.floor((high - low) / 2) + low;
        return nums[mid];
    }
}
