""" Design a data structure that supports adding new words and searching for existing words.

Implement the WordDictionary class:

void addWord(word) Adds word to the data structure.
bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter. """

""" 
My thought process:
1. Everything in addWord looks similar to insert in the Trie data structure
2. Now the search also looks similar as it is in the Trie data structure until it hits '.'
3. When it hit '.' we need to explore all possible combination

How do I go about it 
4. I loop to check all children of the present current_node (the one before char)
5. For each child found, I then replace the '.' in the string with the child character and run the search function (that makes it recursive)
6. And if one of them return true - then the whole function returns true
7. But if there the current_node being explored have no children, we return False 
"""

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

        def dfs(node: TrieNode, index: int):
            if index == len(word):
                return node.isEndOfWord

            char = word[index]

            if char == '.':
                no_of_children = len(node.children)
                for i in range(no_of_children):
                    if node.children[i] is not None:
                        result = dfs(node.children[i], index+1)
                        if result:
                            return True
                    
                # tried all children but none of them worked
                return False

            char_index = ord(char) - ord('a')

            if node.children[char_index] is None:
                return False
            
            return dfs(node=node.children[char_index], index=index+1)

        return dfs(self.root, 0)

        

