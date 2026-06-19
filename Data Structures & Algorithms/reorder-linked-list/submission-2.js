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
     * @param {ListNode} head
     * @return {void}
     */
    reorderList(head) {
        let midPoint = this.findMidPointLinkedList(head);
        let reversedSecondHalfHead = this.reverseLinkedList(midPoint);
        while (head && reversedSecondHalfHead) {
            let temp = head.next;
            let temp2 = reversedSecondHalfHead.next;
            head.next = reversedSecondHalfHead;
            head = temp;
            reversedSecondHalfHead.next = head;
            reversedSecondHalfHead = temp2;
        }
    }

    findMidPointLinkedList(head) {
        let pointerA = head;
        let pointerB = head.next;

        while (pointerB || pointerB.next) {
            pointerB = pointerB.next.next;
            pointerA = pointerA.next;
        }
        return pointerA;
    }

    reverseLinkedList(head) {
        let prev = null;
        let curr = head;

        while (curr) {
            let temp = curr.next;
            curr.next = prev;
            prev = curr;
            curr = temp;
        }

        return prev;
    }
}
