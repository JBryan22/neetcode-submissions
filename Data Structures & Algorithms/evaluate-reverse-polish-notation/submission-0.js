class Solution {
    /**
     * @param {string[]} tokens
     * @return {number}
     */
    evalRPN(tokens) {
                let operators = new Set('+', '-', '*', '/');
    let currStack = [];

    for (let token of tokens) {
        debugger;
        if (operators.has(token)) {
            let operand2 = currStack.pop();
            let operand1 = currStack.pop();

            switch (token) {
                case '+':
                    currStack.push(parseInt(operand1) + parseInt(operand2));
                    break;
                case '-':
                    currStack.push(parseInt(operand1) - parseInt(operand2));
                    break;
                case '*':
                    currStack.push(parseInt(operand1) * parseInt(operand2));
                    break;
                case '/':
                    currStack.push(parseInt(operand1) / parseInt(operand2));
                    break;
            }
        } else {
            currStack.push(parseInt(token))
        }
    }

    return parseInt(currStack.pop());
    }
}
