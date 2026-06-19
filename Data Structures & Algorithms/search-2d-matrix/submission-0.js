class Solution {
    /**
     * @param {number[][]} matrix
     * @param {number} target
     * @return {boolean}
     */
    searchMatrix(matrix, target) {
        let left = 0;
        let colCount = matrix[0].length;
        let right = (matrix.length * colCount) - 1;

        while (left < right) {
            debugger;
            let mid = left + (Math.floor(right - left / 2));
            let row = Math.floor(mid / colCount);
            let col = mid % colCount;
            if (matrix[row][col] == target) {
                return true
            } else if (target < matrix[row][col]) {
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }
        return false;
    }
}
