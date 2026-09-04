class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root

        for c in word:
            if c in node.children:
                node = node.children[c]
                continue
            node.children[c] = TrieNode()
            node = node.children[c]
        node.isWord = True

    def search(self, word: str) -> bool:
        def dfsSearch(node: TrieNode, ind: int) -> bool:
            curNode = node
            for i in range(ind, len(word)):
                c = word[i]
                if c in curNode.children:
                    curNode = curNode.children[c]
                    continue
                elif c == '.':
                    for char in curNode.children:
                        if dfsSearch(curNode.children[char], i+1):
                            return True
                    return False
                else:
                    return False
            return curNode.isWord
        return dfsSearch(self.root, 0)

