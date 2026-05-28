class Stack:
    # arr = list()
    def __init__(self):
        self.arr = list()
        

    def push(self, elem):
        return self.arr.append(elem)
    
    def pop(self):
        if len(self.arr) > 0:
            return self.arr.pop()
        else:
            return None
    
    def peek(self):
        if len(self.arr) > 0:
            return self.arr[-1]
        else:
            return None

    def length(self):
        return len(self.arr)
            

class Solution:
    def isValid(self, s: str) -> bool:
        open_close_lookup = {
            '{': '}',
            '(': ')',
            '[': ']',
        }

        close_open_lookup = {
            '}': '{',
            ')': '(',
            ']': '[',
        }

        n = len(s)

        stack1 = Stack()

        for i in range(n):
            paren = s[i]
            if paren in open_close_lookup:
                stack1.push(paren)
            else:
                last_paren = stack1.peek()
                if last_paren is not None and open_close_lookup[last_paren] == paren:
                    stack1.pop()
                else:
                    return False
        
        if stack1.length() == 0:
            return True
        
        return False



        