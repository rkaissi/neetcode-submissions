class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class PrefixTree:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word: str):
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endOfWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:        
        # Init Trie
        trie = PrefixTree()
        for word in words:
            trie.insert(word)

        DIRS = [(0, -1), (0, 1), (-1, 0), (1, 0)] # up, down, left, right
        ROWS, COLS = len(board), len(board[0])

        res, visit = set(), set()

        def dfs(r, c, node, word):
            if (r < 0 or c < 0 or
                r == ROWS or c == COLS or
                (r, c) in visit or board[r][c] not in node.children):
                return
            
            visit.add((r, c))
            char = board[r][c]
            node = node.children[char]
            word += char
            if node.endOfWord:
                res.add(word)
            
            for dr, dc in DIRS:
                dfs(r+dr, c+dc, node, word)

            visit.remove((r, c))


        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, trie.root, "")
        
        return list(res)
