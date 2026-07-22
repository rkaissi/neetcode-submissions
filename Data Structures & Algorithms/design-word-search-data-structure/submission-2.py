class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endOfWord = True

    def search(self, word: str) -> bool:

        def dfs(node, j) -> bool:
            cur = node
            for i in range(j, len(word)):
                c = word[i]
                if c == ".":
                    found = False
                    for key in cur.children:
                        found = found or dfs(cur.children[key], i+1)
                    return found
                elif c not in cur.children:
                    return False
                cur = cur.children[c]
            return cur.endOfWord
        
        return dfs(self.root, 0)
