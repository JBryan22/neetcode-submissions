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
        let resHead = new ListNode();
        let curr = resHead;
        let carry = 0;
        while(l1 && l2) {
            let sum = l1.val + l2.val + carry;
            if (sum < 10) {
                curr.val = sum;
                carry = 0;
            } else {
                carry = 1;
                curr.val = sum % 10;
            }
            if (l1.next || l2.next) {
                curr.next = new ListNode();
                curr = curr.next;
            }
            l1 = l1.next;
            l2 = l2.next;
        }
        while (l1) {
            curr.val = l1.val + carry;
            if (curr.val > 9) {
                curr.val = curr.val % 10;
                carry = 1;
            } else {
                carry = 0;
            }
            if (l1.next) {
                curr.next = new ListNode();
                curr = curr.next;
            }
            l1 = l1.next;
        }
        while (l2) {
            curr.val = l2.val + carry;
            if (curr.val > 9) {
                curr.val = curr.val % 10;
                carry = 1;
            } else {
                carry = 0;
            }
            if (l2.next) {
                curr.next = new ListNode();
                curr = curr.next;
            }
            l2 = l2.next;
        }
        if (carry) {
            curr.next = new ListNode(1);
        }
        return resHead;
    }
}
