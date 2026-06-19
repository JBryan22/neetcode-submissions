class TimeMap {
    constructor() {
        this.keyStore = new Map();
    }

    /**
     * @param {string} key
     * @param {string} value
     * @param {number} timestamp
     * @return {void}
     */
    set(key, value, timestamp) {
        if (this.keyStore.has(key)) {
            this.keyStore[key].push([value, timestamp]);
        } else {
            this.keyStore[key] = [[value,timestamp]];
        }
    }

    /**
     * @param {string} key
     * @param {number} timestamp
     * @return {string}
     */
    get(key, timestamp) {
        if (!this.keyStore.has(key)) {
            return null;
        }
        const valueArr = this.keyStore.get(key);
        let minTimestamp = valueArr[0];
        let low = 0;
        let high = valueArr.length - 1;

        while (low <= high) {
            let mid = Math.floor((high - low) / 2) + low;
            let currTs = valueArr[mid];
            if (currTs[1] === timestamp) {
                return currTs[0];
            }
            if (currTs[1] < timestamp) {
                minTimestamp = currTs;
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }
        return minTimestamp[0];
    }
}
