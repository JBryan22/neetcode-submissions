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
        if (!head) {
            return null;
        }
        let mapOfNodes = new Map();
        let ogHead = head;
        while(head) {
            mapOfNodes.set(head, new Node(head.val));
            head = head.next;
        }
        let newHead = mapOfNodes.get(ogHead);
        while(ogHead) {
            let newNode = mapOfNodes.get(ogHead);
            newNode.next = mapOfNodes.get(ogHead.next);
            newNode.random = mapOfNodes.get(ogHead.random);
            ogHead = ogHead.next;
        }
        return newHead;
    }
}
