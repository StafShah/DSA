class Node:
    def __init__(self, value):
        self.value = value
        self.children = {}
        self.word = False

class WordDictionary:

    def __init__(self):
        self.root = Node(None)

    def addWord(self, word: str) -> None:
        currNode = self.root
        for i in range(len(word)):
            letter = word[i]
            if letter not in currNode.children:
                currNode.children[letter] = Node(letter)
            currNode = currNode.children[letter]
        currNode.word = True

    def search(self, word: str) -> bool:
        currNode = self.root
        for i in range(len(word)):
            letter = word[i]
            if letter == '.':
                for child in currNode.children.values():
                    if self.dfs(word[i+1:], child):
                        return True
                return False
            if letter not in currNode.children:
                return False
            currNode = currNode.children[letter]
        return currNode.word
    
    def dfs(self, word, node):
        currNode = node
        for i in range(len(word)):
            letter = word[i]
            if letter == '.':
                for child in currNode.children.values():
                    if self.dfs(word[i+1:], child):
                        return True
                return False
            if letter not in currNode.children:
                return False
            currNode = currNode.children[letter]
        return currNode.word


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)