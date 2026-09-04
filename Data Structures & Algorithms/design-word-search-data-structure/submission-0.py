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
        node = self.root

        def dfsSearch(node: TrieNode, postfix: str) -> bool:
            if len(postfix) == 0:
                return True
            for i, c in enumerate(postfix):
                if c in node.children:
                    node = node.children[c]
                    continue
                elif c == '.':
                    for char in node.children:
                        if dfsSearch(node.children[char], postfix[i+1:]):
                            return True
                else:
                    return False
            return True
        return dfsSearch(node, word)

