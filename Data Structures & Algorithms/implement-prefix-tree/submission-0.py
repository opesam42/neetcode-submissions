class TrieNode:
    def __init__(self) -> None:
        self.children = [None] * 26
        self.isEndOfWord = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()        


    def insert(self, word: str) -> None:
        curr_node = self.root
        
        for char in word:
            index = ord(char) - ord('a')
            if curr_node.children[index] is None:
                new_node = TrieNode()
                curr_node.children[index] = new_node
            
            curr_node = curr_node.children[index]

        # set last character or node as end of the word
        curr_node.isEndOfWord = True


    def search(self, word: str) -> bool:
        curr_node = self.root

        for char in word:
            index = ord(char) - ord('a')
            if curr_node.children[index] is None:
                return False
            curr_node = curr_node.children[index]
        
        # confirm if the last string of the word in the arg, is truly the end of the world in the predix node
        return curr_node.isEndOfWord
        

    def startsWith(self, prefix: str) -> bool:
        curr_node = self.root

        for char in prefix:
            index = ord(char) - ord('a')
            if curr_node.children[index] is None:
                return False
            curr_node = curr_node.children[index]
        return True
        