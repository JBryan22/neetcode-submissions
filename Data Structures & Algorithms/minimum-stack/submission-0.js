class MinStack {
    constructor() {}
    min = null;
    stackData = [];
    /**
     * @param {number} val
     * @return {void}
     */
    push(val) {
        let min;
        if (this.stackData.length === 0) {
            min = val;
        } else if (this.stackData[this.stackData.length - 1][1] < val) {
            min = this.stackData[this.stackData.length - 1][1];
        } else {
            min = val;
        }
        
        this.stackData.push([val, min]);
    }

    /**
     * @return {void}
     */
    pop() {
        return this.stackData.pop()[0];
    }

    /**
     * @return {number}
     */
    top() {
        return this.stackData.length > 0 ? this.stackData[this.stackData.length - 1][0] : null;
    }

    /**
     * @return {number}
     */
    getMin() {
        return this.stackData[this.stackData.length - 1][1];
    }
}
