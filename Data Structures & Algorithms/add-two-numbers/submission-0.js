/**
 * Definition for singly-linked list.
 * class ListNode {
 *     constructor(val = 0, next = null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */

class Solution {
    /**
     * @param {ListNode} l1
     * @param {ListNode} l2
     * @return {ListNode}
     */
    addTwoNumbers(l1, l2) {
        let num1 = l1.val;
        l1 = l1.next;
        while(l1) {
            num1 += (10 * l1.val) + num1;
            l1 = l1.next;
        }
        let num2 = l2.val;
        l2 = l2.next;
        while(l2) {
            num2 += (10 * l2.val) + num2;
            l2 = l2.next;
        }
        let resNum = num1+num2;
        let head = new ListNode();
        let ogHead = head;
        while (resNum) {
            head.val = resNum % 10;
            resNum = Math.floor(resNum / 10);
            if (resNum) {
                head.next = new ListNode();
            }
            head = head.next;
        }
        return ogHead;
    }
}
