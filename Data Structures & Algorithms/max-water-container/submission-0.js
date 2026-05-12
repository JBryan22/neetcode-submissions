class Solution {
    /**
     * @param {number[]} heights
     * @return {number}
     */
    maxArea(heights) {
                    if (heights.length < 2) {
        return heights[0];
    }
    let left = 0;
    let right = heights.length - 1;
    let max = Math.min(heights[left], heights[right]) * (right - left);

    while (left < right) {
        debugger;
        if (Math.min(heights[left], heights[right]) * (right - left) > max) {
            max = Math.min(heights[left], heights[right]) * (right - left)
        }
        if (heights[left] < heights[right]) {
            left++;
        } else {
            right--;
        }
        
    }
    return max;
    }
}
