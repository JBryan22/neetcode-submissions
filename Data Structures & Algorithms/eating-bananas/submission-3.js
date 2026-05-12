class Solution {
    /**
     * @param {number[]} piles
     * @param {number} h
     * @return {number}
     */
    minEatingSpeed(piles, h) {
        if (piles.length === 1) {
            return Math.ceil(piles[0] / h);
        }
        const max = piles.reduce((a, b) => Math.max(a, b), -Infinity);

        let min = max;
        let low = 1;
        let high = max;

        while (low <= high) {
            let mid = Math.floor((high - low) / 2) + low;

            let hours = this.hoursTakenToEat(piles, mid);
            if (hours <= h) {
                high = mid - 1;
                min = Math.min(min, mid);
            } else {
                low = mid + 1;
            }

        }

        return min;
    }

    hoursTakenToEat(piles, speed) {
        let hoursTaken = 0;
        for (let pile of piles) {
            hoursTaken += Math.ceil(pile / speed);
        }
        return hoursTaken;
    }
}