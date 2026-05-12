// Singly Linked List Node
public class ListNode {
    public int val;
    public ListNode next;

    // Constructor that sets 'next' to null by default
    public ListNode(int val) {
        this.val = val;
        this.next = null;
    }

    // Constructor that accepts both value and next node
    public ListNode(int val, ListNode next) {
        this.val = val;
        this.next = next;
    }
}

// Implementation for Singly Linked List
public class LinkedList {
    private ListNode head;
    private ListNode tail;

    // Constructor
    public LinkedList() {
        // Init the list with a 'dummy' node which makes
        // removing a node from the beginning of list easier.
        this.head = new ListNode(-1);
        this.tail = this.head;
    }

    public int Get(int index) {
        ListNode curr = head.next;
        int i = 0;
        while (curr != null) {
            if (i == index) {
                return curr.val;
            }
            i++;
            curr = curr.next;
        }
        return -1;  // Index out of bounds or list is empty
    }

    public void InsertHead(int val) {
        ListNode newNode = new ListNode(val);
        newNode.next = head.next;
        head.next = newNode;
        if (newNode.next == null) {  // If list was empty before insertion
            tail = newNode;
        }
    }

    // Method to insert at the end
    public void InsertTail(int val) {
        this.tail.next = new ListNode(val);
        this.tail = this.tail.next;
    }

    // Method to remove at given index
    public bool Remove(int index) {
        int i = 0;
        ListNode curr = this.head;
        while (i < index && curr != null) {
            i++;
            curr = curr.next;
        }

        // Remove the node ahead of curr
        if (curr != null && curr.next != null) {
            if (curr.next == this.tail) {
                this.tail = curr;
            }
            curr.next = curr.next.next;
            return true;
        }
        return false;
    }

    // Method to get values of the linked list
    public List<int> GetValues() {
        List<int> res = new List<int>();
        ListNode curr = this.head.next;
        while (curr != null) {
            res.Add(curr.val);
            curr = curr.next;
        }
        return res;
    }
}