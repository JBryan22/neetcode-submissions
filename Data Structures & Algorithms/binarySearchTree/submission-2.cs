class TreeNode {
    public TreeNode(int key, int value)
    {
        Key = key;
        Value = value;
    }
    public int Key {get;set;}
    public int Value {get;set;}
    public TreeNode? LeftChild { get; set; }
    public TreeNode? RightChild { get; set; }
}

class TreeMap {
    private TreeNode? root = null;

    public TreeMap() {

    }

    public void Insert(int key, int val) {
        root = Insert(root, key, val);
    }

    private TreeNode Insert(TreeNode? curr, int key, int value)
    {
        if (curr == null)
        {
            return new TreeNode(key, value);
        }
        if (curr.Key > key)
        {
            curr.LeftChild = Insert(curr.LeftChild, key, value);
        }
        else if (curr.Key < key)
        {
            curr.RightChild = Insert(curr.RightChild, key, value);
        }
        else {
            curr.Value = value;
        }
        return curr;
    }

    public int Get(int key) {
        var node = Get(root, key);

        return node == null ? -1 : node.Value;
    }

    private TreeNode? Get(TreeNode? node, int key)
    {
        if (node == null)
        {
            return null;
        }

        if (node.Key == key)
        {
            return node;
        }
        else if (node.Key > key)
        {
            return Get(node.LeftChild, key);
        }
        else
        {
            return Get(node.RightChild, key);
        }
    }

    public int GetMin() {
        if (root == null)
        {
            return -1;
        }
        else
        {
            TreeNode curr = root;
            while(curr.LeftChild != null)
            {
                curr = curr.LeftChild;
            }
            return curr.Value;
        }
    }

    private TreeNode GetMinTreeNode(TreeNode node) {
        while(node.LeftChild != null)
        {
            node = node.LeftChild;
        }
        return node;
    }

    public int GetMax() {
        if (root == null)
        {
            return -1;
        }
        else
        {
            TreeNode curr = root;
            while(curr.RightChild != null)
            {
                curr = curr.RightChild;
            }
            return curr.Value;
        }
    }

    public void Remove(int key) {
        root = Remove(root, key);
    }

    private TreeNode? Remove(TreeNode? node, int key)
    {
        if (node == null)
        {
            return null;
        }

        if (node.Key > key)
        {
            node.LeftChild = Remove(node.LeftChild, key);
        }
        else if (node.Key < key)
        {
            node.RightChild = Remove(node.RightChild, key);
        }
        else
        {
            if (node.LeftChild == null || node.RightChild == null)
            {
                return node.LeftChild ?? node.RightChild;
            }
            else
            {
                var minNodeFromRight = GetMinTreeNode(node.RightChild);
                node.Value = minNodeFromRight.Value;
                node.Key = minNodeFromRight.Key;
                node.RightChild = Remove(node.RightChild, minNodeFromRight.Key);
            }
        }
        return node;
    }

    public List<int> GetInorderKeys() {
        List<int> inOrderKeys = new List<int>();

        if (root != null)
        {
            GetInorderKeys(root, inOrderKeys);
        }

        return inOrderKeys;
    }

    private void GetInorderKeys(TreeNode node, List<int> keys)
    {
        if (node.LeftChild != null)
        {
            GetInorderKeys(node.LeftChild, keys);
        }
        keys.Add(node.Key);
        if (node.RightChild != null)
        {
            GetInorderKeys(node.RightChild, keys);
        }
    }
}
