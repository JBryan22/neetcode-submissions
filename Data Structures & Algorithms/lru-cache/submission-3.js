class Node {
    /**
     * @param {number} key
     * @param {number} val
     */
    constructor(key, val) {
        this.key = key;
        this.val = val;
        this.prev = null;
        this.next = null;
    }
}

class LRUCache {
    /**
     * @param {number} capacity
     */
    
    
    constructor(capacity) {
        this.cap = capacity;
        this.cache = new Map();
        this.left = new Node(0,0);
        this.right = new Node(0,0);
        this.left.next = this.right;
        this.right.prev = this.left;
    }

    insert(node) {
        const prev = this.right.prev;
        prev.next = this.node;
        node.prev = prev;
        node.next = this.right;
        this.right.prev = node;
    }

    remove (node) {
        const prev = node.prev;
        const nxt = node.next;
        prev.next = nxt;
        nxt.prev = prev;
    }

    /**
     * @param {number} key
     * @return {number}
     */
    get(key) {
        if (this.cache.has(key)) {
            const node = cache.get(key);
            this.remove(node);
            this.insert(node);
            return node.val;
        } else {
            return -1;
        }
    }

    /**
     * @param {number} key
     * @param {number} value
     * @return {void}
     */
    put(key, value) {
        if (this.cache.has(key)) {
            this.remove(node);
        }
        const node = new Node(key,value);
        this.insert(node);
        this.cache.set(key, node);

        if (this.cache.size > this.cap) {
            const lru = this.left.next;
            this.remove(lru);
            this.cache.delete(lru.key);
        }
    }
}
