class Solution {
    /**
     * @param {number[]} piles
     * @param {number} h
     * @return {number}
     */
    minEatingSpeed(piles, h) {
        const max = piles.reduce((a, b) => Math.max(a, b), -Infinity);

        let low = 0;
        let high = max - 1;
        let min = max;
        const eatingSpeeds = Array.from({length: max}, (_, i) => i + 1);

        while (low <= high) {
            let mid = Math.floor((high - low) / 2) + low;

            let hours = this.hoursTakenToEat(piles, eatingSpeeds[mid]);
            if (hours <= h) {
                high = mid - 1;
                min = Math.min(min, eatingSpeeds[mid]);
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