class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root

        for i in range(len(word)):
            if word[i] not in cur.children:
                cur.children[word[i]] = TrieNode()
            
            cur = cur.children[word[i]]

            if i == len(word) - 1:
                cur.endOfWord = True

    def search(self, word: str) -> bool:
        cur = self.root

        for i in range(len(word)):
            if word[i] not in cur.children:
                return False
            
            cur = cur.children[word[i]]

            if i == len(word) - 1:
                if cur.endOfWord:
                    return True
        
        return False

    def startsWith(self, prefix: str) -> bool:
        cur = self.root

        for i in range(len(prefix)):
            if prefix[i] not in cur.children:
                return False
            
            cur = cur.children[prefix[i]]
        
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)