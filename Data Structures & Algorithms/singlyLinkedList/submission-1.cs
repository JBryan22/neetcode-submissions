public class LinkedList {
    private Node? head;
    private Node? tail;
    private class Node {
        public Node(int val, Node? node)
        {
            Value = val;
            Next = node;
        }

        public int Value { get; set; }
        public Node? Next { get; set; }
    }
    public LinkedList() {
    }

    public int Get(int index) {
        if (head == null)
        {
            return -1;
        }

        Node currNode = head;
        int idx = 0;
        while (currNode.Next != null && idx != index) {
            currNode = currNode.Next;
            idx += 1;
        }
        if (idx != index)
        {
            return -1;
        }
        return currNode.Value;
    }

    public void InsertHead(int val) {
        if (head == null)
        {
            head = new Node(val, null);
            
        } 
        else
        {
            var newHead = new Node(val, head);
            head = newHead;
        }

    }

    public void InsertTail(int val) {
        if (tail != null)
        {
            var newTail = new Node(val, null);
            tail.Next = newTail;
            tail = newTail;
        }

    }

    public bool Remove(int index) {
        if (head == null)
        {
            return false;
        }

        Node currNode = head;
        int idx = 0;
        while (currNode.Next != null && idx < index) {
            currNode = currNode.Next;
            idx += 1;
        }
        if (idx != index)
        {
            return false;
        }
        currNode.Next = currNode.Next?.Next;

        return true;
    }

    public List<int> GetValues() {
        List<int> vals = new();

        var currNode = head;
        while(currNode != null)
        {
            vals.Add(currNode.Value);
            currNode = currNode.Next;
        }
        return vals;
    }
}