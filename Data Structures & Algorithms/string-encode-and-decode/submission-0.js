class Solution {
    /**
     * @param {string[]} strs
     * @returns {string}
     */
    encode(strs) {
        let resultStr = "";
        strs.forEach(element => {
            resultStr += `${element.length}L${element}`
        });
        return resultStr;
    }

    /**
     * @param {string} str
     * @returns {string[]}
     */
    decode(str) {
        let resultArr = [];
        for (let i = 0; i < str.length; i++)
        {
            let lengthStr = "";
            while (str[i] !== "L" && i < str.length) {
                lengthStr += str[i];
                i++;
            }
            i++;
            let length = parseInt(lengthStr);
            let elementStr = "";
            for (let j = 0; j < length; j++)
            {
                elementStr += str[i + j];
            }
            resultArr.push(elementStr);
            i += length - 1;
        }
        return resultArr;
    }
}
