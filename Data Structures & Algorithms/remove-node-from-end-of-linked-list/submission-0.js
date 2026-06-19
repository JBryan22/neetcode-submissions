/**
 * Definition for singly-linked list.
 * class ListNode {
 *     constructor(val = 0, next = null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 * 
 * [1,2,3,4,5,6,7,8,9,10] n = 3 --> remove 8
 *  a     a     a      b
 */

class Solution {
    /**
     * @param {ListNode} head
     * @param {number} n
     * @return {ListNode}
     */
    removeNthFromEnd(head, n) {
        let a = head;
        let b = head;
        for(let i = 0; i < n && b !== null; i++) {
            b = b.next;
        }
        while (b) {
            b = b.next;
            if (!b) {
                a.next = a.next.next;
                return head;
            }
            a = a.next;
        }
        return head;
    }
}
