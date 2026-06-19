class QueueNode 
{
    public QueueNode(int value, QueueNode? left = null, QueueNode? right = null)
    {
        Value = value;
        Left = left;
        Right = right;
    }

    public int Value { get; set; }
    public QueueNode? Left { get; set; }
    public QueueNode? Right { get; set; }
}

class Deque {
    private QueueNode? head = null;
    private QueueNode? tail = null;
    public Deque() {

    }

    public bool isEmpty() {
        return head == null;
    }

    public void append(int value) {
        if (head == null)
        {
            head = new QueueNode(value);
        }
        else if (tail == null)
        {
            tail = new QueueNode(value, head, null);
            head.Right = tail;
        }
        else 
        {
            var newTail = new QueueNode(value, tail, null);
            tail.Right = newTail;
            tail = newTail;
        }
    }

    public void appendleft(int value) {
        if (head == null)
        {
            head = new QueueNode(value);
        }
        else if (tail == null)
        {
            var newHead = new QueueNode(value, null, head);
            head.Left = newHead;
            head = newHead;
            tail = head.Right;
        }
        else
        {
            var newHead = new QueueNode(value, null, head);
            head.Left = newHead;
            head = newHead;
        }
    }

    public int pop() {
        int result;

        if (head == null)
        {
            return -1;
        }
        else if (tail == null)
        {
            result = head.Value;
            head = null;
        }
        else
        {
            result = tail.Value;
            tail = tail.Left;
            tail!.Right = null;
        }
        return result;
    }

    public int popleft() {
        int result;

        if (head == null)
        {
            return -1;
        }
        else if (tail == null)
        {
            result = head.Value;
            head = null;
        }
        else
        {
            result = head.Value;
            if (head.Right == tail)
            {
                tail = null;
            }
            head = head.Right;
            head!.Left = null;
        }
        return result;
    }
}
