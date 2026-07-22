class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False


class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curNode = self.root
        for i in range(len(word)):
            c = word[i]
            if c not in curNode.children:
                curNode.children[c] = TrieNode()
            curNode = curNode.children[c]
            if i == len(word) - 1:
                curNode.endOfWord = True


    def search(self, word: str) -> bool:
        curNode = self.root
        for i in range(len(word)):
            c = word[i]
            if c not in curNode.children:
                return False
            curNode = curNode.children[c]
            if i == len(word) - 1:
                return curNode.endOfWord

    def startsWith(self, prefix: str) -> bool:
        curNode = self.root
        for i in range(len(prefix)):
            c = prefix[i]
            if c not in curNode.children:
                return False
            curNode = curNode.children[c]
        return True
        