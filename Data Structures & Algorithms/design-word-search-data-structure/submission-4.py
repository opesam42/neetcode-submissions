class TrieNode:
    def __init__(self) -> None:
        self.children = [None] * 26
        self.isEndOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        
    def addWord(self, word: str) -> None:
        curr_node = self.root

        for char in word:
            index = ord(char) - ord('a')
            if curr_node.children[index] is None:
                new_node = TrieNode()
                curr_node.children[index] = new_node
            
            curr_node = curr_node.children[index]

        curr_node.isEndOfWord = True

    def search(self, word: str) -> bool:
        curr_node = self.root

        for char in word:
            if char == '.':
                # loop through all children node that are not None
                match = 0
                for i in range(len(curr_node.children)):
                    # take all possible combinations
                    if curr_node.children[i]:
                        match += 1
                        # get the correspoding character that matches the ascii code
                        ascii_code = ord('a') + i
                        char = chr(ascii_code)
                        key = word.replace('.', char, 1)
                        
                        result = self.search(key)
                        if result:
                            return True

                # if the node have no children, then terminate (catches case when u have like dog, but the input is do..)
                if match == 0:
                    return False


            index = ord(char) - ord('a')
            if curr_node.children[index] is None:
                return False
            curr_node = curr_node.children[index]
        
        return curr_node.isEndOfWord


