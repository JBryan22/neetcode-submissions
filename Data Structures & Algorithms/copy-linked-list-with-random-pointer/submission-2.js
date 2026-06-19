// class Node {
//   constructor(val, next = null, random = null) {
//       this.val = val;
//       this.next = next;
//       this.random = random;
//   }
// }

class Solution {
    /**
     * @param {Node} head
     * @return {Node}
     */
    copyRandomList(head) {
        let mapOfNodes = new Map();
        let newHead = new Node(head.val);
        let newCurr = newHead;
        let ogHead = head;
        while(head) {
            newCurr.val = head.val;
            if (head.next) {
                newCurr.next = new Node(head.next.val);
                newCurr = newCurr.next;
            }
            mapOfNodes.set(head, newCurr);
            head = head.next;
        }

        while(ogHead) {
            let rand = ogHead.random;
            mapOfNodes.get(ogHead).random = rand;
            ogHead = ogHead.next;
        }
        return newHead;
    }
}
